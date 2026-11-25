# Family book and evidence package

Use this when the user asks for a family history book, a printable PDF or reusable research data. For a first look, an evidence table and a small tree often suffice.

## What the user gets

| File | Role |
| --- | --- |
| `family-book.pdf` | Reading and print edition with source citations, page numbers, legible images and links. |
| `family-book.md` or the agreed editable layout | Same text and figure captions in a form the user can revise. Keep images linked to files they are permitted to retain. |
| `evidence/` | Machine-readable people, relationships, sources, claims and search log. A spreadsheet with equivalent tables is also suitable. |
| `media/` | Permitted scans or excerpts used in this edition, with original captions and access or reuse notes. |
| GEDCOM when requested | A tree for import. Preserve evidence and relationship status in the editable register and report which fields the chosen tool imports. |

Agree the intended reader, language, scope and image audience first. Pick the format the user can maintain. To add later discoveries, update the evidence register and regenerate the relevant book pages.

## Page plan for the PDF

Start with [this example](../examples/family-book-sample.pdf) or its [editable source](../examples/family-book-sample.md). Scale page count to the branch and amount of evidence.

1. **Cover and publication note.** Family or branch, geographic scope, period, revision date, audience and any image or privacy notes. Include a contents list for longer books.
2. **Read the tree.** Show the branch and key people on a page. Put an evidence ID on each family link. Use words or a dashed line and matching legend for provisional links. Use separate trees for dense branches. Label what the dates refer to.
3. **Tell the story.** Give each generation or place a concise narrative. Use a dated timeline for movements, military service or surname changes when there is evidence. Start each person profile with key facts and source references. Explain conflicts where the reader first meets them.
4. **Show a document.** Put a readable crop or the permitted original next to the faithful reading and separate translation. Mark which entry was used. Caption with repository, fonds/file, page/entry and rights or access. If the scan is restricted, give a stable viewer link and reference alongside a permitted summary.
5. **Close with evidence and open questions.** Include one evidence row per material claim, unresolved candidates, the strongest next source and the record index. For a larger book, add people and place indexes and an appendix for full transcriptions.

For print, A4 portrait is a practical starting point. Use generous margins, a readable body font with the required language glyphs, clear headings, large-enough facsimiles and consistent page numbers. Let wide trees use a landscape page or split the branch. Captions and text must remain readable in grayscale. Export searchable text and working links. Use PDF/A only when requested and test the resulting conformance.

## Evidence register

Use stable IDs through all files. The table describes fields to capture as evidence allows. Store empty or approximate values as such. Use UTF-8 for data exports and consistency-check IDs before delivery.

| Table | Suggested fields |
| --- | --- |
| People | person ID, names as written, normalized display name, name variants, birth/death as recorded and normalized, place IDs or place labels, privacy status |
| Relationships | relationship ID, both person IDs, type and roles, status, supporting claim IDs, alternatives |
| Sources | source ID, repository, collection/fond, series, file, page/image, entry, record type and date, original URL, access date, image/reuse status |
| Claims | claim ID, person or relationship ID, field or event, original reading, translation, normalized value, date precision, status, source IDs, conflict note |
| Searches | search ID, question, repository or collection, locality, variants, exact year ranges reviewed, date, result or access limit, next action |

Use source IDs in citations (`S-014`) and person IDs (`P-006`) for consistency. One source can support several claims. Compare source independence and type before resolving conflicts. For military records, roles and abbreviations should be translated only after the record type and issuing authority are understood.

### Example of a claim at the right scale

A register directly names two parents for a child. Record the stated relationship to each named parent as **documented** against the entry. If linking one parent to a similarly named adult in a later military record, create a separate **candidate** or **likely** claim, depending on evidence. Note the place, relative, birth year or occupation that would distinguish that person. In the book, give that reasoning in a short sidebar or an evidence note.

## Before handing it over

- Trace a few book claims and all important tree links back to a specific record, using the actual page or entry reference.
- Check citations, attachment rights, identity conflicts and the handling of living people against the intended audience.
- Render the PDF and inspect all pages. Check names with accents, dates, image captions, tree legends, page numbers, clipping and link targets.
- Open the editable master and tabular files. Check the IDs, searchable PDF text and that new evidence can be added without retyping the book.
- Hand over a short revision note, with the most useful next search and the gaps still open.
