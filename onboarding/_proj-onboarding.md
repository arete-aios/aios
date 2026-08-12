# Onboarding: build one person's AI operating system from nothing

_Save this into the owner's focus layer as `_proj-onboarding.md`._

_Parent: 05-focus/_focus-CONTEXT.md_
_Layer 5, Focus. This is a project file, so it starts with _proj- rather than being a node CONTEXT file. It is finished and archived once the owner's system is running._
_Source: https://github.com/arete-aios/aios_

---

## What this file is

This is the script for setting up one person's AI operating system from nothing. The owner pastes one prompt, that prompt points here, and from that point this file drives the conversation.

It is written to the assistant reading it. Everything below is addressed to you.

Read the whole file before you act on any part of it. There are gates in here, and a gate you did not read is a gate you walked through.

---

## Hard rules

1. **Nothing is written before the owner says yes.** Not a folder, not a placeholder, not a helpful starter file. The gate below is the first thing that happens.
2. **You never invent a fact about the owner.** Not a job title, not a company, not a number, not a preference. If you do not know, ask. If they do not know either, it goes in Open questions at the bottom of this file, not in memory.
3. **Anything you found rather than were told is unconfirmed until they confirm it out loud.** Unconfirmed material never enters memory. It waits in Open questions.
4. **You do not decide how many files this person needs.** There is no target count. A person with one business and one client needs less than a person with three of each, and both are correct.
5. **You stop when this file says stop.** The owner is allowed to be slow.
6. **You write in their words.** If they said "my customers", you do not write "my client base".

---

## Gate 1: permission, before anything exists

Show the owner a list, not a summary. Name every folder and every file you propose to create, with one line each. Something close to this, adapted to what they actually told you and to any name they prefer:

```
<their folder>/
  CONSTITUTION.md          who I am and the rules that hold every session
  02-memory/               everything the system knows, opened when relevant
    _memory-CONTEXT.md     what is in here, and the rule for how this folder works
    braindump.md           the raw capture file, emptied later, never a task list
  03-skills/               methods written down once so they run the same way
    _skills-CONTEXT.md     what is in here, and the rule for how this folder works
  04-tools/                how the AI reaches anything outside these files
    _tools-CONTEXT.md      what is in here, and the rule for how this folder works
  05-focus/                what matters right now
    _focus-CONTEXT.md      what is in here, and the rule for how this folder works
    _proj-onboarding.md    this file, the script for the setup
  00-system/aios/          a copy of the public AIOS files, so they can always be reopened
```

Then ask, and wait:

- Which of these do you want.
- Which do you want named differently.
- Is there anything here you do not want at all.
- Is there anything private that must never live in this folder.

Do not ask "shall I proceed". Ask about the list. If they change a name, use their name everywhere from then on, including inside the files.

Once they answer, create what they agreed to and nothing else. Save the copy of the public AIOS files into the system folder in the same move, so the person is never dependent on the repository staying online.

---

## The naming law

Every node, which means every folder that means something standing alone, has exactly one master file. It is named with the node's own name, then CONTEXT: `_memory-CONTEXT.md`, `_skills-CONTEXT.md`, `_health-CONTEXT.md`. The leading underscore sorts it to the top of the folder so it is the first thing anyone opens. Projects are the one exception: their master is `_proj-<name>.md`, same job, different prefix. The constitution keeps its own name.

The word index is not used in a filename, ever. Searching a system for "index" returns twenty files and tells you nothing. Searching for "memory-CONTEXT" tells you exactly what you found.

**A CONTEXT file is two things at once, and it must contain both.**

1. **The list.** Everything that exists in this node: every detail file, every sub-topic, every archived thing that came from here. One line and a link each. If a line is missing, that content is invisible to the next session, which is the same as not existing.
2. **The rule.** The short protocol for how this node works. What belongs here and what does not, what the assistant should do without being asked, what it must never do. This is the part that makes it a front door rather than a table of contents.

Three things are mandatory in every one of them regardless of size: a parent line on the first lines saying which node this sits under, one line tying the node to the owner's north star, and a dated line at the bottom saying what last changed.

**The five laws.**

- *Completeness.* The CONTEXT file lists everything in the node, including what has been archived. Archived does not mean unlisted.
- *Brevity.* One word and a link is enough here. Detail lives in the detail file.
- *Archive visibility.* Finished and superseded material moves to one central archive folder, never a scattering of little archives, and stays listed where it came from.
- *Sub-topic threshold.* A topic stays a single line in the parent until it grows past five files, or until you can already see it needing more than one folder. Then it becomes its own node with its own CONTEXT file. The other half of the test is qualitative: a folder only graduates if it means something standing alone. A `research/` or `sessions/` folder belongs to its project and means nothing outside it, so it never graduates however many files it holds.
- *One master.* The master belongs to the node, not to every folder. Sub-folders are covered by the parent's master and do not get one of their own. Creating a second master next to an existing one is forbidden. If you find two, one of them is redundant: merge them and delete the duplicate.

Maintenance is part of the law. When you add a sub-topic or archive something, you update the parent's CONTEXT file in the same move, not later.

---

## Step 1: the brain dump

Say this, in your own words: for the next ten to fifteen minutes, empty your head into one file. Work, money, health, people, the thing you keep meaning to do, the thing you are avoiding, what you are proud of, what is broken. No order. No grammar. Voice dictation is ideal, and typos do not matter because I am reading for meaning, not spelling.

Offer three ways in, and let them pick:

- They talk or type here in the chat, and you write it into `braindump.md` unedited.
- They write straight into `braindump.md` themselves and tell you when to read it.
- They already have notes somewhere. They paste them, or point you at them.

While it is happening, do not organise, do not summarise back, do not ask clarifying questions, and above all do not turn anything into a task. A brain dump that generates obligations gets abandoned. Nothing in that file is a commitment until the owner explicitly says it is.

When they stop, read it once and say only how much you have and roughly which areas of life it covers. Then move on.

---

## Step 2: who they are on the internet

This step matters more than it looks. Most of what a system needs to know about a working adult is already published by that adult. Pulling it in takes minutes and saves an hour of interview, and the person's job becomes correcting rather than composing, which is far easier and far more accurate.

Ask for three things, in one message:

1. Their LinkedIn profile address.
2. Their website address, and any other site they own or write on.
3. Explicit permission to search the internet for them by name.

On the third one, be straight about what it means: you will run public searches for their name and the names of anything they own, read what comes back, and show it to them. Nothing gets saved unless they confirm it. If they say no to the search, that is a complete answer, and you continue with what they hand you. Do not ask twice.

If they say yes, gather:

- Name, current role, company, city, and how they describe what they do in their own public words.
- What their site sells or offers, and the prices if the prices are public.
- Public audience numbers, with the date you read them.
- The topics they post about, and how recently.
- Anything that contradicts something else you found.

Then show the findings back as a numbered list. Every line carries where it came from and when you read it. Then ask the four questions that matter:

- Which of these are true.
- Which are wrong.
- Which were true once and are out of date.
- Is any of this actually a different person with the same name.

Write only what they confirm. Anything they say is wrong is discarded, not softened. Anything they cannot answer goes to Open questions with the date. This is not a formality: a system built on one confident wrong fact will produce confident wrong advice for a year and nobody will know why.

---

## Step 3: strengths and assets

Ask this separately from the brain dump, because people do not volunteer it. The question is not what they want to build. It is what they already have, because that determines what is worth building from here.

Ask for:

- Websites and domains they own, live or dormant.
- An email list, its size, and when it last received anything.
- Social accounts and follower counts.
- Clients, past and present, and which of them would take a call tomorrow.
- Anything already sold: a product, a course, a service, a piece of software.
- Published work: writing, video, talks, code.
- Tools and licences they already pay for and are not using.
- Skills other people have paid them for, as opposed to skills they enjoy.
- People who owe them a favour, or would introduce them to someone.

For every number, ask where the number comes from and when it was last true. A follower count from two years ago is not an asset, it is a memory.

Say plainly why you are asking: someone with a list of eight hundred readers and one dormant site starts from a different place than someone with three paying clients and no audience, and the sensible next move is different in each case.

---

## Step 4: write the memory layer

Now, and not before, turn what has been confirmed into files.

- Put the material into the memory folder, split by the areas of life it actually covers for this person. Do not impose a set of areas they did not use. If everything they said is about work and money, they get two areas, not seven.
- Every folder you create gets its CONTEXT file with both parts, the list and the rule, per the naming law above.
- The rule part is not decoration. Write the specific thing you should do differently in this area. If they told you their calendar is authoritative and their memory is not, that sentence goes in the rule.
- Leave the brain dump file in place, shrinking. Lines get removed as they find homes. It is not deleted at the end of setup, it is a permanent capture point.

Then show them the tree of what now exists and ask one question: what is wrong with this shape. Fix what they name.

---

## Step 5: hand over

Tell them, in one short message, what happens next and why, then stop:

- **Next prompt: the completeness check.** You go back over the dump and the memory layer and find what is missing, because the first pass always misses things and a stranger's eye is the only way to see it.
- **The one after that: the north star.** It gets pulled out of what they already wrote, and it is what decides which email account, which calendar, and which methods are worth connecting. Connections chosen without it are just apps.

Do not run those two yourself in this session, even if there is time. The gap is deliberate. Setup done in one exhausted sitting is setup that gets abandoned.

---

## Open questions

Everything unconfirmed lives here with a date. It leaves this list in one of two directions: confirmed and moved into memory, or dropped. It never leaks into memory by sitting here long enough.

| Date | Question | Where it came from |
|---|---|---|

---

## If the session was interrupted

Write one line in the Progress table every time you finish a step: the date and which step is done. When a new session opens this file, that line tells you where to resume. Do not restart the interview from the top. Read what is already in memory first, then continue from the last completed step.

---

## Progress

| Date | Step completed |
|---|---|

---

_This file is finished when the north star exists and the owner has run one week without adding anything. Then it moves to the archive and stays listed in the focus layer's CONTEXT file._
_LOG: created from https://github.com/arete-aios/aios . Update this line with the date whenever the script itself changes._
