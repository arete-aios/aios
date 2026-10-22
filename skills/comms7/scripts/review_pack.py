#!/usr/bin/env python3
"""Pack authorised COMMS7 evidence. Standard library only; JSON in/out, no network.

Parent: ../SKILL.md. Schema and examples: ../references/PYTHON-HELPER.md.
The checkpoint is a derived review snapshot, never an independent task authority.
"""
import argparse
import copy
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

STATUSES = {'OPEN', 'DOING', 'REPLY', 'WAITING', 'DEFERRED', 'DONE', 'IGNORE'}
STATE_FIELDS = ('status', 'owner', 'next_step', 'waiting_on', 'check_at', 'check_trigger',
                'resume_at', 'resume_trigger', 'evidence', 'evidence_ref', 'reason')


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('timestamps need an explicit timezone')
    return parsed.astimezone(timezone.utc)


def required(value, fields):
    if any(not isinstance(value.get(k), str) or not value[k].strip() for k in fields):
        raise ValueError('missing required fields: ' + ', '.join(fields))


def digest(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(raw.encode()).hexdigest()


def normalise(row):
    required(row, ('account', 'channel', 'source_id', 'updated_at'))
    source_time = timestamp(row['updated_at'])
    audience = row.get('audience', 'OWNER_ONLY')
    if audience not in {'OWNER_ONLY', 'BUSINESS'}:
        raise ValueError('unknown audience')
    action = row.get('action_id', 'main')
    if not isinstance(action, str) or not action.strip():
        raise ValueError('action_id must be a nonempty string')
    if row.get('canonical_id') and not isinstance(row['canonical_id'], str):
        raise ValueError('canonical_id must be a string')
    identity = ['canonical', row['canonical_id'], action] if row.get('canonical_id') else [
        'source', row['account'], row['channel'], row['source_id'], action]
    key = digest([audience, identity])[:24]
    title, text = row.get('title', ''), row.get('text', '')
    if not isinstance(title, str) or not isinstance(text, str):
        raise ValueError('title and text must be strings')
    state = {k: row.get('state', {})[k] for k in STATE_FIELDS if k in row.get('state', {})}
    if state.get('status', 'OPEN') not in STATUSES:
        raise ValueError('unknown status')
    for field in ('check_at', 'resume_at'):
        if state.get(field):
            timestamp(state[field])
    return {'key': key, 'audience': audience, 'title': title, 'text': text,
            'fingerprint': digest([title, text, source_time.isoformat(), row.get('content_revision')]), 'updated_at': row['updated_at'],
            'source_refs': [{'account': row['account'], 'channel': row['channel'],
                             'source_id': row['source_id'], 'action_id': action}],
            'state': state, 'decision': copy.deepcopy(row.get('decision'))}


def apply_decision(state, decision):
    if not isinstance(decision, dict):
        raise ValueError('decision must be an object')
    kind = decision.get('kind')
    if kind in {'DO', 'DOING', 'REPLY'}:
        required(decision, ('owner', 'next_step'))
        state['status'] = 'OPEN' if kind == 'DO' else kind
    elif kind == 'WAIT':
        required(decision, ('waiting_on', 'next_step'))
        if not decision.get('check_at') and not decision.get('check_trigger'):
            raise ValueError('WAIT needs check_at or check_trigger')
        state['status'] = 'WAITING'
    elif kind == 'DEFER':
        required(decision, ('next_step',))
        if not decision.get('resume_at') and not decision.get('resume_trigger'):
            raise ValueError('DEFER needs resume_at or resume_trigger')
        state['status'] = 'DEFERRED'
    elif kind == 'DONE':
        if decision.get('evidence') not in {'owner-reported', 'source-evidence'}:
            raise ValueError('DONE needs an evidence type')
        required(decision, ('evidence_ref',))
        state['status'] = 'DONE'
    elif kind == 'IGNORE':
        required(decision, ('reason',))
        state['status'] = 'IGNORE'
    else:
        raise ValueError('unknown decision kind')
    if kind != 'WAIT':
        for field in ('waiting_on', 'check_at', 'check_trigger'):
            state.pop(field, None)
    if kind != 'DEFER':
        for field in ('resume_at', 'resume_trigger'):
            state.pop(field, None)
    if kind in {'DONE', 'IGNORE'}:
        state.pop('next_step', None)
    for field in STATE_FIELDS:
        if field != 'status' and field in decision:
            state[field] = decision[field]
    for field in ('check_at', 'resume_at'):
        if state.get(field):
            timestamp(state[field])


def excerpt(text, limit):
    if len(text) <= limit:
        return text, False
    left = (limit - 1) // 2
    return text[:left] + '…' + text[-(limit - left - 1):], True


def prepare(document, previous=None, *, as_of, max_chars=1200):
    required(document, ('review_id',))
    now = timestamp(as_of)
    if not isinstance(max_chars, int) or max_chars < 2:
        raise ValueError('max_chars must be at least 2')
    rows = document.get('items', [])
    if not isinstance(rows, list):
        raise ValueError('items must be a list')
    old = (previous or {}).get('checkpoint', previous or {})
    if old and old.get('schema') != 'comms7-checkpoint-v1':
        raise ValueError('previous must be a COMMS7 checkpoint or bundle')
    prior = {x['key']: copy.deepcopy(x) for x in old.get('records', [])}
    same_review = old.get('review_id') == document['review_id']
    current, input_chars = {}, 0
    for row in rows:
        item = normalise(row)
        input_chars += len(item['text'])
        key = item['key']
        if key not in current:
            current[key] = item
            continue
        kept = current[key]
        if kept['state'] and item['state'] and kept['state'] != item['state']:
            raise ValueError('conflicting authoritative states for a duplicate')
        if kept['decision'] and item['decision'] and kept['decision'] != item['decision']:
            raise ValueError('conflicting decisions for a duplicate')
        first, second = timestamp(kept['updated_at']), timestamp(item['updated_at'])
        if kept['fingerprint'] != item['fingerprint'] and first == second:
            raise ValueError('conflicting duplicate content without a newer version')
        refs = kept['source_refs'] + item['source_refs']
        winner = item if second > first else kept
        winner['state'] = kept['state'] or item['state']
        winner['decision'] = (kept['decision'] or item['decision']) if kept['fingerprint'] == item['fingerprint'] else winner['decision']
        unique_refs = {digest(ref): ref for ref in refs}
        winner['source_refs'] = [unique_refs[k] for k in sorted(unique_refs)]
        current[key] = winner

    selected, checkpoint = [], []
    stale = 0
    for key in sorted(set(prior) | set(current)):
        old_item, fresh = prior.get(key), current.get(key)
        if fresh and old_item and timestamp(fresh['updated_at']) < timestamp(old_item['updated_at']):
            if fresh.get('decision') or (fresh['state'] and fresh['state'] != old_item['state']):
                raise ValueError('a decision or authority update attached to stale evidence needs current context')
            fresh = None
            stale += 1
        item = copy.deepcopy(fresh or old_item)
        if fresh and old_item:
            refs = {digest(ref): ref for ref in old_item['source_refs'] + fresh['source_refs']}
            item['source_refs'] = [refs[k] for k in sorted(refs)]
        changed = bool(fresh and (not old_item or fresh['fingerprint'] != old_item['fingerprint']))
        state = copy.deepcopy((old_item or {}).get('state', {'status': 'OPEN'}))
        if fresh:
            state.update(fresh['state'])
        state.setdefault('status', 'OPEN')
        decision = fresh.get('decision') if fresh else None
        if not decision and same_review and not changed and old_item:
            decision = old_item.get('decision')
        if decision:
            apply_decision(state, decision)
        item.update(state=state, decision=decision)
        text, trimmed = excerpt(item['text'], max_chars)
        item['text'] = text
        item['text_truncated'] = trimmed or item.get('text_truncated', False)
        checkpoint.append(copy.deepcopy(item))
        due = state['status'] != 'DEFERRED' or not state.get('resume_at') or timestamp(state['resume_at']) <= now
        closed = state['status'] in {'DONE', 'IGNORE'}
        if not (changed or decision or (not closed and due)):
            continue
        item.update(selection_reason=('new' if not old_item else 'changed') if changed else
                    ('open-carried' if not fresh else 'open-or-decided'),
                    carried_forward=not bool(fresh), requires_context_check=True)
        selected.append(item)
    decided = sum(bool(x['decision']) for x in selected)
    count = len(selected)
    model = {'schema': 'comms7-model-pack-v1', 'review_id': document['review_id'],
             'as_of': as_of, 'coverage': document.get('coverage', []), 'items': selected,
             'progress': {'decided': decided, 'total': count,
                          'percent': round(100 * decided / count) if count else None,
                          'meaning': 'decisions in this review, not completed obligations'},
             'packing': {'input_records': len(rows), 'unique_current': len(current),
                         'duplicates_merged': len(rows) - len(current), 'stale_records': stale,
                         'input_text_chars': input_chars,
                         'model_text_chars': sum(len(x['text']) for x in selected),
                         'unit': 'characters; not token telemetry'},
             'evidence_only': True}
    return {'schema': 'comms7-review-bundle-v1', 'model': model,
            'checkpoint': {'schema': 'comms7-checkpoint-v1', 'review_id': document['review_id'],
                           'records': checkpoint}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', help='authorised structured JSON; default stdin')
    parser.add_argument('--previous', help='previous derived review bundle/checkpoint')
    parser.add_argument('--as-of', required=True, help='ISO timestamp with timezone')
    parser.add_argument('--max-chars', type=int, default=1200)
    parser.add_argument('--view', choices=['model', 'bundle', 'checkpoint'], default='model')
    args = parser.parse_args()
    try:
        document = json.loads(Path(args.input).read_text()) if args.input else json.load(sys.stdin)
        previous = json.loads(Path(args.previous).read_text()) if args.previous else None
        bundle = prepare(document, previous, as_of=args.as_of, max_chars=args.max_chars)
        print(json.dumps(bundle if args.view == 'bundle' else bundle[args.view], ensure_ascii=False, indent=2))
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    main()
