# CC7 Health demo

Maple Briefs is a fictional editing studio used to test the public AIOS starter with **B + JĀ + CC7**. The dates are from the test run on 2026-11-13. Each evidence link opens the relevant sample record below.

| Health section | Last audit | Scope and result | Evidence |
| --- | --- | --- | --- |
| Constitution | 2026-11-13 | Checked the five layers, owner approval rules, and startup links. Both startup links resolved. | [Sample constitution](#sample-constitution) |
| Memory | 2026-11-13 | Followed the Memory index to the business profile and checked its goal against the constitution. | [Memory index](#memory-index), [business profile](#business-profile) |
| Skills | 2026-11-13 | Matched all five installed files and their registered versions to the local public library. | [Skills index](#skills-index), [EXIT7 method](#exit7-method) |
| Tools | 2026-11-13 | Checked that the Tools index records local file access and that its Health link opens the same page as the onboarding map. | [Tools index](#tools-index) |
| Focus | 2026-11-13 | Followed the first-brief priority to its active project and the next check. | [Focus index](#focus-index) |
| EXIT7 feedback loop | 2026-11-13 | Two sample briefs omitted the reviewer. After simulated approval, the next brief used the updated checklist and named a reviewer. | [Improvement record](#improvement-record), [follow-up brief](#follow-up-brief) |

## Evidence from the sample files

### Sample constitution

`CONSTITUTION.md` names Constitution, Memory, Skills, Tools, and Focus. Changes to the constitution and the addition of a tool or automation require owner approval. The test opened the startup links to `ONBOARDING.md` and `AIOS-INSTRUCTIONS.md`. The recorded goal was:

> Deliver twelve edited briefs in twelve months.

### Memory index

`02-memory/_memory-CONTEXT.md` points to the [Maple Briefs profile](#business-profile) and the sample brief records.

### Business profile

From `02-memory/businesses/maple-briefs/business-profile.md`:

> New editing studio for software teams. Goal: twelve briefs.

### Skills index

The installed versions in `03-skills/_skills-CONTEXT.md` matched the local library in the test.

| Method | Version |
| --- | --- |
| EVAL7 | 1.0.1 |
| EXIT7 | 1.1.0 |
| CONTEXT7 | 1.0.1 |
| MEETING7 | 1.1.0 |
| FOCUS7 | 1.1.0 |

### EXIT7 method

The installed EXIT7 1.1.0 method required the improvement to stay pending until a later task verified its effect. [Read the EXIT7 feedback loop](../../exit7/SKILL.md#feedback-loop)

### Tools index

`04-tools/_tools-CONTEXT.md` records “Local files only” and links to Health. The test opened the same local page through this link and the link in `ONBOARDING.md`.

### Focus index

`05-focus/_focus-CONTEXT.md` lists “First client brief” and links to the [brief quality project](#improvement-record), which tracks the check on the next brief.

### Improvement record

The brief quality project recorded a repeated gap: both sample briefs had a goal and neither named a reviewer. The proposed checklist change was:

```diff
 - Goal
+- Reviewer
```

The test applied the change after simulated approval. The record stayed pending until the next brief used the revised checklist. On 2026-11-13, that result was verified and linked from the onboarding map.

### Follow-up brief

The third sample brief was generated from the revised checklist:

```text
Goal: Prepare the editing brief
Reviewer: Sample reviewer
```

[Set up CC7 Health in your own B starter](../SKILL.md#set-up-once)
