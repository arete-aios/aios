# Layer 1 · Constitution

**The file your AI reads before it knows anything else, and the only file that costs you on every single message.**

That second half decides everything about how it is written. A constitution is not the place for the best writing about the owner. It is the place for the lines that change what the AI does, paid for again on every message for the rest of the year.

---

## What belongs in it

**Only what passes the deletion test: if I remove this line, does the AI behave differently?**

In practice that is five kinds of thing.

- **Who the owner is, operationally.** What they do in one sentence, who depends on them, what they are trying to make true and by when.
- **Hard rules.** What the AI must never do without asking: send, spend, delete, speak in their name. And the other side, what it may do unasked, so the owner does not end up with an assistant asking permission to read a file.
- **Voice and directness.** Language, how much hedging is tolerated, what the AI should stop doing.
- **The loop**, with a real mechanism named at each of its three steps. See [feedback-loop.md](feedback-loop.md).
- **Pointers to the other four layers.** Where memory lives, where the skills index is, which file says what matters now.

That last one is the constitution's real job: **to make the other four layers findable.** It does not contain memory, it says where memory is.

---

## What does not belong in it

This is the useful part, because every failed constitution failed the same way.

- **Description instead of instruction.** A paragraph about the owner's childhood, values, personality, the story of how they got here. It reads beautifully and changes nothing, and it is loaded on every message forever. Move it to memory.
- **Anything dated.** This week, this quarter, the current client, the number as of last month. Dated content in an always loaded file is wrong within weeks and expensive the whole time.
- **Project detail.** One project's context belongs with that project, not in the file every message pays for.
- **The skill library itself.** A trigger line for a skill fired most days, yes. Twenty-four lines for skills nobody triggers, no. Those belong in an index the core links to.
- **Anything updated more than a few times a year.** Pointer in the core, moving thing behind it.

**The most common way these fail is absorption.** The constitution starts as a core and slowly eats the whole system, one reasonable addition at a time, until the owner is loading their entire life on every message and wondering why the answers got vaguer.

---

## How you know it is working

**The proof is a fresh session.** Start one, ask something the AI could only answer from the constitution, and watch it answer. If it cannot, the file is in the wrong place, and everything built on top of it is sitting on nothing.

**One caveat on that test: the core has to actually be in front of the AI when you run it.** That is the loading requirement, and meeting it is a ladder, best to workable: (a) a client with a project or memory feature that auto-loads the file; (b) a client where you paste or pin it at the start of a working session; (c) plain chat, where you paste it each session. All three produce a real constitution. Starting in plain chat is fine and common; the file is not in the wrong place, it simply has to be pasted in before the session can use it, and removing that manual paste is what the later stages are for. What changes as you climb the ladder is how automatically the core loads, not whether it exists.

Three further signs:

1. **Its size is known in tokens**, and the owner has seen the number. Anything read on every message deserves a number rather than a feeling.
2. **It has a written ceiling**, set while the file was still small. Constitutions do not grow by decision. They grow by accretion, and a written ceiling is the only thing that ever stops it.
3. **The revision trigger is a condition, not a date.** Revise when the AI gets something wrong that it should have known, because the mistake names the missing line. A constitution reviewed on a schedule accumulates paragraphs.

**The strongest single line in most constitutions** comes from asking the owner what has gone wrong with an AI before that they do not want repeated. Almost nobody asks it. The answer becomes a hard rule, and hard rules are the part that earns the running cost.

---

## Which skill maintains it

**`constitution7`** writes it and revises it. It is the first skill anyone runs, because every other skill ends with a line about registering itself in the always loaded core, and without a core those lines attach to nothing and quietly do nothing.

`audit7` measures it later: size, what actually loads, whether anything in it has stopped being true.

Keep the old versions. When a constitution changes, the previous one is the record of who the owner used to be, and that turns out to be worth reading.

---

**Built by Egils Boitmanis with [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
