---
name: constitution7
description: "CONSTITUTION7: write the file your AI reads at the start of every session, so every other skill has somewhere to attach. Use first, before any other skill, and again when it stops being true."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: constitution7
  synced: "2026-07-23"
---

# SKILL: Write the file your AI reads first

**Trigger word: `CONSTITUTION7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **Do this one before anything else.** Every other skill ends with "add this line to your always loaded core". This is the skill that creates the core. Without it the others have nowhere to attach and quietly do nothing.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With raw material:** the owner already has notes, a brain dump, old journals, a website about page, anything they have written about their own work. You draft from that and ask fewer questions.
**Without it:** you interview them. Slower, and the result is often better, because the answers are fresh rather than copied from something they wrote for an audience.

What you actually need:

| What | Why |
|---|---|
| **Somewhere to save a file** | A folder the AI can write to. That is the whole technical requirement |
| **A client that loads files at session start** | Otherwise the constitution exists and never gets read, which is worse than not having one |
| **Twenty to forty minutes of the owner's attention** | The bottleneck. Not your speed, their thinking |

**Know where your client loads from before you write a word.** Every tool does this differently: some read a named file in the project root, some a settings folder, some need the file listed explicitly. Find out first, because a constitution in the wrong place is a document, not a constitution.

**One structural note worth getting right on day one.** Keep the owner's content in **one folder** that holds nothing but their own material, and keep the machinery, scripts, configuration, keys, a level above or beside it, never inside. The content folder should survive being copied to a new machine, a new tool, or a new AI. Most agent runtimes already work this way. It matters because tools get replaced roughly every eighteen months and the notes are supposed to outlive them.

**Setup time, honestly.** One session to a working first version. It will be wrong in places and that is expected. It becomes accurate after about three weeks of use, because you only find out what is missing when the AI gets something wrong and you trace it back to a line that was never written.

---

## WHAT

**A constitution is the file your AI reads before it knows anything else, and it is the only file that costs you on every single message.**

That second half is why most of them fail. People write a constitution that describes them: history, values, personality, a paragraph about their childhood. It reads beautifully and changes nothing, and it is loaded again on every message for the rest of the year.

**The opposite failure is just as common:** no constitution at all, so every session starts from zero. The owner explains who they are, what they are working on, and how they want to be spoken to, and then does it again tomorrow. That is not an AI with memory, it is a stranger with a good vocabulary.

This skill exists to produce the short version that actually changes behaviour, and to keep it short as the owner's life gets longer.

---

## GOAL

**A file, short enough to load on every message, that changes what the AI does.**

The test for every line is one question: **if I delete this, does the AI behave differently?** If not, it is description, and description belongs in the memory layer where it loads only when relevant.

Four things must be true:

1. **It exists** where the client actually loads it, and the owner has seen the AI use it.
2. **It is measured.** State its size in tokens. Anything the owner reads on every message deserves a number, not a feeling.
3. **Every line earns its place** by the deletion test above.
4. **It defines the loop** (below). Without that the system is a filing cabinet.

---

## TRIGGER

- The owner says `CONSTITUTION7`, or asks how to start, what their AI should know, or why it keeps forgetting.
- **Before any other skill**, because every other skill needs the core to exist.
- **When the AI gets something wrong that it should have known.** That is the most valuable trigger there is: the mistake names the missing line.
- **When something changes that changes the answers:** new work, a new goal for the year, a rule that turned out to matter.

**Not a trigger:** a calendar reminder to review it. A constitution revised on a schedule accumulates paragraphs. Revise it when reality moves.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

The constitution is layer one, and its real job is **to make the other four findable.** It does not contain memory, it says where memory lives. It does not contain the skills, it points at the index. Get that boundary wrong and the constitution absorbs the whole system, which is the single most common way these fail.

### CONSTITUTION

This skill writes the constitution, so the line goes inside the file it creates:

```
CONSTITUTION7. This file is the core. It stays short enough to load every message, every line changes what my AI does, and it points at the other layers rather than containing them. Revise when reality moves, not on a schedule. Spec: skills/constitution7.md
```

### MEMORY

**The constitution is not memory and must not become it.** The rule that holds the line: the constitution holds **what is always true**, memory holds **what happened**.

Anything dated goes to memory. Anything about one project goes to memory. Anything you would have to update more than a few times a year goes to memory, with the constitution holding only a pointer to where it lives.

Keep the old versions. When a constitution changes, the previous one is the record of who the owner used to be, and that turns out to be worth reading.

### TOOLS

None required beyond a place to write a file. That is deliberate, and it is worth saying to the owner: **the most important layer of the system needs no integrations at all.** Everything that needs an API can wait.

The layer is called Tools because a tool is what the model finally calls. Today those usually arrive as MCP servers or connectors the client installs. Name the mechanism when you use one, and do not let the mechanism rename the layer.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Read anything they have already written** before asking a single question. A brain dump, old notes, their site, anything. Come back with what you already know, and only then ask.

**2. Interview them, one question at a time.** Not a form. Wait for each answer, because the second answer is usually better than the first and only arrives if you did not move on.

Six questions produce most of a working constitution:

- **What do you do, in one sentence someone else could repeat?**
- **Who depends on you?** Family, clients, a team. This shapes almost every judgment call you will make later.
- **What are you trying to make true, and by when?** A goal with no horizon cannot be planned against, and one with no test cannot be finished. Get both.
- **What do you have to work with?** Money and how long it lasts, hours actually free in a week, what you already know how to do, who you already know, what you have already paid for. **Without this you will give advice that assumes a runway or a network that is not there**, which is the most common way an AI is confidently useless. A rough answer is enough here; the full inventory belongs in memory.
- **What must I never do without asking you first?** Send something, spend something, delete something, speak in their name.
- **How do you want to be spoken to?** Language, directness, how much hedging they will tolerate.
- **What has gone wrong with an AI before that you do not want repeated?** This is the highest value question in the set and almost nobody asks it. The answer becomes a hard rule, and hard rules are the part of a constitution that earns its cost.

**3. You write the draft. Not them.** They have already answered. Asking them to write it turns a twenty minute job into a project that never finishes. Show them a complete file, not a template with blanks.

**4. Run the deletion test on every line, out loud.** For each one: what would the AI do differently without this? Delete anything with no answer. Expect to cut a third of your own draft, and cut it before showing them rather than after.

**5. Define the loop, because this is what makes it a system.** Write into the constitution, in the owner's own terms, how what happens gets back in:

> Something happened → it got written where the next session will see it → it changed what I do next.

Name the actual mechanism for each of the three. What captures, what stores, what redirects. **Any of the three missing means the loop is open**, and an open loop is a filing cabinet with good intentions. The third step is the one people leave out, and it is the one that makes the difference.

**6. Measure it.** Count the tokens and tell them the number. Then tell them what it costs across a month of use. Nobody optimises what they cannot see, and this is the one file where size is a running cost rather than a one time one.

**7. Install it where the client actually loads it,** then prove it: start a fresh session and ask the AI something only the constitution would let it answer. If it cannot, the file is in the wrong place and everything else you are about to build sits on nothing.

**8. Set the revision trigger, not a schedule.** Write into the file: revise when the AI gets something wrong that it should have known, or when the answer to one of the six questions changes. Then leave it alone.

---

## DEFINITION OF DONE

1. **The file exists** where the client loads it, proven by a fresh session that used it.
2. **Its size is known** in tokens, and the owner has seen the number.
3. **Every line passes the deletion test.**
4. **The loop is written down**, with all three steps named and a real mechanism for each.
5. **The revision trigger is inside the file**, and it is a condition rather than a date.

Missing the first means you wrote a document. Missing the fourth means you built storage, not a system.

---

## MAKE IT YOURS

1. **Set the size ceiling now, while the file is small.** Pick a number in tokens or characters and put it in the file. Constitutions do not grow by decision, they grow by one reasonable addition at a time, and a written ceiling is the only thing that ever stops it.
2. **Decide what the AI may do unasked.** Reading and organising, almost always yes. Anything that leaves the machine, almost always no. Write both sides, because a rule that only lists prohibitions produces an assistant that asks permission to read a file.
3. **Split it when it gets too big**, do not compress it. One core file that always loads, plus linked files it points at. Compressing a constitution into dense abbreviations makes it cheaper and stops it working.
4. **Write the first version knowing it is wrong.** It becomes accurate through use, when the AI makes a mistake and the fix turns out to be a line nobody thought to write. Waiting for a perfect first version is the most common way this never gets done at all.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
