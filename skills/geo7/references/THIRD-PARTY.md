# GEO7 source and adaptation record

Parent: [SKILL.md](../SKILL.md). Retrieved 2026-10-11. Code was read before running; no upstream installers executed.

| Source | Revision | Use |
|---|---|---|
| [Staksoft](https://github.com/staksoft/geo-seo-aeo-skill) | 003b5145fd79fe8996c18a9f02d94fe08d7c6e80 | MIT PageParser adapted into scripts/audit.py. Same-origin links, HTTP bounds/public destination checks, graph schema parsing and crawl evidence added. Hedge-word score and automatic llms.txt/network heuristic removed. |
| [ReScienceLab](https://github.com/ReScienceLab/opc-skills) | 83eed27e7693e3cea54ae44f3440dd1c40dd5b72 | Apache-2.0 domain-gap request adapted into scripts/research_plan.py; credentials/direct API transport replaced with declared shared MCP route. US/English defaults replaced with required market inputs. |
| [Corey Haines](https://github.com/coreyhaines31/marketingskills/tree/main/skills/ai-seo) | 1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff | Research reference for separate citation/mention/recommendation measurements. No full skill or script copied. Verify dated third-party claims before using them. |
| [SNLabat](https://github.com/SNLabat/SEO-GEO-AEO-Skill) | a2c8769b85813912b2b01cd12c3484f061b439fc | Reviewed. No declared license found; code/text not bundled. |

[Staksoft MIT license](LICENSE-STAKSOFT.txt) · [ReScienceLab Apache license](LICENSE-RESCIENCELAB.txt).

Upstream claims such as universal +40% FAQ/schema visibility, training-bot access as a prerequisite to search, HTTP elapsed time as Core Web Vitals, and fixed character lengths as Google rules were not adopted. Prefer [Google AI feature guidance](https://developers.google.com/search/docs/appearance/ai-features) and actual observations. [GEO paper](https://arxiv.org/abs/2311.09735) describes benchmark results, not a promised gain for a Business website.

## Community portability adaptation —22 October2026

Public instruction licence is retained from the previously published GEO7 community beta. The1.2.0 adaptation includes the existing public helper implementations, complete report fonts and notices. Output confinement uses the explicitly selected current working directory rather than a host-specific ancestor. Named deployment roles and pilot-specific report assumptions were replaced with generic responsibilities and source-dependent statements. The existing read-operation validator was moved into research_plan.py for its offline tests; no provider transport was added. A deployment-specific account collector and old guide UI history are not included. See SOURCE.json for exact source revisions and package adaptation records.
