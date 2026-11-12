---
name: exit7
description: "EXIT7: close a work session, save authorised results, prepare diffs for owner decisions, and follow up on improvements. Use when the owner says they are done for the day."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.1.0"
  source: exit7
  synced: "2026-09-16"
  updated: "2026-11-12"
---

# SKILL: Close a session so nothing survives only in the chat

**Trigger word: `EXIT7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With write access:** save work the owner has already authorised and verify the write. For a change that needs approval under the owner's constitution, prepare an exact diff and wait for that approval. Version control can supply the changed files list.
**Without write access:** you rebuild the inventory by rereading the conversation and hand back copy-ready blocks with the destination named for each one. Same discipline, the owner pastes. The moment storage exists, the skill upgrades itself with no rewrite.

| What | Needed | How to connect |
|---|---|---|
| **A place to write** | required | Files or structured notes. Anything the next session will actually load |
| **Version control** | strongly recommended | [git-scm.com/docs](https://git-scm.com/docs). The changed files list is the mechanical half of the inventory, for free |
| **A CONTEXT checker** | recommended | Whatever script the owner's system already has for verifying that new files are listed in their parent CONTEXT file. It gets run here, not trusted |
| **A task or calendar layer** | recommended | Promises made out loud need a date somewhere the owner will see it. A connector or [developers.google.com/calendar/api](https://developers.google.com/calendar/api/guides/overview) |

Several of these arrive as MCP servers or built in connectors rather than something you build. Check what the client already offers first. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** Minutes. Initialising version control takes about a minute and pays back on the first run. The real cost is the first three or four runs, where the list comes back long and slightly uncomfortable because it holds everything that has been quietly dropping for months. That list gets short quickly, and when it does, the skill is working.

---

## WHAT

**A session ends, the chat scrolls away, and the decision made an hour ago never reaches a file, so the next session does not know it happened.**

Chat is temporary. If a decision, a number, a discovery or a status change does not land in a file, it did not happen, because nothing will ever read it again. This skill catches exactly that, once, at the end of the session.

**Without it an AI fails in two directions at once.** It writes a warm summary of the session, which reads well and changes nothing, because a summary in the chat is still in the chat. Or it asks the owner whether anything is missing, and the owner says no, honestly, because nobody holds that map in their head at the end of a working day. Both feel like closure. Neither writes a line.

It is the structural counterweight for an owner who starts a lot and finishes less, and it works because it never relies on them remembering what to save.

---

## GOAL

**The session ends with verified saves, a short list of exact diffs that need the owner's decision, or a clean confirmation.**

Record where each saved item lives. Give pending changes their destination and the decision they need.

Where each item goes is the owner's structure, not yours. Take it from their constitution and their existing files. If a thing genuinely has no home, say so and propose one, rather than inventing a folder at the end of a long day.

---

## TRIGGER

- The owner writes `EXIT7`, or says something that means closing time: we are done, that is it for today, wrapping up.
- **The end of any session that produced a decision**, even a short one. Length is not the test, output is.
- **Before a break long enough that the context will be gone**, in practice anything over a day.

Use EXIT7 once at the close of the work. Hand back the verified saves and the exact diffs still awaiting a decision.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill is the closing valve between a conversation and the other four layers, so almost all of its judgment is routing, and **routing is entirely the owner's structure**. A decision goes to the project file, a number to the topic file, a changed priority to the focus layer, a promise to a person into wherever people live. Read the constitution for that map, and for the part that decides how you behave here: what may be written without asking, and what must always wait. A closing routine that writes freely is not a convenience, it is an edit the owner never reviewed, made at the least attentive moment of their day.

Read the focus layer too, because it holds the current goal, and this skill is where a new idea either gets written down or quietly becomes tomorrow's work. That call is not yours to make from the enthusiasm in the room.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Primary skill, triggered most days:** put it in the always loaded core, the part read at the start of every session. A closing skill usually earns this, because it fires at the end of every working session by definition.
**Occasional:** put it in the skills-CONTEXT file the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
EXIT7 at session close. Save authorised results, verify CONTEXT, show exact diffs for decisions and capture any improvement that needs a follow-up check. Spec: skills/exit7/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**This skill writes into the structural layer**, the places the next session will actually load: the topic files, the project files, the focus layer.

**What it does not write:** the raw journal of what happened. That lives in the daily memory layer and is written elsewhere. Two different jobs, and confusing them produces a second diary that nobody reads and that contradicts the first one within a month. One records events, this one records what changed.

**What rots:** open questions. An item captured as a question the owner never answered stays true for about a week and then becomes noise that every future reader skips. Give each one either an answer, a date, or a deliberate deletion.

### TOOLS

Version control makes step one nearly free, since the changed files list is the session inventory. Any CONTEXT checker the owner's system has gets run here rather than trusted. With no tooling at all the skill still works, you just rebuild the inventory by rereading the session, which is slower and less reliable.

The layer is called Tools because a tool is what the model finally calls. Today it usually arrives as an MCP server or a connector the client installs. Name the mechanism when you use one, and do not let the mechanism rename the layer.

> **Follow the owner's writing permissions.** A specific approval or a standing permission in the constitution covers the work it names. Changes to the constitution require the owner's approval of the exact diff. Propose any other write outside the authorised scope and wait for the owner's decision.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Collect the inventory.** What did this session create, change, discover or decide? Take the mechanical part from the file diff if you have one, and the rest from the conversation itself: decisions, numbers, dates, names, discoveries, promises made out loud. Promises are the ones that vanish most often, because nobody thinks of them as content.

**2. Run the four hanging checks.** Was something written in the chat, a draft, a list, an analysis, that exists in no file? Did you ask a question the owner never got around to answering before the topic moved on? Was something decided in conversation that no file knows about? Did a "we should" appear with no owner and no date? Each hit becomes a numbered item.

**3. Verify the CONTEXT file actively, do not ask about it.** For every node the session touched, check that each new file is listed in its parent CONTEXT file, and that status changes are recorded in the right master file. Run the checker if one exists. Check the nodes this session actually touched, and say that is what you checked. "I verified the whole system" is a claim you did not earn in a closing run. Asking "is anything missing?" always returns no, because the owner does not hold that map in their head, which is the entire reason this step exists. Do not return a clean result until it is actually clean.

**4. Ask the one focus question.** Does anything here change what the owner is working on right now: a shift in priority, a new critical date, a discovery that changes direction? Respect the size limits of the focus layer, and send overflow into the log rather than deleting it. If the change touches several areas, hand it to the dedicated focus update routine instead of doing it here.

**An approved project or task goes to the focus layer, which in this system is `FOCUS7`, and keeps a link back to where it was decided.** Never open a second list of session tasks beside it. An idea that came up is one written line, not an approved project.

**5. Save authorised work and show the remaining diffs.** Verify each saved item and report its path. For each change awaiting a decision, show the file, the section, the exact diff and the evidence behind it. The owner can approve individual changes.

**6. Refuse new work.** If the session surfaced a new idea or a new project, write it down and do not start it. This is a gate against novelty, not a door into it. When the owner floats optional polish of the system itself, answer whether it is worth it, not only whether it is possible, and say plainly when it would eat the one goal that pays.

**7. Do not invent hanging items, and never reconstruct content you no longer hold.** If a draft from earlier in the session is gone from your context, name it and ask for it back. Regenerating a plausible version of it is worse than losing it, because the owner cannot tell the difference. If the session was short and clean, say so in one line and stop. A manufactured five point list, produced to look useful, is exactly the performative helpfulness that makes a closing ritual get skipped after two weeks.

---

## FEEDBACK LOOP

1. **Capture the signal.** A repeated difficulty, a meaningful owner correction, or a failed check can justify one improvement entry. Use the existing project or skill home. Record the layer, evidence, proposed change and how to check its effect. Add further evidence to the same entry when the signal recurs.
2. **Apply it within scope.** Follow the constitution's permissions. Show an exact diff and keep the entry pending whenever a decision is required.
3. **Check the effect in real work.** On the next relevant task, record the outcome and its evidence at the source. Keep the entry pending until that check takes place.
4. **Make the result easy to find.** Update the existing source and its status pointer in `ONBOARDING.md` when relevant. If the owner has set up CC7, show the feedback loop beside the five layers with the latest verified date, scope, result and evidence. Use the actual check date.

## DEFINITION OF DONE

1. **Each item has a recorded outcome.** It is saved, awaiting a specific decision, or declined by the owner.
2. **Saved items live in their existing homes** and their contents have been checked after writing.
3. **The CONTEXT check has run for the touched scope.** Any unresolved result has a destination and next step.
4. **Focus reflects accepted decisions** and due commitments appear in their agreed task or calendar source.
5. **Improvement entries show their real state.** A proposed, applied or verified change has the corresponding evidence and next step.

A clean session ends at one line of confirmation. That is a valid result and should be reported as one, without inventing work to justify the run.

---

## MAKE IT YOURS

1. **Add a weekly variant.** On the owner's review day, also offer a draft of whatever public or group commitment they owe, one win and one next step, since the end of a session is where it naturally falls.
2. **Set your own hanging checks.** Four is a working set. If the owner keeps losing a specific kind of thing, contacts, invoices, follow ups, add a fifth check for it, and delete any check that never fires.
3. **Record any standing maintenance permission in the constitution.** State which categories and files it covers, such as verified CONTEXT links or source-backed status updates. Apply that permission within its recorded scope.
4. **Set the size of a normal run.** If the list is regularly longer than five items, the problem is upstream: things are not being written when they happen. Say that out loud rather than getting better at the cleanup.
5. **No file system at all?** Produce the numbered diffs as copy ready blocks and tell the owner where each one goes. Same discipline, manual paste.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills-CONTEXT file, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
