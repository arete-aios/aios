# AIOS · an AI operating system you own

Most people now have an AI that is good at everything and knows nothing about them. Every session starts from zero: who you are, what you are working on, what you decided last month, how you want to be spoken to. You explain it again, and tomorrow you explain it again.

An **AIOS** fixes that with five layers you own and your AI reads. This repository is how one gets built, in stages, with a test at the end of each one.

---

## What you will have at the end

Concretely, five things:

1. **A core file** your AI reads at the start of every session, short enough to be cheap, written so that every line changes what it does.
2. **Folders that fit you**, built from your own material, where a new note has an obvious home without you thinking about it.
3. **Three working methods**, not twenty. One of them will run without you asking for it.
4. **A closed loop**: something happened, it got written where the next session sees it, and it changed what you did next. This is the part that separates a system from a folder of notes.
5. **One file that says what matters right now**, current enough that your AI argues with you when you propose something new.

Plain files, in a folder you keep. No platform, no subscription, nothing that stops working when a tool is replaced.

---

## The five layers

| # | Layer | What it is | Kept by |
|---|---|---|---|
| 1 | **[Constitution](references/1-constitution.md)** | Who you are and the rules that hold in every session. The only file that costs you on every message | `constitution7` |
| 2 | **[Memory](references/2-memory.md)** | Everything the system knows. Long, cheap, opened when relevant | `memory7`, `context7` |
| 3 | **[Skills](references/3-skills.md)** | Methods written down once, so they run the same way every time | the library, `audit7` |
| 4 | **[Tools](references/4-tools.md)** | How the AI reaches anything outside its own files | each skill's requirements |
| 5 | **[Focus](references/5-focus.md)** | What matters right now. One small file | `focus7`, `week7` |

And the thing that makes them a system rather than five folders: **[the loop](references/feedback-loop.md)**. Read that one first if you only read one.

---

## How to start

**One link, one paste.**

1. Open **[SKILL.md](SKILL.md)** in this repository.
2. Copy the whole file and paste it into your AI. Claude, ChatGPT, or anything that reads text. Nothing to install.
3. It will start stage 1, which is writing the file your AI reads first. That takes one session, most of it your AI asking and you answering.

**What "reads first" needs.** For this to be an operating system and not another chat, your AI has to reliably see your core at the start of work. There is a ladder for that, best to workable: (a) a client with a project or memory feature that auto-loads files, so the core loads itself every session; (b) a client where you paste or pin the core at the start of a working session; (c) plain chat, where you paste the core each session. All three work. Starting in plain ChatGPT is fine and common, and stage 1 writes a real constitution either way, the last option just costs the most effort and is the thing the later stages exist to remove. What changes as you go is how automatically the core loads, not whether it exists.

There are nine stages and each has an exit test. **Stage 1 passes when a brand new session answers something it could only know from what you wrote.** Not before.

Your AI creates a small progress file in stage 1 and reads it at the start of every session after that. This is deliberate: a build that runs over weeks cannot survive in a chat window.

**Install the skills** when you get to stage 5. First add the marketplace, then install only the group you need:

```
/plugin marketplace add arete-aios/aios
/plugin install start@arete-aios
```

The group names are `start`, `aios`, `capture`, `decide`, `people`, `reach`. Install `start` at stage 1, add others only when a stage calls for them. The marketplace alone installs nothing; you pick the group.

Or take any single skill as a file and paste it in, with nothing installed at all. The skills are in [skills/](skills/) in this repository, one folder each. When you paste a folder skill, its `references/` files are not pasted with it, so if a skill mentions one, either add it too or tell your AI it is not present.

---

## The skills, grouped by what changes when they finish

Each raises a specific layer. When an evaluation finds a gap, the skill that closes it is here, in `skills/`.

| Group | After a run | Skills |
|---|---|---|
| **start** | the system exists where there was nothing | `constitution7` `braindump7` `deepdive7` `memory7` |
| **aios** | the system's own files stay honest | `context7` `focus7` `exit7` `week7` `audit7` `dashboard7` |
| **capture** | memory holds a record that did not exist | `in7` `inbox7` `voice7` `watch7` `meeting7` `news7` |
| **decide** | a written judgment exists where there was an opinion | `eval7` `evalx` `verify7` `kw7` |
| **people** | you know one named human better | `warm7` |
| **reach** | something outside your own files changed | `mail7` `slides7` `site-cloudflare7` `site-lovable7` `ads7` |
| **channel** | you can reach your system from your pocket | `channel7` (in start) |

**Do not install them all.** The build is staged for a reason: three standing skills until the loop closes once. The evaluation in [references/evaluate.md](references/evaluate.md) tells you which few you need, in order.

---

## Already have a second brain?

Then this is a comparison, not a build. Give your AI this repository and ask it to evaluate what you have, layer by layer.

**[references/evaluate.md](references/evaluate.md)** has the scoring dimensions: one per layer, plus the loop, plus whether the whole thing actually fits the person carrying it. It returns a score per dimension, an overall with a band, and three lists: what is missing, what is excess, and what is too complex for you specifically.

Expect the honest answer to be shorter than you hoped. For most systems that are already running, the useful advice is to remove something, not to add one more thing.

---

## Honestly, how long

**This is weeks of small work, not an afternoon.**

The first stage is one sitting. Stages 1 to 5 spread across one to two weeks, twenty to forty minutes at a time, and the limiting factor is your thinking, not the AI's speed.

**Stage 6 is a deliberate stop: two full weeks of using it and adding nothing.** That is the step everybody wants to skip, and skipping it is the reason most second brains are abandoned in the third week. There is a hard rule in the build to stop you: no more than three methods installed before the loop has closed once.

Anyone selling you a complete second brain in an afternoon is selling you a folder.

---

---

**Built by Egils Boitmanis with [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The skills live in [skills/](skills/) in this repository
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
