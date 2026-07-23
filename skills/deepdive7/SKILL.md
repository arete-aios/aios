---
name: deepdive7
description: "DEEPDIVE7: the interview that turns who the owner is, what they already have, and what is in the way into one inventory. Use after the brain dump, before designing memory."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: deepdive7
  synced: "2026-07-23"
---

# SKILL: Interview the owner into a real inventory

**Trigger word: `DEEPDIVE7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Interview mode** needs a conversation and somewhere to write a file. That is how most first runs happen.
**Assisted mode** adds read access to the places the answers already sit, so the owner corrects a draft instead of recalling from nothing. Correcting is faster and more accurate than remembering.

| Where the answers already are | How to reach it |
|---|---|
| **The brain dump and anything they have written** | Their own files. Read all of it before asking a single question |
| **Recurring card charges, twelve months** | The bank or card statement. The fastest route to the dormant tools category below |
| **App store subscriptions** | [Apple](https://support.apple.com/en-us/118428) · [Google Play](https://support.google.com/googleplay/answer/7018481) |
| **Payments taken outside the app stores** | [Google account payments](https://support.google.com/accounts/answer/3024190) · [PayPal automatic payments](https://www.paypal.com/us/cshelp/article/how-do-i-manage-my-automatic-payments-in-the-paypal-app-help241) |
| **Audience and network size** | Each platform's own analytics. LinkedIn also exports the connection list: [data export](https://www.linkedin.com/help/linkedin/answer/a1339364) |
| **Documents, decks and courses already made** | Wherever their files live. A drive connector reads them directly: [Drive API](https://developers.google.com/workspace/drive/api/guides/about-sdk) |

**Check the client's connectors before building anything.** Several of these now arrive as MCP servers or ready connectors, which is a connect and approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** The high importance pass is 45 to 60 minutes of conversation and is enough for most people to start working from. The full inventory including every asset category is two to three hours and does not need to be one sitting. A connector the client already offers takes minutes, a first OAuth setup you build yourself an hour or two. None of it blocks the interview. Talk today, attach tooling later.

---

## WHAT

**Without this, an AI gives advice to a person it invented.**

It assumes a runway, an audience, free hours in the week, and a budget for tools, because those are the defaults in everything it has read. Then it produces a plan that is good for someone else. In one real run the second question, how long can you last on current resources, came back as: the savings go next week on a repair. Everything drafted before that answer was fiction, and it had looked completely reasonable.

The mirror failure costs money in the other direction. Owners pay every month for software, courses, licences and memberships they have not opened in a year, nobody asks them to list it, and the AI proposes buying a tool they already own. **Dormant paid tools is the asset category almost nobody writes down and the one that most often returns cash in the first week.**

Run this with enough people and the pattern holds: the answer that changes the plan is rarely the business one. It is the runway, the operation scheduled next month, the thing they know they should have done and have not.

---

## GOAL

**One inventory the AI can plan from, so it stops assuming.**

Three things go in it: who the owner is, what they actually have, and what is in the way. Each item carries an importance score from 0 to 10 for the next twelve months, so later sessions can tell an asset from a fact.

The test is behavioural. **Before it existed, answering a planning question meant guessing at money, time, audience, skills or tools. After it exists, it does not.** Still guessing at one of those five means that part is not done, whatever the file length says.

Completeness is not the goal. An inventory that stops early with real answers beats a full form of tidy ones.

---

## TRIGGER

- The owner says `DEEPDIVE7`, or asks for a plan, a strategy, positioning or a next move, and you notice you would have to invent facts to answer.
- **Right after the brain dump and before the memory layer is designed.** The dump says what is on their mind, this says what is true, and folders built before both fit an imaginary person.
- **When you catch yourself about to assume** runway, hours, audience size, or that a tool needs buying.
- **When a load bearing fact moves:** an income source ends or starts, a health event, a new role, a separation, a move.

**Not a trigger:** a calendar date, or the wish to fill in blanks. Chasing empty fields for completeness turns this into homework and gets it abandoned. Refresh what has gone stale, leave the rest.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

Read the constitution before the first question, for two reasons. It already answers part of this, and asking someone what they wrote down last week teaches them that writing things down does nothing. It also carries the rules for this conversation: what may never be stored, what may never leave the machine, how direct they want you. **This is the most private conversation the system will ever have,** and what it produces is the raw feed for the memory layer, which is why it runs before memory is designed rather than after.

### CONSTITUTION

This runs rarely: once properly, then in pieces when reality moves. **Do not spend core context on the method.** Put the spec in the skills index the core already links to. What does belong in the always loaded core is one line, because it changes what you are allowed to do in every other session:

```
DEEPDIVE7. My inventory lives in memory: who I am, what I have, what is in the way, each item scored 0 to 10 for the next twelve months. My money disclosure level is [everything in / summary only / nothing]. Never plan against a resource that is not in it. Spec: skills/deepdive7.md
```

### MEMORY

**One file per section, not one long document.** Sections age at different speeds, and a single file forces you to rewrite the durable parts to update the volatile ones.

**Date stamp everything that rots:** runway, income, hours free per week, health status, subscriptions, audience numbers. A number without a date gets quoted back with total confidence a year later. Values, achievements, lessons and skills do not rot and need no date.

**Do not store:** account numbers, card details, passwords, medical documents, or the private business of other people mentioned in passing. Store the conclusion, not the evidence. The runway figure is the useful part, the statement it came from is not.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. Today that usually arrives as an **MCP server** or a **connector** the client installs. Name the mechanism when you use one, and do not let the mechanism rename the layer.

> 🔒 **The disclosure gate.** Ask before the first money question, never after it. Three levels, offered in the owner's words: **everything in**, exact numbers and balances. **Summary only**, bands rather than figures, so "runway about six months" instead of a bank statement, which is where most people land and is enough for nearly every decision. **Nothing**, no financial detail at all.
>
> If they choose nothing, say out loud in that moment which advice you can no longer give: whether to take the low paid work or hold out, what they can afford to spend, whether a three month build is survivable, how urgent anything is. Then work without it and stop offering it. **A silent guess dressed as advice is the failure this gate exists to prevent.**

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Arrive with a draft.** Read the brain dump, the constitution, their site, old notes. Open with what you already believe to be true and ask them to correct it. Never open with a blank form.

**2. Set the disclosure level, then start.** One question, thirty seconds, before anything about money.

**3. Ask in priority order, one question at a time, and say how long it will take.** This is the rule that decides whether the inventory ever gets finished. Being shown two hundred fields at once is the biggest single reason people abandon it, so never show the full map. The high importance pass is roughly a dozen questions: where they are right now across work, money, health and head; how long current resources last and how urgently the next income is needed; what they are unusually good at; their non negotiable values; how a former colleague would recommend them in thirty seconds; what the business really does today, growing, flat or dormant; where they want to be in two to three years and what they will not do again; and what is in the way.

**4. Let them stop at any point, and mean it.** Save after every block so the file is useful when they walk away. "Skip this" is a complete answer and never gets asked twice in one session.

**5. Make the ammunition block carry numbers.** Two or three achievements they are proudest of, with the figure, the timespan and the outcome attached. One story where they grew something, built a team from nothing, or walked into chaos and made it work. Their three to five strongest skills, soft and hard. Adjectives are not evidence: "grew the team from one and a half people to eight in a year" is an asset, "good with people" is a mood.

**6. Walk the asset categories out loud, one at a time.** Recorded video and content. Testimonials and client results. Services and programs already built. Products, digital and physical. Tools and technology actually in use. Partnerships and affiliate arrangements. Groups and communities they run or belong to. Awards, certifications, media mentions, speaking. Audience size per platform. Past mistakes and what they cost. And the one nobody lists: **subscriptions and licences still being paid for and no longer used.** Ask for twelve months of recurring charges, and expect the first cash result of the exercise to come from that line.

**7. Score every item 0 to 10 for importance in the next twelve months.** Without a score it is a list, and lists all look equally urgent. With it, later sessions know the dormant course is a 2 and the referral network is a 9 without asking again.

**8. Ask about obstacles and fears last, and ask plainly.** What is actually blocking this: clarity, energy, fear, discipline, or missing proof. What could break the next thirty days if nobody plans for it. What they know they should have done and have not. Do not soften these into consultant phrasing and do not fix them here. You are taking inventory, not treating anything.

**9. Close with the question that outperforms the rest of the interview.** *What did I not ask that I should know?* Then: *what do you most need from me right now?* Both regularly change the plan more than any structured section did.

**10. You write the file. Answering was their work.** Show a finished document, read back the three things that most change your advice, and name what you will now not do because of an answer they gave.

---

## DEFINITION OF DONE

1. **The disclosure level is recorded**, and if it is the third one, the list of advice you cannot give was said out loud and is in the file.
2. **The five planning variables have real answers or an explicit blank:** money, time, audience, skills, tools. A blank is a valid state; a guess is not.
3. **Achievements carry numbers.**
4. **Every asset has a 0 to 10 importance score**, and the dormant paid tools list exists even if empty.
5. **Volatile facts are date stamped**, durable ones are not.
6. **The owner has seen one concrete thing change** as a result, a plan corrected, a purchase cancelled, an asset put back to work. Otherwise you ran an interview, not an inventory.

---

## MAKE IT YOURS

1. **Cut the sections that do not apply before you ask anything.** Someone looking for a job and someone scaling a practice need different middles. Current reality, ammunition and obstacles stay in every version.
2. **Make each section's refresh trigger a condition, not a date.** Runway when income changes, assets when something new gets built, obstacles when the owner repeats the same complaint twice.
3. **Let them answer in their strongest language**, even when the file is written in another. Answers get thinner in a second language and the thinness is invisible in the transcript.
4. **Match the stopping rule to their attention.** Twenty minutes at a time suits most people, and finishing across four sessions beats abandoning in one.
5. **If money stays out entirely**, run everything else and treat that section as a known blank you re-offer once a quarter, never as a reason to skip the inventory.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
