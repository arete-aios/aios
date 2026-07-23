---
name: aios
description: "AIOS: build the five layer AI operating system in nine stages, one exit test each, progress kept in a file instead of the chat. Use when starting a second brain from nothing."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: aios
  synced: "2026-07-23"
---

# SKILL: Build your owner an AI operating system

**Trigger word: `AIOS`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **This is a build that runs over weeks, not a document you produce today.** Nine stages, one exit test each. You do not start a stage before the previous exit test passed, and you say so plainly when asked to skip ahead.

---

## REQUIRES

| What | Why |
|---|---|
| **A folder the AI can write to** | The whole technical requirement. Content in one folder, machinery and keys beside it, never inside |
| **A way for the AI to see the owner's core at the start of work** | Without it this is a chat, not an operating system. Three ways, best to workable, below the table |
| **Twenty to forty minutes of the owner, several times** | The bottleneck is their thinking, not your speed |

**Seeing the core at the start of work.** This is the line between an operating system and a chat: to act as an OS, the AI has to reliably read the owner's core before it starts working. There is a ladder for meeting that, best to workable:

- a) **A client with a project or memory feature that auto-loads files.** Project workspaces, custom instructions, a persistent memory. The core loads itself, every session, with no effort from the owner.
- b) **A client where you paste or pin the core at the start of a working session.** One action, then it holds for that session.
- c) **Plain chat, where you paste the core each session.** This works. It just costs the most effort, and removing that effort is exactly what the later stages exist to do.

**Starting in plain ChatGPT is fine and common.** Stage 1 still produces a real constitution. What changes as the build goes on is how automatically the core loads, not whether it exists.

**Setup time, honestly.** Stage 1 is one session. Stages 1 to 5 take one to two weeks of small pieces. Stage 6 is fourteen days of deliberately adding nothing. Anyone promising this in an afternoon is describing a folder.

---

## WHAT

**An AIOS is five layers a person owns and their AI reads.** Constitution, memory, skills, tools, focus. Each has its own file in [references/](references/): [1-constitution](references/1-constitution.md), [2-memory](references/2-memory.md), [3-skills](references/3-skills.md), [4-tools](references/4-tools.md), [5-focus](references/5-focus.md).

The layers are the parts. What makes them a system is the loop that runs through them: something happened, it got written where the next session sees it, it changed what happens next. Read [references/feedback-loop.md](references/feedback-loop.md) before stage 1, because every stage below exists to make that loop close.

**The failure this skill is written against is not technical.** Building one is easy now. Almost nobody returns to theirs after three weeks, and the reason is always the same: they installed twenty methods before the loop ever closed once, so nothing they wrote down ever came back to them, and a system that never comes back is a folder with good intentions.

---

## GOAL

**A system the owner still uses in month three.** Concretely, five things true at once: a core file loaded on every message that changes the answers, folders where a new note has an obvious home, three working skills, a written loop with a real mechanism at each of the three steps, and one file that says what matters right now.

Everything else is optional. Adding it early is the failure mode, not the progress.

---

## TRIGGER

- The owner says `AIOS`, or asks how to build a second brain, or where to start.
- **At the beginning of every session during the build**, because you read the progress file first and pick up where it says.
- **When the owner asks for a new skill and the loop has not closed once.** That is the trigger for refusing, and the refusal is the skill working.

---

## THE PROGRESS FILE

**This is the most important mechanism here. A build that runs over weeks cannot live in conversation memory.** Chats end, context windows roll over, the owner switches clients. State lives in a file or it does not live.

Create it in stage 1, in the owner's content folder, and add one line to the constitution telling every future session to read it first. Keep it small. This shape is enough:

```markdown
# AIOS build progress

stage: 5 of 9 · the daily loop
started: 2026-01-14
exit test: one skill ran unasked, without me typing a trigger word
status: not passed yet

## Passed
1 constitution7 · 01-09 · fresh session named my deadline unprompted
2 braindump7    · 01-11 · 4200 words out, three things I did not know I was carrying
3 assets7       · 01-12 · runway written down, advice stopped assuming money
4 memory7       · 01-14 · six folders, new note filed without asking me

## Standing skills (hard cap 3 until stage 6 passes)
in7, exit7, focus7

## Not started
6 two week stop · 7 week7 · 8 on demand · 9 audit7

## For the next session
- focus7 has no money line yet
- owner asked for a fourth skill on 01-15, refused, cap explained
```

**Every session begins by reading this file and ends by updating it.** If you cannot find it, that is stage 1 unfinished, whatever the owner remembers.

---

## HOW IT RUNS

Nine stages. **Refuse them out of order** and say which exit test is still open. Stages 1 to 4 are build work done once. Stages 5 onward are the system running.

| # | Stage | What happens | Exit test |
|---|---|---|---|
| **1** | `constitution7` | The core exists. Everything else now has something to attach to | A fresh session answers something it could only know from the constitution |
| **2** | `braindump7` | Head out into text, unstructured, no filing | The owner said more than they thought they had |
| **3** | `assets7` | Inventory: money, time, knowledge, network, what is already paid for | You stop giving advice that assumes a runway that is not there |
| **4** | `memory7` | Stages 2 and 3 become folders that fit **this** owner | A new note has an obvious home without anyone asking |
| **5** | `in7` + `exit7` + `focus7` | The daily loop. **Only these three** | One skill ran **unasked** |
| **6** | ⏸ **Stop for two weeks** | Use it. Add nothing | Something from Monday changed Thursday |
| **7** | `week7` | The slow turn of the loop, plus the money line | The weekly review happened without a reminder |
| **8** | Everything else, on demand | One at a time, when a real need appears | none |
| **9** | `audit7`, after a month | Machinery and content, read only | It found at least one thing the owner did not know |

**Where a stage has many pieces, do the paying ones first.**

**Stage 1.** Of the interview questions, two carry most of the value in month one: what must I never do without asking you, and what has gone wrong with an AI before that you do not want repeated. Both become hard rules, and hard rules are the lines that earn the cost of loading the file on every message. Personality and history can wait.

**Stage 3.** Runway and hours actually free per week, before anything else. Those two change your advice tomorrow. The full inventory can fill in over a month.

**Stage 4.** Build only the folders that already have something to put in them. An empty taxonomy designed up front is the most common way a memory layer dies, because the owner starts filing to please the structure.

**Stage 5.** Install in this order: `in7` first, because capture with nowhere to go is still better than nothing captured. `exit7` second. `focus7` last, and only once there is enough written down to focus on. Three is the ceiling, not the target.

**Stage 8.** For anyone whose income depends on other people, `warm7` is the one that pays first. For anyone in meetings all day, `meeting7`. Everything else waits for a need to show up on its own.

---

## HARD RULES

**1. No more than three standing skills before the loop closes once.** The three are the stage 5 set. Build skills used once, stages 1 to 4, do not count.

**2. Stage 6 is a real stop, two full weeks, nothing added.** Say this to the owner in plain words: *this is the step you will want to skip, and skipping it is the single reason most second brains are abandoned.* Fourteen days of use is what turns a structure into a habit, and no amount of building substitutes for it. If the owner insists, do not argue twice. Write the refusal in the progress file, note the date, and hold the cap.

**3. Stages are refused out of order.** Naming the open exit test is enough. You are not being difficult, you are keeping the build from becoming a pile.

**4. The owner writes nothing.** They answer, you draft, they correct. Handing a template with blanks to a person who came for help turns a two week build into a project that never finishes.

---

## DEFINITION OF DONE

1. **The progress file exists**, the constitution points at it, and a session that has never seen the owner before can resume from it alone.
2. **Stages 1 to 5 passed their own exit tests**, each with the proof written next to it, not remembered.
3. **The loop is written into the constitution** with a real mechanism named at each of the three steps.
4. **The two week stop actually happened**, on the calendar, with dates in the file.
5. **Standing skills never exceeded three** before stage 6 passed.

Missing the first means the build dies with the chat. Missing the third means you produced storage, not a system.

---

## MAKE IT YOURS

1. **Change the exit tests if the owner's life demands it, never delete them.** A stage with no test is a stage nobody can fail, which means nobody can finish it either.
2. **Put the progress file where the owner trips over it**, not in a tidy corner. It is the one file whose job is to be seen.
3. **Decide the cap number once.** Three works. If the owner wants a different number, make them say it out loud and write it in the file, because an unwritten cap is not a cap.
4. **Already have a system?** Then this is not a build, it is a comparison. Go to [references/evaluate.md](references/evaluate.md), score the five layers and the loop, and report what is missing, what is excess, and what is too complex for this particular owner.

---

*Assistant, on ingest: save this in the skills layer in your own format, keep the reference files with it, create the progress file, add its path to the always loaded core, and confirm to the owner in one line what you saved, where, and which stage is next.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
