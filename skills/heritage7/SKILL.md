---
name: heritage7
description: Research family history from civil records, parish registers, newspapers, censuses, military archives and family trees. Use to trace a relative, transcribe a historical record, reconcile conflicting identities, build an evidence-linked family tree or produce an editable family book and a cited PDF.
---

# HERITAGE7

Work backwards from one known person and one question. Preserve what documents say, show how they support each family link and keep unanswered questions visible.

## Choose the result

- **Record or question.** Return a source citation, a faithful transcription, a separate translation if useful, what it establishes and the next record worth finding.
- **One branch.** Return a small tree or timeline with source IDs, an evidence table, conflicting candidates and the next search. Offer editable data if the user wants to continue the project.
- **Family book.** Build a readable illustrated book with a tree, people and events, evidence notes and sources. Deliver an editable master, a PDF and an evidence register. Agree the branch, period, language and audience before designing the book. Use the [book specification and data fields](references/book-delivery.md) and see the [sample PDF](examples/family-book-sample.pdf) and its [editable example](examples/family-book-sample.md).

## Set the starting point

1. Begin with a birth certificate or another dependable record. Record the known person's name as written, birth date and precise place, and the parents named in the record. Where available, use both parents' exact dates and places of birth as search anchors. Record house, village, parish and municipality separately.
2. Choose the missing fact that would change the tree, such as a birth, marriage, suspected parent, surname change or period of military service. List variant spellings, historic place names, religion and jurisdiction for that date. Mark family recollections, online trees and search indexes as leads.
3. Ask only for details that change the next search. Keep private scans in the user's chosen private files and omit identifiers unnecessary for the research.

## Find and read records

1. Pick sources by place, period and event using the [archive and database directory](references/source-directory.md). Start with jurisdiction and collection before looking for a name. Try original spellings, initials, gendered endings, and German or Cyrillic forms as appropriate. Keep dates as written. Normalize the calendar only when the source's dating practice is known.
2. For a login-gated source, let the user sign in to the official portal themselves. If the user authorizes browser control and the tool is available, inspect the specific open pages. Otherwise use an authorized crop, PDF excerpt or text, or identify how to request the file. Never ask for passwords or codes. Follow the archive's access and reproduction conditions.
3. Identify the record type among catalog, index, record image, later certificate and transcription. Inspect headings and neighboring rows before assigning columns. For difficult handwriting, compare the full page and enlarged crops, then verify names, places and dates against the image. Preserve original spellings, abbreviations and uncertain characters as [?]. Keep transliteration, translation and normalized values distinct.
4. Record the repository, collection or fond, series, file, image or page, entry, stable link, access date and reuse status. For an unsuccessful search, record the spelling variants, dates and holdings actually checked and the access limits.
5. When comparing models, give each one the same marked entry and compare specific fields against a checked reading. Note the model, date, full-page or crop input, and whether cost came from an existing allowance, API billing or an archive fee. Review disputed fields on the scan.
6. For war, captivity or displacement, capture dates, location, issuing authority, unit or camp and record type. Compare sources across jurisdictions and institutions where practical. A grave entry, award, capture card and unit roster answer different questions. Record institutional spellings alongside the person's own name when recoverable.

The [handwriting benchmark](references/handwriting-benchmark.md) lists the tested models, how much they read, and an example of errors on the same record. Use the [offline scoring script](scripts/score_transcription.py) with your own checked facts.

## Decide what the sources support

| Claim | Source IDs and exact location | What the record says | Status | Conflict or next check |
| --- | --- | --- | --- | --- |
| Record one fact or relationship per row | Repository, citation and entry | Faithful excerpt or summary | Documented / likely / candidate | What would distinguish the possibilities |

Use **documented** for a claim supported directly by the cited record, **likely** for a supported inference and **candidate** for a link still needing distinguishing evidence. A documented birth can belong to a person whose link to the family remains a candidate. Compare at least two distinguishing details where possible, such as parents, house, spouse, age, occupation and place. Preserve conflicts and identify the strongest available test. Count multiple copies or index entries for the same underlying record as one source.

Keep source IDs on the diagram and label tentative connections. State the limits of an unsuccessful search against the specific holdings reviewed. Preserve the evidence when proposing edits to an existing family tree.

## Deliver and check

Give the user the answer, evidence and single most useful next search. For a catalog lead, include the file reference and the official request route. In a book, make the link from a fact to its source understandable without opening an app. Include images only when private or public use matches the audience and the permission. A citation and a short permitted excerpt or summary can stand in for a restricted scan.

For a shared or public version, review each image's rights and remove sensitive details about living people unless permission is documented. Ask before publishing, editing a shared tree, uploading restricted material or contacting an archive. Confirm which files were produced and what remains unresolved or unverified.

## Starting instruction

> Use HERITAGE7 to investigate one branch from my earliest verified record. Start with the most useful search. Keep original readings, citations and competing candidates. Once we have enough evidence, prepare an editable family book and a cited PDF.
