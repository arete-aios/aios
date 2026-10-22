# GEO7 audit and improvement method

Main instruction: [SKILL.md](../SKILL.md). First run: [INSTALL.md](../INSTALL.md). Code/data details: [INPUTS.md](INPUTS.md). Version 1.2.0 community edition.

## 1. Scope and evidence home

Agree site, offer, audience, market/language, desired visitor action, period, source set, output directory and authorised request/cost limits. Start a limited supplied-material/public review if a missing noncritical input allows it; ask for the one missing choice that materially changes the result.

Use a new dated/unique prefix for each run. Keep source JSON, report JSON/MD/HTML and the actual run receipt together. Record observation times separately from comparison periods. The helpers keep their existing timestamp_riga/Europe/Riga schema; convert explicitly when comparing another timezone.

## 2. Audit — eight checks

1. Access: HTTP status/redirects, robots.txt and robots/noindex headers. The robots parser is advisory, not proof of CDN access or index state.
2. Discovery: sitemap, internal links and canonical. State sampled versus discovered URLs; unsampled is not failed.
3. Page identity: title/description, clear H1, language and hreflang.
4. Content: answer to the actual audience question, real author/company, examples and verifiable sources. Short text is not automatically wrong.
5. Technical availability: raw HTTP text and a separate rendered-browser check when needed. Do not call an HTML parse a browser test.
6. Structured data: JSON-LD syntax, @graph and agreement with visible facts. Organization/Person/WebSite belong only where appropriate; FAQ/HowTo is not a universal AI-search requirement.
7. Performance: Lighthouse lab and CrUX field data separately. A failed PageSpeed request means not measured; HTTP elapsed time is not Core Web Vitals.
8. Outcome baseline: actual GSC queries/pages, analytics acquisition/actions and qualification evidence. Empty GSC is not proof of zero traffic.

The Python public crawler uses only stdlib, public HTTP(S) and system TLS certificates. It refuses private destinations, credentials and excluded private/checkout/query routes; unknown robots stops page crawling. Limits: at most30 pages,2MB per response, sequential requests. It does not bypass restrictions or execute JavaScript. See script --help for exact flags.

## 3. Questions, keywords and competitors

GSC shows observed queries for an authorised property. Keyword Planner provides market demand ideas, not SEO difficulty. A separately authorised SERP provider may add rankings and competitors. Record question, intent, country/language, source/date, measured volume if any, business relevance, existing/target page and desired action. Do not add volumes as unique people.

Use observed SERPs to select up to five real search competitors for a specific query/market/time. Compare up to five relevant public pages for intent, structure, examples, proof, CTA and update date. Keep candidates distinct from observed competitors. Do not copy their text.

research_plan.py writes a three-operation DataForSEO plan; --competitor adds one gap operation. It makes zero API calls. Verify current provider schema/pricing and approve the exact endpoint, arguments, maximum calls and spend through your own authorised client. No automatic paid retry is provided. Tool names in the plan are descriptive adapter identifiers, not installed connections.

## 4. Priorities and page briefs

For each selected priority record audience/question, URL, observed fact, business implication, proposed action, responsible role, source/time and acceptance check. P1 means a significant customer-path blocker worth verifying/fixing first; P2 a justified intent/content/measurement improvement; P3 a smaller structural/maintenance task. These are work-order judgements, not measured ranking impact. If the evidence is weak, the action is a targeted verification.

A page brief includes one answer, factual support, sections, example, appropriate structured-data draft, internal links and meaningful next action. A generated draft needs fact/user review. Do not invent reviews, experience, customer counts, price or guarantees. llms.txt may be an experiment, not a Google requirement; no citation is not proof of a technical error.

## 5. Implementation

The user accepts priorities and specifically authorises external changes. Prepare a reviewable diff/preview, preserve recovery and check affected paths. A technical contributor may implement a concrete authorised change. This skill is not a deployment backend. After implementation repeat the affected HTTP/render check and record actual changes/date.

## 6. Measure and learn

Compare like periods, markets and pages. Separate paid/organic traffic, seasonality, attribution gaps and data delays. Qualified conversations require an identifiable qualification chain, not a sum of clicks or registrations. Directional metrics include impressions/clicks, organic sessions, contact actions and observed AI citations/mentions/recommendations.

For AI search use the same8–12 audience questions, market/language and actual search product mode. Record engine/model/date/run_id, saved answer and cited URLs. Three independent observations per question is a sampling proposal, not statistical representativeness. Do not substitute an ordinary LLM answer for an actual search product result. Exclude error/unknown from the observed-answer denominator. ai_visibility.py validates and summarises saved observations; it does not query a model.

## AIOS contribution and standalone use

Integration is qualitatively medium, not a measured accuracy rating. Constitution provides business direction/permission → select qualified intent; Memory provides offer facts/history/evidence → avoid stale claims and keep a traceable result; Skills connects audit/brief to review/delivery → clear responsibility; Tools supplies actually authorised public/analytics/SERP evidence → fewer guesses; Focus provides accepted attention → choose one relevant next page without inventing a schedule.

Standalone use needs a site or supplied HTML, audience/offer, market and output home. Public helpers need no AIOS runtime. Without account responses, analytics/SERP remains unknown; without saved search answers, citations remain unmeasured; without qualification evidence, the main business outcome is unproven.

## Acceptance and primary sources

Every material claim has source/time/scope. Observation, interpretation and plan are distinct. A priority states action, responsible role and acceptance check. External/paid work follows specific permission. Preserve before/after evidence and relative package resources.

- [Google AI features](https://developers.google.com/search/docs/appearance/ai-features).
- [JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics).
- [Structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).
- [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro).
- [PageSpeed API](https://developers.google.com/speed/docs/insights/v5/get-started).
- [GEO research paper](https://arxiv.org/abs/2311.09735): benchmark results, not a promised site gain.
- [Code provenance and licences](THIRD-PARTY.md).
