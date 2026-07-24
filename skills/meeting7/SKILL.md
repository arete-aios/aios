---
name: meeting7
description: "MEETING7: turn a conversation into a record of what was decided and what is owed, and many conversations into a profile of the person. Use after any meeting or call."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: meeting7
  synced: "2026-07-23"
---

# SKILL: Turn meetings into decisions, and many meetings into a person

**Trigger word: `MEETING7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With a recorder:** transcripts arrive as files and everything new is processed in one pass, without the owner writing a sentence.
**Without one:** the owner talks the meeting through with you in the ten minutes after it ends, or pastes their own notes. Slower per meeting, and often sharper, because they tell you what mattered instead of everything that was said.

**Most people do not record, so build for that mode first.** A recorder is an upgrade in volume, not in value per meeting.

| Source | How to get it |
|---|---|
| **A meeting recorder** | [tactiq.io](https://tactiq.io), [otter.ai](https://otter.ai), [fireflies.ai](https://fireflies.ai). All export text or PDF |
| **The meeting platform itself** | Often already there on paid plans, no extra tool: [Google Meet](https://support.google.com/meet/answer/12849897), [Teams](https://support.microsoft.com/en-us/office/view-live-transcription-in-microsoft-teams-dc1a8f23-2e20-4684-885e-2152e06a4a8b), [Zoom](https://support.zoom.com/hc/en) |
| **In person meetings** | A phone recording plus local transcription, for example [Whisper](https://github.com/openai/whisper), which keeps the audio on the owner's machine |
| **Nothing at all** | The owner tells you what happened, right after it happened. This is a mode, not a consolation prize |

**Check the client's connectors before building anything.** Some recorders and drive folders now arrive as MCP servers or ready connectors, which turns an export into a live read. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Two places to write inside the owner's own system:** the memory layer for the notes, a task or calendar layer for the commitments. Without the second, step 5 hands the dates back as text and says plainly that they are now the owner's to store.

**Use a strong model for the person layer.** The cheapest one produces flattery, which reads well and is worth nothing.

**Setup time, honestly.** Zero for the talk it through mode, first note inside the same session. An hour or two to wire a recorder's export folder for unattended runs. The person layer needs no setup and cannot be used for weeks, because it needs several conversations before it has anything to merge.

---

## WHAT

**Handed a transcript, a connected AI does the obvious thing: it summarises. That is the failure.**

Three months later the owner opens the note and reads a paragraph in the AI's voice. The decision is in there. The sentence that produced it is gone, and nothing separates what the other person said from what the model inferred. A summary ages into an opinion. A quote is still theirs a year later.

The second failure is quieter. A meeting produces a promise, the promise goes into a note nobody reopens, and it expires. From the other side that looks like an owner who does not keep their word.

The third is that everything stays filed per conversation, so after twenty calls with the same person the owner still walks in cold. The notes answer what happened. Nothing answers who this is.

**One more, about method rather than software.** This began as two skills with a numbered suffix, one for the meeting and one for the person. The author could not reliably remember which had processed which call, and neither could the AI, so some calls got done twice and others not at all. **A method split across two names a stranger cannot tell apart is one method with a bug.** Hence one skill, two depths.

---

## GOAL

**After a meeting: one note holding what was decided, in the words the people used, with every commitment carrying a date. After several meetings with the same person: one file that means no meeting with them starts cold.**

The shallow depth is done when a reader a year from now can tell who said what and what was owed. The deep one is done when the owner opens a single file before a meeting instead of scrolling a year of fragments.

**Who decides what counts as a commitment, and which people deserve a profile?** Take it from the owner's constitution and memory, where priorities and key relationships usually already are. If it is not there, ask once and write the answer down. Never decide it silently: an assistant that promotes every good intention to a commitment produces a task list the owner stops reading.

---

## TRIGGER

- The owner says `MEETING7`, alone, with a person's name, or with a file path.
- **After any meeting or call**, ideally within the hour, while they still remember the tone and not only the content.
- **When a transcript lands** in whatever folder the recorder fills.
- **Before a meeting with someone the system already knows.** Same skill, read direction.

**Not a trigger:** a conversation that already has a note. Skip it silently and say so in one line. Also not a trigger: building a person profile after one or two conversations, however good they were.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

Read the constitution and memory before the transcript, because the transcript cannot give you the two things that decide the output: **what the owner is currently trying to make true**, which is what makes one sentence in an hour of talk worth keeping, and **who these people are to them**, which is the difference between a client, a friend and someone selling something.

### CONSTITUTION

One line makes this skill exist. In meetings most days, put it in the always loaded core. Occasional, put it in the skills index the core already links to. A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

```
MEETING7. After every meeting: one note, fixed sections, their words quoted not summarised, every commitment dated where I will see it. After several meetings with one person: one profile, two lenses, confidence stated. Never process the same meeting twice. Spec: skills/meeting7/SKILL.md
```

### MEMORY

**Three places, kept apart.** The raw transcripts, untouched, because everything else is derived and derivation loses things. One note per meeting, named by date and participants so the filename alone is useful, carrying the person's id so the person layer can find every conversation later. One file per person, supporting material beside it. Plus a small index of what has been processed, so the check for already done is a lookup and not a guess.

**Do not store:** your interpretation where a quote belongs, a number for anyone's intelligence, or details about people the owner has no reason to keep.

**What rots:** roles, companies and phone numbers rot silently. Open threads rot fastest, and a profile listing four that closed months ago is worse than no profile. Date every layer so its age is visible.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. How it arrives keeps changing: an MCP server, a connector the client installs, a folder sync, a hand written script. Name the mechanism when you tell the owner what you are using, and do not let the mechanism rename the layer.

> 🔒 **Consent, said once, and it is not a formality.** Recording and transcribing another person is regulated, and the rules differ by country and sometimes by region: somewhere one participant's consent is enough, elsewhere everyone must agree, elsewhere again a recording made without notice is unusable or illegal. The owner is responsible for knowing which applies to them. Your part is concrete. **If it is not clear the other person knew, say so before you process it**, and never fetch anything about a person from outside the conversation without a direct instruction naming them.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

### Part 1 · The single meeting

**1. Take whatever exists, from every source.** The recorder's folder, a pasted export, the owner's notes, the owner talking. Build one candidate list before touching anything and show the scope first: found four, one already done, processing three.

**2. Check what is already done before spending anything.** One lookup per candidate. This separates a skill the owner can run daily without thinking from one that quietly doubles the archive and the model bill.

**3. Then the rule that matters more than any other here.**

> **Quote, do not summarise.** Anything decided, refused, promised or felt strongly goes in verbatim, with the speaker named. Summarise the connective tissue, never the load bearing sentence.

The test is a year out. A summary reads as your interpretation of a conversation you were not in, and a quote is still evidence. When unsure, quote it. The cost is a few words.

**4. Use the same sections every time.** Decide them once with the owner and never improvise per meeting, because comparability across a year is most of the value. What was decided, what was promised and by whom, what the other person needs, what landed, what is still open.

**5. Every commitment gets a date, somewhere the owner will actually see it.** Not inside the note. The task list, the calendar, whatever they open without being asked. **A meeting that produced a promise and no date produced nothing**, and this is the step most often skipped, because by then the note already looks finished.

**6. Clean up only what succeeded.** Move processed files out of the intake, leave failures where they are and name them in the report. A skill that empties the inbox on failure gets distrusted once and forever.

**7. End with the intersection, not the summary.** The owner was in the meeting. What they cannot see is how it touches what they are working on now. About five lines, one each, tagged with the area it belongs to. If it touches nothing current, say that in one line. A quiet nothing here keeps the other lines worth reading.

### Part 2 · The accumulated person

**8. Wait until there is enough.** Three conversations is the floor, five is where it gets interesting. Below that, say no and say why: **a profile built from one conversation is a first impression wearing a data structure**, and it is more dangerous than no profile because it looks like analysis. Refresh monthly at most, or when something large changes.

**9. Read the file before you write it.** The owner has put things in there by hand: a contact, a promise, something from a dinner. Wrap the part you generate between two markers and rewrite strictly between them, leaving the rest untouched. Back it up before the first restructure. **The file is co owned, and losing the owner's paragraph once ends the skill.**

**10. Build exactly two lenses.** *How this person thinks*, layered from the stable core through their values to the behaviours that actually move, and *how to work with them*: what they expect, what they judge through, and three things the owner specifically should not do with them. Keep that contrast explicit, because this person's own risks are not the owner's mistakes. The lenses meet in one recommendation for the next conversation.

**11. Confidence on every layer, and never a number on a mind.** Cognitive range is a qualitative band plus the markers that produced it. A number read out of conversation text is pseudoscience wearing a lab coat. Anchor to a validated model such as the [Big Five](https://en.wikipedia.org/wiki/Big_Five_personality_traits), and label any popular team role or personality type as shorthand for talking, never as measurement.

**12. Name the bias in the file, not in your reply.** Every conversation in the pile is with the owner, so a single context profile mistakes the relationship for the person: someone open and over adapting with the owner may be neither with anyone else. Write that limit where it gets reread.

---

## DEFINITION OF DONE

1. **One note per meeting**, same sections, no duplicates, raw source still intact.
2. **The load bearing lines are quotes**, with the speaker named.
3. **Every commitment has a date** in the place the owner actually opens.
4. **The intersection with current focus was delivered**, even when it was nothing.
5. **Each person with enough conversations has one file**, two lenses, confidence and dates on every layer, and the owner's handwriting untouched.

Missing the second means you wrote a summary. Missing the third means the meeting produced nothing.

---

## MAKE IT YOURS

1. **Write the sections yourself, before the first run.** Borrowed sections produce borrowed notes. Five is plenty, and changing them later costs comparability.
2. **Choose the second lens for the work the owner actually does.** A recruiter, a therapist and a founder need different ones. Keep it at exactly two, because three stops being read.
3. **Set the thresholds out loud:** how many conversations before a profile, how often it refreshes, and what turns a sentence into a commitment rather than a nice intention.
4. **Decide who never gets a profile.** Family, close friends, anyone the owner would be uncomfortable seeing analysed. That belongs in the constitution, not in a judgment call at midnight.
5. **Start with the mode that needs nothing.** Talk it through, one note, one dated promise. Add the recorder once the habit exists, because automating a habit that does not exist yet produces a full archive nobody opens.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
