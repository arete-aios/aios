# GEO7 helper inputs and outputs

Main instruction: [SKILL.md](../SKILL.md). All helpers use Python3.10+ stdlib; --help supplies exact CLI. Output parents must exist, stay inside the selected working directory and use a new filename/prefix. No credentials are needed by any included script.

- audit.py URL --max-pages N --out FILE: bounded public HTTP crawl; writes geo7-crawl/v1 JSON containing site, scope, pages, raw responses, robots/sitemaps, errors and timestamp_riga. Network side effect only; no account writes.
- report.py --crawl FILE [--native FILE] [--performance FILE] [--keyword-source FILE] --out-prefix PREFIX: local JSON/MD/HTML report. report_detail.py is its imported renderer. Fonts/CSS/logo are loaded package-relative and embedded into generated HTML. No network calls.
- performance.py URL --strategy mobile --out FILE: one keyless external PageSpeed request. Stores observed/unavailable status; lab/field remain distinct. A rate limit is not zero performance.
- research_plan.py DOMAIN --keyword TEXT --location INTEGER --language CODE [--competitor DOMAIN] --out FILE: geo7-research-plan/v1 operations/name/tool/arguments plan; api_calls_made=0. Required market IDs are provider-specific; verify current provider documentation before separately executing.
- ai_visibility.py FILE --out FILE: validates a list of saved observations and returns group sample counts/shares. It does not query an AI provider.
- test_geo7.py: offline parser, planner, missing-data and report logic checks; no network.

## Optional analytics envelope

The legacy --native flag means a supplied data envelope, not a bundled native account connection. Use operations:[{name, arguments, result}] and optional timestamp_riga. Supported names are gsc-sites, gsc-queries, gsc-pages, ga4-channels, ga4-events and keyword-ideas. A result is {ok:true,result:{content:[{type:"text",text:"<JSON payload>"}]}}; failed ok:false stays unavailable. GSC payloads use data.rows; GA4 uses data.dimensionHeaders, metricHeaders and rows as in its report API. arguments carries start_date/end_date and relevant market IDs. Keep source responses, property and period provenance yourself; do not invent a successful connection.

## AI observation list

Each row requires prompt_id, engine, model, market, observed_at, run_id, answer_source and status (observed, unknown or error). An observed row also requires boolean cited/mentioned/recommended. cited=true needs citations with URLs; recommended=true needs recommendation_excerpt. Duplicate observations and missing proof are rejected. examples/observations.json is explicitly fictional and for validation only, not a search measurement.

The existing report renderer’s diagnostic labels are Latvian; data keys are English. It compares English/Latvian hreflang depth in one optional heuristic; it does not automatically assess every language pair or translation quality. Account properties, provider grants and source answers are never included in this package.
