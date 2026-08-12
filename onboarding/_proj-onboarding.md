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
    harvest-<date>.md      everything recovered from this account's own history, if there is any and they want it kept
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

## Step 1: what you already know about them

Some owners open a fresh account for this. Then there is nothing to harvest, and that is a clean start rather than a disadvantage. Say so in one line and go to Step 2.

Others have been talking to an assistant for months or years. **That history is the richest source you will ever get from this person, it costs them nothing to produce, and almost none of it has ever been written anywhere they can read.** It is also the only source that shows what changed, because it was recorded as it happened rather than remembered afterwards.

### First, say what you can actually reach

Before you extract a single line, tell them plainly which of these you have, and name the ones you do not:

- Saved memories, the short facts the product keeps about them.
- Past conversations, if this product lets you search or reference them, and whether that setting is switched on.
- Files, projects or documents already sitting in this account.
- Nothing at all, which is the honest answer for several products and settings.

**Then the rule that makes this step safe rather than dangerous.** You have no memory of your own beyond what the product hands you right now. If you cannot read past conversations, say that sentence and move on to Step 2. Do not reconstruct a plausible history. Do not write "I recall you mentioned" about anything you did not just read. **An invented memory handed back to the owner is worse than no memory at all**, because they will believe it, it will go into their files, and it will still be there in a year, shaping advice, with nothing to trace it back to.

### Extract properly, which means more than one pass

Do not stop at the first pile you find. One sweep returns the loudest material and misses most of it. Run repeated passes, each from a different angle, because each angle surfaces what the others cannot see:

- By area of life: work, money, health, family, home.
- By name: every person they have mentioned more than once.
- By project or product name.
- By problem that keeps returning.
- By decision, especially reversed ones.
- By number: prices, weights, counts, dates, deadlines.
- By period: what was being discussed six months ago and is never mentioned now.

**Keep going until two passes in a row return nothing new.** Then say how many passes you ran and what the last one added, so they can see whether you actually reached the bottom or ran out of patience.

Four rules on how you record it:

1. **Quote, do not paraphrase.** A sentence in their own words is evidence. Your summary of it is an interpretation, and interpretations cannot be checked.
2. **Date everything, or say the date is unknown.** An undated fact cannot be aged, and a fact that cannot be aged never gets retired.
3. **Record contradictions, do not resolve them.** If March says one thing and October says another, write both with their dates and put them together. **That pair is the single most valuable thing in the whole harvest**, because it is the only reliable way to tell what has changed rather than what was said loudest.
4. **Keep the weak signal separate.** Something said once and never again is not the same as something said every month. Both are worth having, and mixing them destroys the difference.

### Sort it into categories

Group everything into these, and drop any that come back empty rather than padding them:

1. **Who they are and what they do.**
2. **Work, business and clients.**
3. **Money:** prices, income, costs, anything with a currency on it.
4. **People, by name,** and what the relationship appears to be.
5. **Health and body.**
6. **What keeps coming back:** the problem raised in five different months.
7. **Decisions already made,** with dates, including the ones later reversed.
8. **How they want an assistant to behave.** Every correction they have ever given you: what annoyed them, what they asked you to stop doing, what they said was wrong. **This category is the most useful one in the list and the one nobody expects**, because it is the raw material of their constitution and it was written by them, over months, without being asked.
9. **Tools and systems they already use.**
10. **Said once, never again.** The weak signal, kept apart on purpose.
11. **Contradictions and changes,** with both dates.

### Two outputs, and they are not the same thing

**Ask before you write the full file.** A complete dossier assembled from someone's own chat history is a strange thing to meet for the first time, and some people will not want it to exist. Show them the categories and the rough size first, then ask whether to save all of it, only the parts they confirm, or none of it. Any of the three is a complete answer.

If they say yes:

- **The file holds everything.** `harvest-<date>.md` in the memory folder, nothing trimmed for length, quotes intact, dates intact, contradictions intact. This is an archive, not memory. Nothing in it is true yet.
- **The chat holds only what matters.** Category by category, the short version. Do not paste the file into the conversation. They asked for their system back, not for a transcript.

### Then confirm it, category by category

This material was found, not told, so hard rule 3 applies to all of it: **it is unconfirmed until they say otherwise out loud.** Walk the categories and ask for one of three answers per item:

- Still true.
- Wrong, and it was always wrong.
- Was true, and is now out of date.

Only the first goes into memory. The second gets marked wrong **in the harvest file rather than deleted**, so that a later run does not cheerfully rediscover it. The third is the interesting one: it goes to memory as history with both dates, because knowing what someone used to be doing is how you notice a pattern later.

Anything they cannot answer goes to Open questions with today's date, not into memory.

---

## Step 2: the brain dump

If Step 1 found anything, this step changes shape. Do not ask them to empty their head from nothing. Say what you already have, then ask for **what is missing from it, what it got wrong, and what has happened since.** Correcting is easier and far more accurate than composing, and they have just watched you demonstrate how much is already there.

If Step 1 found nothing, run it as written below.

Say this, in your own words: for the next ten to fifteen minutes, empty your head into one file. Work, money, health, people, the thing you keep meaning to do, the thing you are avoiding, what you are proud of, what is broken. No order. No grammar. Voice dictation is ideal, and typos do not matter because I am reading for meaning, not spelling.

Offer three ways in, and let them pick:

- They talk or type here in the chat, and you write it into `braindump.md` unedited.
- They write straight into `braindump.md` themselves and tell you when to read it.
- They already have notes somewhere. They paste them, or point you at them.

While it is happening, do not organise, do not summarise back, do not ask clarifying questions, and above all do not turn anything into a task. A brain dump that generates obligations gets abandoned. Nothing in that file is a commitment until the owner explicitly says it is.

When they stop, read it once and say only how much you have and roughly which areas of life it covers. Then move on.

---

## Step 3: who they are on the internet

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

## Step 4: strengths and assets

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

## Step 5: write the memory layer

Now, and not before, turn what has been confirmed into files.

- Put the material into the memory folder, split by the areas of life it actually covers for this person. Do not impose a set of areas they did not use. If everything they said is about work and money, they get two areas, not seven.
- Every folder you create gets its CONTEXT file with both parts, the list and the rule, per the naming law above.
- The rule part is not decoration. Write the specific thing you should do differently in this area. If they told you their calendar is authoritative and their memory is not, that sentence goes in the rule.
- Leave the brain dump file in place, shrinking. Lines get removed as they find homes. It is not deleted at the end of setup, it is a permanent capture point.
- **The harvest file behaves the opposite way: it does not shrink and it is never edited down.** It is a dated record of what the account held on the day you read it, and its value is that it stays exactly as it was. Confirmed material gets copied out of it into memory, not moved out of it.

Then show them the tree of what now exists and ask one question: what is wrong with this shape. Fix what they name.

---

## Step 6: write the constitution

The folder has held an empty `CONSTITUTION.md` since the gate. Now it gets filled, and it gets filled from what has been confirmed in the five steps above rather than from a fresh set of questions.

**You write the draft. Do not interview them for it.** By this point they have already answered nearly everything a constitution needs: Step 1 recovered how they want an assistant to behave, in their own words, written by them over months of corrections. Steps 2 to 4 covered what they do, who depends on them, and what they have to work with. Asking those questions again after all that reads as though you were not listening. Show them a finished file and let them correct it.

**Category 8 from the harvest is the part to mine hardest.** Every time this person told an assistant to stop doing something, that was them writing a hard rule without knowing it. Those lines are worth more than anything they would produce by being asked "how do you want me to talk to you", because they were written while annoyed rather than while being polite to a form.

What goes in, following the AIOS shape:

- **Who they are,** in the few sentences that change what you do. Not a biography.
- **Who depends on them.** This decides most judgment calls later.
- **What you must never do without asking first.** Send, spend, delete, publish, or speak in their name. Write the permitted side too, or you produce an assistant that asks permission to read a file.
- **How they want to be spoken to,** including their language, and how much hedging they will tolerate.
- **What has gone wrong with an AI before that must not repeat.** Straight out of harvest category 8.
- **Where the other four layers live.** Pointers, not contents.

**The test for every line is one question: if I delete this, does the assistant behave differently?** If there is no answer, it is description, and description belongs in the memory layer where it loads only when it is relevant. Expect to cut a third of your own draft, and cut it before you show them rather than after.

**Layer one points, it does not contain.** The most common way these fail is that the constitution slowly absorbs the whole system. It does not hold memory, it says where memory lives. Anything dated, anything about one project, anything you would have to update more than a few times a year: that is memory, and the constitution keeps only the pointer.

Two things to finish with:

- **Say its size in tokens**, and say what that costs across a month, because this is the one file that is paid for on every single message.
- **Leave the north star line honest.** It is not chosen yet, and session three is where it gets chosen. Write that the north star is still open and point at this file, rather than inventing a mission statement to fill the gap. A borrowed north star in layer one is worse than an empty line, because everything downstream will quietly align to it.

Then prove it works. Start a fresh session and ask something only the constitution would let you answer. If it cannot, the file is in the wrong place, and everything built on top of it is sitting on nothing.

Full method, if they want to go deeper later: `skills/constitution7/SKILL.md`.

---

## Step 7: hand over

Tell them, in one short message, what happens next and why, then stop:

- **Next prompt: the completeness check.** You go back over the dump and the memory layer and find what is missing, because the first pass always misses things and a stranger's eye is the only way to see it.
- **The one after that: the north star.** You will put up three candidates pulled out of what they already wrote, they choose or reject all three, and the three priorities follow from whichever wins. It is also what decides which email account, which calendar, and which methods are worth connecting. Connections chosen without it are just apps.

Do not run those two yourself in this session, even if there is time. The gap is deliberate. Setup done in one exhausted sitting is setup that gets abandoned. The script for both is in the next section, written down so the session that opens this file knows what it is for.

---

## The two sessions after this one

> **Read this, do not run it.** The rest of this section is the script for the second and third sessions. It sits in this file so that whichever session opens it knows what it is for. Running it in session one, because there was time and it seemed helpful, is the one failure this whole file is shaped to prevent.

### Session two: the completeness check

Go back over the harvest, the dump and the memory layer, and look for what is missing rather than for what is wrong. The first pass always misses things, and it misses them in a predictable direction: whatever the owner did not think to mention because it is obvious to them.

Check specifically for the areas of life with nothing in them, the people mentioned once and never filed, the numbers with no date, the decisions with no outcome recorded, and anything sitting in Open questions long enough to have gone stale. Ask about those, and file what comes back.

### Session three: the north star

**Pull the candidates out of what they have already written.** This is not a visioning exercise and you are not there to inspire anyone. Everything you need is in the harvest, the dump and the assets list, and the owner's job is to recognise something rather than to invent it.

**Offer exactly three, and make them genuinely different.** Three wordings of the same ambition is not a choice, it is a leading question. The three that work:

1. **The obvious continuation.** Where the current work already points, done properly. Usually the safest and the least interesting to them, which is exactly why it has to be on the list.
2. **The one the material keeps circling.** The thing that turns up in five separate months and has never been said as a goal. This is the one the harvest earns its place for, and it is often the one that lands.
3. **The smaller, more certain version.** Clearly achievable, unglamorous, possibly being avoided for that reason. Put it up honestly rather than as a consolation prize.

For each of the three, give five things and nothing more:

- One sentence, in their words, of what would be true.
- By when.
- How they would know it happened, which has to be something observable rather than a feeling.
- What it costs: what they would have to stop doing to make room for it.
- The evidence. Name the lines in the harvest or the dump that point at it, so they can see this came from them and not from you.

Then say plainly that this is a proposal drawn from their own words, not a diagnosis, and that they can pick one, merge two, or reject all three. **Rejecting all three is a good outcome, not a failed session.** The rejection almost always names the real one, and it names it faster than any question you could have asked.

### Then, and only after one is chosen, the three priorities

Propose three, in order, and only three. Call them P1, P2 and P3: the first, second and third thing that gets attention when the week is short.

- **P1 is the one that makes the other two pointless if it stalls.** Usually money or health. The honest answer here is frequently not the exciting one, and saying so is part of the job.
- Each gets one sentence, one measure, and one date to check it.
- **Name the drop order now**, while nothing is at stake: if the week goes badly, which of the three goes first. A priority list with no drop order is a wish list, and it will be abandoned in the first bad week rather than deliberately reduced.
- Sequence them against the north star, not against how urgent they feel. Urgency is not a ranking, it is a mood with a deadline attached.

**Write the priorities into the focus layer, never into the constitution.** Priorities change every few months by design. The constitution is the file that is supposed to stay still, and a constitution that carries this quarter's priorities has to be rewritten every quarter, which is how it stops being read.

Last, go back to layer one and replace the honest empty line from Step 6 with the chosen north star, and note the date it was chosen. That date matters later: a north star nobody has looked at in a year is either finished or wrong, and both are worth knowing.

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
_2026-08-12: added Step 1, harvesting an existing account's own history, and Step 6, writing the constitution, which the script created at the gate and then never filled. Added the script for the second and third sessions, including three north star candidates drawn from the owner's own words and the three priorities that follow from the one they choose._
