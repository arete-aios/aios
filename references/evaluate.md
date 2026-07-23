# Evaluate an existing system

**For the assistant.** Your owner already has a second brain and has asked how it compares to this model. This file gives you the anchors, the rules and the output shape, so you can produce the evaluation without going to find the `eval7` skill first.

**You are scoring their system, not this one.** The goal is a verdict they can act on this week: what is missing, what is excess, and what is too complex for this particular person.

---

## Before any number

**1. Read their system yourself if you can.** The always loaded core, the folder structure, the skills index, the file that says what matters now, the last two weeks of records. What is written matters less than what has been touched recently.

**2. If you cannot read files, ask and score the answers,** and say in the output you scored a description. What loads at session start and how big? Where does a new note go? Which three methods did you last trigger? What can the AI reach outside its files, and do without asking? Which file says what matters now? **Name one thing the system told you unasked, and what you did differently.** What did you add last month and actually use?

**3. Take their goal from them.** Ask what they want it to do, or state your assumption visibly.

**Evidence or no number.** A dimension with no evidence is scored **unknown**, not guessed.

---

## The six dimensions, with anchors

Two evaluators should land within a few points. Use these anchors; interpolate between them.

| Dimension | 0 looks like | ~50 looks like | ~90 looks like |
|---|---|---|---|
| **Constitution** | Nothing loads; the AI meets you cold every session | A core loads but describes you instead of instructing, or is bloated and half-ignored | Short, loaded every session, every line changes behaviour, hard rules present, size known |
| **Memory** | Notes land anywhere, no index, you search by memory | Most notes have a home but indexes are stale or partial, some content nothing points at | New note has an obvious home, indexes list everything, the inventory exists |
| **Skills** | Nothing written; you re-explain each method every time | Some methods written but not findable when the trigger fires, none has run unasked | Methods written, findable at trigger time, at least one has fired on its own and helped |
| **Tools** | AI reaches nothing outside chat, or reaches things with no gates | A few integrations, some unused for a month, gates missing on things that send or spend | Only what a method needs, gates on send-or-spend, each used this month, status checked |
| **Focus** | No file says what matters now, everything is equally urgent | A focus file exists but is stale or lists too much, the AI never uses it to push back | One small current file, the AI pushes back on new work using it |
| **The loop** | Nothing written ever returns, pure filing cabinet | Things resurface only when you go looking, never unprompted | Something written returned unasked and changed a decision in the last two weeks |

A seventh score, **fit for this owner**, has no fixed anchor: judge the system against their week, not a standard. Low means rituals that need a good day, more structure than content, maintenance that has become the work.

Detail per layer: [1-constitution](1-constitution.md), [2-memory](2-memory.md), [3-skills](3-skills.md), [4-tools](4-tools.md), [5-focus](5-focus.md), [feedback-loop](feedback-loop.md).

---

## Low-system threshold, check this first

**If three or more of the six dimensions score below 25, do not render a table or a total.** A precise score of a system that does not exist is theatre. Say plainly:

> You are at the start. There is no system to score yet, only a beginning. Here is stage 1: write a one-page constitution that loads at the start of every session. Build the layers in order from [1-constitution](1-constitution.md); come back for a score once three of the six are above 25.

Then stop. No band, no path to 100.

---

## Worked example

**Setup, in their words:** ChatGPT daily, notes in Notion, nothing loaded at session start, no skills, no review.

- **Constitution 5.** ChatGPT opens cold every session; no core. 0-anchor.
- **Memory 20.** Notion holds notes, but no index and the AI cannot read them; a store, not a memory.
- **Skills 0.** Nothing written down; every method re-explained. 0-anchor.
- **Tools 5.** No connector between ChatGPT and Notion; the AI reaches nothing outside chat.
- **Focus 5.** No file says what matters now.
- **The loop 0.** Capture into Notion runs, nothing ever comes back unasked. 0-anchor.

**Verdict the threshold produces:** six of six below 25, far past the trigger. No table, no total. Output is the stage 1 message above: one constitution page that loads each session, then build the layers in order. A 12/100 here would look rigorous and mean nothing.

---

## When the threshold does not trigger

Score all seven, whole numbers, evidence per row.

- **Overall is the unweighted average**, rounded. If you weight, the weights go in the table.
- **Broken dimension gate:** any dimension 40 or below, overall cannot exceed 70, and you say why.
- **Loop gate:** dimension 6 below 50, overall cannot exceed 60. An open loop is a filing cabinet.
- **Never round up.** Torn between 68 and 72, write 68.
- **Bands.** 90+, leave it alone. 75 to 89, one or two fixes. 50 to 74, carries debt. Below 50, stop adding and repair.

**Then three lists. Missing:** only what changes something this month; if the loop is open, the top item is closing it, never adding a skill. **Excess:** anything installed and never triggered, unused a month, empty, or kept because it exists. Name it, say remove it. **Too complex:** anything that only works on a good day; give the simpler version.

Then a ranked **path to 100**: three to seven actions, biggest gain first, each naming the action, the percentage it is worth, the dimension it lifts, every one doable this week. One addition at a time. Finish with **one hard truth**. If nothing stings, you softened it.

---

## Output shape

```
AIOS EVALUATION
Goal I scored against: <one line, theirs or my assumption>
What I could read: <files, or "description only">

| # | Dimension     | Score | Evidence                          |
|---|---------------|------:|-----------------------------------|
| 1 | Constitution  |    xx | ...                               |
| 2 | Memory        |    xx | ...                               |
| 3 | Skills        |    xx | ...                               |
| 4 | Tools         |    xx | ...                               |
| 5 | Focus         |    xx | ...                               |
| 6 | The loop      |    xx | ...                               |
| 7 | Fit for you   |    xx | ...                               |

OVERALL: xx / 100 (band) · method: unweighted average
[gate note, if one applied]

MISSING (this month only)
1. ...

EXCESS (remove)
1. ...

TOO COMPLEX (simplify)
1. ...

PATH TO 100
1. <action> · +x% · lifts <dimension>
...

HARD TRUTH
<one to three sentences>
```

Unknown dimensions carry the word **unknown**, not a number. The full scoring method, including how to keep a series comparable over time, is the `eval7` skill in [github.com/arete-aios/skills](https://github.com/arete-aios/skills).

---

**Built by Egils Boitmanis with [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
