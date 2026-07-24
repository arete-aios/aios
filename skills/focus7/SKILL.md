---
name: focus7
description: "FOCUS7: rebuild the one file that says what matters right now, area by area, from real data, with a diff the owner approves. Use at the weekly review or after a decision that moves priorities."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: focus7
  synced: "2026-07-23"
---

# SKILL: Keep the file that says what matters now true

**Trigger word: `FOCUS7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With data feeds:** you scan calendar, health, money and notes yourself, and the numbers in the file come from measurements rather than impressions. Faster and far harder to argue with.
**Without them:** you run the same thing as a structured interview, one area at a time, one line per answer. Slower, and it still produces a true file, because the diff and the approval are the valuable parts and the feeds only make them quicker.

| What | Needed | How to connect |
|---|---|---|
| **A focus file that loads every session** | required | Whatever your client reads at session start. If it does not load automatically, this skill maintains a document nobody opens |
| **Notes the assistant can read** | required | The per area notes, the weekly file, project files. Usually the same folder access the rest of the system already has |
| **Calendar** | strongly recommended | [developers.google.com/calendar/api](https://developers.google.com/calendar/api/guides/overview), or a connector the client already offers |
| **A sheet for money or metrics** | recommended | [developers.google.com/sheets/api](https://developers.google.com/sheets/api/guides/concepts) |
| **Health or activity export** | optional | Whatever the owner's device vendor provides. A weekly CSV is enough, live access is a convenience |

**Check your connectors before writing code.** Several of these now arrive as MCP servers or as ready connectors inside AI clients, which is a connect and approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** The file itself takes one session. Each feed costs an hour or two of first time authentication and can be added later without changing the method. The first real run is the long one, usually forty minutes or more, because the file has never been cleaned and the owner is deciding for the first time what belongs in it. Later runs land between ten and twenty minutes.

---

## WHAT

**Every second brain grows one file that says what matters right now, and within a month it is a swamp of half true statements nobody trusts enough to act on.**

The focus file is loaded into every conversation, so its errors get repeated all day, in every answer, with confidence. That is the part people underestimate: a wrong line in a normal note is wrong when someone opens it, a wrong line here is wrong in every conversation until someone catches it.

Left alone it rots in two directions. Facts go stale. And long lived material that belongs in a permanent note settles into it until the file is too big to read and too vague to act on.

**Without this skill an AI makes it worse rather than better.** Asked what is going on, it repeats the file. Given something new, it appends, because appending is safe and cutting looks like losing information. The result is a file that grows monotonically and gets less true every week, while sounding more authoritative as it gets longer.

This skill is the scheduled cleaning. It reads what actually happened, proposes a diff, and writes only what the owner approves.

---

## GOAL

**A current focus file, under the size limits, where every line is true today.**

Four things have to hold:

1. **Every line would change within about three weeks.** Anything more durable belongs in a permanent note with a one line pointer here.
2. **Every date appears exactly once**, in one table, and nowhere else.
3. **Nothing is lost.** Anything cut moves into a log with a date, and you report the move.
4. **The owner saw and approved each area** before it was written.

The owner decides what an area is and where the limits sit. Take both from their constitution if it is written there, ask once if it is not, and never quietly invent a seventh area because your draft needed somewhere to put something.

---

## TRIGGER

- The owner writes `FOCUS7`, optionally with one area name to do just that area, or a mode word for a fast pass or a deep pass.
- **The weekly review.** This is the recurring trigger and it is the one that keeps the file small.
- **After a decision or event big enough to change what the owner should be doing.** A result arrived, a plan died, a date moved.

**Not a trigger:** noticing that one line is wrong in the middle of another task. You never rewrite the focus file silently while doing something else, even when you are certain. Flag it in one sentence, carry on with the actual work, propose the diff when the skill runs.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill maintains layer five, and layer five is the only one that cannot be written from its own contents. **What belongs in focus is decided by the constitution, and what is true is decided by memory.** Read the constitution first for the owner's areas, their longer horizon and their stated priorities, because without it you will rank by whatever is loudest in this week's notes, which is how a new idea gets promoted over the thing that pays. Then read memory, because focus is a view of it and not a second copy: every line you write here should be traceable to something that actually happened, in a file, with a date.

Focus is also the second file that costs on every message, after the constitution. Everything else loads only when relevant, so these two are where size is a running cost rather than a one time one, and that is why the limits below are rules rather than preferences.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Primary skill, triggered most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
FOCUS7 [area]. Rescan my life areas from real data, show a diff per area, write only what I approve, move overflow to the logs, never delete. Spec: skills/focus7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**Two homes, and the boundary is the whole discipline.** The focus file holds only the live, changing present. Everything else goes back where it belongs: the per area context note, the project note, the weekly file.

The test for any line: **will this still be true in three weeks?** If yes, it belongs in a permanent note with a one line pointer in focus, not in focus itself.

**What does not belong here at all:** raw daily entries, project debate, anything dated that is not a deadline, and the reasoning behind a decision. Focus carries the conclusion and a link. The reasoning is worth more in the file where the decision lives, where someone will read it on purpose.

**What rots fastest:** numbers, because they were true on the day they were written and nothing marks them as old. Give every number a date at the point it enters, so the next run can tell a current measurement from an old one without asking.

Overflow moves to the relevant log with a date, and you report each move.

### TOOLS

File read and write is all you strictly need. Everything else is a bonus, and you say plainly when you did not have it: a calendar feed for dates, a health export for body numbers, a bank or spreadsheet for money, transcripts or a contact list for people.

The layer is called Tools because a tool is what the model finally calls. Today that usually arrives as an MCP server or a connector the client installs. Name the mechanism when you tell the owner what you used, and do not let the mechanism rename the layer.

> 🔒 **Never invent, never delete.** A missing number gets a visible marker asking the owner, never an estimate. An overflowing area gets its oldest entry moved to a log with a date, never dropped. A guessed number in a permanently loaded file becomes a fact by repetition, and weeks later nobody remembers it was a guess.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Scan, do not remember.** For each area, read its log, its context note, the current weekly file and any project notes belonging to it. The weekly file is usually the richest source, because that is where daily entries and session notes land. Work the areas in parallel rather than as one long sequence. If a source has not changed since the last run, mark the area unchanged and do not inflate it to look busy.

**2. Build a diff per area, never a rewrite.** Three blocks: what the file says now, your proposed draft, and what changed with the source of each change. Naming the source is what lets the owner approve in seconds instead of rereading everything. List additions, edits and removals, including what you propose to drop and where it would go.

**3. One date, one place.** Dates live only in the critical dates table, sorted, four to six weeks ahead, capped at around ten entries. The area says what the thing is, the table says when. A date written in the area, in the table and in the weekly theme is three copies that will age apart and start contradicting each other. The exception is a date that is part of a state rather than a deadline, such as when something started.

**4. Hold the size limits.** Roughly a thousand characters per area, roughly fourteen kilobytes in total. When an area overflows you do not delete, you move the oldest entry to that area's log with a date and report the move. The limits exist because a focus file that grows into a master document stops being read, and an unread focus file is worse than none, since it still loads into every session and still costs on every message.

**5. Never fill a gap with a plausible guess.** If a number is not in the data, write a marker asking the owner. Unknown is a legitimate value and it is the one that keeps the file trustworthy. Same for status.

**6. Approve area by area.** Present all areas plus the dates block in one message, then take short commands: approve these numbers, edit this one with my text, skip that one, approve everything, approve nothing. Write only the approved sections, one clean edit per area, leave the rest untouched, then report what was written, skipped and moved.

**7. Stay out of the structure.** You update live content. You do not touch the file's own instructions block, and you do not change the owner's top level priorities from here, those live in their north star and project notes. A focus skill that starts editing priorities has quietly promoted itself.

---

## DEFINITION OF DONE

1. **Every area is either updated and approved, or explicitly marked unchanged.** No area silently skipped.
2. **Every date sits in one table**, sorted, inside the horizon, and nowhere else in the file.
3. **The file is inside its size limits**, and you told the owner the number rather than an impression.
4. **Everything cut landed in a log with a date**, and the moves were reported line by line.
5. **Every gap you could not fill is visible in the file** as a marker addressed to the owner, not smoothed over.

Missing the fourth means you deleted. Missing the fifth means the file now contains your guesses, and nobody will be able to tell which lines those were.

---

## MAKE IT YOURS

1. **Pick your own areas.** Seven works well because it fits on one screen and forces choices, but the labels should be the owner's life, not a template's.
2. **Set the size limits by how the file actually reads on the owner's phone**, then hold them. Aspirational limits broken every run are the same as no limits.
3. **Set the horizon that matches the owner's pace.** Three weeks suits someone whose situation moves monthly. A slower life can use six, and the test line changes with it.
4. **No integrations at all?** It still works. Run it as a structured interview once a week, ask about each area in turn, and let the owner answer in one line each. The diff and approval flow is the valuable part, the data feeds only make it faster.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
