# Skills

_Parent: CONSTITUTION.md_
_Layer 3. A method written down once, so the same work runs the same way the second time._

<!-- Starter registry, created by the starter onboarding. Translate the explanatory text into the owner's language. Keep trigger words, file names, and paths unchanged. Do not use the eleven-skill registry from the full build here. -->

## The five methods this brain starts with

| Trigger | What it does | Method file |
|---|---|---|
| `EVAL7 <thing>` | Scores one finished thing against its own stated goal: seven dimensions, evidence for each, visible arithmetic, and a ranked list of what to fix first | `03-skills/eval7/SKILL.md` |
| `EXIT7` | Closes a working session by finding what exists only in the chat and handing back ready changes to approve | `03-skills/exit7/SKILL.md` |
| `COX7` or `CONTEXT7 <folder>` | Checks that a folder has exactly one CONTEXT file, that it lists what is really inside, and that its links point at files that exist | `03-skills/context7/SKILL.md` |
| `MEETING7` | Turns meeting notes or a transcript into one dated note with decisions, open questions, and candidate commitments to approve | `03-skills/meeting7/SKILL.md` |
| `FOCUS7` | Keeps current priorities true, and runs the projects and tasks that come out of them | `03-skills/focus7/SKILL.md` |

`COX7` and `CONTEXT7` are two names for one method and one file. There is no `03-skills/cox7/` folder.

## Installed does not mean loaded

A method file sits on disk and costs nothing until its trigger fires. This index is short on purpose: the assistant reads the table, and opens the full method file only when the owner asks for that method or the method's own trigger conditions are met.

- No method runs automatically in every answer.
- `EVAL7` is never self-invoked. Unrequested scoring of the owner's work is criticism nobody asked for.
- A trigger in this table is not permission to send, publish, pay, delete, or change access. Those gates stay in the constitution.

## Trigger lines

These are the lines that make the five methods real for the assistant. They live here, and the constitution links to this file. Move one into the constitution only if the owner triggers that method most days.

```
EVAL7 {thing}. Score ONE existing thing against its stated goal, 7 dimensions with evidence, overall score, ranked path to 100, one hard truth at the end. Never self-invoked. Spec: 03-skills/eval7/SKILL.md
```

```
EXIT7 at session close. Find everything that lives only in the chat, come back with ready diffs not questions, verify the CONTEXT file actively, then ask whether the focus layer changes. No new work. Spec: 03-skills/exit7/SKILL.md
```

```
CONTEXT7 / COX7 {folder}. One master file per folder, it lists everything inside, unlisted means invisible. Check, report gaps, propose the missing lines, wait for my OK. Spec: 03-skills/context7/SKILL.md
```

```
MEETING7. After a meeting: one dated note, fixed sections, their words quoted not summarised, commitments proposed for my approval and then handed to FOCUS7. Never process the same meeting twice. Spec: 03-skills/meeting7/SKILL.md
```

```
FOCUS7 [area | project]. Keep what matters now true from real data, run my projects and tasks from it, show a diff before changing a priority or a status, write only what I approve, move overflow to the logs, never delete. Spec: 03-skills/focus7/SKILL.md
```

## Where each file came from

Record the real source and the version from each method file's own metadata block when it is installed. Do not fill this table from memory.

| Method | Public source | Source version | Installed |
|---|---|---|---|
| `eval7` | `https://raw.githubusercontent.com/arete-aios/aios/main/skills/eval7/SKILL.md` | `<version>` | `<YYYY-MM-DD>` |
| `exit7` | `https://raw.githubusercontent.com/arete-aios/aios/main/skills/exit7/SKILL.md` | `<version>` | `<YYYY-MM-DD>` |
| `context7` | `https://raw.githubusercontent.com/arete-aios/aios/main/skills/context7/SKILL.md` | `<version>` | `<YYYY-MM-DD>` |
| `meeting7` | `https://raw.githubusercontent.com/arete-aios/aios/main/skills/meeting7/SKILL.md` | `<version>` | `<YYYY-MM-DD>` |
| `focus7` | `https://raw.githubusercontent.com/arete-aios/aios/main/skills/focus7/SKILL.md` | `<version>` | `<YYYY-MM-DD>` |

Every installed file keeps its own attribution and CC BY 4.0 licence line. Adapt a method to the owner's real folders and approved way of working. Never write a personal fact into a method as if it were a universal rule.

## When a method file could not be written to disk

If this client cannot fetch the five files, keep the rows above, mark the method `NOT INSTALLED — source only`, and say so plainly to the owner. When the trigger fires, open the source URL then. Never claim a local file exists before it has been read back.

## Adding a sixth method

The public library holds many more methods: `https://github.com/arete-aios/aios/tree/main/skills`. Add one after real work has shown the need, one at a time, and register it in this table with its source and version. A method installed before its first real use is a file nobody opens.

---

_LOG: `<date>`, five starter methods registered by the onboarding. Update this line whenever a method is added, adapted, or removed._
