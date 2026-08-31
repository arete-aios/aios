# Editable timeline and round trip

The rendered video proves what the current cut looks and sounds like. The editable timeline preserves the owner's ability to disagree with it. Produce both from the same decision list unless the owner asks for only one.

## Version the pair together

Use one version for the render and timeline that describe the same cut. Keep source timelines and timelines returned by an editor as separate lineages.

```text
out/<date>_<slug>-v3.mp4
out/<date>_<slug>-v3.fcpxml
out/<date>_<slug>-SOURCE-v1.fcpxml
out/<date>_<slug>-v3-THEIRS.fcpxml
```

A small correction increments the decimal version. A different cut or intent increments the major version. Do not overwrite an earlier result just because the new one is expected to be better.

## Validate before handoff

An XML file can be well formed and still be rejected by an editor or mean something different from what you intended. Check all of these:

1. The XML parses.
2. Every media path resolves from the project file's actual location.
3. Times use the format the editor expects, including rational time where required.
4. Elements and attributes match the editor's schema or DTD when one is available.
5. Each connected overlay is attached to the clip it sits above.
6. Every connected item's offset falls inside its parent's extent.
7. The timeline duration and clip order match the decision list.
8. Absolute local paths, usernames, GPS fields, and other machine-specific metadata are removed from the handoff package unless the owner explicitly needs them.

The fifth and sixth checks matter because a connected item's offset is expressed in its parent's time, not in global timeline time. Attaching every title to the first spine clip can produce a document that passes schema validation but imports with missing overlays.

Keep timeline-referenced overlays and other generated assets in the versioned output package. Do not point the timeline at disposable working files that another machine will not receive.

## Make the human return path explicit

Importing a project file creates state inside the editor. The editor does not usually write changes back into the imported file. Use this loop:

1. Generate and validate the timeline.
2. The person imports and edits it.
3. They export a new timeline beside the original under a different name.
4. Read both files and report trims, reorderings, removals, additions, effects, and retiming.
5. Render from the returned version and repeat if needed.

The returned file is evidence of what changed. Without it, "I changed the edit" cannot be translated into a reproducible next render.

## Delivery checklist

- Render and timeline share the same cut version.
- All referenced media and overlays travel with the timeline or resolve to agreed shared paths.
- XML, schema, paths, parent extents, duration, clip order, and metadata-leak checks pass locally.
- A short import test has been performed when the editor is available.
- Validation status is recorded as `schema_validated`, `import_tested`, or `import_unverified`. Never describe an untested import as proven editable.
- The owner knows they must export a new project file after editing.
