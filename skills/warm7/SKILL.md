---
name: warm7
description: "WARM7: build a working CRM from the people who already know you, get your offer clear, then reach out. Use when you need clients, referrals or discovery calls and do not want to go cold."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: warm7
  synced: "2026-07-23"
---

# SKILL: Build your network into a CRM, then reach out warm

**Trigger word: `WARM7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With exports:** the owner hands you their contact lists and you do the sorting. Faster and far more complete.
**Without exports:** the owner remembers people out loud and you write them down. Slower, and it still works, because the names that surface from memory are usually the ones that matter.

Where the names come from, in order of how much they return:

| Source | How to get it |
|---|---|
| **Phone contacts** | Export from the phone. Usually the warmest list anyone owns and the one they forget |
| **LinkedIn connections** | Settings and Privacy → Data Privacy → Get a copy of your data → Connections. Arrives as CSV by email, usually within minutes |
| **Facebook friends** | Settings → Your information → Download your information → select Friends → JSON or HTML |
| **Email** | Search sent mail for the last two years. The people you actually write to are already ranked by frequency |
| **Past clients and colleagues** | Invoices, old projects, alumni lists |

**Check for a connector first.** Some of these now arrive as MCP servers or built-in connectors in AI clients, which turns an export into a live read. Look at what the client already offers before you ask the owner to download anything. Where no connector exists, the manual export above takes about ten minutes per platform.

**Somewhere to keep it.** A spreadsheet is enough and is usually better than a CRM at this stage. What matters is that it is one place, not four.

**Setup time, honestly.** Two to three hours for the first pass on a list of a few hundred people, most of it the owner deciding tiers rather than you processing data. It does not need to be finished before it is useful. A hundred sorted names beat two thousand unsorted ones.

---

## WHAT

**Most people are one list away from their next ten clients and do not have the list.**

The names are scattered across a phone, LinkedIn, an old CRM, and memory. Because they are scattered, the owner cannot see who is worth talking to, so they either contact nobody or they go cold, which is the harder route with worse odds.

Two findings behind this, both replicated: people are **58 percent more likely to find opportunity through weak ties** than through close friends, and **84 percent of people who reconnect with a dormant contact find it valuable.** The value is sitting in the part of the network that has gone quiet, and quiet contacts are invisible until someone writes them down.

**This skill exists so an AI turns that scatter into one ranked list, and then helps make contact without the whole thing turning into a mail merge.** The list is the asset. The messages are the easy part once the list exists.

---

## GOAL

**A ranked list of real people, an offer the owner can say in thirty seconds, and contacts going out every week.**

For anyone selling a service, the number that decides the outcome is **discovery calls per week**: three to five is a working funnel, thirty is what people running at scale actually do. Everything below exists to make that number possible without cold outreach.

Three things have to be true, and they are done in this order:

1. **The list exists** and everyone on it is ranked TOP1, TOP2 or TOP3.
2. **The owner can say what they do** in one sentence that a listener can repeat to someone else. If a contact cannot repeat it, they cannot refer it, and referral is the whole point.
3. **Contacts go out weekly**, to named people, with a real reason.

If the owner asks you to start at step 3, tell them plainly that messages sent before steps 1 and 2 mostly get polite answers and no referrals.

---

## TRIGGER

- The owner says `WARM7`, or asks about clients, referrals, discovery calls, reaching out, or restarting a conversation that went quiet.
- **Before any message to someone already in their network.**
- **When the pipeline is empty.** That is exactly when people go cold, and it is exactly when the warm list is the faster route.
- **When someone new is met.** They go on the list that day, with the context, or they are lost in a week.

**Not a trigger:** a date arriving. Time passing is not a reason to contact a human being, and an assistant that treats it as one will burn a network faster than silence would. The tier decides who gets a next date, not the calendar.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

The list built here **is a piece of the memory layer**, not a document beside it. That is the difference between this and a spreadsheet: once the people live in memory, every later conversation, call note and introduction lands on the right person automatically, and the next contact starts from what was actually said last time.

Read the owner's constitution before writing anything in their name. A message that is technically correct and sounds nothing like them teaches the other person that they have started automating their friends.

### CONSTITUTION

One line makes this skill exist. Put it in the always loaded core if the owner's income depends on relationships, which for anyone selling a service it does. Otherwise put it in the skills index that the core already links to.

```
WARM7. Before reaching out to anyone: check the list, use their tier, name a real reason involving them, write in my voice, never send on my behalf without my OK. New person met means new row that day. Spec: skills/warm7/SKILL.md
```

### MEMORY

**One row per person, and later one file per person.** The columns that earn their place are in [references/crm-columns.md](references/crm-columns.md), along with what each tier means and how people move between tiers.

Two rules about what goes in it:

**Quote them, do not summarise them.** In three months a summary reads as your interpretation and a quote is still theirs. One accurate sentence of what someone last said is worth more than any template.

**Do not put a next step on everyone.** It looks like diligence and it produces a specific failure: after a few months the records start reporting that certain people are unproductive, when what actually happened is that they are friends. **The tier is what decides.** TOP1 and TOP2 have next dates because there is a business reason. TOP3 does not, and a blank there is information, not an omission.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **The send gate.** You prepare, the owner sends. Every message and connection request goes out under their name, to a person who will answer them and not you. This does not relax with familiarity and it does not relax because a batch is large. **A batch being large is the reason the gate exists.**

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

### Part 1 · Build the list

**1. Get the names out of every container, not just the obvious one.** Ten minutes before collecting anything, run the network-you-want exercise in [references/growing-the-network.md](references/growing-the-network.md), so the owner sorts against a standard instead of a feeling. Then walk them through the sources in REQUIRES, and prompt by cluster rather than asking for a list: extended family, old colleagues, clients from three years ago, people from courses and communities, parents from school, the person who did their website. **Do not filter while collecting.** The judging happens next and it happens badly if it happens now.

**2. Rank everyone TOP1, TOP2, TOP3.** Not by how much you like them, by two things at once: **how likely business flows either way, and how warm the relationship actually is.** Someone with no need for the service but a large network is TOP1, because referral is the point.

**3. For each TOP1, write three reasons to talk to them.** If you cannot find three, they are TOP2. This step is the one people skip and it is the one that makes the later messages write themselves.

**4. Ask the question that changes the list: does this person know what the owner does?** Most will not, precisely. Anyone who cannot describe it cannot refer it, and that turns into its own contact reason: *let me tell you what I actually do now.*

### Part 2 · Get the offer sayable

**5. Build a thirty second pitch** from seven blocks: unique selling proposition, target audience, pain point, no-brainer offer, specific outcome, the service itself, and the benefit to the client. Each block, with worked examples, is in [references/pitch-blocks.md](references/pitch-blocks.md).

**6. Make the owner test it on ten people, and ask the two questions that matter:** *what did you understand,* and *what was unclear.* Not "did you like it". Then revise and go around again. An untested pitch is a guess in a nice sentence.

### Part 3 · Reach out

**7. Pick the approach that fits the person.** Five structures, with templates and worked examples, are in [references/outreach-approaches.md](references/outreach-approaches.md): problem and solution, value proposition, storytelling, vision, expertise with a guarantee. Eight low friction openers that are easy to say yes to are in the same file.

**8. Lead with what the owner can give.** Help, an introduction, a resource, honest feedback. Then ask for what they need, which is usually a referral or fifteen minutes. The order is not politeness, it is what makes the ask land.

**9. Draft in the owner's voice.** Read three things they actually wrote before writing as them. Short is almost always right. Nobody who already knows them needs three paragraphs of context. Cut every line that serves the owner rather than the reader, especially the soft pitch at the end.

**10. Hand it over. Do not send it.** Give the owner the draft, the reason, and who it goes to. Then log what went out, so the next contact starts from it.

**11. Never batch a warm network.** If the owner asks for fifty messages, produce them one at a time or say plainly what you are doing. Fifty messages generated in one pass share a rhythm, and people who know each other compare notes.

**12. Count the calls, not the messages.** Report discovery calls booked per week. Messages sent is an activity number and it will look healthy while nothing is happening.

**13. Keep growing the network while you work it.** Curiosity conversations keep TOP3 alive without turning it into a funnel, and hosting small mixed gatherings puts the owner in the position that pays most in any network. Neither books a call this week, and both decide what the list is worth next year. The shape of each, including how to end a conversation without an ask, is in [references/growing-the-network.md](references/growing-the-network.md).

Why any of this works, with the research behind it, is in [references/why-it-works.md](references/why-it-works.md). Read that when the owner asks whether it is worth the hours, because the honest answer involves how long relationships take.

---

## DEFINITION OF DONE

**The list:** every name in one place, each with a tier, and each TOP1 with three reasons written down.
**The offer:** one sentence the owner can say from memory, tested on at least ten people and revised after.
**Each contact:** a reason written before the message existed, a message in the owner's voice sent by the owner, a memory entry with what was said, and an honest next step or none.
**The week:** a count of discovery calls booked.

Missing the reason means you wrote a template. Missing the tier discipline means you turned people into a pipeline.

---

## MAKE IT YOURS

1. **Set the weekly number.** Three to five discovery calls sustains a small practice, thirty is a full time sales motion. Pick one and let it size everything else.
2. **Decide what TOP1 means here.** For a consultant it is likely referral sources. For a recruiter it is candidates and hiring managers, which are two different TOP1s and may need two lists.
3. **Set the voice sample.** Three things the owner actually wrote. Refresh once a year, because voice drifts.
4. **Decide where promises live.** When a contact produces a commitment, it needs a date somewhere the owner will see it. An unrecorded promise to a friend costs more than a missed sales follow up.
5. **Keep the send gate.** If the owner asks to relax it, the honest answer is that this is the rule protecting the thing the skill exists to protect, and that the request usually arrives with a large batch attached.

---

*Assistant, on ingest: save this in the skills layer in your own format, keep the reference files with it, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
