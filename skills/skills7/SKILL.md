---
name: skills7
description: "SKILLS7 (also SKILL7): create a reusable AI skill, audit or improve an existing skill, and build its human guide. Use for purpose, triggers, decision rules, AIOS integration, supporting code, examples and package validation; viewer-only requests do not execute the audited skill."
license: CC-BY-4.0
metadata:
  author: Egils Boitmanis / FullDigital
  version: "2.0.0"
  status: community-portable
  updated: "2026-10-22"
---

# SKILLS7 — Create, audit and explain a skill

Parent: [package guide](README.md). Human guide: [APP guide](https://app.areteaios.com/learning/skills/skills7), separately downloadable as HTML; rebuild locally from manifest.json and view.json. Method: [references/METHOD.md](references/METHOD.md).

Turn a recurring need into an AI decision method and a verifiable result. Audit whether an existing skill does what it claims, retaining useful work and fixing specific gaps. When an ordinary prompt or existing skill is sufficient, say so rather than creating another package.

## Select the mode

- **Create:** find the nearest existing skill first. Define a realistic request, intended user, observable result and responsible person. Start with a use case, not a folder inventory.
- **Audit / improve:** read the existing SKILL.md and only relevant sources. Compare claims, implementation and evidence. An evidence-backed audit without edits is a valid result.
- **View only:** explain the existing method and its dependencies without running its scripts, calling accounts or expanding its permissions. For a GitHub skill use [Visualise any skill](references/VISUALISE-ANY-SKILL.md).

Use the context and decisions already supplied. Ask only about gaps that materially change the result, audience or permitted action. A package being present does not prove native installation, a working connector or permission to execute it.

## Method

1. Identify the need and choose create, audit or view mode; reuse the nearest method when sufficient.
2. Read the existing instructions, relevant evidence and actual status. Identify the owner, audience, authoritative sources and write/send boundary. Preserve recovery before edits.
3. Define how AI chooses actions, what evidence supports them and where the human decides. Explain this skill’s actual AIOS contribution and standalone use.
4. Keep SKILL.md concise: trigger, decision rules, essential workflow, output and boundaries. Link deeper references. Add code only for concrete repeatable work, then run it with appropriate inputs.
5. Build a clear human guide and a labelled realistic example. Method metadata lives in manifest.json, explanations in view.json; the local shared engine builds one self-contained HTML page.
6. Check a realistic core request, a neighbouring request where this skill should not trigger and a relevant missing-tool/permission case. Technical checks, AI behavior and human review are separate evidence.
7. Deliver to the authorised audience, preserve a version and source receipt, report unresolved work and give a concrete next step. Read back a deployed release before claiming publication.

Details and acceptance: [METHOD.md](references/METHOD.md). Viewer fields and commands: [VIEW-CONTRACT.md](references/VIEW-CONTRACT.md), [scripts/README.md](scripts/README.md).

## Decision principles

Keep what changes the AI’s behavior in the entry instructions; load long reference material only when needed. A Python icon does not justify a script. Code may inventory files, transform data or check an exact invariant; it does not replace judgment. Never invent tools, source access, scores, measured outcomes or permissions.

For an audit, each finding names the claim, evidence, gap, concrete repair and retest. Do not rewrite a working method merely for uniformity. Preserve established terminology and useful code, licences and history. Use an independent reviewer only when delegation is permitted.

## Why AIOS helps

Show input → decision/action → benefit for each relevant layer: Constitution supplies direction and boundaries; Memory supplies facts and their authoritative home; Skills supplies complementary methods and responsible roles; Tools supplies actual capabilities and permissions; Focus supplies accepted current priorities. Name the concrete contribution to this skill, not a repeated list of five labels. Explain any layer that has little effect.

SKILLS7 has **medium integration**, a qualitative dependency assessment. Skill authoring and auditing work independently with supplied files; an AIOS adds an existing source map, accepted goals and governed handoffs. Without that context, request the facts needed for the particular task and mark unknowns. Do not claim a numerical accuracy benefit from this architectural description.

## Human guide and portable engine

Use Overview, Principles, Workflow, Example and Changes when they help. Start with a detailed diagram and provide a genuinely simpler diagram; both use identical full step descriptions (`flow.modeBehavior: canvas`). Real Python and file nodes refer to real helper code and saved outputs. Label synthetic examples; state the basis of any qualitative rating.

The full source archive includes the engine, template, local fonts, icons and licences. It excludes its generated index.html to avoid recursive self-embedding; rebuild that file offline after unpacking. Python 3.10+ standard library builds/audits; Node.js 18+ checks the page’s actual binary ZIP implementation. No account, browser or network is needed for those steps. Browser and AI-behavior checks remain separate.

## Boundaries and completion

A view does not run a process or grant access. Never execute a linked external skill to explain it. External sending, account changes, paid calls, publication and schedules require the task’s actual authorisation. Reuse valid authorisation without asking again. If a required tool or source is unavailable, deliver what can be verified and identify the concrete missing capability.

Separate community material from personal setup. Inspect all instructions, JSON, HTML and ZIP for private identifiers, account data and machine-specific paths; a public-export flag alone does not rewrite private prose. Keep one accepted source version across delivery channels. Report actual checks and limitations without calling structural tests proof of AI judgment.

## Package contents

- [README.md](README.md), [SOURCE.json](SOURCE.json), [LICENSE.txt](LICENSE.txt).
- [manifest.json](manifest.json), [view.json](view.json), [locally generated index.html](index.html), available after rebuilding; APP also supplies the separate HTML download.
- [references/README.md](references/README.md): method, viewer contract and external-skill prompt.
- [scripts/README.md](scripts/README.md): audit, build, check and ZIP verification.
- [assets/README.md](assets/README.md): template, wording, fonts and individually documented icons.
