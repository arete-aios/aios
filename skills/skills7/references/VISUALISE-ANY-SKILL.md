# Visualise any skill

Parent: [SKILL.md](../SKILL.md). This is the owner-provided second copyable prompt. Use it after giving your AI SKILLS7; replace the bracketed GitHub link. It performs audit + view work only, without running the linked skill, connecting accounts or installing anything.

```text
**Visualise any skill with SKILLS7.** You have the SKILLS7 skill above. Use it in audit + view mode on this external skill: **[paste a GitHub link to a skill folder or its SKILL.md]**.
1. Open the link. Read SKILL.md and only the files it references (references/, scripts/, examples/). If you cannot open links, ask me to paste the SKILL.md text. Do not run scripts or connect any accounts.
2. Build one self-contained HTML page (single file, no external libraries) with: **Overview** — what it does, when it triggers, what you get at the end; **Workflow** — every step in order, decision points, loops and where a human approves, with the tools each step uses (MCP servers, scripts, APIs, apps, files read or written); **Simple view** — the same flow in 5–7 boxes for a beginner; **What it needs** — accounts, permissions, installs, costs, and what it can change or send; **Risks and limits**; **In my AIOS** — how it connects to my Constitution, Memory, Skills, Tools and Focus, and whether it is worth adding or one good prompt is enough.
3. Describe only what the files say; mark anything you infer as "inferred".
4. Give me the HTML as a downloadable file, then a three-line summary.
```

The HTML should make dependencies, decision points, approvals, written artifacts, risks and the five-layer AIOS fit inspectable. A link that cannot be opened is a missing source: ask for SKILL.md rather than guessing. Preserve only source-supported claims and label inferences. Detailed and short diagrams explain the same method.

Optional external examples supplied for trying the prompt (links are starting sources, not claims that these packages have been executed or audited by this release):

- [MCP builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder).
- [Webapp testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing).
- [Brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming).
- [Brand guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines).
