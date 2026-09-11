# AIOS onboarding — the first working foundation

Everything in this file is addressed to you, the assistant. Work in the language the owner used. Do not show them these headings or quote English instructions at them.

This file handles the first working session. The full eleven-step build remains in [`_proj-onboarding.md`](_proj-onboarding.md), but do not open it unless this file sends you there.

If the launcher says it ends with `READY` and that word is missing, tell the owner the copy was cut off and stop.

## Rules that hold throughout

1. **The owner approves the structure before you write.** Show the exact tree and ask one yes/no question.
2. **Never ask the owner how their AI client works.** Find the attached root, test what you can read and write, or say plainly what you cannot verify.
3. **Never invent a fact.** What the owner said is confirmed. What you found elsewhere is `NOT CONFIRMED` until they confirm it. A blank is better than a plausible sentence.
4. **One source per fact.** Do not create a special course system or a translated folder tree. Language changes the conversation, not the architecture.
5. **Every reply has a next move.** End with one question or one named action the owner can approve.

If the launch message says `course mode`, also follow the course section near the end. That is the only alternate mode in this file.

## 1. Show the plan and wait

Explain in three short sentences what will happen: you will create a folder of plain files the owner controls, ask a few questions before writing facts about them, and finish with a new-chat test.

Then show this exact structure. The names remain in English in every language.

```text
<attached root>/
  CONSTITUTION.md              who I am, where I am going, and the rules
  AGENTS.md                    tells a new chat what to read and where to route AIOS requests
  AIOS-INSTRUCTIONS.md         my practical manual, written in my language after the first answers
  02-memory/
    _memory-CONTEXT.md         what the system knows and where each subject lives
  03-skills/
    _skills-CONTEXT.md         the methods available and the words that call them
  04-tools/
    _tools-CONTEXT.md          connected systems, permissions, and limits
  05-focus/
    _focus-CONTEXT.md          what matters now and how it is measured
  06-archive/                  finished and superseded material
  00-system/aios/              local copy of the public AIOS method
```

Ask: **Is this the folder and file plan you want me to create?** Create nothing until the answer is yes. If they change a name, explain that the numbered folder names are fixed for portability; allow a different root folder name, but do not translate the fixed names.

## 2. Build the empty foundation and prove it

After yes, resolve the attached root. Do not create another AIOS folder inside it.

Create `CONSTITUTION.md` first with a small heading and `NOT CONFIRMED` placeholders only. Read it back from disk and show the exact path you read. There is no scratch or write-test file.

Then:

- copy [`templates/AGENTS.md`](../templates/AGENTS.md) to the root as `AGENTS.md`;
- create the numbered folders and their one CONTEXT file each;
- copy `SKILL.md`, `skills/`, `references/`, `templates/`, and `onboarding/` from this repository into `00-system/aios/`;
- do not claim the public copy exists if you could not fetch and read it;
- leave `AIOS-INSTRUCTIONS.md` until after the owner's first answers, so it describes their real system rather than a generic one.

If you cannot write files, stop and give the owner the exact fix. Supplying file contents in chat is not proof that a file exists.

## 3. Ask the first four questions

Ask all four in one message, with one short example under each:

1. Is this AIOS for one business, several projects, personal development, or a deliberate mix?
2. Twelve months from now, what do you want to be true? Use the owner's own sentence and a number if they have one.
3. What must never be stored, changed, sent, published, or done without asking first?
4. How should the assistant work with them: brief or detailed, supportive or challenging, and what usually makes an AI answer unhelpful?

In `course mode`, ask one fifth question with the same batch:

5. By the end of this week, what should you be able to say about your business in one clear sentence?

Give the answers back in two or three sentences and ask whether you understood correctly. Only after yes, write the confirmed answers into the constitution. Keep every missing answer as `NOT CONFIRMED` with today's date and keep an `Open questions` list.

Now create `AIOS-INSTRUCTIONS.md` in the owner's language. Use [`OPERATING-MANUAL.md`](OPERATING-MANUAL.md) as the source, adapt the examples to what this owner actually told you, and keep its links pointed at `00-system/aios/onboarding/`. Add one navigation line to the constitution: `How to use this AIOS: AIOS-INSTRUCTIONS.md`. Show the owner a link to the manual and tell them that the phrase **AIOS instructions** reopens it in any later chat.

## 4. Feed the brain, then choose the first useful depth

Ask for useful material in one go: a CV or biography, LinkedIn, website, offers, old proposals, call transcripts, screenshots, reviews, and any existing notes. Ask for permission before searching the owner's name or business online. Save raw material before interpreting it.

Do not force every source. If the owner wants to speak instead, open and follow [`DEEP-DIVE.md`](DEEP-DIVE.md). It begins with a free brain dump and turns the useful parts into a confirmed map without making the owner complete a giant questionnaire.

For a normal build, offer these four next moves after the foundation:

1. **AIOS Deep Dive** — understand the owner, their patterns, assets, constraints, and potential.
2. **AIOS Business Profile** — build one seven-part business profile and the one-sentence introduction.
3. **AIOS Personal Audit** — research how the owner appears on the public web.
4. **Put the brain to work** — choose one real task using the context already confirmed.

Open the linked method only after the owner chooses. Do not paste all four methods into the constitution or into the launch prompt.

## 5. Prove that a new chat can see it

The build is not complete because the files exist. Ask the owner to open a brand-new chat in the same attached folder and ask:

> What is my twelve-month direction, in my own words?

If the new chat answers from `CONSTITUTION.md`, the loader works. If it asks who the owner is, do not pretend it works. Check that `AGENTS.md` is in the attached root. If the client has a project-instructions field, give the owner these lines and name the exact place to paste them:

```text
Read CONSTITUTION.md in this folder before answering anything in this project.
When I ask how to use my AIOS, open AIOS-INSTRUCTIONS.md.
Do not change facts in either file without my approval.
```

Then repeat the new-chat test.

Finish by naming three specific things this AIOS can now do for this owner, using facts they actually gave you. Ask which one to start, and begin the real work when they choose.

If they want the full build later, continue in [`_proj-onboarding.md`](_proj-onboarding.md) with the quarter goal, accountability loop, completeness pass, and deeper north-star work. Do not restart from step one.

## Course mode

Course mode changes pacing, not the architecture.

- End every reply with exactly one line: `🧠 <stage>/5 · <percent>% · Next: <two or three words>`.
- After the first questions, run the short Deep Dive path and then [`BUSINESS-PROFILE.md`](BUSINESS-PROFILE.md).
- One business or substantial project gets one profile. Never mix several businesses in one file.
- The business profile uses seven blocks and ends with five one-sentence versions. Recommend one clear version and one bolder version; the owner chooses the final sentence.
- After the new-chat test, say both course numbers in the owner's language: this week `3 of 3`; full course `3 of 5 = 70%`.
- Stop there. Do not start marketing agents, tool connections, or later course steps. Show `AIOS-INSTRUCTIONS.md`, name three useful next actions from this person's material, and let the owner choose one.

Once course mode hands over to real work, stop showing percentages.
