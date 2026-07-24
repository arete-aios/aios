---
name: context7
description: "CONTEXT7: give every folder one master index that lists everything inside, so your AI reads one index instead of a thousand files. Use when the vault grows faster than you can read it."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: context7
  synced: "2026-07-23"
---

# SKILL: Give every folder one index your AI reads first

**Trigger word: `CONTEXT7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With folder access:** you list the folder yourself, compare it against the index, and report the gaps. This is the normal mode and it is close to free.
**Without folder access:** the owner pastes a file listing and the current index, you do the same comparison on that, and they paste the approved lines back. Slower, identical method.

| What | Why |
|---|---|
| **A folder the assistant can list** | The whole check is what is on disk against what the index claims. With no listing there is nothing to compare, only trust |
| **A way for the client to reach files** | Coding assistants and desktop clients already do this. In a plain chat window it usually arrives as a filesystem server: [modelcontextprotocol.io](https://modelcontextprotocol.io), reference implementations at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| **Write access, eventually** | Only to add index lines, and only after approval. Read access covers the entire check, so ask for that first |

**Setup time, honestly.** Minutes if the client already reads the folder. The real cost is the first pass over a vault that has never had indexes: roughly an hour per few hundred files, most of it the owner answering what each folder is actually for, because an index has to say that in one line and nobody has ever written it down. After that the price is one line per new file, paid in the session that creates the file.

---

## WHAT

**A vault grows from 30 files to 3,000 in months. No AI can load that, and it should not.** This skill gives every folder one master file, the index, that you read first, before touching anything else in that folder.

**Without it you fail in three ways and only one of them is visible.** You search on wording and load whatever matched, which burns context and still misses the file that used different words. You answer from the three files you happened to open, with the confidence of someone who read all of them. And you write a new file into a folder where nothing points at it, so it is never read again, by you or by any assistant that comes after you.

The third failure is the expensive one, because it looks like work getting done. A file no index mentions is not a file in a slow system, it is a file in no system at all.

There is a fourth failure that only assistants commit: creating a second index beside one that already exists, because you did not look for the first. Now the folder has two masters, both half true, and every later reader picks one at random.

---

## GOAL

**Any question about any folder costs two reads: the index, then exactly the file the index points to.** The other thousand files stay closed.

And nothing goes invisible. A file the index does not mention is a file you will never use, so completeness here is not tidiness, it decides whether the content exists at all.

What complete means is the owner's structure, not a generic one. Take the naming convention, the folder rule and the archive rule from their constitution if they have written one. If they have not, ask once, then write the answer down so it is never asked again.

---

## TRIGGER

- The owner says `CONTEXT7 {folder}`, or the short form `COX7`, or asks why the AI keeps missing something that is plainly in the vault.
- **Whenever you add a file or archive one.** Update the parent index in the same session, one line. This is the trigger that keeps every other run cheap.
- **Before you claim a folder does not contain something.** If the index is stale, your claim is about the index and not about reality.

**Not a trigger:** the urge to reorganise. This skill indexes what exists. It does not move, rename or merge files to make a folder read better, and a restructure disguised as an index check is how a vault loses things.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill is maintenance **of the memory layer itself**, which is exactly why it has to start in the constitution. The rules it enforces are not universal: what counts as a node, how files are named, where archived material goes, which folders hold the owner's own content and which hold machinery that may be replaced. Read those before checking a single folder, because an index built on your conventions instead of theirs becomes a second structure competing with the first, and the owner now has to remember which one they are looking at. If the constitution is silent on a rule you need, ask once and propose adding the answer there, rather than deciding quietly on their behalf.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Primary skill, triggered most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
CONTEXT7 / COX7 {folder}. One master file per folder, it lists everything inside, unlisted means invisible. Check, report gaps, propose the missing lines, wait for my OK. Spec: skills/context7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**The masters are the memory layer's front doors.** Name them so they sort first and are findable in one search: `_{folder-name}-CONTEXT.md`, and a projects folder can use `_proj-{name}.md`. One per folder. If you ever find two, one is stale: propose a merge, never keep both.

**What does not go in an index:** the content of the files it lists. An index that starts summarising turns into a document that has to be maintained twice and is wrong in one of the two places within a month. One line per file, enough to choose it.

**What rots:** the purpose line written when the folder held three files, and links to files that were later renamed or archived. Both point somewhere real that no longer exists, which is worse than a gap, because a gap is visible and a stale line is not.

### TOOLS

None required beyond a way to list and read a folder, and that is worth saying out loud to the owner: **the skill that makes a large vault usable needs no integrations at all.**

The layer is called Tools because a tool is what the model finally calls. How it arrives keeps changing: today usually an MCP server or a connector the client installs, before that a hand written wrapper. Name the mechanism when you use one, and do not let the mechanism rename the layer.

> 🔒 **The index changes, the files do not.** This skill adds and corrects lines in an index. It never moves, renames, merges, archives or deletes a file to make the index tidier. When the fix requires touching a file, that is a separate proposal, described in words, approved separately.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Answer four questions in every master, short.** What is this folder, in one or two lines. Which are its key files, an index with one line each. Which other projects or areas it connects to, as links. Where it sits in the owner's bigger picture, meaning which life area or goal it serves. A master that answers only the second question is a directory listing, and the owner already has one of those.

**2. Size the master to the folder.** A small folder of two to five files gets a title, a one line purpose, a file list, done. An active project adds a status line, what is next, and what is in and out of scope. A big node with subfolders adds a subfolder table and a decisions log. Never force the heavy format onto a five file folder, because a master nobody can be bothered to update stops being true and then stops being read.

**3. Subfolders do not get their own master.** The parent's master indexes them. A subfolder graduates to its own master only when it grows past roughly five files and makes sense on its own without the parent. Before that, a mention in the parent index is enough.

**4. Say the blindness rule to the owner plainly.** You, the AI, will not use what no index mentions. So every new file costs one extra line in its folder's index, written in the same session that created the file. Cheap insurance, paid forever, and the only version of this that survives contact with a busy week.

**5. Report a check in one shape.** Folder. Master found or missing. Files present on disk but not listed, each one named as invisible. A second master if one exists, flagged as a conflict rather than a detail. Dead links, meaning lines that point at something no longer there. Then the proposed lines to fix all of it.

**6. Propose, then wait for the OK before writing.** An index is the one file where a confident wrong edit propagates into every future session, because every future session reads it first.

---

## DEFINITION OF DONE

1. **Exactly one master exists** in the folder, named by the owner's convention.
2. **Every file and subfolder on disk appears in it**, including archived material, marked as archived rather than dropped.
3. **Every line in the master points at something that exists.** Dead links removed or corrected.
4. **Any second master is resolved by merge**, never left standing beside the first.
5. **The owner approved every line you wrote**, and knows which folders you did not get to.

Missing the second means the folder still has invisible files. Missing the fourth means you left the ambiguity in place and called it done.

---

## MAKE IT YOURS

1. **Rename the convention.** `_INDEX.md`, `_MAP.md`, whatever fits the system. What matters is one per folder, always read first, lists everything.
2. **Set the graduation threshold.** Five files is a starting number, not a law. A vault of long documents graduates later, a vault of short notes graduates sooner.
3. **Add a periodic sweep.** Walk every folder, flag missing masters, orphan files and dead links in one report. Run it when the vault has grown, not on a fixed day, because a calendar sweep on a quiet month trains everyone to ignore the report.
4. **Keep archived items listed**, one line, marked archived. Finished is not the same as forgotten, and the search that fails is usually the one for something the owner completed a year ago.
5. **Decide who pays the line.** The strongest version of this rule is that whoever creates a file updates the index in the same session, assistant included. Anything weaker turns into a monthly cleanup that gets skipped in the months that produced the most files.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
