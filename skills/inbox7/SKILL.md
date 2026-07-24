---
name: inbox7
description: "INBOX7: triage the folder where files pile up into file, archive or delete, and move only what was approved. Use when the capture folder has grown too big to open."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: inbox7
  synced: "2026-07-23"
---

# SKILL: Empty the folder where files pile up

**Trigger word: `INBOX7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Operating mode** needs file access: list, read, rename, move. You do the sorting and the moving, the owner approves a table.
**Guided mode** needs only a folder listing pasted in. Same three lanes, same destinations, the owner moves the files by hand.

Start in whichever mode today allows. Moving from guided to operating later changes who drags the file, not the method. The deciding is the expensive half, and it is identical in both.

| What | Needed | How to connect |
|---|---|---|
| **One dump folder** | required | Wherever downloads, screenshots and exports already land. If there are three such folders, pick one and point the rest at it before the first run |
| **List, read, rename, move** | required for operating mode | A file tool in the client, or the reference filesystem server: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) |
| **PDF text extraction** | strongly recommended | `pdftotext`, part of Poppler: [poppler.freedesktop.org](https://poppler.freedesktop.org/). Identifying a document from its first lines costs a fraction of opening it whole |
| **Read access to the memory layer and its index files** | required to file anything | A file that no index lists does not exist to a future AI, so filing without index access only moves the problem |

**Check your connectors before you write code.** File access usually arrives as an MCP server or as a connector the client installs, which is a connect and approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** Minutes if the client already has file access. About an hour for a first filesystem server setup you do yourself, and one package install for the PDF extractor. **The first pass over a folder that has been filling for a year takes thirty to sixty minutes**, most of it the owner reading a table, and it is better done in two sittings than one. Every pass after that is a few minutes.

---

## WHAT

**Every second brain grows a folder where PDFs, screenshots and exports pile up, because filing them properly took one thought too many.** After a month nobody dares open it.

The dump folder is the price of a fast capture habit, and it works only if something empties it. Left alone it becomes a second unsorted hard drive, the owner starts avoiding it, and the capture habit dies with it. This skill does the deciding work, which is the expensive part, and leaves the owner the approving work, which takes seconds.

**Two things go wrong when an AI meets that folder without instructions.** The eager version tidies: it renames and moves on its own judgment, and the owner, who could at least find things by scrolling before, now cannot find them at all. The careful version opens every file to be sure, including forty screenshots, spends a fortune in context, and returns a summary instead of an empty folder. Both end with the folder still full.

**The third failure is quieter and it is permanent.** A file moved somewhere correct but never listed in the index of its new home is gone. A future session will not find it, will not know it exists, and will tell the owner with full confidence that there is nothing on that topic. Filing without indexing loses a document more thoroughly than deleting it does, because it also costs a folder move and looks like work.

---

## GOAL

**An empty or near empty folder, and every file that came out of it either living where the owner will recognise it in a year, or waiting in a clearly labelled delete pile for a human hand.** Nothing moved that the owner did not approve.

**The naming convention is the owner's, and it is settled before the first run.** Date first or topic first both work, and mixing them costs more than either choice. If it is written in their constitution, use that. If it is not, ask once, apply it silently from then on, and write it down where the next session will read it.

---

## TRIGGER

- The owner says `INBOX7`, optionally naming a subfolder.
- **Right after a burst of capture:** a conference, a tax month, a research afternoon that produced thirty downloads.
- **Before anything that needs the folder to be trustworthy**, such as a weekly review or a search for a document that should be in there.

**Not a trigger:** your own initiative, and never as a side task while doing something else. If the folder is empty, answer with one line and stop. Do not invent work.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

Almost nothing about this job is decidable from inside the folder. **A filename tells you what a file is called, not where it belongs**, and the difference is the owner's structure: which topics exist, what is currently active, where finished things go, what a document must be named for them to recognise it in a year. All of that lives in their constitution and memory layer, and reading it first is what separates filing from moving things around.

There is a second reason, and it is the expensive one to learn by accident. **Some file types belong to an automated pipeline** that already ingests them on a schedule. Handle those by hand and you create duplicates, or you take the input away from a process that runs at night. Which types those are is written in the owner's system and is invisible in the folder listing.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Runs it most weeks:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
INBOX7. Triage my file dump folder into file / archive / delete, show a table, wait for my OK, never delete anything yourself. Spec: skills/inbox7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

Files that survive triage go into the memory layer where their topic already lives, and **the same pass updates the index of that node**, because a file no index lists does not exist to a future AI. Finished material and old versions go to a single central archive, dated, and the archive gets a mention at index level too.

The delete pile stays inside the dump folder in a dated subfolder, so that recovery is one move back.

**What does not belong in memory:** the contents of the file, copied out into a note beside it. One document, one home. A summary is fine and useful, a second copy of the same material is how two versions of the truth start.

**What rots:** anything in the dated delete folders once the owner has confirmed the removal, and old snapshots of a process that has since changed. The archive is a record, not a warehouse, and it earns its keep only if what is in there is still recognisable.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

You need to list, read, rename and move files, plus a text extractor for PDFs. Images are the expensive case: identify them by filename and surrounding context first, and open one visually only when a decision genuinely depends on it.

> 🔒 **Never delete a file yourself, no matter how obvious it is.** Approved deletions move into a dated subfolder inside the dump folder, and the owner does the final removal by hand. This one rule is what makes fast triage safe, because it makes every mistake reversible by moving the file back.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Scan once.** List every file, sorted, skipping system junk and skipping any dated delete folder from an earlier run, since those already wait for a human. An empty folder means one line back and nothing more.

**2. Identify each file as cheaply as possible.** PDFs by their first lines, text and markdown by reading them, everything else by name, size and date. When a file type is unclear, ask rather than guess. Never open a batch of images to find out what they are.

**3. Sort into exactly three lanes, nothing else.** FILE means active working material, roughly anything the owner might touch in the next quarter, renamed to their convention and placed with its topic. ARCHIVE means it belongs to a topic as history, or is a snapshot of a finished process. DELETE means a duplicate, an empty export, a transient artifact. Three lanes only, because a fourth lane called maybe later is how the folder refilled last time.

**4. When you cannot decide between ARCHIVE and DELETE, put it in DELETE** with a question mark in the comment and let the owner rule. The archive is not a bin. Filling it for safety costs the owner more than losing a screenshot does.

**5. Show one table and stop.** Number, filename, what it actually is, the lane, the exact destination. Then say plainly that OK approves all of them and OK with numbers approves only those. Nothing moves before the answer arrives. Partial approval is normal, and you execute only what was named.

**6. Never delete a file yourself.** Approved deletions go into the dated subfolder, and the owner removes them by hand. Say that out loud in the confirmation, so nobody assumes the folder is already clean.

**7. After moving anything, update the index of its new home in the same pass.** This is not bookkeeping, it is the difference between a filed document and a lost one, and it is the step that gets skipped when a run is nearly over.

---

## DEFINITION OF DONE

1. **The folder is empty**, or holds only a dated delete folder waiting for a human.
2. **Every filed document sits with its topic**, under a name that follows the owner's convention.
3. **The index of every node you touched names the new file**, in the same session.
4. **Approved deletions are in one dated subfolder**, and the owner has been told the final removal is theirs.
5. **One line back:** how many files, how many in each lane, and what was left undecided and why.

Missing the third means the files are filed and lost. Missing the fourth means you deleted something.

---

## MAKE IT YOURS

1. **Set the naming convention before the first run,** date first or topic first, and let the skill apply it silently from then on. Deciding it per file is how a folder ends up with four conventions and no way to sort.
2. **Name the file types this skill must not touch.** Anything an automated pipeline already ingests gets reported in one line and left alone, because handling it by hand creates duplicates.
3. **Set the quarter rule to the owner's actual horizon.** Active means what they might touch soon, and soon is three months for some people and a year for others. That number decides how much lands in the archive.
4. **Decide how long dated delete folders live.** A month is generous and it keeps the folder from filling with graveyards of its own. Whatever you pick, the owner still does the removal.
5. **No file access at all? Degrade gracefully.** The owner pastes the folder listing, you return the same three lane table with destinations, and they move the files. The deciding work was always the expensive half.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
