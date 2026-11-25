# Historical handwriting benchmark

AreteAIOS tested AI readers on 12 selected Kurzeme parish-register pages dated 1799–1906. The task was to locate and transcribe **one target entry per page**. The reference contained **112 checked fields** across dates, names, places and other details. These results describe how the readers performed on this sample in October and November 2026.

## 2 October 2026 · full-page images

| Reader | Hits / 112 | Exact | Gothic Kurrent / Cyrillic / German 1906 | P03, 1847 / 10 | Recorded time | Estimated USD per run |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| Claude Opus 5.5 | 93 (83%) | 72% | 76% / 94% / 90% | 7 | 247 s | $0.56 |
| Claude Sonnet 5.5 | 83 (74%) | 57% | 59% / 97% / 90% | 5 | 142 s | $0.28 |
| GPT-6 Astra | 75 (67%) | 55% | 52% / 97% / 60% | 6 | 12 min 52 s | $2.75 ($1.25–8.00) |
| GPT-6.1 Sol | 63 (56%) | 41% | 41% / 86% / 50% | 3 | 17 min 26 s | $0.95 ($0.35–2.60) |
| Gemini 3.1 Pro | 54 (48%) | 37% | 32% / 72% / 70% | 3 | ≈259 s | $0.35 ($0.17–0.83) |
| Gemini 3.5 Flash-Lite | 33 (29%) | 18% | 21% / 44% / 30% | 0 | ≈335 s | $0.044 ($0.019–0.12) |
| GPT-6 Luna | 8 (7%) | 6% | 11% / 3% / 0% | 1 | 2 min 38 s | $0.017 |
| Claude Haiku | 3 (3%) | 1% | 2% / 3% / 10% | 0 | 84 s | $0.08 |

The script groups comprised 66 fields in seven Gothic Kurrent pages (1799–1873), 36 fields in four Cyrillic pages (1892–1902) and ten fields on one German page (1906). The historical scorer accepted normalized exact matches, plus text matches at a similarity threshold of 0.80. “Exact” still involved normalization and accepted reference spellings.

**Incomplete run.** The Gemini 3.8 Flash first batch, P01–P06, returned a platform error. It hit 37 of 56 fields on P07–P12 (66%). Gemini 3.1 Pro also hit 37/56 on those same pages. The recorded ≈197 s includes the failed batch, while $0.056 ($0.019–0.17) estimates the six completed pages.

**Reading the time and cost columns.** Claude runtimes came from subagents, ChatGPT from the interface's elapsed time, and Gemini from an approximate elapsed window that included polling delay. Claude's cost estimates used recorded tokens and an approximate input/output split. ChatGPT and Gemini used assumed token volumes because their interfaces did not report hidden reasoning tokens. The estimates can move substantially and do not represent invoices or the terms of an AI subscription.

## 15 November 2026 · full page and overlapping crops

The follow-up reused the 12 pages and 112 reference fields. The Gemini full-page run used one call per page. The tiled Gemini and Opus runs had the full image plus the same four overlapping quadrants, each approximately 54% of the original width and height.

| Reader and input | Hits / 112 | 95% interval | Exact | Gothic Kurrent / Cyrillic / German 1906 | P03 / 10 | Transcribed characters |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gemini 4 Hydrogen High · full page | 78 (70%) | 62–78% | 54% | 61% / 89% / 60% | 6 | 4,986 |
| Gemini 4 Hydrogen High · page + crops | 97 (87%) | 82–91% | 76% | 83% / 94% / 80% | 8 | 6,000 |
| Claude Opus 5.5 · page + same crops | 97 (87%) | 76–96% | 74% | 77% / 100% / 100% | 7 | 7,186 |

Character counts are the length of the saved verbatim-transcription fields, including spaces and uncertainty marks. For scale, October full-page Opus produced 3,969 characters and Sonnet 4,043. Longer output can come from repeated column labels or more text around an entry. The counts measure output volume.

For Gemini, supplying crops improved the score by 19 of 112 fields, or about 17 percentage points (paired 95% interval +10 to +24 points). The two tiled readers tied on total hits, with a paired difference interval of −9.9 to +7.8 points for Opus minus Gemini. Opus read more fields in the Cyrillic and 1906 subsets, while Gemini read more Gothic fields on these pages.

The Gemini runner logged about 2,125 seconds of summed per-page work with the full image and 1,624 seconds with crops (about 177 and 135 seconds a page, with four calls running in parallel). It reported about 562,000 and 519,000 tokens respectively under an existing subscription. The tiling report records a $2.93 cost estimate for the Opus run. It provides no comparable Gemini dollar cost.

## What the percentages hide

P03 is an 1847 burial entry. The research reference reads **Fritz Boitmann**, buried **17 July**. Full-page Gemini 4 returned **“Friz Soikans”** without an uncertainty marker and read the burial day as 16 July. With crops it returned **“Fritz Bockmans[?]”** and recovered 17 July. The same tiles gave Opus the right burial day and a different unsure name, **“Lerk [?] Bertmas [?]”**. For a family-tree entry, those names require another reading against the scan. A higher page score can leave a critical surname unresolved.

Use this method on your own material:

1. Pick confirmed fields from several representative pages. Include the hardest names and dates. Preserve the original spelling and record the source next to each checked value.
2. Give each reader the same images and instructions. Keep answers independent. Try the full page first, then give each reader the same overlapping crops. Ask for **[?]** on a tentative reading and **[…]** for an unreadable passage.
3. Separate literal readings, inferred details and translations. Put only the literal reading of each checked field into the strict scorer below. Review disagreements on the original image, and use a separate record to verify material identity or kinship claims.

The historical runs had one attempt per page, some reference values were informed by earlier Claude readings, and platform settings, tool access and batching differed. The intervals use bootstrap resampling by page to account for fields from the same page. This captures uncertainty within the sample. General performance on other registers or whole-page indexing remains unmeasured. The package shares aggregate results and a short excerpt. The full inputs, answer key and historical scorer are outside the public package.

## Score your own checked fields

From the skill directory, use Python 3.8+ and two UTF-8 JSON files.

`checked.json` (synthetic data):

```json
[
  {"id": "example-01.name", "expected": ["Marta Kalne", "Marta Kalns"]},
  {"id": "example-01.burial_date", "expected": ["1900-05-17"]},
  {"id": "example-01.place", "expected": ["Liepu mājas"]}
]
```

`candidate.json` (synthetic data):

```json
{
  "example-01.name": "Marta Kalne",
  "example-01.burial_date": "1900-05-16",
  "example-01.place": null
}
```

```sh
python3 scripts/score_transcription.py checked.json candidate.json
```

This example reports one match, one mismatch and one missing value. Every checked field stays in the denominator. The scorer normalizes Unicode to NFC and collapses whitespace. Spelling, letter case, accents, punctuation and uncertainty marks stay meaningful. Accepted variants must be verified in advance and listed explicitly. Omitted, null and blank candidates count as missing. Candidate-only fields are listed separately. The output contains counts and field IDs rather than the source text. Everything runs offline with the Python standard library. [Read the scoring script](../scripts/score_transcription.py).

This is a strict field-by-field starter for new checks. The historical scores used normalized search over each entry and allowed fuzzy text matches, so this script's results use a different metric.
