# Optional Python packing helper

Parent: [SKILL.md](../SKILL.md). Implementation: [review_pack.py](../scripts/review_pack.py).
Python3 standard library only; no network, account access or external libraries.

The helper merges duplicate authorised records, preserves older open work and emits
a compact model pack plus an optional derived checkpoint. The AI must still check
full context when needed. A checkpoint never replaces the task/CRM authority.

```sh
python3 scripts/review_pack.py --input input.json --as-of 2026-10-22T10:00:00Z --view bundle
```

Input has review_id and items. Each item requires account, channel, source_id and
timezone-aware updated_at; optional fields include title, text, audience (OWNER_ONLY
or BUSINESS), action_id, canonical_id, state and decision. Prefix account/source IDs
consistently. Supply canonical_id only when the underlying commitment identity has
actually been reconciled. A previous bundle can be passed with --previous.

WAIT decisions need waiting_on, next_step and check_at or check_trigger. DEFER needs
a resume date/trigger. DONE needs evidence=owner-reported or source-evidence and an
evidence_ref. Conflicting duplicates and stale-evidence state updates are refused.

Text can be truncated visibly; it is not complete evidence. Packing telemetry uses
characters, not token savings. Decision progress describes this review's decisions,
not obligations completed or the percentage of the entire inbox checked.

A model-pack record without a decision is evidence awaiting semantic review. Its default OPEN state is not an accepted Gmail Action label or a notification decision.
