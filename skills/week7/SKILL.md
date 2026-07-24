---
name: week7
description: "WEEK7: read the week's own records, count the money, name the patterns, and decide what changes next week. Use once a week, on the same day, instead of writing a recap."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: week7
  synced: "2026-07-23"
---

# SKILL: The weekly review that changes the next week

**Trigger word: `WEEK7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Reading mode:** the week already left records somewhere, daily entries, a calendar, files, a bank app. You read them and hand the owner a draft they correct.
**Interview mode:** there are no records yet, so you ask. Say plainly what that costs: **a person asked to recall their week returns the last three days and a mood.** Even here, have them open the calendar and the bank app while you talk, so two sources are real rather than remembered.

| What to connect | Why it matters here | Where to start |
|---|---|---|
| **Calendar** | What was planned against what happened. The cheapest honest record anyone already has | [developers.google.com/workspace/calendar](https://developers.google.com/workspace/calendar/api/guides/overview) |
| **Bank account, read only** | Money in and money out, without the owner guessing | [developer.gocardless.com/bank-account-data](https://developer.gocardless.com/bank-account-data/overview) · [plaid.com/docs](https://plaid.com/docs/) |
| **Payment processor** | Revenue that exists but has not landed yet, the number people are wrong about most | [docs.stripe.com/api](https://docs.stripe.com/api) |
| **One spreadsheet** | The fallback for all of the above, and often enough for a year | [developers.google.com/workspace/sheets](https://developers.google.com/workspace/sheets/api/guides/concepts) |
| **File history or version control** | What shipped, as opposed to what was discussed | Whatever the owner already uses |

**Check the client's connectors before building anything.** Several of these arrive as MCP servers or ready connectors, which turns a build step into a connect and approve step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** The first review takes forty five to sixty minutes, because there is nothing to read and you are building the shape. Later ones take fifteen to twenty five. A read only bank connection takes half an hour to an afternoon, and in Europe that consent expires every ninety days, so schedule the renewal.

---

## WHAT

**In a working system the loop has three steps: something happened, it got written where the next session sees it, it changed what happens next. This skill owns the third step, and it is the one people leave out.**

Daily capture and session close cover the first two. Without the third, all of that is a diary with good formatting: an excellent record of a year in which nothing was redirected.

**What an AI does wrong without this.** It answers from the last few messages, so it optimizes the most recent thing instead of the repeating thing. It cannot see that a problem is on its third week, because weeks one and two scrolled away. And asked for a weekly review it produces what it is best at, a well organized recap that reads as progress and asks nothing of anyone.

**Be honest with the owner about the odds.** Most people who start a weekly review have stopped inside a month. Two fixes work, and both are built into the steps below: **keep it short enough to survive a bad week**, and **hand over a draft to correct instead of a blank page to fill.**

**One real failure.** A body weight number was reported as four kilograms of progress in two weeks, and plans were adjusted around it. It was the first measurement after a seventeen day gap, next to a stale baseline. Nobody lied: the number was correct and the reading was invented. It survived because a single session sees a value, and only a review sees a series. That same week the effort that was genuinely working stayed invisible for the opposite reason. It improved slowly, so no single day showed it.

That is the job. A session sees a value. This skill sees a series.

---

## GOAL

**A week that ends with at most three decisions written into the focus layer, and a money picture the owner has looked at.**

One test decides whether it ran: **what will be different next week because of this?** If the honest answer is nothing, the review did not run, it was read. A weekly review that ends in a nice summary is a newsletter the owner writes to themselves, and people cancel those.

Four things must be true when it is done:

1. **It read the records** rather than the owner's memory.
2. **The money got counted**, not estimated.
3. **The patterns are named across weeks**, not events listed inside one.
4. **The focus layer changed**, or a line says it did not and why.

What counts as a good week is not yours to invent. Take the standard from the owner's constitution and goals. If it is written nowhere, ask once, then store it so nobody asks again.

---

## TRIGGER

- The owner writes `WEEK7`, or asks how the week went, how the month is going, or where the money is going.
- **The recurring slot.** Same day, same time, every week. One of the few skills where the calendar is the trigger, because the rhythm is the value.
- **The end of something bigger:** a project shipped, a trip, a quarter. Run it then even if it is out of slot.

**Not a trigger: a missed week.** Never run two reviews back to back to catch up. Doubling up is how this habit dies around week five, and it is unnecessary, because the missed week's records did not go anywhere. Read them as history in one line inside the current review, then run the current week normally.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This one touches four layers in a single run, which is why it is the slow turn of the loop: it **reads memory**, **judges against the constitution**, and **writes to focus**. Read the constitution before the records. Without it you grade the week against a generic productivity template, hours worked, tasks closed, inbox emptied. A week can score well on all three and move nothing the owner cares about, and an AI that congratulates them for it is worse than silence.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on whether the owner really reviews weekly.

**They do:** put it in the always loaded core. It fires every week, and the core is where rhythms live.
**They intend to:** put it in the skills index the core already links to, and let it load on the trigger. An aspirational habit does not deserve permanent context.

Either way the line is the same:

```
WEEK7, once a week on the same day. Read the week's own records, not my memory of it. Money in, out, left. Patterns across weeks, not events inside one. Max three decisions, then update focus. You draft, I correct. Spec: skills/week7.md
```

### MEMORY

**One file per week, and it is never cleaned.** Comparability is the whole asset, so keep the format boring for a year at a time. Daily capture writes into the same file, which is what makes this skill reading rather than gathering.

**Store raw numbers, not your reading of them.** Money in, money out, the balance, whatever else the owner counts. In two months the argument will be whether things were better before, and a summary sentence cannot settle that while three numbers can. **Do not store the recap prose either.** It is the part nobody rereads, and the part that makes the file too long to reread.

**What rots:** plans, statuses, and any decision without a check date. Those belong in the focus layer or in a task. Left in the weekly record they quietly contradict the live version within a month.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. Today those usually arrive as MCP servers or connectors the client installs, before that they were hand written API wrappers. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **Money connections are read only.** A review never moves money, pays an invoice, cancels a subscription or issues a refund. It names what should be cancelled and the owner clicks. Ask for read scope when connecting and decline write scope even when it is offered, because this is the one layer where a mistake cannot be fixed by editing a file.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Read the week before asking a single question.** Daily entries, calendar planned against calendar happened, files changed, things shipped, money. Arrive with a filled draft. **A blank page handed to a tired person on a Sunday evening is the most common way this habit dies.** You write first, they correct.

**2. Check last week's decisions first.** They were written down, so mark each one done, dropped, or still running before anything new is discussed. A review that never audits its own previous output is a suggestion box.

**3. Count the money, every week, in its own section.** What came in, what went out, and the one number that tells this owner where they stand. Someone living on savings wants runway, given as a date, because months are abstract and a date is not. A business wants its cash position. Someone on a salary wants money in against money out this week, nothing more. Pick the number once and keep it for a year. **Never estimate a number a statement holds.** Missing is a legitimate value, and a guess in a permanent record becomes a fact by repetition.

Then the part that makes this belong here rather than in a finance app: **say what that number changes about next week.** Whichever one it is, it is usually the strongest single input into what the owner does on Monday, and most reviews leave it out because it feels like a separate topic. It is not. Financial data is memory, and reading it on a rhythm is the loop.

**4. Look across weeks, not inside one.** Keep a short standing list of live patterns and mark each one continuing, broken, or new. **Something on its third consecutive week is a signal. One bad Tuesday is weather.** Report what changed state and stay quiet about the rest, because a pattern list read out in full every week gets skipped in full.

**5. Force it down to at most three decisions.** A decision names what changes, who does it, and when it gets checked. "Be better about X" is a feeling. If the week produced none, say so in one line rather than manufacturing one. If it produced eleven, the owner has a week of intentions and no week to put them in.

**6. Update the focus layer. This is the redirect, and it is what makes this a loop rather than a record.** Every decision lands either in the focus layer or in a task with a date. Anything that lands nowhere gets deleted in front of the owner, with a sentence saying why. If they have a dedicated focus routine, hand it over rather than editing that file yourself.

**7. Keep it short enough to survive a bad week.** Agree a ceiling, twenty minutes or one screen, and hold it. Bad weeks are when the review is worth the most and when a long ritual gets skipped, so write the short version in advance: money, one pattern, one decision. **A short review that happens beats a thorough one that stops happening in month two.**

**8. Do not soften the record.** If nothing moved, write that nothing moved. A review that finds a win every single week is a mood management service, and the owner will stop believing the weeks when there really was one.

---

## DEFINITION OF DONE

1. **The weekly file exists**, holding raw numbers rather than a summary of them.
2. **Money is written down:** in, out, and the one number that fits this owner, a runway date on savings, cash position for a business, money in against money out on a salary.
3. **Live patterns are listed**, each marked continuing, broken, or new.
4. **Last week's decisions are marked** done, dropped, or running.
5. **At most three decisions for next week**, each with a person and a check date.
6. **The focus layer was updated**, or a line explains why nothing changed.

Missing the sixth means you wrote a newsletter. Missing the fourth means every week starts over and the loop never closes.

---

## MAKE IT YOURS

1. **Pick the day and stop moving it.** Sunday evening, Friday afternoon, Monday morning all work. A day that moves does not, because a rhythm cannot be rescheduled twice.
2. **Choose the three money numbers for this owner and keep them for a year.** An employee wants spend and savings rate. A freelancer wants invoiced, paid and collected, three different numbers routinely treated as one. A business owner wants runway. Changing the metrics deletes the history.
3. **Set the pattern window.** Three weeks is a good default. Pick the number at which the owner would want to hear about it, and not one week sooner.
4. **Write the bad week version now**, while things are calm. Decide which two sections survive when there is no time and no morale, because that call cannot be made well in the moment it is needed.
5. **Review the reviews after about two months.** Read the last eight weeks of decisions and count how many happened. Under half means the decisions are too big, not that the owner is undisciplined. Cut their size, not the ritual.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
