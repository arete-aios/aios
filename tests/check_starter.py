#!/usr/bin/env python3
"""Static checks for the starter onboarding path.

What this proves: the files exist, the five methods are named consistently, the
relative links resolve, and the promises in README, START and the templates do
not contradict each other.

What it cannot prove: how an assistant actually behaves during a real run. The
execution paths in a live client are tested separately, by hand.

Usage: python3 tests/check_starter.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STARTER_SKILLS = ["eval7", "exit7", "context7", "meeting7", "focus7"]
STARTER_TRIGGERS = ["EVAL7", "EXIT7", "CONTEXT7", "MEETING7", "FOCUS7"]

# Files whose relative markdown links must resolve.
LINK_CHECKED = [
    "README.md",
    "onboarding/START.md",
    "onboarding/AIOS-INSTRUCTIONS.md",
    "onboarding/UPGRADE.md",
    "references/3-skills.md",
    "templates/_skills-STARTER-CONTEXT.md",
    "templates/AGENTS.md",
    "templates/CLAUDE.md",
    "templates/CONSTITUTION-LITE.md",
    "templates/ONBOARDING.md",
    "templates/SYSTEM-POINTER.md",
]

# Links inside a local brain, not paths in this repository.
LINK_IGNORE_PREFIXES = ("03-skills/", "00-system/", "02-memory/", "04-tools/", "05-focus/", "06-archive/")
LINK_IGNORE_EXACT = {"ONBOARDING.md", "CONSTITUTION.md", "AIOS-INSTRUCTIONS.md", "AGENTS.md", "CLAUDE.md"}

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

failures: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        failures.append(message)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


# 1. The five method files exist, with frontmatter that names them.
for skill in STARTER_SKILLS:
    path = ROOT / "skills" / skill / "SKILL.md"
    check(path.is_file(), f"missing method file: skills/{skill}/SKILL.md")
    if path.is_file():
        head = path.read_text(encoding="utf-8")[:400]
        check(f"name: {skill}" in head, f"skills/{skill}/SKILL.md frontmatter does not declare name: {skill}")
        check("version:" in head, f"skills/{skill}/SKILL.md has no version in its metadata")

# COX7 is an alias, never a sixth folder.
check(not (ROOT / "skills" / "cox7").exists(), "skills/cox7/ exists; COX7 must stay an alias of context7")
check("COX7" in read("skills/context7/SKILL.md"), "context7 does not mention its COX7 short name")

# 2. The starter registry.
registry = read("templates/_skills-STARTER-CONTEXT.md")
for skill in STARTER_SKILLS:
    check(f"03-skills/{skill}/SKILL.md" in registry, f"starter registry does not register 03-skills/{skill}/SKILL.md")
    check(
        f"https://raw.githubusercontent.com/arete-aios/aios/main/skills/{skill}/SKILL.md" in registry,
        f"starter registry has no public source URL for {skill}",
    )
for trigger in STARTER_TRIGGERS:
    check(trigger in registry, f"starter registry does not name trigger {trigger}")
check("COX7" in registry, "starter registry does not name the COX7 alias")
check("library/" not in registry, "starter registry invents a library/ path")

# 3. The starter path uses the starter registry, not the eleven-skill one.
start = read("onboarding/START.md")
check("templates/_skills-STARTER-CONTEXT.md" in start, "START.md does not point at the starter registry")
check(
    "_skills-CONTEXT.md`" in start and "never from the eleven-skill" in start,
    "START.md does not warn against the eleven-skill registry",
)
for skill in STARTER_SKILLS:
    check(f"{skill}/SKILL.md" in start, f"START.md tree or install step omits {skill}")
check("00-system/aios/library/" in start, "START.md lost the no-library/ prohibition")
check("05-focus/projects/" in start, "START.md does not name the starter projects location")

# The old registry states which path it belongs to.
check(
    "templates/_skills-STARTER-CONTEXT.md" in read("templates/_skills-CONTEXT.md"),
    "the eleven-skill registry does not separate itself from the starter registry",
)

# 3b. The upgrade path exists and refuses to rebuild.
upgrade = read("onboarding/UPGRADE.md")
check("UPGRADE.md" in start, "START.md does not send an existing brain to the upgrade path")
for trigger in STARTER_TRIGGERS:
    check(trigger in upgrade, f"UPGRADE.md does not name {trigger}")
check("Never overwrite an adapted method" in upgrade, "UPGRADE.md does not protect an adapted method")

# 4. The adapters route the five triggers to real starter paths.
agents = read("templates/AGENTS.md")
for skill in STARTER_SKILLS:
    check(f"03-skills/{skill}/SKILL.md" in agents, f"AGENTS.md does not route to 03-skills/{skill}/SKILL.md")
check("03-skills/_skills-CONTEXT.md" in agents, "AGENTS.md does not read the skills index")

claude_md = read("templates/CLAUDE.md")
check(claude_md.lstrip().startswith("@AGENTS.md"), "templates/CLAUDE.md must import AGENTS.md on its first line")
check(len(claude_md.splitlines()) <= 15, "templates/CLAUDE.md is growing into a second constitution")

check(
    "03-skills/_skills-CONTEXT.md" in read("templates/CONSTITUTION-LITE.md"),
    "the starter constitution does not point at the skills index",
)

# 5. The status panel tracks the five methods without inflating the step counter.
onboarding = read("templates/ONBOARDING.md")
for skill in STARTER_SKILLS:
    check(f"03-skills/{skill}/SKILL.md" in onboarding, f"ONBOARDING.md does not track {skill}")
check("NOT INSTALLED — source only" in onboarding, "ONBOARDING.md has no honest not-installed state")
check("out of five" in onboarding or "not onboarding progress" in onboarding, "ONBOARDING.md conflates methods with steps")

# 6. Same promise in README, the pointer, and the manual.
readme = read("README.md")
pointer = read("templates/SYSTEM-POINTER.md")
manual = read("onboarding/AIOS-INSTRUCTIONS.md")
for trigger in STARTER_TRIGGERS:
    check(trigger in readme, f"README does not name {trigger}")
    check(trigger in manual, f"AIOS-INSTRUCTIONS does not name {trigger}")
for skill in STARTER_SKILLS:
    check(
        f"https://raw.githubusercontent.com/arete-aios/aios/main/skills/{skill}/SKILL.md" in pointer,
        f"SYSTEM-POINTER has no source for {skill}",
    )
check("WAITING" in manual and "CANCELLED" in manual, "AIOS-INSTRUCTIONS does not state the task statuses")
check("05-focus/projects/" in manual, "AIOS-INSTRUCTIONS does not name where projects live")

# 7. FOCUS7 really carries the projects and tasks contract.
focus = read("skills/focus7/SKILL.md")
check("## PROJECTS AND TASKS" in focus, "focus7 has no projects and tasks section")
for status in ["OPEN", "DOING", "WAITING", "DONE", "CANCELLED"]:
    check(status in focus, f"focus7 does not define the {status} status")
check("05-focus/projects/" in focus, "focus7 does not give a starter default location")
check("one authoritative home" in focus, "focus7 does not state the single-home rule for a task")

# 8. MEETING7 hands approved work to FOCUS7 instead of a parallel list.
meeting = read("skills/meeting7/SKILL.md")
check("FOCUS7" in meeting, "meeting7 does not hand approved commitments to the focus layer")
check("to confirm" in meeting, "meeting7 does not require unknowns to stay unknown")
check("FOCUS7" in read("skills/exit7/SKILL.md"), "exit7 does not hand approved work to the focus layer")

# 9. Relative links resolve.
for rel in LINK_CHECKED:
    text = read(rel)
    base = (ROOT / rel).parent
    for target in MD_LINK.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#")[0]
        if not clean or clean in LINK_IGNORE_EXACT or clean.startswith(LINK_IGNORE_PREFIXES):
            continue
        check((base / clean).exists(), f"broken relative link in {rel}: {target}")

print(f"{checks} checks run")
if failures:
    print(f"\nFAIL — {len(failures)} problem(s):")
    for line in failures:
        print(f"  - {line}")
    sys.exit(1)
print("PASS — starter onboarding is internally consistent")
