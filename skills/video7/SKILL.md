---
name: video7
description: "VIDEO7: turn a pile of phone clips into an archive that describes itself, then cut a finished video out of it. Use when footage arrives faster than it gets edited, and nobody remembers what is in the files."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  contributors: "Gianluca Mauro (cutting method), Egils Boitmanis (archive protocol)"
  version: "1.0.0"
  source: video7
  synced: "2026-08-26"
---

# SKILL: Keep footage findable, then cut it

**Trigger word: `VIDEO7`.**

**Human:** paste this file into your AI. It will ask where your footage lives, and nothing else until it has looked at it.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose. The code shapes here are a worked example, not a library: read them, then write your own.

---

## REQUIRES

| What | Needed | How to connect |
|---|---|---|
| **A video tool** | required | `ffmpeg` and `ffprobe`, free: [ffmpeg.org](https://ffmpeg.org). Static builds need no admin rights |
| **Speech to text with word times** | required for anything with talking | faster-whisper: [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper), local and offline, or any hosted model that returns word level timestamps |
| **An image library** | required for on-screen text | Pillow, or anything that renders a PNG. Many static ffmpeg builds ship **without** a text filter, so type is drawn as a transparent image and laid over the frame |
| **Disk** | required | Roughly three times the source size while working. Intermediates are deleted afterwards |

No API key and no paid account. On the local path, nothing leaves the owner's machine, which matters because home footage is the most private material most people own.

**Setup time, honestly.** Ten minutes for the video tool. The speech model pulls a few gigabytes on first run and is offline forever after. Budget an afternoon once.

---

## WHAT

**Footage arrives faster than it gets edited, and undescribed footage is lost footage.**

A folder called `IMG_4590.MOV` tells nobody anything. Six months later the owner cannot find the clip they remember, cannot tell which of four takes was the good one, and cannot ask you for help either, because you cannot watch video. So the pile grows, and the one video that was supposed to get made never does.

This skill does two things, and the first matters more than the second:

1. **An archive that describes itself.** Every clip lands in a dated folder with a written record of what is in it, what it is for, and what came out. That record is text, so it is searchable, versionable, and readable by you next year.
2. **A cut.** Once the material is described, cutting is mechanical.

The reason the order is that way round: an unedited archive that is well described still has all its value. A finished video on top of an undescribed pile has none, because the next one starts from zero again.

---

## HOW

### 1. Look at the footage. You can, and most assistants forget it

You cannot watch a video. You **can** read an image. So turn each clip into one:

```bash
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 clip.mov)
ffmpeg -i clip.mov -vf "fps=9/$dur,scale=480:-1,tile=3x3" -frames:v 1 sheet.jpg
```

Nine frames spread across the whole clip, in one picture you can open. This one trick is the difference between guessing and knowing. It has found a football match filed under basketball, identified which child in a team was the owner's, and caught that a frame was too tight for the on-screen cards that were planned for it.

Do this **before** proposing anything. A treatment written without looking is fiction.

Measure at the same time: duration, resolution, frame rate, rotation, and the audio level. A recording averaging −45 dB has room tone and footsteps, not speech, and that changes what the video can be.

### 2. Put it away properly

```
<year>/
  <MM>-<slug>/
    _<slug>-CONTEXT.md      what, why, what came out
    edl.json                the cut decisions
    sources/                originals, never edited, never renamed
    work/                   intermediates, deletable at any moment
    out/                    finished files, v1 / v2 / v3
```

Full folder rules and the context file template: [references/archive-protocol.md](references/archive-protocol.md).

### 3. Transcribe, with word times

Segment level timings are not enough; the cut happens between words.

**Be honest with the owner about the cost.** On a small local machine, word level transcription runs slower than real time, sometimes ten to fifteen times slower. Ninety seconds of audio can take twenty minutes. A fourteen minute talk is an overnight job, not a conversation. Say this before starting it, offer a smaller model for a rough pass, and start the long one in the background rather than making them wait.

### 4. Find the cuts, and verify them against the sound

Read the transcript for aborted takes, restarted sentences, and dead air. Decide which spans to keep. Then, before rendering anything:

- **Never cut on word timestamps.** They are off by up to a few hundred milliseconds, which is exactly enough to clip the first consonant off a word.
- **Verify every boundary against the audio envelope.** Compute short-window loudness, find the real onset of speech, and place the cut about 0.10 s before it. Leave about 0.15 s of room tone after the last word so the ending does not sound chopped.
- **Snap every region's duration to a whole frame.** Without it, video rounds up to a frame while audio keeps the exact length, and the drift accumulates across joins into audible lip sync error.

The algorithms and the traps in detail: [references/cutting-code.md](references/cutting-code.md).

### 5. Dress it

On-screen text as rendered PNG overlays, captions as a subtitle file burned in at the end.

⚠️ **Verify fonts by rendering, never by inspecting the font file.** A font containing a language's glyphs is not proof that your renderer will draw them. Render one frame with the actual accented characters and look at it.

Anything laid over a speaker needs measuring per take, not reusing last time's numbers. The clear band above someone's head moves by hundreds of pixels between recordings.

### 6. Master and check

Normalise loudness to about −16 LUFS. Then verify, every time: the output frame count matches the sum of the regions, and audio and video are aligned at several probe points. Single pass loudness correction can undershoot by more than a decibel; measure the result rather than trusting the request.

---

## TWO LANES, DECIDED PER VIDEO

**Render it finished** when the edit is "remove the mistakes, add the text": a talk, an intro, a short piece. The machine can do all of it.

**Hand over a timeline** when choosing the moment is taste rather than technique: family footage, stories, anything where the owner will disagree with you about which shot is the good one. Generate an editing project file with every clip and title as a separate object, and let them finish it in a real editor. A flat exported video imports anywhere but is welded shut; only a timeline stays editable.

Recording the lane in the context file stops this being re-argued every time.

---

## HARD RULES

- **`sources/` is never edited and never renamed.** It is the thread back to the camera. The human readable names live in the context file.
- **`work/` may be deleted without asking.** If something must not be lost, it does not belong there.
- **No spaces, accents, or leading dashes in folder names.** A leading dash makes a path look like a command line option and commands fail in ways that read as missing files. The human name lives in the text.
- **Media never goes into version control.** Track the descriptions and the cut decisions, exclude the media. Those are the parts that cannot be regenerated from the originals.
- **Sync is not backup.** Two machines kept identical propagate a deletion in seconds. One genuine one-way copy that never deletes is worth more than three synced ones.
- **Never publish someone's footage, or music you do not have rights to, because a private edit worked.** A video made for a group chat is not cleared for a website. Ask before anything leaves the owner's circle.

---

## FAILURE MODES SEEN IN PRACTICE

| What happens | Why | What to do instead |
|---|---|---|
| Words lose their first consonant | Cut placed on a word timestamp | Verify against the audio envelope |
| Lip sync drifts on longer edits | Region durations not snapped to whole frames | Snap the duration, pad the audio |
| Accented characters render as blanks | Font assumed rather than tested | Render a frame and look at it |
| Cards land on the speaker's face | Reused positions from a previous take | Measure the clear band per take |
| The finished file cannot be adjusted | A flat export was handed over | Hand over a timeline as well |
| A project folder can no longer find its media | Files moved after the timeline was written | Rewrite the relative paths and check every one resolves |

---

## CREDIT

The cutting method here, the boundary verification, the frame snapping, and the caption timing that survives a recut are **Gianluca Mauro's** work, published with his permission. The archive protocol, the contact sheet inspection step, and the two lane split are **Egils Boitmanis'**.

Everything here is an example to adapt, not a library to depend on. Take it, change the parts that do not fit, and keep whichever hard rules you have not yet learned the hard way.
