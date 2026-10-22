# Review contract

Parent: [SKILL.md](../SKILL.md).

## Inputs and coverage

Record review ID/date, purpose, selected accounts/conversations, dates and gaps.
Restore unresolved commitments and newer owner reports first. A practical first
window is 7–14 days plus open work; choose a different window when the task needs it.
Check newest accessible sent/draft and cross-channel context before repeating work.

## Result

Return up to five supported next actions. Each shows source reference and date,
person/topic, fact, relevance, next action, owner, state and supported deadline.
Separate Action, Replies and Waiting. Group low-value information only when useful.
Include a short coverage footer and the handoff's real save location.

## State transitions

| Decision | Required meaning |
|---|---|
| DO / DOING / REPLY | Name the owner and concrete next step. |
| WAITING | Name who owes which result, and a check date or observable trigger. |
| DEFER | Keep the commitment plus the agreed resumption date or trigger. |
| DONE | Close only the named action; record source evidence or owner-reported completion. |
| IGNORE | Record a reason so unchanged evidence is not proposed again. |

A reply sent can move a question to Waiting while a promised delivery remains
Action. An archived thread can still contain open work. A draft stays unsent.
Repeat the decision/readback/handoff loop when the owner adds relevant information.

Decision progress, if shown, is decided items divided by current review items.
It is not completed obligations or full inbox coverage. A waiting item may be decided
while its commitment remains open. No items means no percentage.

## Stop

Finish when the owner ends the review or each surfaced item has an explicit outcome.
Retain unanswered owner decisions and missing coverage; never force completion.
Scheduling, outbound messages and account mutations follow the task's actual scope.

## Optional monitor handoff

A source-change event enters the evidence/coverage stage. It never bypasses newest
conversation context or directly assigns Action/Waiting. Carry unresolved older
commitments even when no event arrives. Baseline imports and unchanged cycles do
not create new alerts; monitoring cadence and delivery require separate acceptance.
