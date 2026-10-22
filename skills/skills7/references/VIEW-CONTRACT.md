# Portable SKILLS7 viewer contract

Parent: [SKILL.md](../SKILL.md). Workflow: [METHOD.md](METHOD.md). Runtime commands: [scripts/README.md](../scripts/README.md).

## Package metadata

manifest.json contains `id`, `name`, `title`, `version`, `updated_on`, `author`, `owner.label`, `status_label`, `resources`, `workflow`, declared `tools`, optional `tool_groups`, method `changelog` and `overview`. Text is a string or an `{en, lv}` object. Use a plain string for `owner.label`.

`distribution: community` selects a shareable guide by default. No personal setup, account identifiers or private runs should be present in any source file. The exporter removes `owner_setup` and private run records, but cannot rewrite private prose or hard-coded credentials; inspect the entire package yourself.

`overview.title/summary/starting_prompt` form the short Overview. Optional `overview.additional_prompts[]` contains `id/title/description/prompt/copy_label/file`; each entry becomes a separate real copyable prompt. Its `file` must be in view.fileGroups. SKILLS7 uses this for the exact Visualise any skill prompt.

Each workflow row has `number/name/label/output/doc`. `doc` is a relative file plus an optional Markdown anchor. Tool rows have `id/name/icon_id/requirement/purpose/scope/limit`, with optional `importance` only when its qualitative basis is supplied in `tool_rating`. Do not present an illustrative judgment as a measured result.

## Human guide source

view.json defines `eyebrow`, `onboarding`, `fileGroups`, `layout`, optional `guides`, `flow` and `preview`. fileGroups are ordered groups with `id/title/desc/zip/files`; each file has `path/desc` and optional `historical`. All paths resolve inside the package. Display text is escaped.

`layout.tabs` selects `overview/principles/flow/example/log` for the community five-tab guide; optional backwards-compatible `how`, `aios` and internal `settings` are supported. `overview.compact: true` requires overview/flow/example. `exampleTab: true` creates the separate example. `changesOnly: true` displays method changes. `filesTab: principles` displays the file library in a guide defined by `guides.principles`.

Guides have `eyebrow/title/lead/sections`. Sections support `title/text/items` (title/text), `rows` (label/text), `note`, and `docs` (file/label). An optional section ID is unique and begins `guide-`. Include each referenced document in fileGroups.

## Workflow

`flow.presentation: journey`, `modeBehavior: canvas`, `defaultMode: detailed` provide detailed and short diagrams with identical full step descriptions below. `sequence` lists main node IDs with consecutive `step` values starting at 1. `width/height/left/top/start` set the canvas.

Nodes: `id/x/y/kind/icon/label`, with optional `step/actor/what/summary/paragraphs/in/out/files/headerIcons`. Kinds: `you`, `ai`, `py`, `tool`, `skill`. Real helper nodes use `kind: py` and point to actual files. Saved-output nodes use `artifact: true`, optional `w/h/caption` and `detailFor` pointing to a sequence node. `stored.title/text` explains a saved result; do not embed personal storage paths in a community flow.

Edges are `[from,to]` or `[from,to,type]`; type can be `side/loop/min/full`. A fourth element may contain exact SVG `path/label/x/y`. Keep paths and nodes inside the canvas. Optional `goal`, `notes`, `legend`, `channels` and `rhythm` explain context; a cadence card does not create a schedule.

`simple` has its own `width/height/goal/nodes/edges/loopLabel`. Each short node has `id/target/kind/icon/label/caption/x/y`; target points to a real sequence step. It summarises the same process without adding or cancelling an execution step. `modeNote` should explain that full descriptions stay identical.

Neutral icons are included in the template. Brand icons resolve first from a skill’s assets/tool-logos, then from this engine’s bundled assets/icons. Include source and rights for any added icon; there is no external logo-library dependency. A brand image does not imply a connection.

## Example

preview contains `eyebrow/title/lead/label/period/headline/summary`, optional action/draft/wait/copy labels, `note/sourceDoc/sourceLabel` and `items`. Each item may have `id/icon/channel/priority/title/brief/contextLabel/quote/why/action/source`, `draft` or `followup`, `draftNote` and a source URL. Copying a draft is local, never sending.

Label synthetic examples visibly. Real results require evidence and the right audience. Optional progress is meaningful only when its denominator is defined; absence of progress is normal. Do not invent growth percentages or tool results.

## Complete binary archive

`manifest.archive.files` is an explicit unique ordered list of every file to include in the full source ZIP: method, actual scripts, required runtime assets, binary fonts/images, licences and metadata. `resources` inventories the package. Generated index.html is excluded from its own archive to avoid recursive self-embedding. The SKILLS7 source archive includes its full local engine, so unpacking and rebuilding regenerates index.html offline.

The generated data stores UTF-8 files as `{encoding: utf-8,text,bytes,zip}` and binary assets as `{encoding: base64,base64,bytes,zip}`. Python and browser ZIP writers decode the same bytes. check_view.py runs the page’s actual ZIP code under Node and compares the archives byte for byte. File dialogs can download original binary bytes; text copy is disabled for binary files.

Do not include credentials, caches, execution outputs, personal setup or a private machine path in an archive. A full source archive need not bundle a user’s external Python/Node interpreter, AI model or account connectors; declare those real prerequisites. External skills use the SKILLS7 engine as an optional guide-rebuild tool, not as a hidden live-account dependency.
