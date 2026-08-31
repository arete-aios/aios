# The archive protocol

The half of `video7` that keeps its value even if no video is ever cut.

---

## Folders

```
<video root>/
  _video-CONTEXT.md            index: every project, one line each
  <year>/
    <MM>-<slug>/
      _<slug>-CONTEXT.md       the project record
      edl.json                 cut decisions
      *.fcpxml / *.xml         editing timelines, if any
      sources/                 verified archive copies; media bytes never edited
      work/                    regenerable intermediates; cleanup is approved
      out/                     finished files, versioned
```

**Why the month is in the project folder name and not its own level.** Two videos in one month turn a bare `08/` into a box with two unnamed things in it, and the year view stops telling you what happened. `08-old-room-return/` sorts chronologically and reads as a sentence.

**Why four folders and not two.** The tempting shape is originals and results. It fails at the third folder, the intermediates, which are large, regenerable, and indistinguishable from results once they sit side by side. Six months later nobody dares delete anything. Separating `work/` makes the disposal decision clear: after verified outputs exist, its contents are eligible for owner-approved cleanup. They are not deleted automatically.

**Why `edl.json` sits outside `work/`.** It is the one artefact that cannot be regenerated. Everything else is a function of the sources; the decision about where to cut is a function of somebody's judgement, and losing it means doing the work again.

---

## Naming

Folder names are for machines: lowercase, ASCII, hyphens, no spaces, no leading dashes.

A leading dash is worth spelling out because it fails so strangely. A path beginning with `-` is read as a command line option by nearly every tool, and the error says something about an unknown option rather than about a file, so it reads like a bug in your script. The same applies to spaces: an unquoted path with a space arrives as two arguments and the tool reports both halves missing.

Copy each source into the archive and compare SHA-256 before editing. The device or inbox original stays where it is and keeps its name. The archive copy keeps the identifier the camera gave it and **may gain a short tag**: `IMG_4590_corridor-and-241.MOV`. Record original name, archive name, and hash in the context file. The number is the thread back to the device; the tag lets a person or assistant know what the copy contains without opening it.

This is a correction to the obvious rule. Keeping the bare camera name is safe but useless: a folder of `IMG_4590.MOV` through `IMG_4599.MOV` forces you to play all ten. Renaming entirely is meaningful but severs the link. Keeping both costs nothing.

Fully human-readable names still go in `out/`, where a person actually reads them.

---

## The context file

Six sections, always in this order. The value is in filling them at ingest, when someone still remembers, not at the end.

### 1 · What is in the material

A table with one row per source file: filename, duration, resolution and frame rate, and **a written description of what is visible**, written after actually looking at the contact sheets.

This section is the whole point of the skill. It is what makes the archive searchable by a human, and it is the only way an assistant can reason about footage at all.

Note the audio too. "Averages −45 dB: room tone and footsteps, no speech" decides more about the edit than the picture does.

### 2 · Goal

What this video is for and who sees it. A piece for a group chat and a piece for a public page are different films from the same footage, and the difference has to be written down before anyone starts cutting.

### 3 · Format

Aspect ratio, target length, captions or none, language.

Recommend the aspect ratio from both the destination and the material, then ask the owner to approve it. A vertical crop suits corridors and single subjects and destroys wide views. When a film's payoff shot is wide, a squarer frame that keeps it may beat a taller frame that cuts it in half, even when the platform prefers tall video.

### 4 · Lane

Machine renders it finished, or machine builds a timeline and a person finishes it. Written down, so it is decided once.

### 5 · What has to be done

The open steps. This is the section that stops a half finished edit from becoming invisible.

### 6 · Result

What came out, where it was published, and **what was learned**.

The last part is not sentiment. Every edit teaches something specific: a tool that turned out to lack a text filter, a font that failed on accented characters, a folder whose paths broke when files moved. Written into this section, it makes the next edit fast. Left in someone's head, it gets rediscovered at the same cost as the first time.

---

## The index

One table at the root: project, what it is, goal, lane, status. Every project that exists appears, including the ones waiting and the ones abandoned.

A missing row is worse than a missing folder, because the folder is at least visible in a file listing. Anything absent from the index is invisible to the next session, human or otherwise.

---

## Version control and backup

Track the text, exclude the media.

The descriptions, the cut decisions and the timelines are small, they are the irreplaceable part, and they benefit from history. The media is large, unchanging, and would be carried forever in the repository once committed. Exclude the media directories, then re-include the text patterns explicitly, and verify the result with the tool rather than assuming the patterns did what you meant.

**Then, separately, an actual backup.** Two machines kept in sync are one copy visible in two places: a deletion on either propagates within seconds. Whatever the arrangement, at least one copy has to be one-way, so that the file is still there tomorrow after somebody tidies up today.
