---
name: memory7
description: "MEMORY7: shape the folders that hold everything your AI knows about you, built from your own material and named in your own words. Use once the raw material exists and has nowhere to live."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: memory7
  synced: "2026-07-23"
---

# SKILL: Shape the folders that hold what your system knows

**Trigger word: `MEMORY7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **This skill shapes the memory layer. A different skill maintains it.** `MEMORY7` decides what folders exist, what they are called and what belongs in each, for this one person. `CONTEXT7` keeps that structure honest afterwards: one index per node, nothing orphaned, a periodic audit. Shaping is a decision, maintenance is a habit. Do not do both in one session, and do not let audit rules leak into a design conversation.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With file access:** you read the raw material, create the folders, move everything into them and write the entry files. One session, and the layer exists at the end of it.
**Without file access:** you propose the structure and the filing rules as text, and the owner makes the folders. Slower by an hour, and it works, because the value here is the decisions, not the file operations.

| What | Why | Where |
|---|---|---|
| **A folder the AI can read and write** | The whole technical requirement for operating mode | Whatever your client already reaches |
| **Plain text or markdown files** | The layer has to be readable by the next tool, not only this one | [commonmark.org](https://commonmark.org) |
| **A viewer, optional** | For the owner's comfort. The files work without it | [obsidian.md](https://obsidian.md) · [logseq.com](https://logseq.com) |
| **Version history, optional** | So a restructure can be undone without ceremony | [git-scm.com](https://git-scm.com) |
| **A published scheme, to borrow from and never adopt whole** | Vocabulary, not a template | [fortelabs.com/blog/para](https://fortelabs.com/blog/para/) |

**Setup time, honestly.** Sixty to ninety minutes for the first structure with the material filed into it, and most of that is the owner deciding names rather than you moving files. Then two to four weeks of small corrections, because a name only proves itself the first time a note fails to land in it. Usable after one session, accurate about a month later.

---

## WHAT

**The memory layer is where an AI stops starting from zero.** The constitution says who the owner is and how to behave. Memory is what the system knows: what happened, who is involved, what was decided and why.

Without it an AI does one of two things, and both look fine for a week. It writes everything into one growing file that gets slower and less true every time it is touched. Or it invents a folder per session, so within a month the same fact sits in three places, two of them stale, and the answer to "what do you know about this" is whatever happened to be in context that day.

**The failure worth naming is the copied structure.** Someone watches a video, likes the folder names, adopts them. Week one it looks tidy. Week three they are holding a note that could go in three of those folders, they hesitate, they file it in the inbox, and then they stop filing at all. The structure was not wrong in the abstract. It was not theirs, so every filing decision cost a translation step, and nobody pays that tax for long.

**A memory layer built from a template gets abandoned. One built from the owner's own material gets used.**

---

## GOAL

**A small set of areas, named in the owner's own words, where a new note has an obvious home without anyone having to ask.**

Four things must be true:

1. **The names came from the owner's material**, not from a list. If you could hand the same tree to a second person, you built a template, not their memory.
2. **A new note lands without hesitation.** Hesitation means the structure is wrong, never that the owner is bad at filing.
3. **Content and machinery are separate.** One folder holds the owner's own material and nothing else.
4. **It is plain files**, so the layer survives the tool that currently reads it.

---

## TRIGGER

- The owner says `MEMORY7`, or asks how to organise their notes, where things should live, or what folders they need.
- **When raw material exists and has nowhere to go.** A brain dump and a deep dive produce a pile of true things about a person. This skill gives that pile an address.
- **When you or the owner have hesitated twice about where something belongs.** Two hesitations is a structural signal, not bad luck.
- **When one folder has grown past scanning.** That is how the layer is meant to grow, and it is a design moment.

**Not a trigger:** the urge to tidy. Rearranging folders with no new material feels like work and produces none. Also not a trigger: a routine check of whether the indexes are complete. That is `CONTEXT7`, and running it here turns a design conversation into bookkeeping.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill builds layer two, and it cannot be done from generic knowledge of how people organise things. **Read the owner's constitution and their raw material before proposing a single folder.** The constitution tells you what they spend a life on and who depends on them. The raw material tells you what they generate volume about. A folder set that disagrees with either one files correctly and answers wrongly, the expensive kind of wrong because it looks organised.

One boundary settles half the arguments you are about to have: **memory holds what happens, the constitution holds what is always true.** "I am someone who does not finish things" is constitution. "This did not get finished" is memory.

### CONSTITUTION

After setup this skill fires rarely, so do not spend always loaded context on it. Put the line in the skills index the core already links to. **What does belong in the core is the map:** the area names and one line each on what lives there, because that is how the AI finds anything without opening everything.

```
MEMORY7. My memory layer: a small set of areas named in my words, one folder holding only my own material, machinery outside it, plain files only. One fact, one home. A new area appears when an existing one is too big to scan, never in advance. Spec: skills/memory7/SKILL.md
```

### MEMORY

The layer built here is the result, so the question is what stays out of it.

**Not in memory:** identity, values and standing rules, which are constitution. Keys, tokens and credentials, which belong with the machinery. Anything whose source of truth is a live external system, because a copied number will be wrong later without announcing it.

**What rots:** status summaries, current figures copied from somewhere else, and any fact that lives in two folders. **One fact, one home, and links from everywhere else.** Two copies means two places to update, and the first time they disagree the system starts lying quietly.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. Today those usually arrive as **MCP servers** or **connectors** the client installs. Name the mechanism when you use one and do not let it rename the layer. Here almost nothing is needed, and say so plainly: **the layer that holds everything the system knows requires no integrations at all.** Connectors matter later, for feeding it.

> 🔒 **Restructuring never deletes.** A design session puts more of a person's own writing in motion at once than anything else you will do. You move, you never remove. If something looks like junk, propose it as a list, get an explicit yes per item, move those to a holding folder, and let the owner do the final deletion. A wrong structure costs an hour. The only copy of something they wrote costs more.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Read all of their raw material before proposing anything.** The dump, the deep dive answers, the constitution, old notes if any. Come back with what is already there: how many distinct threads, what carries the volume, what appears once. The tree is a description of their life, so it is derived, not chosen.

**2. Group what is there, then name the groups in their words.** Use the nouns they used. If they wrote about the van, the area is not "assets". Read the names back and ask a blunt question: would you say this word out loud to a friend? A folder nobody would say aloud is a folder nobody files into.

**3. Keep the top level small enough to recite from memory.** A handful of areas, scannable on one screen. Too few and everything piles into one. Too many and the owner faces a shelf of empty folders that reads like a to-do list for a life they are not living. **Do not create an area for one item. That is a file.** Do not create the folder for the business they plan to start next year.

Numbering, prefixes and published schemes are one person's preference and nothing here depends on them.

**4. Separate the owner's material from the machinery.** One folder holds their content and nothing else. Scripts, configuration, keys, exports and databases sit beside it or above it, never inside. Not for tidiness: tools get replaced roughly every eighteen months, and the content folder has to survive being copied to a new machine and opened by a different AI with nothing else coming along. **The layer must outlive the tool that reads it.**

**5. Test the structure before you build it.** Hand back ten real items from their own material and ask where each goes. One hesitation is a rename, three is a regroup, and both are cheap now and expensive after two hundred files exist. Say out loud that hesitation is evidence about the structure, because most people assume the opposite and apologise.

**6. Build it and file the material in the same session.** An empty structure is a plan. A structure with their own writing inside it is a memory layer. **Nothing gets lost:** every item lands somewhere, and whatever you genuinely cannot place goes to the capture folder marked unplaced.

**7. Write one entry file per area, in their words, with real examples from their own content.** Two or three concrete items each, never generic placeholders. That file is what the next session reads instead of opening everything. Keeping it accurate from here on is `CONTEXT7`'s job.

**8. Tell them how it grows, then stop building.** A new folder appears when an existing one holds more than can be scanned at a glance, and not a day before. Structure created ahead of content is the quieter failure mode, because it looks like foresight.

**9. Prove it in a fresh session.** Ask a question that should require reading exactly one area. If answering it means opening five folders, the grouping is wrong, and now is the cheap time to find out.

---

## DEFINITION OF DONE

1. **The areas exist**, named in the owner's words, few enough to recite, each with an entry file containing real examples.
2. **All the raw material is filed**, with anything unplaceable in capture and marked, so nothing is unaccounted for.
3. **The content folder holds only the owner's material**, with scripts, configuration and keys outside it.
4. **The ten item test passed** with at most one hesitation.
5. **The growth rule and the one fact one home rule are written down** where the next session reads them.

Missing the third means you built a project folder that will not survive its tooling. Missing the fifth means the structure drifts back to a pile within a month and nobody can say when it happened.

---

## MAKE IT YOURS

1. **Pick the number of areas that matches this life, not a list from anywhere.** Most people cluster between five and eight, but someone running one business with no household logistics may need four, and forcing the extra ones produces empty shelves.
2. **Decide where people live, once.** A person shows up in work, in family and in a project, and the argument returns monthly until it is settled. One home, links from everywhere else, rule written down.
3. **Fix the naming convention early and apply it everywhere.** Dates in front or behind, singular or plural, spaces or dashes. Any consistent convention beats a better one used half the time, because search only works on the consistent part. Decide the archive the same way, and keep archived things listed.
4. **Name the folders in the language the owner thinks in**, even if their AI answers in another one. Filing happens in the head, and a translation step at the moment of filing is the friction that ends the habit.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
