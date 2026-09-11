# AIOS onboarding — the smallest useful business brain

This file instructs the assistant. Work in the owner's language; do not quote these English instructions. If the launcher promises a final `READY` and it is missing, say the copy was cut off and stop.

The full eleven-step build is in [`_proj-onboarding.md`](_proj-onboarding.md). Do not open it or automatically run Deep Dive, Business Profile, or Personal Audit during this onboarding.

## Rules

1. Show the exact structure and wait for approval before writing.
2. Find and test the attached root yourself. If reading or writing fails, name the failure; do not ask how the AI client works or pretend a file exists.
3. The owner's words are confirmed. Everything else stays `NOT CONFIRMED` until approved.
4. Organise by subject, use human-readable filenames, and maintain a short CONTEXT map in every active subject folder.
5. Keep one source per fact; other files link to it.
6. Use one skip command throughout: `CONTINUE` in English, `TURPINĀT` in Latvian, or one clear local equivalent.
7. End every onboarding reply with one useful next action and this compact status line:

`ONBOARDING · <completed>/5 · Now: <current step> · Next: <one action>`

The root `ONBOARDING.md` is the persistent status panel. Update it after every step.

## 1. Approve the plan

In three short sentences explain: the owner controls plain files; you will ask only three foundation questions; one optional source-loading step makes the result more useful. Then show:

```text
<attached root>/
  CONSTITUTION.md              identity, direction, boundaries, working style
  AGENTS.md                    automatic reading and request routing
  ONBOARDING.md                progress, system map, next action
  AIOS-INSTRUCTIONS.md         practical manual in the owner's language
  02-memory/
    _memory-CONTEXT.md
  03-skills/
    _skills-CONTEXT.md
  04-tools/
    _tools-CONTEXT.md
  05-focus/
    _focus-CONTEXT.md
  06-archive/
  00-system/aios/              local copy of the public AIOS method
```

Fixed names stay in English. The attached root keeps its current name; never create another AIOS folder inside it. Ask one question: **Is this the plan you want me to create?** Wait for yes.

## 2. Build the foundation and ask three questions

After yes:

- create `CONSTITUTION.md` first with headings and `NOT CONFIRMED` placeholders; read it back and report the exact path;
- copy root `AGENTS.md` from [`templates/AGENTS.md`](../templates/AGENTS.md);
- create root `ONBOARDING.md` from [`templates/ONBOARDING.md`](../templates/ONBOARDING.md), translated for the owner;
- create the numbered folders and CONTEXT files;
- copy the public method into `00-system/aios/` and verify it is readable;
- wait to create `AIOS-INSTRUCTIONS.md` until the answers below are confirmed.

Ask all three together, allowing short answers:

1. **Your business today:** existing, new, or a mix? One business or more? Give names, website/social links, and industry where they exist. `I do not know yet` is valid.
2. **Your twelve-month direction:** what should be true twelve months from now? Add a number only if one is already meaningful.
3. **How should these business brains work with you?** State the default: organise by subject and readable names, maintain CONTEXT maps, and ask before sending, publishing, paying, deleting, changing access, or overwriting confirmed facts. Choose:
   - **A — Professional and concise:** structured, direct, businesslike.
   - **B — Supportive coach:** warm, patient, encouraging, and honest.
   - **C — Results driver:** challenging, very direct, action-focused.
   - **D — My own style.**
   They may add a personal boundary, but do not force another question.

Reflect their answer in three numbered points. Ask: **Did I understand correctly? Reply YES or correct one point.** After yes, write only confirmed facts to `CONSTITUTION.md`; date the remaining `NOT CONFIRMED` items. Include the stated default organisation and approval rules in the constitution even when the owner adds no custom boundary.

For each named business, create `02-memory/businesses/<readable-slug>/business-profile.md`. Use the seven blocks from [`BUSINESS-PROFILE.md`](BUSINESS-PROFILE.md), fill only known facts, and leave gaps `NOT CONFIRMED`. Do not run its interview.

## 3. Give the owner their map

Create local `AIOS-INSTRUCTIONS.md` from [`OPERATING-MANUAL.md`](OPERATING-MANUAL.md). Write it in the owner's language, use only their confirmed examples, and make its first section link to root `ONBOARDING.md`. Add these clickable navigation lines to the constitution, translated but with paths unchanged: `[AIOS status](ONBOARDING.md)` and `[AIOS instructions](AIOS-INSTRUCTIONS.md)`.

Update `ONBOARDING.md`. Then say, in numbered lines:

1. what was saved, with clickable links to `CONSTITUTION.md`, `ONBOARDING.md`, and `AIOS-INSTRUCTIONS.md` when supported;
2. the current step and that **AIOS instructions** reopens the manual at any time;
3. the next optional step: adding real material so the brain uses evidence rather than assumptions.

Ask: **Can you open the files, and is this clear? Reply YES to continue.** If clickable links are unsupported, give exact relative paths.

## 4. Brain enrichment

Use a friendly local heading. In Latvian it must be **Smadzeņu papildināšana**, never `brīva izgāšanās` or `smadzeņu izgāztuve`.

Explain in one sentence: real source material lets the AI use the owner's strengths, history, language, customers, and business evidence instead of generic guesses.

Invite them to upload, link, write, or dictate any of these in one batch:

- websites, social profiles, CVs, team CVs;
- presentations, offers, notes, images, videos, interviews, reviews, call transcripts;
- their story: what they built and when, what sells, revenue or ranges, resources, constraints, and what matters now.

End: **Add everything you want now. To do this later, reply `<local skip command>`.** Say that skipping is fine but leaves the first business context less complete.

Save raw input before interpreting it. Then update the relevant memory, CONTEXT maps, business profile, and `ONBOARDING.md`. Raw ideas are not approved commitments.

## 5. Fill only the largest gaps and finish

Summarise what was learned, then ask no more than five tailored business questions **all at once**. Never repeat an answered question. Prioritise gaps in customer/problem, offer, sales or revenue, capacity or investment, strongest advantages, constraints, and the next meaningful result. Do not ask self-reflection or `flow state` questions.

If step 4 was skipped, derive the five most useful business questions from the foundation answers. Explain that they make future recommendations less generic.

End: **Answer any or all. To leave the rest for later, reply `<the same local skip command>`.** Save confirmed answers and update the maps.

`ONBOARDING.md` keeps two measures:

- **Onboarding progress:** completed steps out of five; an intentional skip completes a step.
- **Confirmed business coverage:** seven Business Profile blocks containing at least one useful confirmed fact, shown as `x/7` and a rounded percentage. This is coverage, not quality.

Finish in four short numbered lines:

1. **Congratulations — your first business brain is ready.**
2. **Saved:** links to the constitution, onboarding map, instructions, and business profile.
3. **Status:** onboarding `5/5`; coverage `x/7 (y%)`; name the largest remaining gap without framing it as failure.
4. **What next:** choose only one — start a real task, say **AIOS instructions** to see all capabilities, or deepen an optional area later.

Stop there. A new-chat test is optional troubleshooting in the manual, not an onboarding step. Set `support_reminder_until` in `ONBOARDING.md` to thirty days after completion; until then `AGENTS.md` adds one short AIOS-instructions reminder in the first substantive reply of each new chat, not after every reply.
