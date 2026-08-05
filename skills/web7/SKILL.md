---
name: web7
description: "WEB7: audit a company's whole web presence against marketing and sales principles, one base and four doors, and return a score, three risks and three jobs. Use when someone asks why a site is not producing customers."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "0.5.0"
  source: web7
  synced: "2026-08-05"
---

# SKILL: Audit a web presence the way a buyer walks it

**Trigger word: `WEB7`.**

**Human:** paste this file into your AI, give it a domain. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**Nothing below is a hard blocker, and the depth you can reach is set by what you can reach.**

The audit runs at three depths. Pick the one today allows, say which one you ran, and never compare a result from one depth against a result from another.

| Depth | Time | What it needs | What it can answer |
|---|---|---|---|
| **fast** | about 5 minutes | HTTP and DNS only. No browser, no language model, no paid API | whether they are findable and whether the site works |
| **standard** | about 30 to 40 minutes | a headless browser, a language model, a page speed API, optionally a search results API | most of the audit, forms checked but never submitted |
| **deep** | 1 to 2 hours plus a 30 day tail | one real form submission from a mailbox you can read, plus the owner's own accounts | whether a contact actually arrives and whether anyone answers |

| Source | Needed for | How to connect |
|---|---|---|
| **Headless browser** (Playwright or similar) | rendered content, cookies, forms | [playwright.dev](https://playwright.dev/) |
| **PageSpeed Insights API** | speed and core web vitals | [developers.google.com/speed/docs/insights/v5/get-started](https://developers.google.com/speed/docs/insights/v5/get-started) |
| **A search results API** | position, external mentions, local listing | any provider that returns raw results with a date |
| **A mailbox you can read** | the delivery proof, deep only | any account with API or IMAP access |
| **Meta Ad Library** · **Google Ads Transparency Center** | whether they are running ads, no login needed | [facebook.com/ads/library](https://www.facebook.com/ads/library/) · [adstransparency.google.com](https://adstransparency.google.com/) |
| **The owner's own accounts** | Search Console, analytics, ad account. Deep only, never for a stranger's domain | the owner grants them, you never assume them |

**Check your connectors before you write code.** Several of these now arrive as MCP servers or ready connectors inside AI clients, which is a connect and approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**A human step is a legitimate kind of step, not a gap.** Some of the strongest checks here are a person opening a browser: looking up an ad library, walking a checkout, reading a third party traffic estimate. When a step is human, say so, say exactly what the person does, and label what comes back as an estimate if that is what it is.

---

## WHAT

**A business asks why its website is not producing customers, and gets an answer about its website.**

That answer is almost always too small. The site is one surface. The buyer arrived from somewhere, decided whether to believe it, tried to act, and then either heard back or did not. A broken link and an email that silently never arrives look nothing alike in a report and cost the same thing: the customer.

**Without this a connected AI fails here in three specific ways, and all three look like answers.**

It grades taste. Design, tone, whether the hero image is nice. None of that is measured, none of it survives a second opinion, and the owner cannot act on it.

It reports what it read rather than what it tested. A privacy page that returns a page is not a privacy page; a form that renders is not a form that delivers. The difference is the whole finding.

It hands over twenty findings. Twenty findings is a document nobody opens. The only part an owner acts on is the part that says: start Monday with this one thing.

---

## GOAL

**Check a company's web presence against marketing and sales principles, and find how to improve sales and brand results.**

Concretely, one number from 0 to 100, the risks that cap it, and three jobs with a price and a way to check them in thirty days.

**The score is a state, not a grade.** It measures what the business shows a buyer today against the rubric below. It is not revenue, not a forecast, and not a judgment of the product. A good product badly explained and a bad product well explained look identical from outside, and the report says so in words rather than leaving the reader to guess.

---

## TRIGGER

`WEB7 {domain}` · `WEB7 fast {domain}` · `WEB7 deep {domain}` · "audit this site" · "why is this site not selling"

Three modes, and they are not interchangeable:

- **own** the owner's own domain. Everything permitted, including one real form submission.
- **client** a domain the owner has written permission for. Same as own, permission recorded before anything is submitted.
- **foreign** a stranger's domain. Read only. Never submit a form, never create an account, never send a message. One pass, no repeats.

> 🔒 **WEB7 changes nothing, ever.** It measures and it writes a report. Every fix leaves through a different door: the site builder, the ad account, the host, or a person. An audit that quietly edits the thing it is auditing has destroyed its own baseline.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**A finding only becomes a job once you know whose business it is.** The same missing element is urgent for one company and irrelevant for the next: a booking form matters enormously to a clinic and not at all to a wholesaler who sells by phone. What the owner sells, at what price, to whom, and what they count as a result are what turn a list of defects into three ordered jobs. None of that is on the site and all of it is in the owner's own layers.

### CONSTITUTION

One line makes this skill exist.

**Audits sites regularly:** put it in the always loaded core.
**Occasional:** put it in the skills index the core already links to, and let it load when the trigger fires.

```
WEB7 {domain}. Web presence audit: one base and four doors, plus risks, what to measure and where to grow. Every number carries n, method and date or it is not reported. Changes nothing. Spec: skills/web7/SKILL.md
```

### MEMORY

**One folder per audit, named by date and domain.** Inside it: the raw collected data, the findings, and the report. The raw data is what lets a second audit six months later show a delta instead of a fresh opinion.

**What belongs in the owner's own layers:** the verdict, the three jobs, and the date. Not the raw scrape.

**What rots:** speed numbers, search positions, follower counts, and anything about a third party tool's pricing. All four read as current forever and are stale within months. Date them or drop them.

**What must never be written down at all:** anything the audit picked up that identifies a real person and was not already public on the site.

### TOOLS

What to connect is in REQUIRES above. What belongs here is one rule about cost and one about consent.

> 🔒 **Paid scraping and one real form submission are both gated.** Before spending on a third party scrape, say what it will cost and wait for a yes. Before submitting a real form on a domain the owner does not own, have written permission. A test submission is a message a human being will read; sending one uninvited is not a measurement, it is a stranger in someone's inbox.

---

## HOW IT RUNS

**One base, four doors, three conclusions.**

The four doors are the buyer's path and they only work in order. The base is not a door, because the buyer does not walk through it, but it carries the most weight, because everything downstream is about it.

### The base · PRODUCT AND BRAND · weight 12

*Is there anything here worth buying, and does the name carry any weight?*

What it holds: whether a stranger reading the site names the same product, the same buyer and the same problem the owner would · whether the offer sentence is in the first screen · how much of the range has a page of its own · whether the price is findable and holds · why buy here rather than next door · what comes back when you type the brand name into a search engine, and whether anyone types it at all.

Why it is the base: better findability delivers people faster to an empty room.

### Door 1 · FOUND · weight 7

*Do they find you, and by which routes?*

Every route in, not only search. Search position and the queries that actually bring people · whether AI answers name this company when someone asks the question it answers · paid: whether ads are running and since when, from the public ad libraries, no account needed · social accounts, whether they exist, whether they post, and whether anyone responds · who links to and mentions the company from outside its own properties · the direct route, people typing the name.

Third party traffic estimates belong here and are labelled **estimate**, always, without exception.

### Door 2 · BELIEVED · weight 7

*Do they believe you in the first ten seconds?*

Whether it is clear what is sold and to whom · whether a real person stands behind it, with a name and a face · whether testimonials carry a full name and a link that resolves, or are first names nobody can check · whether the legal pages are real pages or wallpaper · whether the company's registered details match what the public register says · **whether trackers fire before anyone consented**.

### Door 3 · ACT · weight 7

*Can they act, and does the thing they click work?*

Speed and the first three seconds · broken links across the site · whether the pages ads point at are alive · whether the form can be filled at all, whether it answers, and whether a confirmation appears on screen · whether the buying path shows shipping, returns and the final price before the last step · accessibility, which is not charity, it is the share of buyers who cannot complete the purchase.

This door stops at the confirmation on screen. What happens to the message after that belongs to the next door.

### Door 4 · KEPT · weight 7

*Does the contact go anywhere, and does anyone answer?*

Whether the message reached a place a human reads · **whether the email actually arrived, and whether it landed in spam** · the mail domain's own records, which is the cheapest check in the whole audit and one of the most commonly broken · whether anyone follows up and how fast against what the site promised · whether a satisfied customer has any way to recommend them onward.

This is where the quiet money sits. Nothing here is visible from outside without a real submission, which is why this door is thin in fast mode and honest about it.

### The three conclusions

These measure nothing. They read what the doors already measured.

**RISKS** are a gate. A red risk does not lower the average, it caps the total and takes the headline. Triggers: tracking before consent · legal pages that are wallpaper or contradict each other · a mail path that is broken or handed to a stranger · a dead landing page under a live ad · a contact that never arrives. Each is a measured contradiction with a named fix and a rough time to fix it, usually under two hours.

**MEASURE** is a recommendation, not a check. It answers: what should *this* business be counting? Not "install analytics". A five product shop and a consultancy that closes two deals a year need different counters. Name between three and five, and say what each one would tell them that they cannot see today.

**GROW** is arithmetic on the four door numbers plus market size. It runs no new check. Where is the cheapest gain, which channel is unused, which market is next.

**Then three jobs.** Each one carries: what to fix, where it lives (site, host, ad account), who does it (the owner, a developer, a tool), roughly how long and how much, and **one number to check in thirty days**. Never a fourth. A fourth job is not a job, it is a list.

---

## THE SCORING MODEL

**Write this into your report so the reader can reproduce it.** A score whose formula is not on the page is a number the owner has to take on faith, and they should not.

**1. Each check gets a colour, and each colour is points.**
green 100 · yellow 55 · red 15 · **not measured is removed from the calculation entirely**, neither zero nor average.

**2. Each check has a weight**, 3 if the section fails without it, 2 if it is desirable.

**3. Section score** is the weighted average of the checks that got a colour.

Two thresholds, and below either one the section gives **no number at all** and prints as grey with two lines, why it was not measured and what would measure it:
- at least half the weight the chosen depth promised, including at least one weight 3 check;
- at least two measured checks. One check is not a section, it is one check wearing a section's name.

**4. Total** is the weighted average of the sections that produced a number:
base 12 · found 7 · believed 7 · act 7 · kept 7.
Sections without a number leave both sides of the fraction and the remaining weights renormalise to 100. **The renormalisation is never silent**: beside the total, always print how many sections of five were measured and what share of the total weight that was. 71 from 70% of the weight and 71 from 100% are not the same 71.

**5. The gate applies last.** Any red risk caps the total at 59, whatever the average said. Store both numbers, before and after the cap, or a genuine improvement from 41 to 58 will look like no change at all.

**6. The headline is named by the weakest door**, not the weakest section. Order: a red risk first, then a red base as the second sentence, then the weakest of the four doors. On a tie the earlier door wins, because the earlier one gates the later. A door that was not measured never takes the headline, however strongly you suspect it.

### Where this model can lie to you, and you say so in the report

**A stranger's score is systematically optimistic.** The checks you cannot run without access are exactly the ones where most businesses are red. Removing them raises the number. A foreign audit carries the label **visible surface only** and is never compared against a full one.

**A weighted average hides the shape of a chain.** Three doors at 90 and one at 0 gives 74. A business where no contact survives is not a 74. Only the headline rule catches that, never the arithmetic.

---

## THE HARD RULES

These are not style. Each one exists because it went wrong once.

1. **Every number carries n, the method and the date.** Missing any of the three and it is not reported, it is marked not measured with one line on how to measure it.
2. **If any part of a green condition is not measurable, the whole check is not measured.** Yellow is for a measured bad result, never for an unknown one. This is the single rule that keeps a rubric honest, and it is the easiest one to break by accident.
3. **Each thing is measured in exactly one place.** Another section may cite it, without its own number and without its own weight. Otherwise one broken landing page gets punished four times and the owner reads four problems where there is one.
4. **Cookies are never judged from a scrape.** A scrape and a real browser session on the same page on the same day return different cookie sets, and the scrape returns fewer. Only a live session counts.
5. **Never the word violation. Only the measured contradiction.** "The banner says no tracking before consent, and three tracking cookies were set before any click, measured on this date." That sentence survives a lawyer. A verdict does not.
6. **Never a percentage from fewer than seven observations.** Three out of four is a sentence, not 75%.
7. **Third party estimates carry the word estimate** every time they appear, including in the summary.
8. **A check that is not built comes back grey**, marked, with what is missing. It never comes back green, and it never quietly disappears from the list. The number of grey checks is part of the result.

---

## DEFINITION OF DONE

1. **One sentence naming where the buyer stops**, chosen by the headline rule.
2. **Five section numbers**, base and four doors, each with how much of it was measured.
3. **The total, with the depth, the mode, and the share of weight measured beside it**, plus both the capped and uncapped value if a gate fired.
4. **Every red risk written as a measured contradiction**, with a date, a fix and a rough time.
5. **What to measure**: three to five counters this specific business should have, each with what it would reveal.
6. **Three jobs**, no more, each with owner, cost, and one number to re-check in thirty days.
7. **A list of what the machine could not check**, including every grey item and every step that needs a human or the owner's accounts. If this list is empty you did not run the audit, you wrote a brochure.

Missing 3 means the number cannot be defended. Missing 7 means it cannot be trusted.

---

## MAKE IT YOURS

1. **Run it on your own site first, then on one you did not build.** Your own site is where you learn the tools. Someone else's is where you learn whether the rubric works, because you cannot unconsciously fill the gaps from memory.
2. **Build the checks in the order the doors run.** Findability is cheap to check and never enough. The delivery proof in door 4 is the most expensive to build and the one that most often finds real money.
3. **Set the weights against your own market.** The ones here were chosen so the base weighs more than any single door and less than any two together. If you change them, write down why, and never compare scores across two different weightings.
4. **Keep a register of what is built and what is not**, and let the report read from it rather than from your memory. This is how grey stays honest as the toolset grows.
5. **Do not build the fixing.** The moment an audit can also change the site, the temptation to fix a small thing quietly and report it as green becomes constant, and the baseline is gone.

---

_Part of the AIOS library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)_
