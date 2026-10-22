# SKILLS7 2.0.0 — Portable community package

Parent: [SKILL.md](SKILL.md). This package contains the method and complete local viewer engine. It needs no private server, credentials or remote logo library.

## Use the method

Read SKILL.md with a capable AI. State whether you want to create, audit or explain a skill and supply the relevant files or GitHub link. An AI without link access should ask for the SKILL.md text. Merely reading this package does not install an agent, run another skill or grant account access.

For an external skill, copy the second prompt in the guide or use [Visualise any skill](references/VISUALISE-ANY-SKILL.md). The generated guide retains Overview, Principles, Workflow, Example and Changes, with detailed/short diagrams, identical full descriptions, EN/LV and light/dark controls.

## Rebuild after unpacking

From any local folder with Python 3.10+:

```sh
python3 -B skills7/scripts/audit_package.py skills7
python3 -B skills7/scripts/build_view.py skills7
python3 -B skills7/scripts/check_view.py skills7
```

The final check also requires Node.js 18+. The first two commands use Python’s standard library and no network. The APP provides a separate Download HTML action for its generated guide. Open skills7/index.html after building locally, or open that separately downloaded HTML. The generated HTML is excluded from its own source archive to avoid recursive self-embedding; all files needed to regenerate it are included, including binary fonts.

To build another adjacent package:

```sh
python3 -B skills7/scripts/build_view.py geo7
python3 -B skills7/scripts/check_view.py geo7
```

The target needs manifest.json, view.json, its declared references and its own required runtime assets. `--public exports` writes HTML/ZIP/JSON delivery artifacts. The full archive is defined by `manifest.archive.files`; all paths must stay within the package. Do not add credentials, personal setup or generated index.html to that list.

## Verification and limits

Structural audit checks resources and local dependencies. Build is deterministic. Check validates versions/links and compares the HTML’s real JavaScript ZIP with the Python ZIP byte for byte, including binary files. These do not prove AI judgment, live connectors, visual accessibility or business outcomes. Inspect the guide in an isolated browser and review the skill’s realistic behavior separately.

[Source and adaptations](SOURCE.json), [method licence](LICENSE.txt), [asset rights](assets/README.md).
