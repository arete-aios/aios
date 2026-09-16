# AIOS instructions — how to use and extend your business brain

This is the public source for the owner's local `AIOS-INSTRUCTIONS.md`. During setup, translate it into the owner's language, link to their real files, and personalise examples only with confirmed facts.

The local file begins with these clickable root links:

```markdown
- [Current status](ONBOARDING.md)
- [Core rules and direction](CONSTITUTION.md)
```

If those relative links do not fit the client, keep the filenames and show their exact paths. Do not duplicate the status or constitution inside this manual.

## What these business brains do

Your AIOS stores useful context in plain files you control. It helps an AI remember the business, use evidence, keep decisions between chats, find the right method, and improve the system without turning one conversation into the only source of truth.

| Part | What belongs there |
|---|---|
| `CONSTITUTION.md` | business scope, twelve-month goal, AI character, standing rules |
| `ONBOARDING.md` | current setup status, file map, business-context coverage |
| `02-memory/` | business facts, history, people, projects, sources, evidence |
| `03-skills/` | the five installed methods, their triggers, and any you add later |
| `04-tools/` | connected services, permissions, costs, limits |
| `05-focus/` | what matters now, the active projects, and their tasks |
| `06-archive/` | finished or replaced material kept for traceability |

Say **AIOS instructions** at any time to reopen this file as a clickable document.

Optional methods live in one of two places. In a light setup, `00-system/aios/README.md` links to the online methods. In a full local setup, use the installed files under `00-system/aios/` first; do not read the whole library unless the task requires it.

## Your five methods

Both setups install the same five. Each one is a written method in `03-skills/`, and the index with the triggers and sources is [`03-skills/_skills-CONTEXT.md`](03-skills/_skills-CONTEXT.md).

| Say this | What happens | Use it when |
|---|---|---|
| `EVAL7 <thing>` | One finished thing is scored against its own goal: seven dimensions with evidence, visible arithmetic, and the fixes worth making first | A page, an offer, a proposal, or a message is ready and you want to know how good it actually is |
| `EXIT7` | Everything that exists only in this chat is collected, shown with its destination, and saved after you approve | You are done for the day, or a session produced decisions |
| `COX7` or `CONTEXT7 <folder>` | One folder is checked: one index file, everything inside it listed, links that really exist | Your AI keeps missing something that is plainly in the folder |
| `MEETING7` | Notes or a transcript become one dated note with decisions, open questions, and commitments proposed for approval | Right after a meeting or call, while you still remember it |
| `FOCUS7` | What matters now stays true, and the projects and tasks that come out of it get created and updated | You want to know what to do next, or turn a goal into a project |

Installed is not running. A method file costs nothing until you type its trigger. None of them evaluates your work, rewrites your priorities, or contacts anyone on its own, and none of them is permission to send, publish, pay, delete, or change access.

The other methods stay in the public library and are added one at a time, after real work has shown the need: [skills library](https://github.com/arete-aios/aios/tree/main/skills).

## Open the deeper guides

The owner's local copy must keep this section clickable. Render only links that really work in the chosen setup:

- **Full local setup:** [Business Profile](00-system/aios/onboarding/BUSINESS-PROFILE.md) · [Deep Dive](00-system/aios/onboarding/DEEP-DIVE.md) · [Personal Audit](00-system/aios/onboarding/PERSONAL-AUDIT.md) · [Weekly Review](00-system/aios/skills/week7/SKILL.md) · [skills library](00-system/aios/skills/)
- **Light setup:** [Business Profile](https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/BUSINESS-PROFILE.md) · [Deep Dive](https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/DEEP-DIVE.md) · [Personal Audit](https://raw.githubusercontent.com/arete-aios/aios/main/onboarding/PERSONAL-AUDIT.md) · [Weekly Review](https://raw.githubusercontent.com/arete-aios/aios/main/skills/week7/SKILL.md) · [skills library](https://github.com/arete-aios/aios/tree/main/skills)

Do not show both rows in the owner's finished manual. Use the row matching the installed setup, translate its labels, keep its destinations unchanged, and verify every local target before linking it.

## The most useful commands

### Correct the foundation

Say: **Update my constitution: ...**

The assistant reads the current file, shows the exact proposed change, and waits for approval before changing a confirmed fact.

### Add knowledge

Say: **Remember this in my AIOS: ...**

The assistant shows where the information belongs, saves it in memory, and updates the relevant CONTEXT map. A statement in chat is not durable memory until it exists in a file.

### Add source material

Say: **Enrich my AIOS brain.** In Latvian: **Smadzeņu papildināšana.**

Upload or link CVs, websites, presentations, offers, reviews, interviews, transcripts, images, videos, numbers, or your own story. The assistant stores the source before interpreting it and separates facts from ideas.

### Just tell it everything

Say it in your own words, in one long message or out loud: what happened, what worries you, what you are thinking of doing.

The assistant saves what you allowed it to save as the source first, then splits it into **facts, assumptions, questions, and possible work**, and asks you to confirm the reading. Nothing becomes a task, a project, or a confirmed fact until you say so. An idea is an idea. What you told it directly is never presented back to you as something verified elsewhere, and where your words contradict a confirmed fact, the assistant raises it instead of quietly overwriting it.

### Decide what to do next

Say: **What should I do next?** or **Review my focus.**

The assistant reads the twelve-month goal, relevant memory, and current focus. It recommends a small next move instead of merely adding another idea to a list.

### Run projects and tasks

Say: **`FOCUS7` — make a project out of this goal**, or **what is open right now?**

The assistant works inside the structure you already have. If there is none, the starter default is one short index at `05-focus/_focus-CONTEXT.md` and one file per project at `05-focus/projects/<project-name>.md` holding that project's own tasks.

A project card is small: the goal and what it serves, what finished looks like, the status, the next step, the tasks, and the decisions and sources behind it. An empty field says `to confirm` rather than being filled with a guess.

A task is one concrete action with a status — `OPEN`, `DOING`, `WAITING`, `DONE`, or `CANCELLED` — an owner if known, a deadline only if you agreed one, and a link to where the result lives. `WAITING` names what it is waiting for. `DONE` means there is a result, not that the AI wrote the word.

One task lives in one place. The index links to it and never copies the table. If you already use another task system, its role and permissions are agreed first; nothing is called synchronised until it really is, and a date in a file is not a calendar event.

Approved commitments from `MEETING7` and unfinished business from `EXIT7` land here too, each keeping a link back to where it came from.

### Build the full business profile

Say: **AIOS Business Profile.**

The assistant opens the local Business Profile method when installed, otherwise its link in `00-system/aios/README.md`. It completes seven evidence-based blocks, asks no more than five questions at once, and creates five versions of the business super-sentence. You choose the final version.

### Explore yourself more deeply

Say: **AIOS Deep Dive**, ask for self-coaching, or ask to understand your strengths and larger potential.

This is optional. The assistant opens the local Deep Dive method when installed, otherwise its link in `00-system/aios/README.md`, and runs the deeper reflection separately from onboarding.

### Audit your public presence

Say: **AIOS Personal Audit.**

The assistant finds known professional links in the constitution, business profile, and actual memory indexes. If identity information is missing, it asks once. It never assumes a filename such as `memory/00-context.md`. It then says what it will search, checks public sources, verifies namesakes, cites pages, and separates evidence from interpretation.

### Design the weekly review that fits this brain

Say: **Design my AIOS weekly review. Read my business-brain setup and recommend the shortest weekly review that would work for me. Tell me which existing skills to adapt, which new skill is worth building, and which plugins or MCP connections would genuinely help. Separate what is available now from what is only possible later, and change nothing until I approve.**

The assistant reads the constitution, business profile, memory and focus before opening the Weekly Review method. It proposes a small review based on the owner's real goal and existing evidence, not a generic productivity questionnaire.

## Find skills that fit your work

Say: **Which AIOS skills would help me?** Add a task if useful, for example web development, video production, sales, research, reporting, or content.

The assistant reads your goal and current work, then proposes no more than five relevant skills. For each it explains the job, benefit, resource cost, and whether it is already available. It installs nothing until you approve it.

Say **Make this repeatable** after a useful workflow. The assistant can turn the workflow into a skill with a trigger, inputs, steps, approval gates, output, and definition of done.

## Find plugins, MCP connections, and tools

These are different things:

- A **skill** is a written repeatable method: when to use it, what it reads, what it may change, and what “done” means. A skill does not grant access by itself.
- A **tool** is the capability the AI can actually call, such as reading a folder, searching the web, editing a document, or using a calendar.
- **MCP** is a standard way an AI client can expose external tools and data to the assistant. Connecting MCP does not automatically grant every permission; read and write access still have to be checked separately.
- A **plugin** is a package a client may use to bundle skills, tools, apps, or MCP connections. Plugin support differs between AI clients.

Say: **Which plugins, MCP connections, or tools could help my AIOS?**

The assistant checks what the current AI client actually supports. It may suggest connected services for files, web research, analytics, email, calendars, automation, images, or video, but must not claim that a named service is available until it verifies it.

For each suggestion it explains:

- what it can read;
- what it can change;
- whether an account, payment, or API key is needed;
- what still works without the connection.

No tool is connected merely because a document mentions it. Read-only access and write access are separate approvals. Never store passwords or secret keys in Markdown files.

## Keeping the five layers current

The layers do not maintain themselves, and each one is kept up to date by a different sentence from you.

| Layer | You say or give | What the AI does | What that is not |
|---|---|---|---|
| Constitution | "From now on, work with me like this…" | Shows the exact change to the standing rule and rewrites it only after you approve | A passing wish does not rewrite a rule |
| Memory | A story, a file, a source, a correction | Saves the source, proposes the tidied facts with where each came from, files the approved ones under the right subject | `COX7` checks that a fact is findable, never that it is true |
| Skills | "Which do I already have?" · "Make this repeatable" | Shows the installed five; after real work, offers to adapt one or add one | A library of available methods is not a list of your methods |
| Tools | "What needs connecting for this job?" | Names the read and write access required, the cost, and checks what this client actually supports | A method's text grants no access |
| Focus | "Make a project out of this" · "What should I do next?" | Project, tasks, a provable next step, and status changes through `FOCUS7` | Another idea is not a new priority |

Above the five sits the one thing that makes them worth having: a loop that closes.

## One closed loop

Here is the whole cycle with nothing connected: you hand over meeting notes → `MEETING7` finds the decision worth confirming → you confirm it → `FOCUS7` writes the task into the project file → at the next work session you bring the result → `EVAL7` scores it when you ask for it → the fix you choose changes the work → `EXIT7` saves what changed and `COX7` checks that the links still resolve.

Email, calendar, web sources, and LinkedIn are possible inputs to that loop, not the loop itself. A schedule that produces no saved result and no next decision is not a closed loop.

An automated version is a separate decision, and it needs all of it named: the source, the rhythm, where it runs, the permissions, where results are saved, what a failure looks like, and the point where a human decides. Setting up your brain never by itself creates a schedule, connects an account, pays for research, or acts on a social network.

## Now, with setup, and only with your permission

- **Now, with nothing connected:** everything in this file that reads and writes your own files — memory, the five methods, projects and tasks, the business profile.
- **After a setup step:** anything that reads outside your folder — web pages, a calendar, a mailbox, a recorder, analytics. Each one is an account, a permission, and sometimes a cost, and it is verified in your client before it is promised.
- **Only with your explicit permission, each time:** sending a message, publishing, paying, deleting, changing access, or acting in your name.

## Keep the system clean

- One fact has one source; other files link to it.
- Human-readable filenames beat clever codes.
- Active subject folders get a short CONTEXT map.
- Current numbers carry a date or live source.
- Online findings remain `NOT CONFIRMED` until approved.
- Ask before external, destructive, paid, or access-changing actions.
- Install only skills and tools that solve a real repeated need.

The AIOS grows through real work. You do not need to complete an advanced questionnaire before using it.
