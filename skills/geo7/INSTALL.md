# Install GEO7 and try an offline report

Start: [SKILL.md](SKILL.md). Unzip the complete folder, preserving scripts/, references/, examples/ and assets/. No accounts or API keys are needed for the first run. The ZIP contains complete method/code/report assets. Use APP Download HTML separately for the standalone teaching guide; optionally save it as index.html beside SKILL.md. The guide is excluded from its own ZIP to avoid recursive embedding.

## Use the method with your AI

Attach SKILL.md and references/METHOD.md, or install the complete folder through your AI host’s documented skills location. Supply a site or HTML, audience, offer, market and desired action. Ask for a limited source-backed proposal before authorising external calls or changes. Folder presence does not prove activation.

## First small run — no network

Requirements: Python3.10+, standard library, IANA timezone data for Europe/Riga. Minimal systems may need their normal timezone-data package. Open a terminal **in the unzipped geo7 folder** and create a local results/ directory. Commands below do not install anything.

```sh
python3 -B scripts/test_geo7.py
python3 -B scripts/report.py --crawl examples/offline_crawl.json --out-prefix results/demo
python3 -B scripts/ai_visibility.py examples/observations.json --out results/ai-demo.json
```

The report writes results/demo.json, .md and a standalone .html with embedded fonts/logo. The fixture is synthetic example.com HTML, not a live audit or search result. The report currently uses Latvian diagnostic/report labels; JSON fields and this method are English, and the teaching guide supports EN/LV. Open the HTML in a browser. No font CDN is needed. Keep source JSON beside reports if you want their source links to resolve.

The helpers refuse to overwrite evidence and confine output to the current working directory after resolving paths. Create the output parent first. A second run needs a new prefix. Run from a folder you explicitly choose; this is output confinement, not a complete OS sandbox.

## One small live sample — only when you authorise it

```sh
python3 -B scripts/audit.py https://example.com --max-pages 1 --out results/live-crawl.json
```

Replace the URL with an authorised public target. This command makes public HTTP requests; its sample is bounded, obeys known robots restrictions and refuses private network destinations/authentication routes. If robots is unknown it stops the page crawl and reports the uncertainty. It is not a full website spider or browser-render test. performance.py makes one external PageSpeed request; do not run it merely to read the method.

Optional analytics/SERP/AI-search observations require your own authorised source, account/property, period and budget. There is no bundled account client. See references/INPUTS.md. If access is missing, state unknown and continue only with supported public/supplied evidence.

The standalone guide is a separate APP Download HTML; it needs no builder. To regenerate its HTML, obtain the separate SKILLS7 community toolkit and use its documented adjacent-folder or explicit-engine build route. Report generation uses only the bundled GEO7 scripts and assets.
