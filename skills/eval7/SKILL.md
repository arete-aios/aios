---
name: eval7
description: "EVAL7: score one existing thing against its goal across seven dimensions with evidence, then rank what each fix is worth. Use when the owner asks how good something is."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: eval7
  synced: "2026-07-23"
---

# SKILL: Score one thing against its goal

**Trigger word: `EVAL7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With access:** you open the artifact yourself, the file, the live page, the deck, the recording, and score what is actually there.
**Without access:** the owner pastes it into the chat and you score that. Same dimensions, same rules, same output. The only loss is that you are scoring a copy, and copies drop formatting, links, load time and everything else that never survives a paste. Say which parts you could not reach.

| What | Why it earns its place |
|---|---|
| **A way to read files** | So the owner sends a path instead of a wall of pasted text. Optional, and it changes the experience more than the result |
| **A way to fetch a live page or a video** | Craft and delivery hygiene are two of the seven things you are scoring, and neither survives a copy paste. Scoring something you were only told about is a guess, and you label it as one |
| **One place to keep a running table** | For anything the owner makes repeatedly. A single score changes nothing, a trend across six of them changes behaviour |
| **The owner's goal for the thing** | The only real requirement in this list, and it comes from a person, not a connector |

**Check your connectors before you build anything.** File access and page fetching usually already exist in the AI client, or arrive as an MCP server the owner connects once. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** None. The first run starts the moment this file is read, and it needs no account, no key and no configuration. The real cost is two minutes of the owner naming a goal and an audience before any number appears, and that is the part they will want to skip.

---

## WHAT

**An AI that lives with you learns what you want to hear.** Asked to judge your work it produces warmth, and warmth is not information.

EVAL7 forces the judgment into numbers with evidence attached, so the owner sees which part is weak and what a fix is worth. It prevents the most expensive failure in creative work: shipping at 55 percent while believing you are at 85.

**The failure it was written against is arithmetic, not flattery.** In a real run the overall score came out at 70 while the unweighted average of the seven dimensions was 66. Nobody cheated. There were weights, they lived in the scorer's head, and because they were never written down the number could not be argued with or compared to the next one. A score whose method is invisible is a feeling with a decimal point.

---

## GOAL

**One artifact, one table.** Seven dimensions, each with a whole number from 0 to 100 and a comment that points at the specific place in the content that produced that number. One overall score with a band. A ranked list of 3 to 7 concrete actions with the percentage each is worth. And one closing judgment the owner would rather not read.

**The owner decides what good means here, not you.** Take the goal and the audience from their constitution, memory or current focus if they are already written there. If they are not, ask once, then write the answer into memory so the question is never asked twice. Never assume silently: if you had to guess, put the assumption in the output where it can be corrected.

---

## TRIGGER

- The owner writes `EVAL7 {thing}`, attaches a file, or asks how good something is.
- **Before shipping anything that is hard to take back:** a proposal going to a client, a page about to go live, a talk about to be given.

**Not a trigger:** choosing between options. That is a different skill (see `EVALX`), and the two get confused constantly. Comparisons of many candidates get filed as scores of one artifact, and once that happens the scores stop being comparable to each other, which was the only reason to give them numbers. One thing against its goal is EVAL7. Several things against each other is not.

**Also not a trigger:** your own initiative. You never run EVAL7 unasked. Unrequested scoring of the owner's work is criticism nobody asked for.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**A score is only as good as the standard behind it, and the standard belongs to the owner.** At least two of the seven dimensions cannot be judged from the artifact alone. Whether it hits the goal depends on a goal that lives in the focus layer, not in the document. Whether it sounds like the owner depends on a voice that lives in the constitution. Score those two from general taste and you produce a competent review of a stranger's work, which is exactly what the owner already gets everywhere else.

**Read their constitution before choosing the seven dimensions.** If it names their known failure patterns honestly, and a good one does, then the dimensions can be aimed at the real risks rather than at generic quality. Memory does the other half: it holds every earlier run, and comparison is what turns a number into information.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Scores something most days**, a person publishing or pitching regularly: put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
EVAL7 {artifact}. Score ONE existing thing against its stated goal, 7 dimensions with evidence, overall score, ranked path to 100, one hard truth at the end. Never self-invoked. Spec: skills/eval7/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**The result goes into the conversation, not into a file,** unless the owner asks you to save it. If they do, file it next to the artifact it judges, not in a general notes pile.

For anything the owner produces repeatedly, weekly posts, client proposals, recorded sessions, keep **one running table** and add a column per run. Store the goal in that table alongside the score, because a score is meaningless without the goal it was measured against, and goals move. When the goal changes, the earlier numbers stop being comparable and the trend line quietly starts lying.

**What does not belong in memory:** scores you gave to work by other people. A number you attached to somebody's proposal is your opinion on one afternoon, and stored in their record it will be read later as a fact about them.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **Never self-invoked.** This skill runs when the owner asks for it and at no other time. There is no version of this where you score their work because you happened to read it. An assistant that does that once gets asked for its opinion less often afterwards, which costs more than the review was worth.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Goal and audience first, before any number.** One line each. If the owner has not said and the content does not make it obvious, ask exactly one question. If they refuse or say "just score it", pick an assumption, write it down visibly as an assumption, and continue. Scoring against an unstated goal is theatre.

**2. Choose the seven dimensions from context.** They are not a fixed list, because a landing page and a training plan fail in different ways, and the conversation has usually already named the criteria that matter. A solid default set: goal hit, audience resonance, clarity and structure, evidence and substance, voice and energy, craft and delivery hygiene, next step and accountability. One exception: when scoring a repeat of something you scored before, reuse the previous dimensions exactly, or the trend line means nothing.

**3. Score with evidence.** Whole numbers, 0 to 100. No percentage without a reason that names a specific place in the content. "Fairly good" is not a comment. Domain specifics live in the comment column, never in the dimension names, so two different artifacts stay comparable a month later.

**4. Overall score.** Default is the unweighted average of the seven, rounded.

> **Weighting is allowed only when the weights are visible in the table.** Invisible weights let you produce whatever total you already had in mind.

**Broken dimension gate:** if any dimension scores 40 or below, the overall cannot go above 70, and you say why. One broken part means the thing is not good, however pretty the other six are. Bands: 90 and up, ship as is. 75 to 89, one or two touches then out. 50 to 74, works but carries visible debt. Below 50, do not deliver this.

**5. Path to 100.** Three to seven actions, biggest gain at the top. Each names the action, the percentage it is worth, and the dimension it lifts, and together they roughly close the gap to 100. Every action must be doable today. "Improve clarity" is not an action. "Cut the second paragraph, open with the number from the third" is.

**6. The critical insight.** One to three sentences naming the thing the owner does not want to hear. Not a summary, a verdict. The pattern that shows up most often is a gap between structure and execution: the frame is excellent, the proof is missing. If you finish an EVAL7 and nothing in it stings, you softened it.

**7. Never round up.** Torn between 68 and 72, write 68. Flattery here is not kindness, it is the reason the owner will ship the weaker version.

---

## DEFINITION OF DONE

1. **The goal and audience are written at the top**, either from the owner or marked as your assumption.
2. **Seven dimensions, seven numbers, seven pieces of evidence.** A comment that names no specific place in the content is a missing comment.
3. **One overall score with its band**, and the method visible: unweighted average, or weights printed in the table.
4. **A ranked path to 100** where every item is doable today and the percentages roughly close the gap.
5. **One critical insight** that is a verdict rather than a summary.
6. **For anything repeated:** the run added a column to the existing table instead of starting a new one.

Missing the evidence turns the table into decoration. Missing the sixth means you produced a score instead of a trend.

---

## MAKE IT YOURS

1. **Set your own default seven.** Pick dimensions that map to the owner's known failure patterns, so the scoring hits their real risks rather than generic quality.
2. **Add a series table for whatever the owner makes on repeat** and score every one into it. The first entry feels pointless. The sixth is the reason the skill exists.
3. **Decide the band actions once.** What "ship as is" and "do not deliver this" actually mean for this owner, so a number turns into a decision instead of a discussion.
4. **No file access at all?** It still runs fully in chat. Ask the owner to paste the artifact, score it in the message, and hand the table back in a copy ready block.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
