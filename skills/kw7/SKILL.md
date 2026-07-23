---
name: kw7
description: "KW7: turn a question about search demand into real numbers, monthly volume, the 12 month curve, cost per click, competitor organic traffic. Use when a decision needs data, not opinion."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: kw7
  synced: "2026-07-23"
---

# SKILL: Turn search demand into numbers

**Trigger word: `KW7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Metered mode** needs one keyword data provider. You return absolute numbers: how many people search a term in a named country each month, what the curve did over twelve months, what a click costs.
**Directional mode** needs no account at all. You work from free public signals and return direction only: rising or falling, bigger or smaller, worth a look or already dead. That is enough to kill a bad idea early, and it is never enough to size a market.

Start in whichever mode today allows. Moving from directional to metered changes the precision of the answer, not the method.

| Source | Needed | How to connect |
|---|---|---|
| **DataForSEO** | fastest route to real numbers, pay per use | [dataforseo.com](https://dataforseo.com/) · reference: [docs.dataforseo.com/v3](https://docs.dataforseo.com/v3/) |
| **Google Ads API, Keyword Planner** | the only source that answers worldwide in one query | [developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) · [keyword planning](https://developers.google.com/google-ads/api/docs/keyword-planning/overview) |
| **Google Trends** | free, relative curve only, never a volume | [trends.google.com](https://trends.google.com/trends/) |
| **SimilarWeb free tier** | total site visits, a manual check in the browser | [similarweb.com](https://www.similarweb.com/) |

Any one of the first two is enough to start. Missing the others changes what you can say, not whether the skill runs, as long as you name which source measured what.

**Check your connectors before you write code.** Some providers now arrive as MCP servers or as ready connectors inside AI clients, which is a connect and approve step rather than a build step. Look at what your client already offers before building a wrapper. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** About ten minutes to register with a pay per use provider, plus a small prepay, and calls then cost roughly a cent each. **Days** for the Google Ads route, because it needs an Ads account with an approved developer token and there is a human review at the other end. Free public signals cost nothing and are available in the next five minutes.

---

## WHAT

**Everyone has an opinion about how many people search for a thing, and the opinion is usually wrong by a factor of ten.**

Which page to write, which term to bid on, whether a market is growing or already dead: these get decided on instinct, and instinct cannot tell 200 searches a month from 200,000. Money follows that guess into ads and content. This skill replaces the guess with a table, so the owner argues with numbers instead of taste.

**Without it a connected AI fails here in two specific ways, and both arrive looking like answers.** It states a volume from training data, confidently, with no country and no date attached, and nothing in the sentence tells the owner it was never measured. Or it does pull real data and then stacks it wrong: total site visits from one tool placed beside organic search traffic from another, as though the two counted the same thing. A domain with large total traffic and small organic traffic is product led or paid led, not a broken measurement, and reading that as a contradiction has sent more than one strategy discussion in the wrong direction with full confidence.

---

## GOAL

**One short table the owner can act on, with a verdict above it.**

For a keyword: monthly search volume, the 12 month curve, cost per click, competition level, top of page bid range. For a competitor domain: organic search traffic and how many keywords it ranks for.

Above the table, one sentence saying what the numbers mean. **A table with no verdict is homework, not an answer.**

What counts as a good number is not universal, so do not invent the standard. Take it from the owner's constitution and memory if it is there, written as a business target rather than a search metric. If it is not there, ask once and write the answer into memory. Never assume silently: if you had to guess what a result is worth to them, say which assumption you used.

---

## TRIGGER

- The owner writes `KW7` followed by one or more keywords, or `KW7 traffic` followed by one or more domains.
- The owner asks how many people search for something, or how much traffic a competitor gets.
- **Before budget goes into a term or a page**, whether that budget is ad spend or the owner's own writing hours.

**Not a trigger:** general strategy questions, and idle curiosity about a market nobody is about to act on. Those are a conversation, not an artifact. Pulling paid data to decorate an opinion wastes the owner's money and your credibility.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**A search volume only becomes an answer once you know who is asking.** The same keyword returns a different number in every country, and the same number means opposite things depending on what the owner sells, at what price, and to whom. Twelve hundred searches a month is a dead end for a low margin product and a full pipeline for a service billed in thousands. None of that is in the API response and all of it is in the owner's own layers.

So read the constitution and memory before the provider. The market they actually sell into, the price of what they sell, and what they count as a result are what turn a table into a verdict. Memory does a second job that saves real money here: it holds what was already looked up and when, which stops you buying the same number twice and stops you quoting last year's figure as if it were current.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Researches demand most days:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
KW7 {keyword} or KW7 traffic {domain}. Real search demand: volume, 12 month curve, CPC, competitor organic traffic. Always name which source measured what, and which country. Spec: skills/kw7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**Default is a table in the conversation and nothing saved.** Most lookups are one off, and filing them all turns the memory layer into a landfill.

A lookup earns a place in memory when it feeds a decision: a page, a campaign, a product bet. Then it goes into that project or topic file, **with the query date and the country it was asked about**. Search volume ages fast, so an undated number is worse than no number.

**What does not belong there:** raw provider responses, and every keyword the owner ever wondered about. **What rots:** cost per click figures, competition levels, and anything about a provider's pricing. All three read as current forever and are stale within a year.

If the provider bills per call, keep one running line of spend so the owner is never surprised by an invoice.

### TOOLS

What to connect is in REQUIRES above and is not repeated here. What belongs here is the naming, because it moves fast and the owner will hear all of it.

The layer is called **Tools** because a tool is what the model finally calls. How that tool arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **Spend without ceremony, top up never.** A normal lookup costs cents and gets no approval gate, because an owner who has to ask permission for every question stops asking, and then the skill is dead. A large batch gets a balance check and an estimate out loud first. **Putting money into the account is always the owner's action, never yours**, and that does not relax because a query looked urgent.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Pick the mode before spending anything.** A keyword question and a competitor question are different calls with different costs. If the owner asked something vague, sharpen it into one of the two before you query, not after.

**2. Pin the location first.** Volume without a country is meaningless, and most APIs silently default to one large market. Confirm the location with the owner once, store it as the default, and print it in every table. **A national number quoted as a global one is the most common lie in this work.**

**3. Read the curve, not only the headline number.** Twelve months tells you whether a term is seasonal, rising, or a spike that already passed. A flat 1,000 a month and a 1,000 a month that was 4,000 last spring are opposite decisions.

**4. State the accuracy law every single time you compare sources.**

> **Organic search traffic, keyword search volume and total site visits are three different quantities. Never place a number from one source next to a number from another without naming which measured what.**

The full picture appears only when the sources are stacked deliberately, and it disappears the moment they are averaged.

**5. Keep cost discipline without bureaucracy.** Cents per call means no gate for a normal lookup. Check the balance before a large batch, and tell the owner before any top up rather than after.

**6. Answer in one sentence, then show the table.** The sentence names the decision the numbers support: worth writing, not worth bidding, market is shrinking, competitor is not winning this on search.

---

## DEFINITION OF DONE

1. **A one sentence verdict** above the table, naming the decision the numbers support.
2. **A table** carrying volume, curve, cost per click and competition, or organic traffic and ranked keyword count for a domain.
3. **Every number labelled** with its source, its country and the date it was pulled.
4. **The accuracy law stated** wherever two sources appear side by side.
5. **Anything that fed a real decision written into that project file**, dated, and the session's spend recorded if the provider bills per call.

Missing the first means you handed over homework. Missing the third means the number cannot be trusted in three months, which is exactly when someone will quote it.

---

## MAKE IT YOURS

1. **Set the default location** for the owner's home market, and a second one for the market they sell into. Print both when the two disagree, because that gap is often the whole finding.
2. **Keep a small saved keyword set** for the owner's core topics and re-run it quarterly. The curve over a year is worth more than any single lookup.
3. **Agree the batch threshold once.** How many calls you may make without asking. Below it, work. Above it, estimate first.
4. **Decide what a result is worth to this owner**, in money, and write it in memory. Then every verdict can be arithmetic instead of taste.
5. **No API access at all?** Use free public signals: search autocomplete, related searches, and the relative curve in Google Trends. Say plainly that these are directional, not absolute, and **never present a Trends index as a search volume.** Direction is still enough to kill a bad idea early.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
