# AIOS operating manual

This is the English source for the owner's local `AIOS-INSTRUCTIONS.md`. During onboarding, rewrite it in the owner's language, keep the fixed file and folder names in English, and replace generic examples with examples from their confirmed context.

The local manual is a map, not a second copy of the method. Keep it short and link to the detailed files under `00-system/aios/`.

## What this folder does

Your AIOS is a folder of plain files that gives an AI continuity. A new chat can read who you are, what matters now, what the system knows, which methods it can run, and which outside systems it may touch.

| Layer | Open it when |
|---|---|
| `CONSTITUTION.md` | identity, direction, boundaries, permissions, or working style changes |
| `02-memory/` | adding facts, history, people, projects, evidence, or reflections |
| `03-skills/` | you want a repeatable method rather than a one-off answer |
| `04-tools/` | connecting email, drive, analytics, a calendar, or another system |
| `05-focus/` | deciding what matters now, what success means, or what to stop doing |
| `06-archive/` | something is finished or replaced but still needs to remain traceable |

Say **AIOS instructions** at any time. The assistant should reopen this file and link to it instead of making you remember the commands.

## The most useful first actions

### Correct the constitution

Say: **Update my constitution: ...**

The assistant reads the current file, shows the exact proposed change, and waits for approval before editing a confirmed fact. Use this when the system gets something about you wrong, your direction changes, or a new boundary must hold in every session.

### Add memory

Say: **Remember this in my AIOS: ...**

The assistant decides which memory node owns the fact, shows the destination, and writes it there. It links the new detail from that node's CONTEXT file. A chat is not durable memory until the fact exists in a file.

### Run an AIOS Deep Dive

Say: **Run AIOS Deep Dive**, or ask for self-reflection questions, self-coaching, or help understanding your larger potential.

The assistant opens [`DEEP-DIVE.md`](DEEP-DIVE.md). In the owner's local manual this link becomes `00-system/aios/onboarding/DEEP-DIVE.md`. It starts with what is already known, lets you speak freely, asks one focused question at a time, and returns a confirmed map of strengths, patterns, constraints, values, and direction.

### Build an AIOS Business Profile

Say: **Build my AIOS Business Profile.**

The assistant opens [`BUSINESS-PROFILE.md`](BUSINESS-PROFILE.md). In the owner's local manual this link becomes `00-system/aios/onboarding/BUSINESS-PROFILE.md`. It creates one seven-part profile for one business or substantial project and ends with a clear one-sentence introduction: who you are, who you help, which problem you solve, which result you create, and how.

### Run an AIOS Personal Audit

Say: **Run my AIOS Personal Audit.**

The assistant opens [`PERSONAL-AUDIT.md`](PERSONAL-AUDIT.md). In the owner's local manual this link becomes `00-system/aios/onboarding/PERSONAL-AUDIT.md`. Your command is permission to inspect your public web presence. It announces what it will search, verifies that results belong to you, cites the pages it uses, and separates evidence from interpretation before anything is saved.

This is not `AUDIT7`. Personal Audit examines how you appear online. `AUDIT7` checks whether the AIOS machinery, files, and tools are still honest and working.

### Empty a brain dump

Say: **Here is a brain dump**, then write or dictate without organising it.

The assistant saves the raw dump first. It then separates facts, decisions, ideas, questions, and possible tasks. Nothing becomes a commitment just because it appeared in the dump.

### Decide what matters now

Say: **Review my focus** or **What should I do next?**

The assistant reads the constitution, relevant memory, and `05-focus/_focus-CONTEXT.md`. It should challenge a new idea when it conflicts with the stated priority, not merely add it to a longer list.

### Turn good work into a skill

Say: **Make this repeatable.**

The assistant extracts the trigger, inputs, steps, approval gates, output, and definition of done into one skill file. A skill is useful when the next run is more reliable than remembering the old chat.

### Connect a tool

Say: **Connect this AIOS to ...**

The assistant first explains what access is needed, what the connection may read or change, where credentials live, and what still works without the connection. It never stores passwords or secret keys in these Markdown files.

## How to work safely

- Ask before sending, publishing, paying, deleting, changing access, or overwriting confirmed content.
- Facts found online stay `NOT CONFIRMED` until you confirm them.
- One fact has one source. Other files link to it instead of keeping competing copies.
- Current numbers and dates carry a date or a live source.
- The assistant reads an existing file before editing it and reports the exact path it changed.
- A tool is not considered connected because a document says it is. It is connected after a live read-only test succeeds.

## If a new chat knows nothing

Check that the chat is attached to the correct root and that `AGENTS.md` sits beside `CONSTITUTION.md`. Ask the new chat to read both files. If the client has a project-instructions field, use:

```text
Read CONSTITUTION.md in this folder before answering anything in this project.
When I ask how to use my AIOS, open AIOS-INSTRUCTIONS.md.
Do not change facts in either file without my approval.
```

Then test again with a question only your constitution can answer.

## The full library

The copied public method lives in `00-system/aios/`. Its reusable methods are in `00-system/aios/skills/`; the five-layer explanations are in `00-system/aios/references/`; the full eleven-step build is in `00-system/aios/onboarding/_proj-onboarding.md`.

Do not install every skill. Keep the few that solve repeated work, and leave the rest as a library until a real need appears.
