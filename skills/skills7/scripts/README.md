# Portable viewer scripts

Parent: [SKILL.md](../SKILL.md). Python 3.10+ standard library. Node.js 18+ for the byte-parity check. These tools do not access a network, model, account, scheduler or publisher.

- [audit_package.py](audit_package.py) — read-only inventory, core fields, local resources/dependencies and SHA-256. Prints JSON; exit 1 on structural errors. Does not score judgment or prove tool availability.
- [build_view.py](build_view.py) — deterministic local index.html build from manifest/view; `--check` reports freshness; `--public DIR` emits `{id}-{version}.html/.zip/.json` without personal setup. All fonts, icons and template are bundled locally.
- [check_view.py](check_view.py) — freshness, versions, relative Markdown links, full binary ZIP parity and optional exported-artifact checks. Browser and AI behavior are separate.
- [verify_zip.js](verify_zip.js) — executes the real ZIP functions from the generated HTML and prints its ZIP as base64 for a byte comparison.

From the folder containing the extracted skills7 package:

```sh
python3 -B skills7/scripts/audit_package.py skills7
python3 -B skills7/scripts/build_view.py skills7
python3 -B skills7/scripts/check_view.py skills7
python3 -B skills7/scripts/build_view.py skills7 --public exports
python3 -B skills7/scripts/check_view.py skills7 --public-dir exports
```

For another package replace the final skills7 argument with its folder. Running this installed engine locates its own assets; no private root or external icon library is required. A complete source archive includes binary assets and excludes its generated HTML to avoid a self-reference. Rebuild after unpacking; do not add index.html to archive.files.

On missing/unreadable resources the build exits with an error instead of inventing a dependency. Keep any real source/account limitation in the method and results. Public mode is a delivery format, not a privacy or permission boundary by itself.
