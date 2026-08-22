---
name: north7
description: "NORTH7: build the accountability system that connects a north star to what you do on a Tuesday, and make it come back at you unasked. Use in week one, before daily capture starts running."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.1"
  source: north7
  synced: "2026-08-22"
---

# SKILL: Build the thing that holds you to what you said

**Trigger word: `NORTH7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **This is a build skill. It runs once, and then it gets out of the way.** It creates six files and one block in the constitution. After that the accountability loop uses `in7`, `week7` and `focus7` as they become available. The guided build seeds them before this run; the staged build may install them afterwards. Run this skill again at a quarter, or when the north star changes. **It gets no trigger line in the constitution**, because a build skill that runs once does not need to be read on every message, and putting it there would make it standing under this method's own definition.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**File mode:** you can write to a folder. You create the six files, add the constitution block, and the system reads itself from then on.
**Chat mode:** there are no files. The same six files become six named blocks in one document the owner keeps, and they paste it at the start of a session. Same headings, same rules, same tables, and they do the filing. Say plainly what that costs: the return only happens when they paste, so in chat mode the calendar carries the trigger instead of the loaded file. Moving to file mode later changes who saves the entry, not the method.

| What | Needed | How to connect |
|---|---|---|
| **One place read at the start of a session** | required | Project instructions, a memory feature, a pinned file, or a paste the owner does themselves. If nothing loads automatically, agree with the owner what they paste and where that decision is written down, because that decision is part of the run |
| **A calendar** | strongly recommended | The review slot and the quarter date. In chat mode it is not a convenience, it is the trigger. [developers.google.com/workspace/calendar](https://developers.google.com/workspace/calendar/api/guides/overview) |
| **Mail, read only** | recommended when a goal names mail as its evidence | Whatever connector the client offers, or the provider's own API |
| **A sheet** | optional | Evidence for any goal whose test is a number. [developers.google.com/workspace/sheets](https://developers.google.com/workspace/sheets/api/guides/concepts) |
| **A scheduler** | optional, the top rung | Scheduled tasks in the client, or cron on a machine that stays on. This is the only way anything arrives without the owner opening something |

**Check the client's connectors before you build anything.** Several of these arrive as MCP servers or ready connectors, which turns a build step into a connect and approve step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Say the price out loud.** The project and memory features that make situation A work are on the paid plans of the products that offer them, and a scheduler needs either a hosted client or a machine that stays on. Situations B and C below are the free paths, they are real, and the method does not change between them. Only who does the filing changes.

**Setup time, honestly.** Forty to sixty minutes for the build, and almost all of it is the owner deciding three things: the north star sentence, what would show it happened, and what they stop doing to make room. The files take you minutes. If the north star has not been chosen yet, this run is twenty minutes and it leaves that line NOT SET on purpose.

**When it starts being worth something.** The ledger is not interesting until something in it has come due, so about two weeks. It is genuinely useful at one quarter, because that is the first time there is a column to count.

---

## WHAT

**A north star written in January and a Tuesday in March have nothing connecting them, and nothing in a normal second brain ever builds that connection.**

The goal gets written into a focus file. The day gets written into a weekly file. Both are true, neither is wrong, and no line anywhere says what was promised, when it was due, and whether it happened. So the weekly review audits last week's decisions from memory, which is the one thing the weekly review is not supposed to do.

**Without this an AI fails in two directions.** It agrees with whatever is in front of it, because it has no record of what was promised three weeks ago and no way to notice that this is the fourth week the same thing has not moved. Or it over-corrects into a tracker, opens every session with a status report, and gets switched off inside a fortnight.

**There is a third failure and it is the one that produces a confident record of a quarter that did not happen.** The owner writes what they wish were true, week after week, and the assistant marks it kept because the owner said so. Nothing in the file is a lie. Every row is a true record of something someone said. The reading is invented, it has a date on every line, and it will be believed in a year. The whole evidence column exists because of this failure.

---

## GOAL

**The owner's north star has a check date on it, and something written on Monday reaches them on a Thursday without them going to look for it.**

Seven things are true when this has run:

1. **A north star sentence with a date it was chosen**, or an honest NOT SET and a ledger row for choosing one.
2. **At most three goals**, each serving that sentence, each with an observable test and a next action. One goal is the normal number in the first months.
3. **At least one goal whose evidence lives outside these files**, in mail, a calendar, a bank, a repository or a sheet, or an explicit written statement that none does.
4. **A ledger with rows in it**, each with a check date and an evidence source.
5. **`OPEN.md` exists, is under one screen, and is read at the start of a session.** Proven this run, not assumed.
6. **The owner has said which of the three return mechanisms is theirs**, and it has been set up in this session rather than described.
7. **The current weekly file exists**, with `Days`, `Detail` and `Review`, so daily capture and weekly review point at a real shared record.

---

## TRIGGER

- The owner writes `NORTH7`, or asks where they stand, what they promised, or why nothing is moving.
- **Week one, after the memory layer exists and before any daily method starts writing.** The skill files may already be seeded; present is not running. This is the ordinary trigger. There is nothing to hold anyone to before the folders exist, and there is nothing worth capturing daily until there is a goal it feeds.
- **The quarter.** Runs as the reset, inside the weekly review, not as a separate ritual.
- **The north star changed**, or a weekly review produced decisions and there was nowhere to write them.

**Not a trigger: a bad week.** Rebuilding the system is the most satisfying possible way to avoid the work the system exists for, and a week where nothing moved is exactly when it is most tempting. Say so in one line and run the weekly review instead.

**Not a trigger: the middle of a week.** The north star does not change on a Wednesday. Write the thought down and bring it to the quarter.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill is step three of the loop given a file and a date. Capture already works and storage already works; what is missing is the thing that comes back. Read [references/feedback-loop.md](../../references/feedback-loop.md) before you run this, because the test at the end of that file is the test for this skill.

Read the constitution first for two reasons. The owner's hard rules decide what you may write without asking, and a system that writes commitments into a permanent record unasked is worse than one that asks twice. And the standard for a good week is theirs, not yours: if it is written down, use it, and if it is not, ask once and store the answer.

### CONSTITUTION

**This skill adds a block to the core and does not add a trigger line for itself.** The block is the mechanism: it is read before the owner asks for anything. The skill is a build step and lives in the skills CONTEXT file with the others that wait.

```
## Accountability

North star: {sentence and chosen date, or not chosen yet} · detail 05-focus/north-star.md
Read 05-focus/OPEN.md before you answer the first message of any session.
While the ONBOARDING block is still in this file, say nothing here.
Once it is gone, say something about OPEN.md only when one of these is true, then say it in one line
at the end of the reply and stop: a check date in OPEN.md is today or past; the last day line in the
current ISO-week file under 05-focus/accountability/weeks/ is three or more days old; today is my review day and this week's review has not run;
the quarter ends within seven days.
If none of them is true, say nothing about it and answer what I asked.
If OPEN.md has a future `paused until` date, or its state is stopped, stay silent.
Whenever you do raise it, offer three answers and accept any of them: carry on, postpone, stop.
A pause always takes a date, seven days if I do not name one.
If I say stop, set OPEN.md to `state: stopped` and stay silent until I explicitly say
`ACCOUNTABILITY`. That word returns it to `state: running`; it does not change a ledger row.
```

**The silence rule is the load bearing half.** Without it every session opens with a status report, and a status report at the top of every session is the thing people switch off in week two.

**The line about the onboarding block is the other half.** Two blocks in one file, both speaking at the end of the first reply, both offering carry on, postpone or stop, is a question nobody can answer, because neither the owner nor you can tell which one they answered.

Say the size of the block in tokens when you add it. It is paid for on every message for the rest of the year, and the owner should see the number rather than a feeling about it.

### MEMORY

**The ledger is memory and it is never cleaned.** One file per quarter, rows appended, format frozen for a year. Comparability is the entire asset, and reordering or tidying a ledger destroys it silently.

**The day lines go into one weekly file shared with `in7`.** Reuse it if it exists; otherwise create the current ISO-week file under `05-focus/accountability/weeks/`, for example `week-2026-W34.md`. Open one new file when the ISO week changes. Do not create a second daily file. Two records of the same week contradict each other inside a month and there is no way to choose between them afterwards.

**What rots:** the goal files. A goal whose next action has not changed in three weeks is either finished, blocked or abandoned, and all three are worth writing down. Say which one you believe and why.

**What moves up:** almost nothing. A closed quarter's ledger goes to the archive and stays listed in the CONTEXT file. Only a north star that was reached or abandoned earns a line in long term memory, with both dates.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. Today that usually arrives as an MCP server or a connector the client installs. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

File read and write is the only hard requirement. The evidence sources are what make the difference between a system that can be argued with and one that cannot, and **the goal decides which connector is worth setting up**, not a list. Whichever source the P1 goal names is the first one to connect. The rest wait for a goal to name them.

> 🔒 **You never write an outcome the owner did not state or you did not verify.** Blank is a legitimate value in every column. `kept (verified)` requires that you looked at the evidence, and a row whose evidence is `none` can never take that word. Nothing from the ledger goes into a message, a post, a shared document or a third party tool without the owner asking for that specific thing. This file holds what someone promised and did not do, and it is the last one that should ever be pasted somewhere for convenience.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Ask whether the north star exists, and do not invent one.** If it has been chosen, take the sentence in the owner's exact words and the date it was chosen. If it has not, write NOT SET, say plainly that this is the honest state, and make choosing it the first row in the ledger. **Ask the owner for that row's check date rather than setting one.** The owner is allowed to be slow, and a deadline on the one decision the method deliberately leaves undated is not yours to add. A borrowed north star in a permanently loaded file is worse than an empty line, because everything downstream quietly aligns to it. In either case, update the `North star:` line in the Accountability block to the same state; never leave the active block with an older north star than `north-star.md`.

**2. Write the six files, filled rather than empty.** They are `north-star.md`, `_accountability-CONTEXT.md`, one `_goal-<slug>.md`, the current quarter ledger, `OPEN.md`, and `weeks/week-<YYYY-Www>.md`. Use the matching repository templates where they exist. Every file gets its parent line, its purpose line, its working fields or table headings, and a dated log line at the bottom. **An empty file teaches the owner that this is a form to fill in later, and later does not arrive.** Every unfilled line reads NOT SET, and NOT SET is never replaced by a plausible guess. That includes `rank`, `check rhythm`, the drop order and `serves`: ask, or leave them.

**3. Take at most three goals, and make each one name its evidence before you write it down.** One is the normal number in the first months. The evidence field is where this skill either becomes real or stays decorative. Ask the question directly: if you did this, what would show it, somewhere that is not this folder. Mail, calendar, bank, repository, sheet, invoice, a published page. **If none of the goals can name an outside source, say so out loud rather than lowering the standard.** The owner may keep the goal anyway, and then it is written as `source: I type it in every week`, which is a legitimate answer written as one rather than a gap.

**4. Turn the next action of P1 into today's line in `OPEN.md`.** Not tomorrow's plan and not a list. One action, small enough to finish in a day, phrased so the owner knows afterwards whether they did it.

**5. Pick the return mechanism with the owner and set it up in this session.** Three, and one of them is theirs. The file that loads at session start. The calendar event with the paste block in its description. The scheduled run, where the client allows one. **Describing the mechanism is not setting it up.** If it is the calendar, the event exists before this session ends, with the block already in the description.

**6. Prove the check fires, before you call the run finished.** Open a fresh session and ask something unrelated. Either the assistant mentions the due row, or it correctly says nothing because nothing is due, and you can show which of the four conditions it evaluated. **This is the step that separates an accountability system from a folder with dates in it**, and it is the one that gets skipped, because writing the files feels like the work. The wiring is the work.

**7. Register the running behaviour with the three methods that will do it.** One line into `in7` about the `p1` field and the ledger check. One line into `week7` about reading the ledger first. `focus7` gets the diff at the weekly review and keeps the dated table. If one is not installed yet, write its exact pending registration into the skills CONTEXT file and apply it when that method arrives; do not claim you edited a file that does not exist. You do not write a fourth daily routine, and this does not change the standing trio chosen by the surrounding AIOS build.

**8. Hand back one line and stop.** What was created, where, and which of the four conditions will fire first. No summary of the session, no encouragement, no list of what could be added next.

---

## WHAT RUNS AFTERWARDS

**The session start check.** Read `OPEN.md` before answering the first message. Speak only when a check date is today or past, or the last day line is three or more days old, or it is the review day and this week's review has not run, or the quarter ends within seven days. Otherwise say nothing and answer what was asked. When you do speak: one line, at the end of the reply, about the file, the smallest next step, and the three answers, carry on, postpone, stop. A pause always takes a date, seven days by default.

**The daily.** `in7`, unchanged, one message. The owner's cost is the message they already send. Add the `p1` field to the day line: the thing that touched the P1 goal in the owner's words, or the word `nothing`. `nothing` gets written and gets no comment, because a system that reacts to every zero teaches people to stop typing zeros. Check the message against ledger rows due today or earlier and fill outcome and evidence where the message names one, marking `kept (verified)` only if you looked at the evidence. Write tomorrow's one thing into `OPEN.md` from the P1 next action. Hand back at most three lines.

**The weekly.** `week7`, unchanged, with the ledger audit first. Read the day lines, the due rows, the goal next actions and **the outside sources the goals name, before asking anything**. Hand back the audit table with outcomes filled from evidence, one line per goal saying how many of the days logged this week had something in the `p1` field out of how many days were logged at all, what the outside source shows next to what the week's own words claimed, at most three new commitments written as ledger rows with check dates and evidence sources, and the diff handed to `focus7`. Then rebuild `OPEN.md` from the ledger.

**Why that is different from a journal nobody rereads.** The owner is never asked to read last week, they are asked to correct a draft that already read it. The output is rows with dates whose next reader is a machine, so the record gets read whether or not the owner ever rereads it, and it gets read against something. And it ends by writing into a file that loads next session, which is step three of the loop, which is the step everybody leaves out.

**The quarterly.** The weekly review on the thirteenth week, one hour ceiling, three extra questions, no new trigger word. Is the north star still it: still it, finished, or wrong, and all three are normal. Close the ledger with counts and report the one number, how many commitments came due with an evidence source already named. Set at most three goals for the next quarter and ask for the drop order now. Archive the ledger, open the next one, and write the next quarterly date into the focus file's dated table. Not into `OPEN.md`: that file is derived from the ledger and a real world deadline written into it is a second copy that will age apart from the first.

---

## WHEN IT BREAKS

**Days one and two missed: nothing.** No mention, no gentle note. One missed day is not a broken run. The finding this follows is on the record: Lally, van Jaarsveld, Potts and Wardle, European Journal of Social Psychology, 2010, found that missing one opportunity to perform a behaviour did not materially affect habit formation.

**Day three: one line, about the file.** Backfill from memory, leave the gap, or pause the daily for a week. All three are complete answers. A backfill is marked as written from memory rather than on the day, because a remembered day and a logged day are different evidence. A gap left as a gap is a real record and it is not filled in with a plausible reconstruction. Then do not come back to it.

**A missed review: one line on the review day.** Two missed in a row: ask whether the day is wrong, before asking anything else. A slot that has been missed twice is worth checking before the person is.

**Three missed weeks: do not catch up.** Never run three reviews at once. Do three things instead. Read the three weeks from the records that exist anyway, the calendar, the sent folder, the changed files, the money, and hand back three lines of history rather than three reviews. Then open the ledger, show what is still `open`, and ask the question that is actually being asked: are these still wanted. Not why they were not done. Marking four rows `dropped` with a date is a good week's work, and `dropped` is in the fixed vocabulary for exactly this. Last, offer the one line version below, and write down which version was chosen so nobody pushes the full one at someone who has already declined it.

**Never:** a streak, a missed day counter, an opening line about how long it has been, or any sentence about discipline or consistency as a property of the person. The reason is published: Kluger and DeNisi, Psychological Bulletin, 1996, pooled 131 papers and found that over a third of feedback interventions decreased performance, and their explanation is where the attention lands. Feedback that points at the task tends to help. Feedback that points at the person tends to hurt, because attention moves off the work and onto the self. **A missed day counter points at the person by construction.** So the system does not have one, and every line it says is about a row, a date, a file or a piece of evidence.

**Stopping is allowed and it is written down.** `stop` gets a dated line and the check goes quiet. The file says in one sentence how to start again. A system nobody is allowed to leave is one people leave silently.

---

## HOW IT COMES BACK, WHICH IS THE HARD PART

**Start with what is true: you cannot start a conversation.** You have no way to reach anyone. Every design that pretends otherwise ends up depending on the owner remembering, which is the thing being fixed.

**The check date is what makes this possible at all.** A commitment written on Monday carries a date. Every session start compares today against those dates. That turns coming back from a push problem, which is unsolvable here, into a read problem, which is solved by one line in the constitution. Nothing else in this design matters as much as that sentence.

**Situation A, a client that loads files by itself.** Project instructions, a memory feature, a workspace that reads a folder. The trigger is the session opening: the core loads, the block fires, you read `OPEN.md` and check the four conditions. The owner opened the chat to ask about something unrelated, and the first thing they hear at the end of the reply is that Tuesday's commitment came due yesterday. That is literally unasked. **What it costs:** `OPEN.md` is read on every message, so it has a one screen ceiling and a silence rule, and these features are usually on a paid plan. **What fails:** nothing fires if they never open a session, and nothing here reaches a phone.

**Situation B, a client where the core gets pasted or pinned once per session.** The trigger is the paste, and the payload rides along with it, because in this situation the core and the open file are one paste. They paste it in order to do some other piece of work, and the check fires anyway. **What fails:** a session where they do not paste is a session where nothing checks. That is normal and it is not worth fighting. The next paste catches it, because the dates did not go anywhere.

**Situation C, plain chat.** The honest rung, and the free one. **The trigger is a repeating calendar event, and the paste block lives in its description.** One event, weekly, on the review day, plus one at the quarter. The description holds the block: the north star, the goals, `OPEN.md` and the rows that are due. The owner opens the event, copies the description, pastes it into a chat and types `WEEK7`. **The calendar is the alarm and the description is the payload.** Setting it up takes about ten minutes once. The daily version is the same trick, smaller: a repeating reminder at the hour they usually stop working, whose text is the word `IN7` and nothing else. **What fails, and say it out loud:** if they ignore the calendar, nothing happens. There is no mechanism underneath this one. Anyone who tells them otherwise is describing a product they do not have.

**The rung above A, where the client can run something on a schedule.** Scheduled tasks, a cron job, an agent that can send mail. This is the only place where the system genuinely arrives rather than waiting to be opened. At a fixed hour a run reads the goal files and the ledger and writes the result into whichever place the owner already opens. **What it costs:** a hosted client, or a machine that is on. **What fails:** a shut laptop. Say so rather than promising delivery.

---

## THE SMALLEST VERSION THAT STILL WORKS

For someone who will only ever do one thing a day. One file, one line.

```markdown
# NORTH

north star: NOT SET
chosen: NOT SET
the one thing that would show it: NOT SET

## Days

| Date | What moved it |
|---|---|
| EXAMPLE 2026-08-20 | sent the pricing mail |
| EXAMPLE 2026-08-21 | nothing |

Rule: one line a day. The word `nothing` is a real answer and gets written down like any other.
Rule: my words, not tidied.
Rule: when I ask where I stand, read the last ten lines and answer with what is in them. Do not add
encouragement.
```

**There is no weekly and no quarterly.** There is one question the owner can ask whenever they want, and you answer it from the file and nothing else: what has moved this in the last ten days. The answer is a count and the lines themselves.

**It upgrades without a rewrite**, because the day lines are already in the format the weekly review reads. **And it is a legitimate end state.** Someone who runs it for a year and never adds a weekly has a working accountability system.

---

## DEFINITION OF DONE

1. **The six files exist and none of them is empty.** The current weekly file has `Days`, `Detail` and `Review`. Every unfilled line reads NOT SET and no NOT SET was replaced by a guess.
2. **At most three goals, and at least one of them names an evidence source outside these files**, or the absence was said out loud and written down as `I type it in every week`.
3. **The ledger has at least one row**, with a check date the owner chose and an evidence source. If the north star is not chosen, that row is choosing it.
4. **`OPEN.md` is under one screen** and you told the owner its size rather than an impression of it.
5. **The constitution block is in the always loaded core**, with its token cost stated, and with the line that keeps it silent while the onboarding block is still there.
6. **A fresh session evaluated the four conditions**, and either raised the due row or correctly stayed silent. Tested this run.
7. **The return mechanism exists rather than being described.** The calendar event was created, or the file loads, or the scheduled run fired once.

Missing the second means you built a closed circle of self report. Missing the sixth means you wrote five documents. Missing the seventh means the owner has an accountability system that waits for them to remember it, which is the thing they already had.

---

## MAKE IT YOURS

1. **Change the rhythm names.** Daily, weekly and quarterly are a default. Someone whose work runs in two week cycles should have a two week review, and the ledger does not care what the interval is called.
2. **Set your own silence conditions.** Four is a working set. Add one if something specific keeps getting lost, and delete any that fires every day, because a condition that always fires is not a condition.
3. **Add a `Not now` table to `OPEN.md`** if the same rejected idea keeps arriving fresh every three weeks. Two columns, what and since when. Keep it under five rows or it becomes a second backlog.
4. **Decide what may be written without asking.** Some owners want the mechanical rows written straight in and only the judgment calls held back. Agree it once and put it in the constitution line, because deciding it every evening is how a ritual gets tiring.
5. **One line a day is a finished system.** North star, a day line, and the word `nothing` when nothing moved. It upgrades later without rewriting anything.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills-CONTEXT file and not to the constitution, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
