---
name: voice7
description: "VOICE7: transcribe voice notes on the owner's own hardware, then file each one only after they approve the destination. Use when voice memos pile up and nobody remembers what is in them."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: voice7
  synced: "2026-07-23"
---

# SKILL: Turn voice notes into filed text without sending the audio anywhere

**Trigger word: `VOICE7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Local engine mode** transcribes on the owner's own machine and routes the result. Audio never leaves the hardware, which is the whole reason this skill is written the way it is.
**Routing only mode** starts from text that arrived some other way: the owner pastes it, dictates it, or copies it out of the app that recorded it. Everything from cleaning onwards runs unchanged.

Start in whichever mode today allows. Adding the engine later changes who types the transcript, not what happens to it.

| What | Needed | How to connect |
|---|---|---|
| **A local speech to text engine** | required for the transcription half | faster-whisper is the usual choice: [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper). The original reference implementation is [github.com/openai/whisper](https://github.com/openai/whisper) |
| **Audio conversion** | recommended | `ffmpeg`, because phones produce a different container every year: [ffmpeg.org](https://ffmpeg.org) |
| **One intake folder, with list, read and move access** | required | A file tool in the client, or the reference filesystem server: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) |
| **Read access to the memory layer and its index files** | required to route anything | A transcript filed into a node that does not list it is lost more thoroughly than one still sitting in the intake folder |

**Check your connectors before you write code.** File access usually arrives as an MCP server or as a connector the client installs, which is a connect and approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** An afternoon, not two minutes. The model weights are a download of a few gigabytes on the first run, the environment needs its own isolated install, and the first batch of a hundred messages is an overnight job. Say all three out loud before the owner starts waiting.

---

## WHAT

**Voice notes are the fastest way a person captures anything and the slowest thing to ever find again**, so they accumulate in a messaging app until nobody remembers what was in them.

**This skill is routing, not transcription.** A script does the transcribing. The skill starts where the script stops, with a folder of raw text nobody has decided anything about. Deciding where each note belongs, and doing it without moving the owner's files behind their back, is the part that needs a method.

**Three things go wrong when an AI meets that folder without instructions.** It proposes a cloud speech service because it is faster, and the owner's family and clients end up on a third party's servers to save an afternoon. It files everything on its own judgment, so the owner, who at least knew the notes were in one pile, now cannot find any of them. Or it writes a summary of the folder instead of emptying it, which reads like work and leaves the pile exactly where it was.

**The quiet fourth failure is state.** With no record of what has already been handled, every run starts from the beginning, re-transcribes what was done last week, and eventually the owner stops running it because it never seems to finish.

---

## GOAL

**Every voice note the owner recorded exists as clean searchable text in the part of the memory layer that owns its topic, and the raw transcript is marked as handled so the next run does not treat it as outstanding work.**

The run is finished only when no raw transcripts remain. **Raw means the work is still standing.**

Where each note belongs is the owner's structure, not yours. If their constitution or memory layer already says where conversations, facts and deadlines live, use that. If it does not, ask once, then write the answer down so it is never asked again.

---

## TRIGGER

- The owner says `VOICE7`, or asks what was in a recording.
- **New audio appearing in the intake folder** is a trigger on its own.
- **After anything that produces a lot of talking:** a drive, a walk, a day of meetings where the notes were spoken rather than typed.

**Not a trigger:** your own initiative in the middle of something else. Never route a transcript into the owner's files without showing the destination first, and never start a large batch during a live conversation without saying how long it will take.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**Almost nothing about routing is decidable from inside the transcript.** A note that says "call about the roof before Friday" belongs to a person, a project, or the focus layer depending on how the owner built their system, and the transcript contains no clue which. Read the structure first, or you are guessing with a confident voice.

There is a second reason, and it is the one that decides whether the text is usable at all. **Speech recognition mangles exactly the words that carry the meaning:** names of people, companies, places and technical terms. The correct spellings already exist in the owner's memory layer. Read the people and project names before cleaning a transcript, and the errors fix themselves against a real list instead of a plausible guess.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Records most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
VOICE7. Voice notes in, local transcript out, I approve the destination before anything moves, and audio never leaves my hardware. Spec: skills/voice7/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**Transcripts land in a working folder carrying a status field: raw when they arrive, routed once handled.** That field is the whole state machine, so update it even when the content was merged into an existing file rather than moved as a document, otherwise the next run redoes work that is already done.

Final homes are the usual ones: the brain dump zone for loose thinking, a person's file for anything about a conversation, the relevant life area for facts, the focus layer for anything with a deadline. Whichever node receives it, **the same pass updates that node's index.**

**What does not belong in memory:** the audio itself, and a second copy of a transcript that was already merged into a file. One thought, one home. Two copies is how two versions of the truth start.

**What rots:** raw transcripts that were merged rather than moved, once their status is flipped. Delete piles once the owner has confirmed the removal. Archived audio has a lifetime the owner sets, and it is longer than you think, because a recording is the only thing here that cannot be reconstructed.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

You need a local transcription engine in its own environment, audio conversion for mixed formats, a state file so repeated runs are idempotent, and file access for the routing half. Everything after that is reading and editing text.

> 🔒 **Audio never leaves the owner's hardware. No cloud speech service, no upload, no exceptions.** These recordings carry the owner's voice, their family's voices and their clients' voices, and none of those people agreed to anything. When someone proposes that a hosted service would be faster, including when that someone is you, the answer is no. Speed is not what this skill optimises, and the slowness was already paid for by running the batch overnight.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Intake.** The owner drops audio into one folder, in whatever format their phone produced. One folder, one rule, no naming ceremony, because any friction at capture time defeats the purpose of a voice note.

**2. Transcribe locally, in batch, and be honest about speed.** On modest hardware a good local model runs at roughly fifteen to twenty times faster than real time, which means a hundred messages is an overnight job, not a one minute wait. Say that out loud when the owner is waiting in chat. Keep the run idempotent so re-running never duplicates. **Move the original audio to an archive folder rather than deleting it**, because the recording is the only unrecoverable thing in this pipeline.

**3. Read and clean each raw transcript.** Automatic recognition merges words, mangles proper names and invents plausible technical terms. Pull the real names out of the memory layer first, then fix what you can while preserving the thought, never inventing content to smooth a sentence. When a passage is genuinely unclear, mark it as unclear with its timestamp and move on. **A marked gap is useful, a confident guess is damage.**

**4. Propose one destination per transcript, in a table, then stop.** Number, what the note is actually about in one line, the destination, and whether it is a move or a merge into an existing file. Say plainly that OK approves all of them and OK with numbers approves only those. Deletion is a destination too, for empty or accidental recordings, but **you never delete: you move the file to a dated pile and the owner removes it by hand.**

**5. After the OK, move what was approved and flip the status field to routed in the same pass**, then update the index of every node you touched. Doing the status and the index later means doing them never, because the run is over and the attention has moved on.

**6. Report what is still raw.** That number is the only honest measure of whether this skill ran. If something was left undecided, name it and say why, so the next run starts from a question rather than from the whole pile again.

---

## DEFINITION OF DONE

1. **Nothing is still marked raw**, or the exceptions are named with the reason they are waiting.
2. **Every routed note lives with its topic**, and the index of that node names it.
3. **The original audio is archived**, not deleted.
4. **Deletion candidates sit in one dated pile**, and the owner has been told the final removal is theirs.
5. **One line back:** how many were transcribed, how many routed, how many still raw.

Missing the first means the pile is still standing under a new name. Missing the second means the notes are filed and lost.

---

## MAKE IT YOURS

1. **Pick the model size against the hardware.** A smaller model on a laptop that runs every night beats a large one on a machine the owner turns off.
2. **Set the language explicitly** in the transcription settings. Auto detection is the main cause of nonsense output on short notes in languages other than English, and short notes are most of them.
3. **Agree the standing destinations once.** If loose thinking, conversations, facts and deadlines each have a known home, the approval table becomes a confirmation instead of a debate, and the whole run drops to a couple of minutes.
4. **Decide how long archived audio lives.** Months, not days. It is the only artifact here that cannot be produced again.
5. **No local engine yet? Degrade gracefully.** Keep the routing half. Have the owner paste or dictate the text and run steps 3 to 6 unchanged. The approval gate and the raw versus routed discipline are what stop voice notes from piling up, and they cost nothing to adopt today.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
