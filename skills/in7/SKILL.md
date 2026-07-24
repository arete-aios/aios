---
name: in7
description: "IN7: turn one messy daily message into a structured check-in in the weekly file, then hear only the gaps. Use for the daily log, or when journaling keeps dying after a week."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: in7
  synced: "2026-07-23"
---

# SKILL: Log the day in one messy sentence

**Trigger word: `IN7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Logging mode** needs one place to write that the owner reopens later: a weekly file, a note, a page. The day becomes a comparable record, and trends become visible after a few weeks.
**Chat mode** needs nothing at all. You parse the message, produce both layers as clean text, and hand them back for the owner to paste. Same fields, same limits, they do the filing.

Start in whichever mode today allows. Moving from chat mode to logging mode later changes who saves the entry, not the method.

| What | Needed | How to connect |
|---|---|---|
| **One file per week** | required for logging mode | Whatever the owner's weekly review already opens. Plain text beats an app here, because the format has to outlive the app |
| **Garmin** | optional, at most one wearable | [developer.garmin.com/gc-developer-program/health-api](https://developer.garmin.com/gc-developer-program/health-api/) |
| **Fitbit** | optional | [dev.fitbit.com/build/reference/web-api](https://dev.fitbit.com/build/reference/web-api/) |
| **Oura** | optional | [cloud.ouraring.com/v2/docs](https://cloud.ouraring.com/v2/docs) |
| **Whoop** | optional | [developer.whoop.com](https://developer.whoop.com/) |
| **Withings** (scales, blood pressure) | optional | [developer.withings.com](https://developer.withings.com/) |
| **Apple Health** | optional, on device | [developer.apple.com/documentation/healthkit](https://developer.apple.com/documentation/healthkit) |

**Check your connectors before you write code.** Several of these now arrive as MCP servers or as ready connectors inside AI clients, which is a connect and approve step rather than a build step. Look at what the client already offers, then fall back to the vendor's own API. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Inside your own system you need one place to write,** and ideally the weekly review that reads it. If your AI cannot write anywhere, hand the owner the finished two layers as text at the end of every run and tell them it is now theirs to store.

**Setup time, honestly.** The first run needs nothing and takes two minutes. One wearable connection is thirty to sixty minutes for a normal OAuth setup, and **days** where the vendor gates health data behind an application with a human reviewer at the other end. The habit is the slow part: the file starts being worth reading at around three weeks, because that is when the first repeat shows up.

---

## WHAT

**Daily journaling dies because filling in a form every night is work, and a chat log nobody re-reads is not data.**

The owner should be able to say one messy sentence about the day and have it become a permanent, comparable record. Apps ask for the same fields every night and get abandoned in a week. This skill flips the effort: the owner talks, you parse.

**Without it a connected AI fails in two directions.** It answers the day's message warmly and stores nothing, so three months later there is nothing to compare and the same pattern repeats for the fifth time undiagnosed. Or it over-corrects, turns every mention of food or sleep into a log entry, and the file fills with noise until the owner stops trusting it.

**There is a third failure, and it is the one that produces confident nonsense.** In one system a wearable reported a four kilogram drop in two weeks, and the AI called the new routine a success. There had been no drop. The platform carries the last known weight forward when no measurement arrives, a gap of seventeen days had been filled with a stale number, and the first real weighing afterwards looked like a fall. The number was real, the reading was not. An AI that logs device numbers without asking whether they are fresh will invent progress, and the owner will believe it, because it arrived with a decimal point.

---

## GOAL

**One free-form message becomes two layers in the owner's weekly file, and the owner is asked for almost nothing back.**

After a run the file holds the day twice: a one line entry with the hard signals, and a fuller block underneath with the causes and the owner's own words. The owner sees a short confirmation, a gap table showing only what is missing or weak, and at most three optional questions. Nothing else is demanded.

**What counts as a field is the owner's decision, not yours.** Take it from their constitution and memory if it is already there, because what someone is working on this year is usually written down before this skill ever runs. If it is not there, ask once, then write the answer into memory so it is never asked again. Never assume a set of fields silently: a check-in built around the wrong five things is a habit that dies politely.

---

## TRIGGER

- The owner writes `IN7` followed by free text, in any language, in any order, with typos.
- **A date modifier in the same message** counts: yesterday, a weekday name, or an explicit date. Otherwise assume today.
- **A catch-up message** covering several days at once. Split it into days, do not refuse it.

**Not a trigger:** any message that merely mentions food, sleep or mood. Without the trigger word the owner is talking, not logging. Turning ordinary conversation into log entries is how the file fills with noise and the owner stops trusting it.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

Those layers do work here that a journaling app cannot. **The fields are only right if you already know what the owner is trying to make true**, and that lives in their constitution and focus layer, never in the check-in itself. The same goes for the gaps: a missing field is worth mentioning only when it belongs to something they said mattered. Otherwise you are running an audit nobody asked for.

**Read the constitution first for a second reason.** A daily check-in puts health, mood, money and family in one place, which makes it the most private file in the system. What may be repeated back, quoted, shown in a summary, or sent anywhere at all is decided there, once, and not by you in the moment.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Logs most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
IN7 {free text}. Parse one daily message into my weekly file, two layers, then show only the gaps plus max 3 optional questions. Never ask for numbers a device already knows. Spec: skills/in7/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

Everything lands in the owner's weekly file, the one their review already reads. Two layers in one file: the day line for signals, the block for causes and quotes.

**Store the owner's words, not your reading of them.** A direct quote is still theirs in a year. A summary is your interpretation wearing their name.

**Do not store what the device already holds.** Numbers you pulled belong in the log as read values with their date, and the full history stays with the source. Copying an export into the weekly file makes it unreadable and adds nothing you could query later.

**Most of a week is allowed to rot,** and that is deliberate. At the end of the week, distil whatever repeated or changed direction into a short patterns section. Only what permanently changes the owner or the system moves up into the long term memory layer. The rest stays in the week and fades.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

Writing to one file is the only real dependency. A health feed is the strong optional addition: if a device already knows weight, sleep or heart rate variability, read it and never ask.

> 🔒 **The check-in never leaves.** Nothing from a daily entry goes into a message, a post, a shared document or a third party tool without the owner asking for that specific thing. This is the file where health sits next to family, and it is the last one that should ever be pasted somewhere for convenience.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Fix the date first, then parse.** Default to today, honour an explicit date or a weekday word. Then read the free text for the fields the owner cares about. A workable default set: one meta question about what they did for themselves and not for others, then food and drink, energy, productive output, one emotion word, one thing they are grateful for. Adapt the set to the owner's actual goals. This is theirs, not a template.

**2. Never ask for what a machine knows.** If a device supplies weight or sleep, take it from there. Asking a human to retype a number their watch already recorded is the fastest way to kill a daily habit. **Then check that the number is fresh.** Many health platforms carry the last known value forward, so a value that never moves is usually no measurement at all rather than a plateau. If you cannot tell whether a reading is new, say so in the same line where you report it.

**3. Write two layers, and let the content decide which.** Signals go in the day line. If the owner explained why, gave a cause, or said something revealing about themselves, that goes into the block underneath in full, including a direct quote in their own words. The quote is the part worth reading a year later. Never paraphrase it into your voice.

**4. Report gaps, not everything.** Show a compact table with only the fields that came back missing, weak or negative. Fields that are fine need no row. Then ask one to three questions, only about the gaps, marked as skippable. If the owner ignores them, move on and do not repeat them tomorrow. This is a mirror, not an audit.

**5. Watch trends, and pick the moment to speak.** Three weak or negative days in a row on the same field becomes a topic for the weekly review, not a nag today. A sharp flip from good to bad gets one question straight away. Long stretches of good need less attention, so check every couple of weeks. If the owner keeps answering "nothing" to the meta question three days running, raise it once, gently.

**6. Rotate the deeper questions instead of stacking them.** One reflective question on a given day, not three. A fixed weekly rotation works well: one theme early in the week, another midweek, another at the end, plain logging on the rest. Three questions every day guarantees the owner starts answering to get it over with, which produces confident garbage.

**7. Distil once a week.** During the weekly review, compress the accumulated blocks into a short list: two repeating patterns, one contradiction, one lesson. Files that only ever grow stop being read.

---

## DEFINITION OF DONE

A finished run leaves five things behind:

1. **The day line** in the current weekly file, with the hard signals, under the date it belongs to.
2. **The block underneath**, with the causes and at least one quote in the owner's own words whenever they gave one.
3. **Device numbers marked as read from a device**, with their freshness stated rather than assumed.
4. **A gap table with rows only for what is missing**, and no more than three optional questions.
5. **Nothing else asked of the owner.**

Missing the second means you logged numbers and lost the reason. Missing the fifth means the habit will not survive the month.

---

## MAKE IT YOURS

1. **Change the fields.** The default set fits someone working on health and focus. A business, a recovery or a creative practice keeps the two layer structure and swaps every field.
2. **Set your own trend thresholds.** Three in a row is a starting point, not a law. Pick the number at which the owner would want to hear about it, and not sooner.
3. **Decide who owns the questions.** Some owners want a reflective question daily, some weekly, some want none and only the log. Ask once and write the answer down, because guessing this one wrong reads as nagging.
4. **Pick the trigger word the owner will actually type,** at night, tired, on a phone. Short and unambiguous beats descriptive. Whatever you choose, use the same word in the constitution line and in the skills index, or the skill quietly stops firing.
5. **No storage and no integrations at all? Still run it.** Produce the two layers as clean text, tell the owner exactly where to paste them, and keep the gap table and the three question limit. The format is most of the value, and it transfers the day storage arrives.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
