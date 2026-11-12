#!/usr/bin/env python3
"""Build a private CC7 Health page from recorded audit results."""

import argparse
import json
import os
from datetime import date
from html import escape
from pathlib import Path, PurePosixPath
from tempfile import NamedTemporaryFile
from urllib.parse import quote


SECTIONS = {
    "constitution": ("Constitution", "CONSTITUTION.md"),
    "memory": ("Memory", "02-memory/_memory-CONTEXT.md"),
    "skills": ("Skills", "03-skills/_skills-CONTEXT.md"),
    "tools": ("Tools", "04-tools/_tools-CONTEXT.md"),
    "focus": ("Focus", "05-focus/_focus-CONTEXT.md"),
    "exit7": ("EXIT7 feedback loop", "03-skills/exit7/SKILL.md"),
}
EMPTY = {"audited_on": None, "scope": "", "result": "", "evidence": [], "open_decisions": ""}
OUTPUT_DIR = Path("04-tools/cc7")

STYLE = """
  :root { color-scheme: light dark; font: 100%/1.55 system-ui, sans-serif; }
  body { margin: 0 auto; max-width: 76rem; padding: clamp(1rem, 4vw, 3rem); }
  h1 { font-size: clamp(2rem, 6vw, 3.25rem); line-height: 1.15; margin: .5rem 0; }
  h2 { font-size: 1.2rem; margin: 0 0 .75rem; }
  header p { margin: .5rem 0; }
  nav ul { display: flex; gap: .5rem 1.2rem; flex-wrap: wrap; padding: 0; list-style: none; }
  main { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 21rem), 1fr)); gap: 1rem; }
  section { border: 1px solid GrayText; border-radius: .7rem; padding: 1.1rem; min-width: 0; }
  section:target { outline: .15rem solid LinkText; outline-offset: .15rem; }
  dt { font-weight: 650; margin-top: .65rem; }
  dd { margin: 0; white-space: pre-line; overflow-wrap: anywhere; }
  dd ul { padding-inline-start: 1.25rem; margin: 0; }
"""


def local_link(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("Evidence paths must be file paths relative to the AIOS root")
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or ":" in relative:
        raise ValueError(f"Path must stay inside the AIOS root: {relative}")
    target = root / path
    if not target.resolve().is_relative_to(root) or not target.is_file():
        raise ValueError(f"Missing or out-of-scope file: {relative}")
    href = quote(Path(os.path.relpath(target, root / OUTPUT_DIR)).as_posix())
    return f'<a href="{href}">{escape(relative)}</a>'


def render_section(root, key, title, source, record):
    if not isinstance(record, dict) or record.keys() != EMPTY.keys():
        raise ValueError(f"{key}: expected {', '.join(EMPTY)}")
    audited = record["audited_on"]
    scope, result, decisions = (record[field] for field in ("scope", "result", "open_decisions"))
    if any(not isinstance(value, str) for value in (scope, result, decisions)):
        raise ValueError(f"{key}: scope, result and open_decisions must be text")
    evidence = record["evidence"]
    if not isinstance(evidence, list):
        raise ValueError(f"{key}: evidence must be a list of local file paths")

    if audited is None:
        if scope or result or evidence:
            raise ValueError(f"{key}: an audit record with a result needs a date")
        audit_date = "Not yet audited"
    else:
        try:
            parsed = date.fromisoformat(audited)
            if parsed.isoformat() != audited:
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError(f"{key}: audited_on must be YYYY-MM-DD") from None
        if not scope.strip() or not result.strip() or not evidence:
            raise ValueError(f"{key}: a dated audit needs a scope, result and evidence")
        audit_date = f'<time datetime="{audited}">{audited}</time>'

    links = [local_link(root, item) for item in evidence]
    proof = "<ul>" + "".join(f"<li>{link}</li>" for link in links) + "</ul>" if links else "—"
    return f"""<section id="{key}" aria-labelledby="{key}-title">
  <h2 id="{key}-title">{title}</h2>
  <dl>
    <dt>Last audit</dt><dd>{audit_date}</dd>
    <dt>Scope</dt><dd>{escape(scope) or "—"}</dd>
    <dt>Result</dt><dd>{escape(result) or "—"}</dd>
    <dt>Evidence</dt><dd>{proof}</dd>
    <dt>Open decisions and next checks</dt><dd>{escape(decisions) or "—"}</dd>
    <dt>Start here</dt><dd>{local_link(root, source)}</dd>
  </dl>
</section>"""


def render_health(root, audits):
    if not isinstance(audits, dict) or audits.keys() != SECTIONS.keys():
        raise ValueError("audits.json must have exactly these entries: " + ", ".join(SECTIONS))
    navigation = "".join(f'<li><a href="#{key}">{title}</a></li>' for key, (title, _) in SECTIONS.items())
    sections = "\n".join(
        render_section(root, key, title, source, audits[key])
        for key, (title, source) in SECTIONS.items()
    )
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CC7 Health</title>
<style>{STYLE}</style>
<body>
<header>
  <p>CC7 · Command Center</p>
  <h1 id="health">Health</h1>
  <p>Latest recorded audits for the five AIOS layers and the EXIT7 feedback loop.</p>
  <p>{local_link(root, "ONBOARDING.md")} · <a href="audits.json">Audit register</a></p>
  <nav aria-label="Health sections"><ul>{navigation}</ul></nav>
</header>
<main>
{sections}
</main>
</body>
</html>
"""


def write_page(path, page):
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as output:
        temporary = Path(output.name)
        try:
            output.write(page)
            output.close()
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)


def build(root, initialise):
    folder = root / OUTPUT_DIR
    if folder.resolve() != folder:
        raise ValueError(f"{OUTPUT_DIR} must be a real directory inside the AIOS root")
    register = folder / "audits.json"
    page = folder / "health.html"
    if register.is_symlink() or page.is_symlink():
        raise ValueError("CC7 files must not be symlinks")
    if register.exists():
        audits = json.loads(register.read_text(encoding="utf-8"))
    elif initialise and not page.exists():
        audits = {key: EMPTY for key in SECTIONS}
    else:
        raise ValueError("Audit register missing. Use --init for the first setup or restore audits.json.")

    html = render_health(root, audits)
    if not register.exists():
        folder.mkdir(exist_ok=True)
        with register.open("x", encoding="utf-8") as output:
            json.dump(audits, output, indent=2)
            output.write("\n")
    write_page(page, html)
    print(OUTPUT_DIR / page.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="AIOS folder (default: current directory)")
    parser.add_argument("--init", action="store_true", help="Create the audit register on first setup")
    args = parser.parse_args()
    try:
        build(args.root.resolve(), args.init)
    except (OSError, ValueError) as error:
        parser.exit(1, f"CC7: {error}\n")


if __name__ == "__main__":
    main()
