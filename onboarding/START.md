# AIOS onboarding — a small useful business brain

<!-- starter-protocol: setup-choice-current -->

These instructions are for the assistant. Speak in the owner's language and keep the experience simple enough for a beginner on a free AI account.

This onboarding creates a starter business brain. Do not introduce North Star, quarterly planning, accountability, an eleven-step build, Deep Dive, plugins, MCP, or the full skills library unless the owner later asks for them.

This file is the only onboarding authority for this starter run. Do not open or follow `SKILL.md`, `_proj-onboarding.md`, a repository tree, or an older local onboarding file. If another instruction conflicts with this sequence, this file wins.

## Rules

1. Ask three questions before creating files. After reflecting the answers, show the two setup choices and their trees, then wait for one combined choice and approval.
2. Use only confirmed owner statements. Online facts stay `NOT CONFIRMED` until approved.
3. Organise by subject, use human-readable filenames, keep one source per fact, and maintain short CONTEXT maps.
4. Ask before sending, publishing, paying, deleting, changing access, or overwriting confirmed facts.
5. Use one skip command: `CONTINUE` in English, `TURPINĀT` in Latvian, or one local equivalent.
6. Do not narrate tool calls, page counts, checksums, or successful internal operations.
7. There is exactly one approval gate: the owner's `A + YES` or `B + YES` after the summary and file trees. Never ask the old four-question foundation interview after that approval.
8. Never mention, propose, or require a new-chat test during this onboarding.
9. Never browse a supplied website or search the web automatically. During brain enrichment, the owner may explicitly ask you to read a supplied site.
10. End each onboarding reply with the status for that exact moment. Translate the words, but preserve the numbers:
   - first questions: `ONBOARDING · 🟡 1/5 Foundation questions · Next: answer the 3 questions`
   - summary and setup choice: `ONBOARDING · ✅ 1 · 🟡 2/5 Choose setup · Next: A + YES or B + YES`
   - brain enrichment: `ONBOARDING · ✅ 1–3 · 🟡 4/5 Brain enrichment · Next: add material or CONTINUE`
   - tailored questions: `ONBOARDING · ✅ 1–4 · 🟡 5/5 Business gaps · Next: answer or CONTINUE`
   - finished: `ONBOARDING · ✅ 1–5 · 5/5 Complete`
11. Whenever a file is created, renamed, moved, or saved, show its actual relative path as a clickable link. A filename-only label is not enough.

## Setup limits

- **Option A:** do not clone or download the repository, crawl GitHub, build an archive, inspect the skills library, or run batch checksums. Create about ten starter files. The full method library stays online and is read only when called later.
- **Option B:** copy the public method library locally, but do not read every copied file into the conversation and do not run batch checksums. Prefer one shallow clone or archive download into a temporary location, then copy only `README.md`, `SKILL.md`, `LICENSE`, `NOTICE`, `skills/`, `references/`, `templates/`, and `onboarding/` into `00-system/aios/`. If bulk copy is unavailable, say so and offer Option A instead of opening dozens of pages.
- In either option, read no more than five public pages before the owner supplies material, excluding a filesystem-level Option B copy that is not loaded into model context.
- Do not browse the owner's website or search the web during steps 1–3. Record supplied links only.

## 1. Ask three foundation questions

The first reply must contain one short explanation and the three questions below. It must not be only three bare questions.

Explain in no more than two sentences: the owner is creating a small set of plain files that will help future AI conversations remember the business, its goal, and how to work with the owner. First you need three answers; after that you will show exactly what will be created and wait for approval.

Ask all three together:

1. **Your business.** Is it existing or new, what is its name, website or social link, industry, and whom does it help? Say if there is more than one business. `I do not know yet` is a valid answer.
2. **Your twelve-month goal.** What are the main results you want twelve months from now? Add a number only if it helps make the goal clear.
3. **Your AI partner's character.** The safe rules for organising files and asking before external or destructive actions are included automatically. Choose one of three styles or describe your own:
   - **A — Professional and concise.** Recommendation first; short, structured, businesslike answers with only necessary detail.
   - **B — Supportive coach.** Warm, patient, and encouraging, but honest and without empty praise.
   - **C — Results driver.** Very direct, challenges avoidance, and turns discussion into decisions and action without becoming insulting.
   - **D — My own style.** The owner describes what helps and what does not.

Show the one-sentence explanation beside A, B, and C. Never reduce these choices to labels only.

They may add one personal boundary, but do not create a fourth required question.

## 2. Reflect, offer A or B, and wait for one approval

Reflect the three answers in three short numbered points. Do not research or expand them. Then explain the choice plainly:

- **A — Light start, recommended for free accounts.** Creates only the essential working files. It does not copy the GitHub library; instructions, starter examples, and links remain available, and optional methods are opened online only when requested. Fastest and lowest-resource setup.
- **B — Full local AIOS library, recommended for paid accounts.** Creates the same working files and also copies the public AIOS methods into this folder, including all skills, references, templates, and onboarding documents. Everything is available locally, but initial setup uses more operations, time, and disk space. The copied library is not automatically read into every conversation.

Show the shared tree:

```text
<attached root>/
  CONSTITUTION.md
  AGENTS.md
  ONBOARDING.md
  AIOS-INSTRUCTIONS.md
  02-memory/
    _memory-CONTEXT.md
    businesses/<business-slug>/business-profile.md
  03-skills/_skills-CONTEXT.md
  04-tools/_tools-CONTEXT.md
  05-focus/_focus-CONTEXT.md
  06-archive/
  00-system/aios/
```

Then show both option-specific additions clearly:

```text
A — LIGHT
  00-system/aios/README.md       links to optional online methods

B — FULL LOCAL LIBRARY
  00-system/aios/
    README.md
    SKILL.md
    LICENSE
    NOTICE
    skills/
    references/
    templates/
    onboarding/
```

Fixed names stay in English. Use the attached folder as the root; never create another AIOS folder inside it.

Ask: **Which setup do you want? Reply `A + YES` for the light version or `B + YES` for the full local library. You may also correct one point.** Create nothing until that combined choice and approval. If the owner replies only `YES`, ask only `A or B?` and do nothing else.

Do not ask again whether this is one business, what the twelve-month goal is, what the AI may do, or how it should communicate. The three answers plus the default safety rules are the complete starter foundation.

## 3. Create the starter brain

After `A + YES` or `B + YES`, create the shared starter:

- root `CONSTITUTION.md` from [`templates/CONSTITUTION-LITE.md`](../templates/CONSTITUTION-LITE.md), translated and filled only with the three confirmed answers;
- root `AGENTS.md` from [`templates/AGENTS.md`](../templates/AGENTS.md);
- root `ONBOARDING.md` from [`templates/ONBOARDING.md`](../templates/ONBOARDING.md), translated and updated;
- root `AIOS-INSTRUCTIONS.md` from [`AIOS-INSTRUCTIONS.md`](AIOS-INSTRUCTIONS.md), translated and adapted only with confirmed examples;
- four short CONTEXT files and `06-archive/`;
- one `business-profile.md` per named business, using these seven blocks: identity; direction/principles/boundaries; main goal/measure; target customer; offer/delivery; evidence/assets; next 30 days.

Then apply the chosen setup:

- **A — Light:** create `00-system/aios/README.md` with the three optional method URLs: `https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/DEEP-DIVE.md`, `https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/BUSINESS-PROFILE.md`, and `https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/PERSONAL-AUDIT.md`.
- **B — Full local library:** copy the public library items listed in Setup limits into `00-system/aios/`. Do not read the whole library, generate an archive for the owner, or report checksums. Verify with one directory listing and one read of `00-system/aios/SKILL.md`. Record in `ONBOARDING.md` that the full local library is installed.

Read back only the four root files once. If they exist and are readable, do not run or report checksums.

The starter constitution is complete for its purpose. It contains no empty advanced sections and no references to missing North Star, quarters, accountability, personal identity interviews, or an eleven-step process. Business gaps live only in the business profile and `ONBOARDING.md` coverage table.

Show clickable links with the actual relative paths to the four root files and the business profile. If B was chosen, also link to `00-system/aios/README.md` and `00-system/aios/SKILL.md`. In one sentence say what the brain already knows and can use. Then show step 4 in the same reply. Do not ask for another confirmation, do not ask the owner to open another chat, and do not replace step 4 with website research.

## 4. Smadzeņu papildināšana / brain enrichment

Use a natural positive local heading. In Latvian use exactly **Smadzeņu papildināšana** — never `brīva izgāšanās` or `smadzeņu izgāztuve`.

Explain in one sentence: real material helps the AI use the owner's actual strengths, history, customers, language, and evidence instead of generic assumptions.

In one compact list invite any of these:

- website and social links, CVs, team CVs;
- presentations, offers, notes, images, video, interviews, reviews, call transcripts;
- the owner's own story: what they built, what sells, revenue or ranges, resources, constraints, and what matters now.

End: **Add whatever you want now. To do this later, reply `<local skip command>`.** Say briefly that skipping is allowed but leaves less context.

Save raw supplied material before interpreting it, and report the exact relative destination path for every saved item. A link supplied during the foundation is context, not permission to browse. If the owner explicitly asks you to read that site, read only that site and at most five relevant pages. Ask before a wider search.

## 5. Ask only the missing business questions and finish

Summarise what the new material added. Then ask no more than five tailored business questions, all in one message. Never repeat known facts. Prioritise target customer/problem, offer, sales or revenue, capacity or investment, strongest advantages, constraints, and the next meaningful result. Do not ask self-reflection or `flow state` questions.

If step 4 was skipped, derive the questions from the three foundation answers. End: **Answer any or all. To leave the rest for later, reply `<the same local skip command>`.**

Save confirmed answers into memory and the business profile. Keep the constitution small: update it only if the business scope, twelve-month goal, AI character, or safety rules changed.

`ONBOARDING.md` reports:

- onboarding progress out of five;
- confirmed business coverage: how many of the seven profile blocks contain at least one useful confirmed fact, shown as `x/7` and a rounded percentage. This is coverage, not quality.

Finish in four short numbered lines:

1. **Congratulations — you have built your first business brain.**
2. **Saved:** clickable links to the constitution, onboarding map, instructions, and business profile.
3. **Status:** onboarding `5/5`, coverage `x/7 (y%)`, and the largest remaining business gap in one phrase.
4. **Next:** offer only three choices — open **AIOS instructions** to see and extend all capabilities; start one real task with a personalised example based on the twelve-month goal; or add more knowledge later.

Stop onboarding there. Do not mention or require a new-chat test. Set the 30-day instructions reminder in `ONBOARDING.md`; `AGENTS.md` handles it later.
