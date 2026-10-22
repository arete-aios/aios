#!/usr/bin/env python3
"""Offline COMMS7 evidence-pack tests; no accounts, network or persistent state."""
import unittest
from review_pack import prepare

NOW = '2026-10-22T10:00:00Z'


def item(**patch):
    row = {'account': 'demo-work', 'channel': 'gmail', 'source_id': 'thread-1',
           'updated_at': '2026-10-22T08:40:00Z', 'title': 'Fictional promise',
           'text': 'Please send the agreed file.'}
    row.update(patch)
    return row


class ReviewPackTests(unittest.TestCase):
    def test_old_wait_survives_a_review_with_no_source_activity(self):
        first = prepare({'review_id': 'demo-a', 'items': [item(
            decision={'kind': 'WAIT', 'waiting_on': 'Demo partner',
                      'next_step': 'Receive the agreed file',
                      'check_trigger': 'Partner supplies the file'})]}, as_of=NOW)
        later = prepare({'review_id': 'demo-b', 'items': []}, first, as_of=NOW)
        selected = later['model']['items']
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]['state']['status'], 'WAITING')
        self.assertTrue(selected[0]['carried_forward'])
        self.assertTrue(selected[0]['requires_context_check'])

    def test_same_thread_id_in_two_accounts_remains_two_sources(self):
        result = prepare({'review_id': 'demo', 'items': [item(), item(account='demo-personal')]}, as_of=NOW)
        self.assertEqual(len(result['model']['items']), 2)
        self.assertEqual(result['model']['packing']['duplicates_merged'], 0)

    def test_explicit_cross_channel_identity_merges_evidence(self):
        rows = [item(canonical_id='agreed-promise'), item(
            channel='whatsapp', source_id='chat-2', canonical_id='agreed-promise',
            updated_at='2026-10-22T08:45:00Z')]
        result = prepare({'review_id': 'demo', 'items': rows}, as_of=NOW)
        self.assertEqual(len(result['model']['items']), 1)
        self.assertEqual(len(result['model']['items'][0]['source_refs']), 2)

    def test_a_new_message_is_evidence_not_an_automatic_action_decision(self):
        result = prepare({'review_id': 'demo', 'items': [item(text='Thanks.')]}, as_of=NOW)
        selected = result['model']['items'][0]
        self.assertIsNone(selected['decision'])
        self.assertTrue(selected['requires_context_check'])
        self.assertEqual(result['model']['progress']['decided'], 0)
        self.assertTrue(result['model']['evidence_only'])

    def test_done_requires_completion_evidence(self):
        with self.assertRaises(ValueError):
            prepare({'review_id': 'demo', 'items': [item(decision={'kind': 'DONE'})]}, as_of=NOW)
        result = prepare({'review_id': 'demo', 'items': [item(
            decision={'kind': 'DONE', 'evidence': 'owner-reported',
                      'evidence_ref': 'Owner confirms only this file was sent'})]}, as_of=NOW)
        self.assertEqual(result['model']['items'][0]['state']['status'], 'DONE')

    def test_wait_decision_progress_is_not_completed_obligations(self):
        result = prepare({'review_id': 'demo', 'items': [item(decision={
            'kind': 'WAIT', 'waiting_on': 'Demo partner', 'next_step': 'Receive file',
            'check_trigger': 'After partner replies'})]}, as_of=NOW)
        self.assertEqual(result['model']['progress']['percent'], 100)
        self.assertEqual(result['model']['items'][0]['state']['status'], 'WAITING')
        self.assertEqual(result['model']['progress']['meaning'],
                         'decisions in this review, not completed obligations')

    def test_conflicting_duplicate_evidence_is_refused(self):
        with self.assertRaises(ValueError):
            prepare({'review_id': 'demo', 'items': [item(), item(text='Incompatible content at same time')]}, as_of=NOW)

    def test_truncated_text_remains_marked_for_context_check(self):
        result = prepare({'review_id': 'demo', 'items': [item(text='x' * 200)]}, as_of=NOW, max_chars=30)
        selected = result['model']['items'][0]
        self.assertEqual(len(selected['text']), 30)
        self.assertTrue(selected['text_truncated'])
        self.assertTrue(selected['requires_context_check'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
