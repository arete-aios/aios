# GEO7 public helpers

Main instruction: [SKILL.md](../SKILL.md). Python3.10+ standard library. Start with [INSTALL.md](../INSTALL.md); [INPUTS.md](../references/INPUTS.md) supplies schemas and side effects. No private broker, credentials or deployment client is included.

- [audit.py](audit.py): bounded public HTTP crawler/parser with robots/sitemap and meta/JSON-LD evidence.
- [research_plan.py](research_plan.py): bounded provider operation plan and read-operation validator; zero API calls.
- [ai_visibility.py](ai_visibility.py): validates/summarises saved actual observations; unknown/error excluded from denominator.
- [performance.py](performance.py): one public keyless PageSpeed request; missing data remains missing.
- [report.py](report.py): combines supplied evidence into JSON/MD/HTML.
- [report_detail.py](report_detail.py): imported page diagnostics and standalone report rendering using bundled fonts/logo.
- [test_geo7.py](test_geo7.py): offline parser, incomplete-data, planner and report checks.

Only audit.py and performance.py make network requests. Other helpers transform supplied local files. All evidence writes refuse overwrite and resolve inside the explicitly selected current working directory. Create the output parent before writing. There is no automatic schedule or retry.

The optional --native report input is a documented supplied-response envelope, not an installed account reader. A separate tool may provide authorised account exports. Rebuilding the teaching guide uses the separate SKILLS7 community toolkit; report generation does not need that engine.
