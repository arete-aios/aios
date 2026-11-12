"""Exercise the optional CC7 command from a fresh B starter layout."""

import json
import shutil
import subprocess
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urlsplit


REPO = Path(__file__).resolve().parents[1]
SCRIPT = Path("00-system/aios/skills/cc7/health.py")
OUTPUT = Path("04-tools/cc7")
SECTIONS = ["constitution", "memory", "skills", "tools", "focus", "exit7"]


class HealthDocument(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.sections = []
        self.links = []
        self.dates = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "section":
            self.sections.append(attributes["id"])
        elif tag == "a":
            self.links.append(attributes["href"])
        elif tag == "time":
            self.dates.append(attributes["datetime"])


class CC7Test(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.brain = Path(temp.name)
        self.page = self.brain / OUTPUT / "health.html"
        self.register = self.brain / OUTPUT / "audits.json"
        library = self.brain / "00-system/aios"
        library.mkdir(parents=True)
        for path in ("README.md", "SKILL.md", "LICENSE", "NOTICE"):
            shutil.copyfile(REPO / path, library / path)
        for directory in ("skills", "references", "templates", "onboarding"):
            shutil.copytree(REPO / directory, library / directory)
        for template, dest in {
            "CONSTITUTION-LITE.md": "CONSTITUTION.md",
            "AGENTS.md": "AGENTS.md",
            "ONBOARDING.md": "ONBOARDING.md",
            "_skills-STARTER-CONTEXT.md": "03-skills/_skills-CONTEXT.md",
            "_tools-CONTEXT.md": "04-tools/_tools-CONTEXT.md",
            "_focus-CONTEXT.md": "05-focus/_focus-CONTEXT.md",
        }.items():
            self.copy_to(library / "templates" / template, dest)
        self.copy_to(library / "onboarding/AIOS-INSTRUCTIONS.md", "AIOS-INSTRUCTIONS.md")
        for skill in ("eval7", "exit7", "context7", "meeting7", "focus7"):
            path = f"skills/{skill}/SKILL.md"
            self.copy_to(library / path, f"03-{path}")
        self.write("02-memory/_memory-CONTEXT.md", "# Memory\n")

    def copy_to(self, source, dest):
        target = self.brain / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    def write(self, dest, value):
        target = self.brain / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value, encoding="utf-8")

    def run_cc7(self, *arguments, check=True):
        return subprocess.run(
            [sys.executable, SCRIPT, *arguments],
            cwd=self.brain,
            capture_output=True,
            text=True,
            check=check,
        )

    def read_health(self):
        document = HealthDocument(self.page)
        self.assertEqual(document.sections, SECTIONS)
        for href in document.links:
            link = urlsplit(href)
            self.assertFalse(link.scheme or link.netloc)
            if link.path:
                self.assertTrue((self.page.parent / unquote(link.path)).is_file(), href)
            else:
                self.assertIn(link.fragment, document.sections)
        return document

    def test_opt_in_records_pending_and_verified_exit7(self):
        self.assertFalse(self.page.parent.exists())
        self.assertNotEqual(self.run_cc7(check=False).returncode, 0)
        self.assertFalse(self.page.parent.exists())
        self.assertEqual(self.run_cc7("--init").stdout.strip(), str(OUTPUT / "health.html"))
        self.assertEqual(self.read_health().dates, [])
        self.assertEqual(self.page.read_text().count("Not yet audited"), 6)

        audits = json.loads(self.register.read_text())
        checklist = "02-memory/brief-checklist.md"
        follow_up = "02-memory/Brief #3.md"
        self.write(checklist, "Goal\n")
        before = (self.brain / checklist).read_text()
        self.assertNotIn("Reviewer", before)
        audits["exit7"]["open_decisions"] = "Proposed. Add Reviewer to the checklist after approval."
        self.register.write_text(json.dumps(audits), encoding="utf-8")
        self.run_cc7()
        self.assertEqual(self.read_health().dates, [])
        self.assertIn("after approval.", self.page.read_text())
        self.assertEqual((self.brain / checklist).read_text(), before)

        self.write(checklist, before + "Reviewer\n")
        audits["exit7"]["open_decisions"] = "Applied. Check the reviewer on the next brief."
        self.register.write_text(json.dumps(audits), encoding="utf-8")
        self.run_cc7()
        self.assertEqual(self.read_health().dates, [])
        self.assertIn("Check the reviewer on the next brief.", self.page.read_text())

        fields = {"Goal": "Prepare the sample", "Reviewer": "Sample owner"}
        self.write(follow_up, "".join(
            f"{field}: {fields[field]}\n" for field in (self.brain / checklist).read_text().splitlines()
        ))
        self.assertIn("Reviewer: Sample owner", (self.brain / follow_up).read_text())
        improvement = "05-focus/projects/brief-quality.md"
        self.write(improvement, "Verified on the next brief: the updated checklist was used.\n")
        for key in SECTIONS[:-1]:
            evidence = f"02-memory/audits/{key}.md"
            self.write(evidence, f"2026-11-11: checked the {key} source in this sample brain.\n")
            audits[key].update(
                audited_on="2026-11-11", scope=f"Sample {key} audit",
                result="Source checked", evidence=[evidence],
            )
        audits["exit7"].update(
            audited_on="2026-11-12", scope="Brief review after checklist update",
            result="Next brief named a reviewer <sample>", evidence=[improvement, follow_up],
            open_decisions="",
        )
        self.register.write_text(json.dumps(audits), encoding="utf-8")
        self.run_cc7("--init")
        page = self.page.read_text()
        document = self.read_health()
        self.assertEqual(document.dates, ["2026-11-11"] * 5 + ["2026-11-12"])
        self.assertIn("../../02-memory/Brief%20%233.md", document.links)
        self.assertIn("reviewer &lt;sample&gt;", page)
        self.assertEqual(json.loads(self.register.read_text()), audits)

        audits["exit7"]["evidence"] = ["../outside.md"]
        self.register.write_text(json.dumps(audits), encoding="utf-8")
        self.assertNotEqual(self.run_cc7(check=False).returncode, 0)
        self.assertEqual(self.page.read_text(), page)


if __name__ == "__main__":
    unittest.main()
