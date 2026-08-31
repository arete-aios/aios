---
name: video7
description: "VIDEO7: inspect, archive, cut, and verify raw footage when phone clips need to become a findable archive, finished video, or editable timeline."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  contributors: "Gianluca Mauro (cutting method), Egils Boitmanis (archive protocol)"
  version: "2.0.0"
  source: video7
  synced: "2026-08-31"
---

# SKILL: Keep footage findable, then cut it

**Trigger words: `VIDEO7` or the short alias `VID7`.**

**Human:** paste this file into your AI and point it at the footage. It will inspect what it can reach before proposing a cut.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and hard rules matter; the exact implementation is yours to choose.

## REQUIRES

**This skill has two modes. Operating mode can complete the delivery; advisory mode can progress only as far as the supplied evidence allows.**

**Operating mode:** you can read the media and run local video tools. Inspect, archive, transcribe, render, and verify the result.

**Advisory mode:** the owner supplies metadata, contact sheets, an audio envelope, and a transcript with word times. You can design the archive, storyboard, cuts, and timeline specification, but state plainly that you did not inspect or render the original media. If those artefacts are also unavailable, stop after the brief and tell the owner exactly what must be produced next.

| What | Needed for | How to connect |
|---|---|---|
| **ffmpeg and ffprobe** | media inspection, contact sheets, cutting, rendering, loudness checks | [ffmpeg.org](https://ffmpeg.org) |
| **Speech to text with word times** | spoken footage | [faster-whisper](https://github.com/SYSTRAN/faster-whisper), or another tool that returns word-level timestamps |
| **An image renderer** | cards and title overlays | [Pillow](https://pillow.readthedocs.io), or any tool that creates transparent PNG files |
| **A numeric array library** | audio-envelope example code | [NumPy](https://numpy.org), or equivalent short-window RMS calculations |
| **Disk space** | sources, working files, and outputs | allow roughly three times the source size while rendering |
| **A named editor and version** | editable timeline delivery | the owner chooses Final Cut Pro, Premiere Pro, DaVinci Resolve, or another target; do not guess |
| **An editor format validator** | editable timeline delivery | the chosen editor's schema or DTD, plus an XML parser |

No paid account is required for the local path. A speech model may download several gigabytes on first use. Budget ten minutes for ffmpeg setup and an afternoon for the first complete pipeline. Do not run transcription and rendering on the same limited machine at the same time when measuring performance.

## WHAT

Raw footage arrives faster than it gets edited. A folder of camera names tells neither the owner nor their AI what is inside, which take worked, or why it was filmed. Six months later the material exists but cannot be found by meaning.

VIDEO7 solves the archive before the edit. A described archive keeps its value even if nobody finishes the video. Once the material, intent, and good spans are written down, the cut becomes repeatable and every revision starts from decisions rather than memory.

## GOAL

Create a searchable archive and the delivery the owner needs: a finished video, an editable timeline, or both. Keep the originals untouched, record the cut decisions, verify the media rather than trusting a successful command, and leave the next session able to reproduce the result.

The owner decides the audience, destination, acceptable length, captions, target editor and version, and whether the footage may leave their circle. You recommend aspect ratio and framing from both the material and destination; the owner approves them. Read known choices from their constitution or memory. If any are missing, ask once in one combined request. Never infer publication rights from permission to edit.

## TRIGGER

- The owner writes `VIDEO7` or `VID7` and names or shares footage.
- A pile of clips needs to become searchable before anyone knows what to cut.
- A finished cut needs an editable timeline, a reproducible revision, or a boundary audit.
- A video sounds clipped, drifts out of sync, loses overlays, or imports incorrectly in an editor.

**Not a trigger:** downloading or republishing somebody else's media without permission. Also not a trigger when the owner only wants feedback on a published video and has supplied no source material; review it as a review, not as an edit.

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and which rules always apply. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches media and editors. **Focus** is what matters now.

Read the owner's layers before touching footage. Private family material, public brand work, and a client recording can look identical to a video tool while carrying different consent, retention, and publication rules.

### CONSTITUTION

If video work is frequent, add one short trigger line to the always-loaded core. If it is occasional, register VIDEO7 in the skills index the core already links to. Publication, copyright, family, and deletion rules remain in the constitution, not in this skill.

### MEMORY

Keep one project context file with the inventory, goal, format, lane, open work, results, and lessons. Store raw measurements and cut decisions next to the project. Move only durable lessons and published results into long-term memory. Dates, current filenames, and output versions belong in the project record.

### TOOLS

Prefer local tools for private footage. Before using a hosted transcription, rendering, or storage service, tell the owner what leaves the machine and wait for approval. A connector or API is only the transport; the Tools layer records how it is reached and what permissions it has.

> 🔒 **Never publish, message, upload, overwrite, or delete media without the owner's explicit approval for that action and destination. Keep the original media bytes untouched. Copy into the archive, verify the copy by SHA-256, and preserve the camera identifier. A copied archive filename may gain a short tag only when the mapping is recorded.**

## HOW IT RUNS

1. **Fix the brief before the cut.** Ask one combined question for the audience and destination, purpose, target length, aspect ratio or framing preference, captions, privacy and cloud-processing permission, publication rights, and target editor plus version. Choose finished render, editable timeline, or both. Until the brief is answered, you may inventory and inspect locally but you do not choose the story or release preset. Missing publication rights block upload, not a local edit: mark it `private, not approved for publication`.

2. **Inspect what is actually there.** Inventory every source with `ffprobe`: duration, streams, resolution, nominal and average frame rate, time base, rotation, colour and HDR metadata, audio, and creation or location metadata. Detect variable frame rate from frame timestamps rather than trusting one FPS field. Create evenly sampled contact sheets and look at them. Do not describe footage you have not inspected; in advisory mode label every supplied observation as owner-provided.

3. **Archive before editing.** Copy sources into the archive, compare SHA-256 hashes, then create the project context, byte-unchanged `sources/`, regenerable `work/`, versioned `out/`, and a durable cut-decision file. An archive copy may keep its camera name or gain a short descriptive tag after that identifier; record the mapping and never rename the device or inbox original. Follow [the archive protocol](references/archive-protocol.md) and [the brief and decision-list contract](references/brief-and-decisions.md). Media stays out of version control; descriptions, decisions, and timelines may be tracked. Cleanup of `work/` happens only after outputs pass and the owner approves it.

4. **Transcribe speech with detected language and word times.** Detect language before pinning it. The transcript decides which ideas to keep, not the exact frame where a cut lands.

5. **Propose the story from evidence.** Name the kept spans, order, pace, audio cleanup, colour and HDR treatment, reframing, jump-cut treatment, cards, captions, brand elements, music, and ending. Recommend aspect ratio from the destination and what the frames can safely hold; the owner approves it. Show real frames for visual decisions. Ask for one approval on the proposed story before an expensive render when the owner's taste decides the result.

6. **Place cuts against sound and frames.** Use the audio envelope to find real speech onsets and decays. Start about 0.10 seconds before onset and leave at least 0.15 seconds of room tone after the last word. For constant-frame-rate media, snap regions to whole output frames. For variable-frame-rate phone footage, either create and record a constant-frame-rate mezzanine or preserve original rational timestamps; never apply one scalar FPS formula to VFR media. Read [the cutting method](references/cutting-code.md) before implementing boundaries.

7. **Render and write the chosen editor's timeline from the same decision list.** The decision list records source ID and hash, rational time base, kept spans, transforms, audio, captions, overlays, target editor and render preset. Draw text into tested transparent images when the video build lacks a reliable text renderer. Version the render, timeline, and source lineage together without overwriting earlier results. Follow [the timeline round trip](references/timeline-roundtrip.md) so media paths, schema, parent time, and return edits survive another machine.

8. **Master, then prove the output.** Use a destination-specific loudness and true-peak preset, then measure the file. If no destination is set, label the output a review copy rather than a release master. Use two-pass linear loudness correction whenever the mix has an intentional fade or swell. Verify frame count or rational duration, audio-video alignment, first and last spoken boundaries, several visual frames, captions, colour metadata, media paths, and timeline validation. Caption checks include reading speed, safe zones, contrast, language review, and whether delivery is burned-in, sidecar, or both. Record timeline status as `schema_validated`, `import_tested`, or `import_unverified`; if the named editor is unavailable, never claim a successful import. A playable file is not yet a passed file.

9. **Clear rights, remove leaks, then hand off.** Before upload, confirm permission from the speaker, client, and footage owner, plus licences for music, fonts, logos, and other assets. Strip or intentionally preserve GPS and QuickTime metadata, and remove local absolute paths from a timeline package. Update the project result with filenames, versions, checks, publication state, link if approved, and the lesson that should change the next edit. Upload only the verified version to the approved destination and privacy setting.

## DEFINITION OF DONE

- Every source is inventoried from evidence, copied with matching SHA-256, its media bytes remain unchanged, and any archive filename tag preserves the camera identifier.
- The archive context names the goal, audience, format, lane, open work, and result.
- Cut decisions follow the documented schema and can reproduce the edit.
- The finished render and timeline for the owner's named editor and version are versioned together.
- Speech boundaries include a natural tail; CFR durations are frame-snapped, VFR timing follows the recorded policy, and measured drift is within one output frame.
- Loudness, duration, image, captions, colour, paths, and timeline structure have been checked after rendering, and timeline import status is explicit.
- Publication status, people and asset rights, metadata handling, and consent are explicit; no upload is implied by a successful local edit.

## MAKE IT YOURS

1. Set the archive root, naming pattern, and context template for the owner's filesystem.
2. Pick one transcription engine and one overlay renderer. Keep editor export profiles separate by editor and version rather than choosing for the owner.
3. Define platform presets for aspect ratio, captions, loudness, thumbnails, and privacy, but keep publication as a separate approval.
4. Turn every real failure into a regression check: clipped words, drift, missing glyphs, broken media paths, invalid schema, or overlays attached to the wrong parent.

Assistant, on ingest: if the owner explicitly asked to install this skill, save it in the skills layer in your own format, add the trigger line to the skills index, and confirm in one line what you saved, where, and the trigger. Otherwise use it for the current task without changing their system, and offer installation only after delivery.

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own. Cutting method developed with Gianluca Mauro and published with permission.**

**Licensed CC BY 4.0.**

_Part of the AIOS library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)_
