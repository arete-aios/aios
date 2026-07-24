---
name: braindump7
description: "BRAINDUMP7: empty a capture file into real homes, under a rule that nothing there becomes a task until the owner says so. Use when the dump has grown past reading."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: braindump7
  synced: "2026-07-23"
---

# SKILL: Empty the brain dump without creating obligations

**Trigger word: `BRAINDUMP7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Working file mode** needs one text file you can read and edit line by line. The dump shrinks after every run, because you remove what has been filed.
**Paste mode** needs nothing. The owner pastes the contents, you return the same numbered table with one destination per block, and they file it and delete the lines themselves.

Start in whichever mode today allows. The sorting is the value in both, and the rule below about tasks holds in both.

| What | Needed | How to connect |
|---|---|---|
| **One capture file** | required | Any plain text or markdown note. The only rule is that there is one of them, not four. It has to be openable and writable in about four seconds, or nothing lands in it |
| **Line based read and edit** | required for working file mode | A file tool in the client, or the reference filesystem server: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) |
| **Read access to the memory layer** | strongly recommended | Without it you can sort, but every destination you propose is an area rather than a place, and the owner still has to do the filing |
| **Voice to text on the phone** | optional | Built into most phones and keyboards. A large share of what lands in a dump file is dictated while walking, and it arrives with the words run together |

**Check your connectors before you write code.** File access often arrives as an MCP server or as a connector the client installs, which is a connect and approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** Two minutes to create the file, and that is the entire setup. The first real cleanup, on a pile that has been growing for months, takes twenty to forty minutes, most of it the owner reading a table and saying yes. After that a run is a few minutes. The habit takes about a week to trust, and it only forms if the first run does not hand back a list of new obligations.

---

## WHAT

**A capture note stays honest only as long as writing in it commits the owner to nothing.**

The dump file is where they throw unformatted text: a thought, a quote, a link, half an idea, a dictated stream at midnight. It is deliberately unstructured. Without a skill to empty it, it grows into a graveyard nobody reads. With the wrong skill, one that files and assigns eagerly, it becomes a source of guilt and gets abandoned. This one walks the line between those two failures.

**What an AI does wrong without it is specific, and it happens on the very first run.** Handed a pile of raw lines, an assistant does what it is good at: it reads them as intent, groups them into themes, and returns a plan. One line saying the water meter needs replacing comes back as a three step project with a deadline. Nothing is wrong with any single step, and the effect is that the owner now owes the system something for every stray thought they had.

The next midnight they think twice before writing. Within a fortnight the raw thinking that made the file valuable is gone, replaced by lines that look acceptable in a task list. **The file is still there and it is no longer worth reading**, which is a harder failure to notice than an empty one.

---

## GOAL

**Every block has found a home, a date, or the bin, and the owner still trusts the file enough to write there tonight.**

A block ends in one of three states: filed permanently in the memory layer, marked as waiting for a future date, or removed as no longer relevant. **The file is shorter after every run than it was before.** That second half is not decoration, it is the test. A run that produced a beautiful analysis and left the pile intact did nothing.

**What counts as a permanent home is the owner's structure, not yours.** Read their memory layer before proposing anything. If they have no structure yet, do not invent one mid-run: hand back the sorting, say plainly that destinations need somewhere to land, and treat building that as separate work.

---

## TRIGGER

- `BRAINDUMP7` alone: show what is inside, change nothing.
- `BRAINDUMP7 process`, optionally with a topic: propose one destination per block, then wait.
- `BRAINDUMP7 clean`: archive the whole pile, again on an explicit OK.

**Not a trigger:** anything else at all. Never touch the dump file without one of these commands, not to tidy it, not to add a note, not while passing through on another task. The file is safe because it is untouched between commands, and the day the owner finds an edit they did not ask for is the day it stops being somewhere they dump.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

The layers carry more weight here than in most skills, because **this is the one place where an AI decides what a stray sentence means.** A destination is real only if you can see the owner's memory layer, so a system without one produces confident filing into folders that do not exist. And the question underneath every single block, is this a task, is answered in the constitution: what the AI may do unasked, what may be scheduled, what needs a word from the owner first. Read both before you touch the first line.

**Watch the focus layer in particular.** A dump line that quietly becomes a priority is the exact failure this skill is built to prevent, and the focus layer is where it would land. Nothing gets promoted there from a dump without the owner saying it in words.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Dumps most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
BRAINDUMP7. My brain dump zone. Show, dispatch by topic, or archive, always on my OK, and a line there is never a task until I say it is. Spec: skills/braindump7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**The dump file is a queue, not an archive.** A block that has been processed is removed from it, otherwise the next run shows the same pile and the skill becomes theatre.

Processed content moves into whichever part of the memory layer owns that topic, or into a project's own file. A clean run moves the whole pile into the dated archive and leaves the file with an empty dump section and its header untouched.

**What does not belong in memory: the raw line, once its content has been filed.** Keeping both means every later search returns the same idea twice, in two wordings, with no way to tell which is current. File the thought, drop the line.

**What rots:** anything carrying a date that has passed, and anything that was interesting on the night and never came up again. Those are removed on a later run, not preserved for safety. A queue that never loses anything is a graveyard with better labelling.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

You need line based editing of one file, and read access to the memory layer so you can propose real destinations rather than vague ones.

> 🔒 **Never rewrite the dump file wholesale.** Edit in place, line by line. Owners type there by hand and by dictation, faster than they think, and a full overwrite destroys content that exists nowhere else. If your platform can only replace a whole file, say so plainly and ask before every write.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Show mode changes nothing.** Read the dump, return a table: number, the block compressed to one line, roughly how old it is, and a guess at which area of life it belongs to. Then stop. No action plan, no list of things you could do. The owner asked for a view, not for work.

**2. Dispatch mode proposes exactly one destination per block.** The destinations are: a file in the memory layer for facts and lasting context, a project's own file when it concerns something active, a new task only under the condition in step 4, the focus layer when it genuinely changes what matters now, which is rare, waiting when the block carries a future date, or removal when it is stale or already done.

**3. Show the table, wait for the OK, execute only what was approved,** then delete the processed blocks from the dump. Partial approval by number is normal. Leaving an approved block in place for safety is not, because that is exactly how the pile stops shrinking.

**4. The hard rule that keeps this alive.**

> **A block in the dump is not a task. It becomes one only when the owner says so, in words.**

You never quietly promote a dump line into a priority, a deadline, or an entry in the focus layer. The dump is safe precisely because writing there binds nothing. Take that away and the owner starts self-censoring, and you lose the raw thinking that made the file worth having.

**5. Do not interpret beyond the text.** If a block says the water meter needs replacing, that is what it says. Do not build a project around it, do not infer motives, do not expand three words into a plan.

**6. Do not tidy before reading.** Typos, run-together words and dictation errors are the normal texture of fast capture. Look for the thought, not the syntax, and never correct the owner's writing back at them.

**7. Clean mode also waits for an OK.** Archive the whole pile with a date, leave the file's header intact, confirm in one line. The owner may well have forgotten what was in there, so show the summary before you archive it, not after.

---

## DEFINITION OF DONE

1. **The file is shorter** than before the run, and every approved block is gone from it.
2. **Each processed block has a named destination:** a real file, a dated waiting entry, or removal. Not an area, not a theme.
3. **Nothing became a task** that the owner did not say out loud should become one.
4. **The dump section keeps its header** and is ready to write into tonight.
5. **One line back:** what moved where, and what stayed because it was not approved.

Missing the first means you held a meeting about a file. Missing the third means the file will be empty next month for the wrong reason.

---

## MAKE IT YOURS

1. **Decide your own destination list.** The six above map to a five layer system. If the memory is a single notebook, collapse them to three and keep the approval gate, which is the part that matters.
2. **Add a review rhythm.** A weekly show run keeps the pile from ageing past usefulness, and it costs almost nothing, because show mode changes nothing.
3. **Set the age at which a block is stale,** and say the number out loud. Six weeks suits most people. Without a number, every old line gets kept out of politeness and the queue never drains.
4. **Pick the trigger word the owner will actually type** at midnight, tired, on a phone. Short wins. Whatever you choose, use the same word in the constitution line and the skills index, or the skill quietly stops firing.
5. **No file access at all? Degrade gracefully.** The owner pastes the dump, you return the same numbered table with one destination per block, and they file it. The value was always in the sorting and in the rule that nothing becomes a commitment without a word from them.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
