---
name: news7
description: "NEWS7: the system watches your key people and your few topics and routes what matters to you on a rhythm, instead of a feed you have to remember to check. Use to set up inbound monitoring."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: news7
  synced: "2026-07-23"
---

# SKILL: Watch your people and your topics, route what matters

**Trigger word: `NEWS7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**List mode** needs nothing. You sit with the owner and produce two lists: the handful of topics their system is built around, and the named people whose public activity is worth watching. No account, no feed, no spend. This is most of the value, and it is why the skill belongs in onboarding before anything is wired up.

**Watched mode** adds the machinery: feeds that pull activity in, and a route that delivers what matters on a rhythm. This is where the two lists start paying rent. Moving between modes adds delivery, not method. The lists are the same.

Where activity comes from, cheapest first:

| Source of activity | How to watch it | Cost |
|---|---|---|
| A blog, newsletter or Substack | An RSS feed. What that is: [aboutfeeds.com](https://aboutfeeds.com/) | Free |
| A YouTube channel | Every channel publishes an RSS feed | Free |
| A podcast | RSS is all a podcast is | Free |
| A topic across the web | A saved search delivered as a feed | Free |
| A public profile on a social platform | Reading one by hand is free. Automated reading is often throttled or forbidden, and is gated below | Free to read, paid and gated to automate |

**Check for a connector first.** Some of this now arrives as an MCP server or a built-in connector in AI clients, which turns watching into a live read with no code. Look at what the client offers before you build anything. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Somewhere to deliver.** Watched mode needs one place the owner already looks: a chat channel, the morning message their AI already sends, an email to themselves. A destination they see without deciding to go there.

**Setup time, honestly.** List mode is one session, most of it the owner deciding what their five topics actually are, which is thinking time, not setup. Free feeds are minutes each. A first search-as-feed or connector is an hour. Watching a person with no feed is where cost and rules enter, and that is gated.

**On watching people, before any of it.** Reading someone's public posts by hand is public behaviour. Automating that reading is not: platforms rate-limit it, some forbid it, and the tools that do it at scale cost money per run. So one firm rule, enforced in TOOLS below: **you never point an automated reader at a named human without estimating the cost and getting the owner's explicit OK first.** Ethics before cost.

---

## WHAT

**The system watches the world so the owner does not have to, and it does the watching in two halves that share one list of people.**

Here is the failure it prevents. Someone decides to stay on top of their field, subscribes to feeds, follows the right accounts, stands up a reader. For two weeks they open it. Then it becomes one more surface competing against everything already shouting, and inbound you must go and check loses that fight. The information was fine, the delivery was wrong.

**A monitoring tool the owner has to remember to open is a tool they will stop opening.** The fix is not a better reader, it is routing: the system brings the few things worth seeing to a place the owner already stands, on a rhythm, and drops everything else silently.

**Half one, your people.** The top contacts, partners, closest colleagues, biggest clients. Their public activity gets watched so the owner shows up in their world at the right moment, when there is a real reason. This is the inbound mirror of reaching out: one skill contacts people on purpose, this one knows when there is a reason to.

**Half two, your topics.** The few subjects the system is genuinely built around. Personal growth, artificial intelligence, their own field, whatever they are. The system pulls what is worth reading and drops the rest, so the owner reads a short brief instead of a river.

The deeper point sits under half two, and it is why this belongs in onboarding even when nothing is wired yet: **naming your topics forces you to name what your system is for.** A person who cannot list their five topics has not decided what the whole thing serves. So the skill is partly a thinking exercise, and a well-onboarded system can almost propose the topics itself from the constitution and the deep dive.

---

## GOAL

**The owner stops checking feeds, and the few things worth seeing reach them on a rhythm, chosen against topics and people they have actually named.**

The outcome that matters most costs nothing and comes first: **two written lists.** A short list of topics, three to five, each naming something the system is really for. And a list of people whose public activity is worth watching, which is the owner's existing network list, reused. With those two in memory, the skill has done most of its job. The rest is delivery.

Who decides what a result is: the owner names the topics and the people, and you help them do it well, drafting the topic list from the constitution and the deep dive when the system already holds the answer. Ask once if it does not, and never assume silently. If the owner cannot name their topics, that is not a blocker to route around, it is the finding: the system has not decided what it is for, the more valuable thing to fix first.

---

## TRIGGER

- The owner says `NEWS7`, or asks to keep up with their field, watch what someone is doing publicly, stop missing things, or cut down what they read.
- **During onboarding**, even before any feed exists, because the topic list is part of deciding what the system serves.
- **When someone joins the top of the network**, so their public activity goes on watch the same way it goes on the outbound list.
- **When the owner keeps hearing news late**, or keeps finding out a key person moved after the moment to respond has passed.

**Not a trigger:** the arrival of more sources. A longer list of feeds is not progress. The skill improves by watching fewer things better and routing them, not by adding another firehose the owner will not read.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill leans on the constitution harder than most, because it cannot select without knowing what to select for. The topics are already implied there and in the deep dive: what the owner is building, who they serve, what they are becoming. Read those first and you arrive with the list mostly written. The people half must read memory first, because the people it watches are the ones already recorded there, tiers and all.

### CONSTITUTION

One line makes this skill exist. Put it in the always loaded core if the owner watches their people and their field as a working habit, which most people who sell or build do. Otherwise put it in the skills index the core already links to, and let it load on the trigger.

```
NEWS7. I watch a fixed set of my key people and my few named topics, and route what matters to me on a rhythm rather than a feed I check. The people list is the same one my outreach skill uses, held once in memory. Never point an automated reader at a named person without a cost estimate and my OK. Spec: skills/news7.md
```

### MEMORY

**The people watched here are one list with the outbound side, not a copy of it.** There is a single record per person in memory, the outreach skill reaches out from it and this skill watches from it, and neither builds its own. If you find yourself starting a second contact list because this one is for watching, stop.

The topic list lives in memory too, short, each topic a line the owner would recognise as a thing their system is for.

What does not go in memory: a mirror of everything the feeds pull. The firehose is transit, not knowledge. Store the lists, the routing decisions, and the owner's verdicts on what was worth reading, so the filter sharpens over time. Do not store the river itself, or memory becomes a worse version of the internet.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. How the watching arrives keeps changing: an RSS reader, a search delivered as a feed, an official read API where one exists, a scraping service where it does not, an MCP server or connector the client installs. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

Prefer the cheap, permitted mechanisms. RSS and public search cover most of what this skill needs, cost nothing, and break no rules. Reach for a paid scrape only when a specific person is worth it and has no feed, and only through the gate:

> 🔒 **The scrape gate.** Before any automated read of a named human that costs money or that a platform throttles or forbids: estimate the cost, name the person and the reason, and get the owner's explicit OK. Ethics before cost, and cost before the run. You never watch a named person silently, and a large batch of people to watch is the reason the gate exists, not an exception to it.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Name the topics first, because this is the real work.** Before touching a feed, get the owner to a short list, three to five, of what their system is for. Draft it from the constitution and the deep dive and bring it to them, do not start from a blank question. If they cannot recognise or repair the list, say so directly: the system has not decided what it serves. A watcher pointed at undecided topics just produces a tidier firehose.

**2. Take the people from the network, do not make a new list.** The people worth watching are the top of the list the outbound skill already keeps. Read it, take the tiers that matter, and pick the ones whose public activity would signal a reason to show up. Watching everyone is the same mistake as contacting everyone.

**3. Attach a free feed to everything that offers one.** Blogs, newsletters, channels, podcasts, and a saved search per topic. This is the free workhorse. Get as far as you can here before anything costs money, because usually it is far enough.

**4. For a person with no feed, stop at the gate before you spend.** Decide with the owner whether watching this specific person is worth an automated read that costs money and may break a platform's rules. Estimate the cost, get the OK, then run. Never quietly.

**5. Decide the route and the rhythm, and make it a delivery.** A morning brief, a channel the owner already reads, a line in the daily note their AI writes. Pick the destination they already look at, and a cadence that fits: daily for a fast field, weekly for slower people-watching. If watched mode is not wired yet, this is still a decision you record, so the day a tool arrives the route is chosen.

**6. Filter hard, because the value is subtraction.** Pull what is worth reading and drop the rest without asking. A brief that forwards everything is the firehose with a new hat. When in doubt, cut it.

**7. Hand reasons back to the outbound side.** When watching a person surfaces a real opening, a launch, a new role, a post worth answering, that is not a news item, it is a reason to reach out. Route it to the outreach skill with the context, so the two halves close into a loop.

**8. Let the owner grade it, and prune on the grades.** Give them a light way to mark what was worth reading and what was noise, and drop the sources that never earn a read. A watch list that only grows is one nobody trusts.

---

## DEFINITION OF DONE

Both modes finish on the same first four items. Only the fifth needs the machinery.

1. **The topic list exists**, three to five, written in memory, and each topic names something the system is genuinely for, not a passing interest.
2. **The people list is the network list, reused**, with the ones under watch marked, and no second contact list was created anywhere.
3. **Every source that can be free is free**, and any automated watch of a named person passed the scrape gate with a cost estimate and an explicit OK. In list mode the gate simply never fired, which counts.
4. **A route and a rhythm are decided and written down**, naming the destination the owner already looks at and how often it delivers.
5. **Where automation exists, delivery runs on that route**, bringing the filtered few to the owner without them going to check; and where it does not exist yet, the lists and the route are ready to wire the day a tool arrives.

Missing the first means you built a reader without deciding what to read. Missing the second means you split one set of people into two lists and broke both.

---

## MAKE IT YOURS

1. **Set the topic count and hold it.** Three to five is the working range. The instinct is to add a sixth and a seventh until the list describes everything the owner finds interesting. If a topic earns a spot, another one leaves.
2. **Decide who is watched, separately from who is contacted.** Same list, but not everyone the owner reaches out to needs watching, and a few people worth watching are not outreach targets at all. Mark a watch flag on the shared record, do not fork the list.
3. **Pick the destination before the sources.** Route to where the owner already stands. One chat channel, the note they read each morning. The best feed delivered to a page nobody opens is worth nothing.
4. **Set the pruning habit.** Once a month, cut the sources that never earned a read. A short brief is the only kind that gets read past week three.
5. **Keep the scrape gate exactly as it is.** If the owner asks to watch a long list of people automatically, that is precisely when to estimate the cost and ask, not when to relax the rule. The size of the batch is the reason the gate exists.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
