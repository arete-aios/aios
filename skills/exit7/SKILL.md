---
name: exit7
description: "EXIT7: close a work session by finding everything that exists only in the chat and handing back ready-to-approve diffs, not questions. Use when the owner says they are done for the day."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: exit7
  synced: "2026-07-23"
---

# SKILL: Close a session so nothing survives only in the chat

**Trigger word: `EXIT7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With write access:** you produce the diffs and, on approval, write them yourself. If the owner's system is also under version control, the session inventory comes free from the changed files list.
**Without write access:** you rebuild the inventory by rereading the conversation and hand back copy-ready blocks with the destination named for each one. Same discipline, the owner pastes. The moment storage exists, the skill upgrades itself with no rewrite.

| What | Needed | How to connect |
|---|---|---|
| **A place to write** | required | Files or structured notes. Anything the next session will actually load |
| **Version control** | strongly recommended | [git-scm.com/docs](https://git-scm.com/docs). The changed files list is the mechanical half of the inventory, for free |
| **An index checker** | recommended | Whatever script the owner's system already has for verifying that new files are listed in their parent index. It gets run here, not trusted |
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

**The session ends with either a clean confirmation, or a short numbered list of things that are still only in the chat, each one already written as the exact line to add and the exact place it goes.**

The owner approves with one word. Nothing from the session survives only as scrollback.

Where each item goes is the owner's structure, not yours. Take it from their constitution and their existing files. If a thing genuinely has no home, say so and propose one, rather than inventing a folder at the end of a long day.

---

## TRIGGER

- The owner writes `EXIT7`, or says something that means closing time: we are done, that is it for today, wrapping up.
- **The end of any session that produced a decision**, even a short one. Length is not the test, output is.
- **Before a break long enough that the context will be gone**, in practice anything over a day.

**Not a trigger:** EXIT7 is not a summary of the day for the owner to read. It is a diff to approve. If you find yourself writing a pleasant recap of what a good session it was, you are running the wrong skill. It is also not a mid session checkpoint, because a gate that fires five times a day stops being a gate.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill is the closing valve between a conversation and the other four layers, so almost all of its judgment is routing, and **routing is entirely the owner's structure**. A decision goes to the project file, a number to the topic file, a changed priority to the focus layer, a promise to a person into wherever people live. Read the constitution for that map, and for the part that decides how you behave here: what may be written without asking, and what must always wait. A closing routine that writes freely is not a convenience, it is an edit the owner never reviewed, made at the least attentive moment of their day.

Read the focus layer too, because it holds the current goal, and this skill is where a new idea either gets written down or quietly becomes tomorrow's work. That call is not yours to make from the enthusiasm in the room.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Primary skill, triggered most days:** put it in the always loaded core, the part read at the start of every session. A closing skill usually earns this, because it fires at the end of every working session by definition.
**Occasional:** put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
EXIT7 at session close. Find everything that lives only in the chat, come back with ready diffs not questions, verify the index actively, then ask whether the focus layer changes. No new work. Spec: skills/exit7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**This skill writes into the structural layer**, the places the next session will actually load: the topic files, the project files, the focus layer.

**What it does not write:** the raw journal of what happened. That lives in the daily memory layer and is written elsewhere. Two different jobs, and confusing them produces a second diary that nobody reads and that contradicts the first one within a month. One records events, this one records what changed.

**What rots:** open questions. An item captured as a question the owner never answered stays true for about a week and then becomes noise that every future reader skips. Give each one either an answer, a date, or a deliberate deletion.

### TOOLS

Version control makes step one nearly free, since the changed files list is the session inventory. Any index checker the owner's system has gets run here rather than trusted. With no tooling at all the skill still works, you just rebuild the inventory by rereading the session, which is slower and less reliable.

The layer is called Tools because a tool is what the model finally calls. Today it usually arrives as an MCP server or a connector the client installs. Name the mechanism when you use one, and do not let the mechanism rename the layer.

> 🔒 **Approved lines only, and nothing new.** Write what the owner said yes to in this message, and not one item more. No new file, no new project, no helpful extra edit that seemed obvious while you were in there. This is the moment of the day with the least attention left in the room, which is precisely why it is the wrong moment to write anything unreviewed.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Collect the inventory.** What did this session create, change, discover or decide? Take the mechanical part from the file diff if you have one, and the rest from the conversation itself: decisions, numbers, dates, names, discoveries, promises made out loud. Promises are the ones that vanish most often, because nobody thinks of them as content.

**2. Run the four hanging checks.** Was something written in the chat, a draft, a list, an analysis, that exists in no file? Did you ask a question the owner never got around to answering before the topic moved on? Was something decided in conversation that no file knows about? Did a "we should" appear with no owner and no date? Each hit becomes a numbered item.

**3. Verify the index actively, do not ask about it.** For every node the session touched, check that each new file is listed in its parent index, and that status changes are recorded in the right master file. Run the checker if one exists. Asking "is anything missing?" always returns no, because the owner does not hold that map in their head, which is the entire reason this step exists. Do not return a clean result until it is actually clean.

**4. Ask the one focus question.** Does anything here change what the owner is working on right now: a shift in priority, a new critical date, a discovery that changes direction? Respect the size limits of the focus layer, and send overflow into the log rather than deleting it. If the change touches several areas, hand it to the dedicated focus update routine instead of doing it here.

**5. Come back with diffs, never with questions.** Each item states the file, the section, and the exact line to add. The owner replies OK to all, OK to some, or no to one. Partial approval is normal and expected. A question puts the work back on the person who just spent the session doing it.

**6. Refuse new work.** If the session surfaced a new idea or a new project, write it down and do not start it. This is a gate against novelty, not a door into it. When the owner floats optional polish of the system itself, answer whether it is worth it, not only whether it is possible, and say plainly when it would eat the one goal that pays.

**7. Do not invent hanging items, and never reconstruct content you no longer hold.** If a draft from earlier in the session is gone from your context, name it and ask for it back. Regenerating a plausible version of it is worse than losing it, because the owner cannot tell the difference. If the session was short and clean, say so in one line and stop. A manufactured five point list, produced to look useful, is exactly the performative helpfulness that makes a closing ritual get skipped after two weeks.

---

## DEFINITION OF DONE

1. **Every hanging item is either written, or explicitly declined by the owner.** Nothing is left in the maybe state.
2. **Each written item landed in a file the next session loads**, not in a note about the session.
3. **The index check came back genuinely clean**, having been run rather than asked about.
4. **The focus question was asked and answered**, even when the answer was no change.
5. **Anything with a date is in the task or calendar layer**, not only in prose.
6. **Nothing new was started**, and any new idea left the session as one written line.

A clean session ends at one line of confirmation. That is a valid result and should be reported as one, without inventing work to justify the run.

---

## MAKE IT YOURS

1. **Add a weekly variant.** On the owner's review day, also offer a draft of whatever public or group commitment they owe, one win and one next step, since the end of a session is where it naturally falls.
2. **Set your own hanging checks.** Four is a working set. If the owner keeps losing a specific kind of thing, contacts, invoices, follow ups, add a fifth check for it, and delete any check that never fires.
3. **Decide what you may write unasked.** Some owners want the obvious mechanical items, an index line, a status flag, written without a round trip, and only the judgment calls held back. Agree that boundary once and write it into the constitution line, because guessing it every evening is how the ritual becomes tiring.
4. **Set the size of a normal run.** If the list is regularly longer than five items, the problem is upstream: things are not being written when they happen. Say that out loud rather than getting better at the cleanup.
5. **No file system at all?** Produce the numbered diffs as copy ready blocks and tell the owner where each one goes. Same discipline, manual paste.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
