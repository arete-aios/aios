---
name: watch7
description: "WATCH7: have your AI watch a video for you, subtitles first and local transcription as the fallback, then a timestamped brief. Use when a long video holds the two minutes you need."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: watch7
  synced: "2026-07-23"
---

# SKILL: Watch a video for the owner and report what was actually said

**Trigger word: `WATCH7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Fetching mode** needs one free command line downloader. You pull the subtitle track or the audio yourself, and the owner sends a link and nothing else.
**Paste mode** needs no tooling at all. The owner opens the platform's own transcript panel, pastes the text, and everything from the reading step onwards runs unchanged.

Start in whichever mode today allows. The brief is the product, and it is identical in both.

| What | Needed | How to connect |
|---|---|---|
| **A subtitle and audio downloader** | required for fetching mode | `yt-dlp`, free, one install: [github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp). What it can reach: [supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) |
| **A video tool for still frames** | optional | `ffmpeg`, free: [ffmpeg.org](https://ffmpeg.org) |
| **A local speech to text model** | only for videos with no subtitles | faster-whisper: [github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper). First run pulls a few gigabytes of weights, then it is offline forever |
| **A scratch work folder** | required | Anywhere you can write. Transcripts and frames are working material and belong outside the memory layer |

No API key, no paid account, and on the local path nothing leaves the owner's machine.

**Setup time, honestly.** About five minutes for the downloader, one package install for the frame tool, and an afternoon for the local speech model if you ever need it. **Most runs never need the third**, because the subtitle track already exists and costs nothing to fetch.

---

## WHAT

**A twenty minute video usually carries two minutes you need, and there is no way to skim it.**

Video is the format that resists everything the owner does with text. You cannot search it, cannot skim it, cannot quote it, and you find out whether it was worth watching only after watching it. So people either burn hours on it or avoid it and miss what the few sources they trust are saying. This skill turns a video back into text, reads the text, and reports what was actually said.

**Without instructions an AI fails at this in three predictable ways.** It writes a confident summary from the title, the description and whatever it half remembers about the speaker, which is the worst outcome because it reads exactly like a real one. It jumps to the expensive path and transcribes audio that already had a free subtitle track. Or it opens every extracted frame to be thorough, spends a fortune in context, and returns a longer retelling than the video deserved.

**There is a fourth failure, and it survives into other people's work.** Automatic subtitles mangle names, numbers and technical terms. Passed on as a direct quote, a recognition error becomes a fact the owner repeats in a meeting, and nobody can trace it back.

---

## GOAL

**A short written brief the owner can read in under a minute:** one sentence on what the video is, three to six real points with timestamps on the moments that matter, and one line on why it matters to this owner specifically.

Behind the brief sits a **full timestamped transcript on disk** that can be searched, quoted and reused later.

The last line is the one that makes it a brief instead of a summary, and it is only writable from the owner's own system. If their focus layer or memory says what they are working on, tie it to that. If nothing in the video touches anything they are doing, say that in one line. **A clean no is a useful result**, and it is the answer that saves the most time.

---

## TRIGGER

- The owner says `WATCH7 {url}`, `watch {url}`, or asks what a video says. A local video file works the same way.
- **Before committing an hour to something long**, especially a recorded talk, a webinar or a podcast episode.
- **When a source the owner trusts publishes** and the question is whether this one is worth their time.

**Not a trigger:** a schedule. This is not a daily ritual and not a feed reader. It runs on sources the owner picked, when the owner asks. **Never subscribe yourself to anything**, and never start a batch of videos because a channel looked interesting.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**A summary is generic and a brief is not, and the whole difference lives in the owner's layers.** Two people watching the same recorded talk need different three sentences out of it. Which three depends on what they are building, what they already decided, and what they are stuck on, and none of that is in the video.

The memory layer does a second job here that is easy to miss. **It tells you what the owner already knows.** A point that is genuinely new to them is worth a line, and the same point restated by a speaker they have already read is noise wearing a timestamp. Without that check, every brief comes back the same length regardless of how much the video actually added, and the owner learns to stop reading them.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Watches most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
WATCH7 {url}. Watch a video for me: subtitles first, local transcription as fallback, frames only on request, then a brief with timestamps. Spec: skills/watch7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**Transcripts and frames are working material, not memory.** Keep them in a scratch work folder, one dated folder per video, and leave them there. Working folders can be cleared any time without loss, and saying so to the owner is part of the job.

They enter the memory layer only when the owner says to keep something, and then **it is the brief that gets filed** into the relevant area or project, not the raw transcript. If a single quote matters, the quote goes with the brief, with its timestamp and the link, so it can be checked later against the source.

**What does not belong in memory:** whole transcripts, and a copy of anything that is one click away at a stable URL. **What rots:** work folders for videos that produced nothing worth keeping, and briefs about tools and prices, which are stale within a year and read as current forever.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

Here the tools are plain command line programs: a downloader for subtitles and audio, a video tool for frames, and a local speech model as the fallback. **Audio never goes to a hosted transcription service. That is a principle, not a convenience**, because the owner's own recordings go through the same path.

> 🔒 **Never report on a video you could not reach.** Login walls, age gates, members only, region blocks, private and deleted videos all fail, and a summary assembled from the title and description is indistinguishable from a real one until it is repeated in public. Say in one line what failed and stop. The same rule covers quotes: **never present a recognition error as a direct quote**, and when a number matters, say that it needs confirming.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level. Build the thinnest script your system allows.

**1. Climb the cost ladder, do not jump to the top.** Default path: pull the existing subtitle track, manual first, auto generated second, and parse it into timestamped text. This costs nothing, no download, no processing. For most talking head and news content it is the whole job.

**2. Only when subtitles do not exist, or the owner explicitly asks for accuracy, download the audio and transcribe it locally.** Warn the owner once about the first run, model weights are large and take a few minutes to arrive, after that it stays local and offline. Expect it to run several times faster than real time, so a long video is minutes, not seconds.

**3. Frames are opt-in, never default.** Extract stills only when the owner asks or when the transcript clearly refers to something on screen: slides, a diagram, a demo. Then open a handful of them, chosen by what the transcript says, not all of them blindly. **Images cost tokens the moment you open them, so pick.**

**4. Read the transcript, then write a brief, not a retelling.** One sentence on the subject. Three to six points that were genuinely made, each with a timestamp if the moment is worth returning to. One closing line on why this matters to the owner, tied to a current project or goal. If the speaker states something as fact that costs money or looks doubtful, flag it for an independent check instead of passing it on.

**5. Treat the transcript as approximate.** Auto subtitles and speech to text both mangle names, numbers and technical terms. Read for the meaning, not the letters. Where a name matters, check it against the owner's own records before you write it down.

**6. Be honest about what you cannot reach**, in one line, and stop. Do not retry forever, and do not fill the gap with the description.

**7. Say where the raw material sits**, and that it can be deleted at any time. Then ask once whether anything from the brief should be kept, and file only that.

---

## DEFINITION OF DONE

1. **A brief that reads in under a minute:** subject in one sentence, three to six real points, timestamps on the ones worth returning to.
2. **One line on why it matters here**, or an honest line saying it does not.
3. **The full timestamped transcript on disk**, in a dated work folder the owner knows about.
4. **Doubtful claims flagged** for an independent check rather than passed on as fact.
5. **Anything unreachable reported as unreachable**, with nothing invented in its place.

Missing the second means you wrote a summary. Missing the fifth means the owner cannot tell which of your briefs were real.

---

## MAKE IT YOURS

1. **Add a section flag for long material** and transcribe only the range the owner cares about. On a two hour recording this is the difference between a minute and half an hour.
2. **Route the output.** A brief can go straight into a content pipeline, a research note, or a message to a colleague. Agree with the owner once where each kind lands.
3. **Agree the trust list.** A handful of sources whose videos are worth the full path, and everything else gets the subtitle skim and one paragraph. Without that list every video looks equally worth watching, which is how the hours went missing in the first place.
4. **Set the frame budget.** A number, agreed once, for how many stills you may open without asking. Blind extraction of a whole video is the most expensive mistake available in this skill.
5. **No command line access at all?** The skill degrades to a conversation: the owner opens the platform's own transcript panel, pastes the text, and you run the reading steps unchanged. Less convenient, same product.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
