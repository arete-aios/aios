---
name: evalx
description: "EVALX: compare 2 to 6 real options for one decision, weights declared before scoring, kill criteria before ranking. Use when a choice has a real cost, owner-invoked only."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: evalx
  synced: "2026-07-23"
---

# SKILL: Choose between real options without fooling yourself

**Trigger word: `EVALX`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With access:** you read the owner's own numbers and check the outside ones. Budget, dates, existing commitments come from their files, and prices, availability and terms get verified before they enter the table.
**Without access:** the owner supplies the facts and you run exactly the same method on what they give you. The weights, the kill criteria and the three bands are the value, and none of them need a connector.

| What | Why it earns its place |
|---|---|
| **A way to read the owner's own numbers** | Budget, runway, dates, what they are already committed to. Without these you score adjectives, and a decision made on adjectives is a decision made on mood |
| **A way to check facts on the web** | Prices, availability, terms, whether the thing still exists. What you cannot confirm gets marked as unconfirmed |
| **The owner's permanent kill criteria** | Their budget floor, their integrity rules, the domain rules for this class of decision. These come from a person once and then apply to every run |
| **One place to file the comparison** | Under the decision it belongs to, so it can be reopened when the outcome arrives |

**Check your connectors before you build anything.** File reading and web fetching usually already exist in the AI client or arrive as an MCP server the owner connects once. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** None to install. Thirty to ninety minutes per decision, and most of that is the owner arguing with the weights before any option is scored. That argument is the work. If it feels slow, that is the skill functioning, because the alternative is a fast answer arrived at by feel and defended with a table afterwards.

---

## WHAT

**Most bad decisions are not made with bad information. They are made by picking the answer first and then arranging the criteria until it wins.**

When a choice is real, the mind builds its justification after the fact. Weights get tuned to the preferred option, the awkward option quietly leaves the table, and the exercise confirms the first instinct in the costume of analysis.

EVALX blocks that with two mechanical rules: the weights are fixed in writing before a single score is given, and every rejected option stays visible with its reason. Neither rule requires anyone to be honest in the moment, which is the point, because in the moment nobody is.

---

## GOAL

**One decision in one sentence, with the cost of getting it wrong in the next.**

A table of 2 to 6 options scored against declared, weighted dimensions, with killed options still visible and their reason attached. Then three recommendations, conservative, balanced and aggressive, each with the case for it, the risk, and when it is the wrong call. It ends with a verdict, not a menu.

**The owner sets the standard, not you.** The weights are their priorities, the kill criteria are their limits, and the choice between the three bands is their risk appetite this month. Take all three from their constitution and memory when they are already written there. Ask once when they are not, then write the answer down so the next decision starts from it. Never assume a weight silently, because a silent weight is the exact failure this skill exists to prevent.

---

## TRIGGER

- The owner writes `EVALX`. That is the trigger.

**Not a trigger:** your own initiative. You never offer or run EVALX on your own. It looks like helpfulness and behaves like a novelty engine, turning every passing thought into a six option table and eating the day. If the owner asks what you think, answer with a judgment, not a matrix.

**Also not a trigger:** scoring one thing against its goal. That is a different skill (see `EVAL7`), and the two get confused in the same direction every time. A comparison of many candidates gets labelled as a score of one artifact, and the numbers stop being comparable to anything. Several things against each other is EVALX. One thing against its own goal is not.

**And say no to your own skill when the decision is cheap.** If the cost is small and the choice reversible, tell the owner to just pick one. Building a table for a cheap decision is procrastination with a spreadsheet.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**A comparison scored against a general standard produces a defensible winner the owner will not act on.** That is the specific way this skill fails without their system. The dimensions can be borrowed from the domain, but the weights cannot: what a decision is worth depends on what this person is trying to do this year, and that is the focus layer. The kill criteria cannot be borrowed either, because a budget floor and an integrity rule are facts about one person.

**And the band the owner picks at the end depends on how much runway they have.** Aggressive is a reasonable answer with two years of cash and an unreasonable one with two months. That number lives in memory, not in the decision. Read it before you recommend anything, or you will confidently hand a stretched person the high variance option.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Makes consequential choices most weeks**, a founder, a buyer, anyone spending other people's money: put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
EVALX. Compare 2 to 6 real options for one decision. Weights declared before scoring, kill criteria before ranking, "do nothing" always on the table, three bands each with its own failure boundary. Owner-invoked only. Spec: skills/evalx/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**Save the comparison filed under the decision it belongs to,** not in a general notes pile. Then add one line to the relevant log: date, decision, chosen option, tiebreaker.

**Store the weights and the assumptions, not just the winner.** When a decision goes wrong the owner does not need to know what they picked, they remember that. They need to see which assumption broke, and a summary that keeps only the result cannot tell them.

**What rots:** prices, availability and anyone else's terms. Mark the date on every external number you record, because a comparison reopened a year later will otherwise be re-read as current. The weights and the kill criteria age much more slowly and are the part worth keeping.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **No number enters the table unverified.** Either you checked it, or the owner gave it, or the cell is marked as an estimate. An unverified number in a decision table is worse than a blank cell, because a blank cell asks a question and a wrong number ends the conversation.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Name the decision and its price.** One sentence on what is being decided. One sentence on what happens if it goes wrong: money, time, relationships, reversibility.

**2. List the options, 2 to 6.** Name plus one line each. Always include "do nothing, keep the status quo" when it is legitimate. It wins more often than anyone likes to admit, and without it the table lies, forcing a choice between actions when the right answer was "not yet". More than six candidates means you filter first with one or two hard cuts, budget, date, location, then table what survives. A 25 row table is research, not a decision.

**3. Declare dimensions and weights before scoring.** Five to nine dimensions, drawn from the nature of the decision. Write the weights first, as numbers, in the output.

> **This one rule is the whole defence against fitting the weights to the option you already want.** If a weight changes after scoring, say so openly, with the reason.

**4. Apply kill criteria before ranking.** Hard constraints knock an option out regardless of score: over budget, breaks a commitment, fails the owner's integrity check, fails a domain rule they set for this class of decision. A killed option stays in the table marked as killed with the reason, so months later the owner sees it was considered and why it lost. **Score never overrides a hard constraint.**

**5. Score, weight, rank.** Each option against each dimension, 0 to 100, evidence in a comment or footnote. No evidence, no number. If the top two land within about 3 points, call it a tie out loud and name the tiebreaker, a specific fact, never "intuition". False precision is worse than an honest draw.

**6. Run the winner through the owner's values check,** in whatever form their system holds it: is this actually theirs to want, what does it do to their health, their money, their relationships, does it pass their integrity bar. If the top scorer fails that gate, it is not the winner, and you say so rather than letting arithmetic settle a values question.

**7. Give three bands, not one answer,** because risk appetite moves with circumstances. Conservative: lowest risk, most reversible, cheapest to be wrong about. Balanced: the highest weighted score, and the default. Aggressive: highest upside, higher risk, on the table only if the owner can name the money or time they are willing to lose. Each band states the option, why, what it risks, and **when it is the wrong choice.** That last field is mandatory: a recommendation without a named failure boundary is selling, not advising.

**8. Close with a bottom line.** One paragraph, direct, in the owner's language. A verdict they can act on, not "choose whichever feels closest to you".

---

## DEFINITION OF DONE

1. **The decision and the cost of getting it wrong** are each written in one sentence at the top.
2. **The weights appear in the output above the scores**, as numbers, and any later change to them is stated with its reason.
3. **Every option is still visible**, including the killed ones with their reason and the status quo.
4. **Every score has evidence**, and anything unconfirmed is labelled as unconfirmed.
5. **Three bands, each with its own failure boundary.** A band missing the "when this is wrong" line is not finished.
6. **A bottom line that is a verdict**, plus one line in the owner's log: date, decision, choice, tiebreaker.

Missing the second means you produced a justification. Missing the third means the table already decided before it was built.

---

## MAKE IT YOURS

1. **Build a standard dimension set for the decision types the owner faces repeatedly**, purchases, clients, hires, so those comparisons stay comparable over years.
2. **Write the owner's permanent kill criteria once**, budget floor, values gates, domain rules, and apply them to every run automatically.
3. **Set the tie threshold.** Three points suits most decisions. For anything scored on soft evidence, five is more honest, because the precision was never there.
4. **Agree what triggers a reopen.** A decision worth this much analysis is worth revisiting when a named assumption breaks. Write the assumption and the trigger together, or the comparison becomes a document nobody ever reads again.
5. **No file or web access at all?** It still runs entirely in chat. Ask for the facts, put the weights in writing before scoring, hand back the table in a copy ready block.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
