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
Build an AIOS business brain in the folder attached to this chat.

Read and follow:
https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/START.md

If the fetched file is an older cached version or conflicts with this message, this message wins for the A/B setup choice and the prohibitions below.

First briefly explain what we are building and ask the three short questions. Show one-sentence explanations for the A, B, and C AI character choices. Then summarise my answers and offer two clearly explained setup options: A, a light start without copying the GitHub library; or B, the full local AIOS library, recommended for a paid account. Show the exact trees and create nothing until I answer A + YES or B + YES.

After my approval, build the selected version directly in the attached folder, then continue immediately to Brain Enrichment. Do not create another AIOS folder, repeat the foundation questions, start automatic web research, or request a new-chat test.

If you cannot read the instructions or write to the folder, say so and stop.
```

This launcher requests the current onboarding method from GitHub. Its explicit A/B rules also protect the run if an AI client's web cache returns an older copy.

The first session follows a visible rhythm:

1. You answer three short foundation questions.
2. You choose A, the light setup, or B, the full local method library, then approve once.
3. The selected business brain is created and you receive clickable status and instructions files with their exact paths.
4. You may add real source material or continue without it.
5. The assistant asks no more than five missing business questions and hands the system over.

The local root also gets `AGENTS.md`. That file tells a new chat to read the constitution and onboarding map, and routes phrases such as **AIOS instructions**, **AIOS Deep Dive**, **AIOS Business Profile**, and **AIOS Personal Audit** to the right method.

Option A is free-account friendly: it creates about ten small files and keeps the larger method library online until requested. Option B copies the library locally without loading every file into the conversation and is recommended when the owner has a paid account and wants all methods on disk.

## What you can do after the foundation

- **[AIOS Deep Dive](onboarding/DEEP-DIVE.md):** a self-coaching interview that turns reflections, patterns, strengths, constraints, and future potential into a confirmed personal map.
- **[AIOS Business Profile](onboarding/BUSINESS-PROFILE.md):** one seven-part profile per business, ending in a one-sentence explanation a stranger can understand.
- **[AIOS Personal Audit](onboarding/PERSONAL-AUDIT.md):** a sourced audit of how you appear on the public web, kept separate from private memory and from the technical AIOS audit.
- **[AIOS instructions](onboarding/AIOS-INSTRUCTIONS.md):** the source used to create your local instructions file in your own language, including skills, plugins, MCP, and tool discovery.

The detailed eleven-step build still exists in [`onboarding/_proj-onboarding.md`](onboarding/_proj-onboarding.md). It adds the quarter goal, accountability loop, completeness pass, and deeper north-star work. It is the full engine, not the first file an owner needs to read.

Already have a second brain or an AIOS-like folder? Use [`references/evaluate.md`](references/evaluate.md) instead of rebuilding from zero.

## Skills

The reusable methods live in [`skills/`](skills/). Install only what solves a real need. A skill that is present in a folder costs nothing; a standing skill is loaded every session and should stay rare.

If you build manually over several weeks, start with [`SKILL.md`](SKILL.md). That is the staged path with exit tests. The guided `START.md` path is faster and ends in the same five-layer architecture.

---

Built by Egils Boitmanis with [FullDigital](https://fulldigital.me). Licensed CC BY 4.0. Use it, change it, ship it, and keep the attribution.
