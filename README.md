# AIOS · an AI operating system you own

Most AI tools are capable but forgetful. They know the world and still make you explain who you are, what you are building, what you decided, and how you want to work.

An **AIOS** fixes that with plain files you own. Your AI reads those files before it answers, uses the methods inside them, and writes important learning back where the next session can find it.

## What you build

| Layer | What it holds |
|---|---|
| **Constitution** | Who you are, where you are going, and the rules that hold in every session |
| **Memory** | The facts, history, people, projects, and evidence the AI may use |
| **Skills** | Repeatable methods, each with a clear trigger and stopping rule |
| **Tools** | The systems the AI can reach and what it may do there |
| **Focus** | What matters now, how it is measured, and when it is reviewed |

The result is not another notes folder. It is a working loop: something happens, the useful learning is written back, and the next session behaves differently because of it.

## Start here

Attach an empty local folder to ChatGPT, Codex, Claude, or another assistant that can read and write files. Then paste this:

```text
Help me build an AIOS in the folder attached to this chat. Work in the language of this message.

This message ends with READY. If you do not see that word, tell me the copy was cut off and do nothing else.

Read this file completely before doing anything:
https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/START.md

Follow it exactly. First explain the plan and show me the complete folder and file list. Do not create or change anything until I answer yes. If you cannot open the file, say so and stop instead of inventing the method.

READY
```

The first session follows a visible rhythm:

1. You see and approve the exact structure.
2. The assistant creates the constitution first and proves it can read it back.
3. You answer four short foundation questions.
4. You receive a personal `AIOS-INSTRUCTIONS.md` showing what the system can now do and how to call each deeper workflow.
5. A new-chat test proves whether the constitution loads automatically.

The local root also gets `AGENTS.md`. That file tells a new chat to read the constitution and routes phrases such as **AIOS instructions**, **AIOS Deep Dive**, **AIOS Business Profile**, and **AIOS Personal Audit** to the right method.

## What you can do after the foundation

- **[AIOS Deep Dive](onboarding/DEEP-DIVE.md):** a self-coaching interview that turns reflections, patterns, strengths, constraints, and future potential into a confirmed personal map.
- **[AIOS Business Profile](onboarding/BUSINESS-PROFILE.md):** one seven-part profile per business, ending in a one-sentence explanation a stranger can understand.
- **[AIOS Personal Audit](onboarding/PERSONAL-AUDIT.md):** a sourced audit of how you appear on the public web, kept separate from private memory and from the technical AIOS audit.
- **[AIOS operating manual](onboarding/OPERATING-MANUAL.md):** the source used to create your local instructions file in your own language.

The detailed eleven-step build still exists in [`onboarding/_proj-onboarding.md`](onboarding/_proj-onboarding.md). It adds the quarter goal, accountability loop, completeness pass, and deeper north-star work. It is the full engine, not the first file an owner needs to read.

Already have a second brain or an AIOS-like folder? Use [`references/evaluate.md`](references/evaluate.md) instead of rebuilding from zero.

## Skills

The reusable methods live in [`skills/`](skills/). Install only what solves a real need. A skill that is present in a folder costs nothing; a standing skill is loaded every session and should stay rare.

If you build manually over several weeks, start with [`SKILL.md`](SKILL.md). That is the staged path with exit tests. The guided `START.md` path is faster and ends in the same five-layer architecture.

---

Built by Egils Boitmanis with [FullDigital](https://fulldigital.me). Licensed CC BY 4.0. Use it, change it, ship it, and keep the attribution.
