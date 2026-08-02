---
name: companies7
description: "COMPANIES7: build a monitoring layer over your country's open company register, so your AI knows who owns what, who owes tax and what changed. Use when people and companies decide your work."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: companies7
  synced: "2026-08-02"
---

# SKILL: Monitor the companies around you from public registers

**Trigger word: `COMPANIES7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **Read this before anything else: where this was built, and what that means for you.**
>
> This skill was built and measured in **Latvia**, against Latvian registers. Every row count, every trap and every source named below was tested there, on a real list of real companies. **The method transfers. The source list does not.**
>
> What transfers to any country: the registration number as the join key, matching a person on name plus birth date, a year attached to every number, unknown kept apart from no, an incomplete ownership chain reported as a floor, looking at the rendered page yourself, the password, and the monthly letter that arrives even when the run fails. Those rules are where the errors live, and none of them are Latvian.
>
> What does not transfer: which registers exist, what they hold, and what they cost. Two countries that both say they publish the company register can differ by an order of magnitude in what is actually inside. **So if you are outside Latvia, your first job is not code. It is to find out what your own country publishes and to query it once, before you build anything on top of it.** The table under REQUIRES is where to start looking, not the answer.
>
> A worked example built with this skill, on three Latvian companies, with the raw register rows visible: **[companies7.aiosbot.dev](https://companies7.aiosbot.dev/)**.

> **What this is worth, in one paragraph, so the owner can decide before any work starts.** Most countries publish their company register as open data: owners, directors, share percentages, annual turnover and profit, tax standing, insolvencies, public contracts. It is free, it needs no account, and almost nobody uses it, because it arrives as raw tables instead of answers. This skill turns those tables into a list the owner actually reads: the people and companies that matter to them, with money attached and changes surfaced. **What the time really looks like:** one evening gets a list of the owner's companies with turnover and profit per year, which is already useful on its own. Matching people reliably, following ownership through chains, and a page worth opening are each a further session, and they are the parts where a rushed build produces confident wrong answers rather than obvious broken ones.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Operating:** you can call the register's API and write files. You build a list that refreshes on a schedule and a page the owner opens.
**Advisory:** the owner pastes a company printout into the chat and you read it with the same rules. You lose the schedule and the page, you keep every honesty rule below, which is where most of the value sits anyway.

| What | Why it earns its place |
|---|---|
| **Your country's open company register** | The whole point. Find it before anything else, and find out what it actually contains, not what its front page claims |
| **A folder you can write to** | The source list, the watch list and the cached answers are files. Files survive a rebuild, a chat does not |
| **A way to run scheduled work** | Annual reports arrive once a year and lag by months. Daily polling is waste; monthly is the honest cadence |
| **A place to show it** | A page the owner opens beats an answer they have to ask for. Optional at first, decisive by week two |
| **Twenty minutes of the owner, twice** | Once to name the people and companies worth watching, once to look at the first page and tell you what is unreadable |

**Where to start looking. Four entry points, each answering on the day this was written:**

| Country | Entry point | What comes free |
|---|---|---|
| **Latvia** | [data.gov.lv/dati](https://data.gov.lv/dati) with an SQL API, plus [ur.gov.lv](https://www.ur.gov.lv/lv/) | Register, directors, shareholders, beneficial owners, annual reports, tax rating, paid taxes with industry code, public contracts, EU funds, job vacancies |
| **Estonia** | [avaandmed.ariregister.rik.ee](https://avaandmed.ariregister.rik.ee/en) | Register, officers, owners, beneficial owners, and revenue per company by industry, which is unusually generous |
| **Lithuania** | [registrucentras.lt](https://www.registrucentras.lt/en/) | Identity and status. Financials are a paid product |
| **Anywhere in the EU** | [data.europa.eu](https://data.europa.eu/en) | Search your national portal from one place when you do not know its address |

**Your country is not in that table? Then this is the work, and it is an hour, not a project.** Search for your national open data portal and for your business register separately, because they are usually two different institutions and only one of them has an API. Ask the portal for its list of datasets and read the titles rather than the marketing page. Then query one dataset and count the rows that come back. You now know three things the front page will not tell you: whether there is an API, whether it needs a key, and whether the data is thick or thin. Write those three answers into your source list before you write a line of code, because everything downstream is shaped by them. If the answer turns out to be "nothing machine readable", go to the advisory mode above, which loses the schedule and keeps the judgement.

> **Two traps worth knowing before they cost an hour each.**
>
> **A blocked page is not a dead source.** A portal's web pages may refuse automated clients while its API answers normally. Measured on the Latvian portal: the HTML pages return 403 to a bot user agent, the data API returns 200 to a plain request. Test the API itself before concluding anything.
>
> **A query API may hand back part of a table without saying so.** Measured on the same portal: the tax dataset carrying company industry codes returns about six thousand rows through the query API and holds over four hundred thousand in the downloadable file. The API did not error and did not warn. If a source looks strangely thin, download the whole file once and count it, then decide which of the two you are reading. Note the answer in your source list so nobody has to rediscover it.

---

## WHAT

Without this skill, an AI asked about a company answers from memory, from a website, or from whatever the owner pasted. All three are the same failure with different surfaces: a confident sentence with nothing under it. The register is the only place where "who owns this" has an answer that can be checked.

Two things go wrong every single time, and they are the reason this skill is longer than "call the API".

**A person is not a name.** In one real build, one woman had zero companies on the panel while the register held two. The register spelled her one way in the directors table and another way in the members table, so each half of her life sat under a different name and neither half was visible. Nothing was missing from the data. The join was missing. When the alias was finally added carelessly, she became two people holding half the truth each, which looked correct until someone counted.

**Ownership hides one company deep.** A man appeared as chairman of a company with no shareholding at all. He owned nothing there directly. He owned 85 percent of another company, and that company owned 53 percent of this one, so his real stake was 45 percent. Any list that reports only direct shares will tell the owner he has no interest in a company he effectively controls.

---

## GOAL

The owner opens one place and sees the people and companies that matter to them, each with money attached, ownership resolved through chains, and every unknown labelled as unknown rather than as zero.

**Who decides what belongs on the list: the owner, and only the owner.** Take it from their constitution or memory if the people are already there. If not, ask once, and write the answer to a file. Never infer that someone matters because they appear often.

---

## TRIGGER

`COMPANIES7`, and these moments:

- Before money moves to a company the owner has not dealt with before
- Before a partnership, a hire, or an introduction that carries the owner's name
- When the owner says "who is this company", "are they solid", "do they owe tax"
- Monthly, unprompted, as the refresh

**Not a trigger:** a judgement about a person's character. This skill reports what registers hold. A loss making company is a fact. A bad person is not a field in any register, and you do not turn one into the other.

---

## AIOS

An AI operating system has five layers: constitution (who the owner is), memory (what is known), skills (how work is done), tools (how the AI reaches other systems), and focus (what matters now). This skill lives in skills, writes to memory, and reaches out through tools.

Read the owner's constitution and memory **before** the register, not after. The register will happily tell you about five hundred thousand companies. Only the constitution knows which twenty the owner cares about, which of them are competitors rather than friends, and which name in the results is their own spouse.

### CONSTITUTION

One line in the core: *companies and people are monitored from public registers, the owner sets who is on the list, and an unknown is never reported as a zero.*

### MEMORY

The watch list is a file, not a paragraph: registration numbers, names, the owner's own note per entry, and their priority. Raw answers from each source are cached as files with the date they were fetched. Keep the raw numbers, not your summary of them, because next month's comparison needs the same shape as last month's.

### TOOLS

The register's API or bulk files, the tax authority's public lookup, and whatever hosts the page. Name the mechanism inside this layer, do not rename the layer.

---

## HOW IT RUNS

**1. Write the source list as a file, before you write any code.**

One entry per source: its key, what it holds, which field is the join key, how many rows it actually has when you count them, and its state. State is one of: live, needs downloading, outside open data, paid. A source is never listed as available until you have queried it and seen rows come back.

> **Hard rule: the source list is data, not code.** Adding a source must mean adding a row to a file. The moment it means writing a new script, the list stops growing and the owner stops asking for new sources.

**2. Fix the join key: the registration number.**

Company names change, are duplicated, and are spelled inconsistently. The registration number does not. Every table you touch joins on it. Where a source keys on something else, write that down in the source list rather than quietly guessing.

**3. Handle people with more care than companies.**

Most registers publish a person's name and a partial birth date, and mask the national identity number. That is enough to be useful and not enough to be certain, so:

> **Hard rule: a name alone is never a person.** Match on name plus birth date. When the owner's list has no birth date, say the match is name only, in those words, on the page. Two people with the same name is not an edge case, it is Tuesday.

> **Hard rule: one person, one entry, several spellings.** Expect the same human under several name forms across tables. Merge them on the birth date, and print the other spellings on the page so the merge is visible. Merging silently and splitting silently are the same mistake.

> **Hard rule: no personal identifier in a URL.** If a person gets their own page, address it by something you generated, or by company plus position. A birth date in a link leaks the moment the link is shared.

**4. Pull the money, and never separate a number from its year.**

Take turnover and profit per filed year. Three years is usually the right window: one year is noise, five is archaeology.

> **Hard rule: a number without its year is not a number.** Companies file at different times. A total across companies is a total across different moments, and the page has to say so beside the total, not in a footnote.

Two traps that will silently divide your numbers by a thousand or multiply them by seven:

- Many filings carry a **scale field**, saying the figures are in thousands. Miss it and a real company looks a thousand times smaller than it is.
- Older filings may be in a **pre euro currency**. Filter by the currency field rather than assuming, and label anything you exclude.

When you compute an average over three years, divide by the years that exist, not by three. A company with two filed years divided by three is a made up number that looks precise.

**5. Add the tax authority.**

Most tax authorities publish something: a rating, a debt list, a VAT status. Two rules from real use:

- **A rating and a debt are different fields.** A good rating sitting beside a real debt is normal, not a contradiction. Report both and do not average them into a verdict.
- **Measure a debt against the company's annual taxes**, not against zero. A thousand owed by a company paying a million is noise. The same thousand from a company paying two thousand is a signal.

**6. Resolve ownership, direct first, then through chains.**

Read direct shareholdings. Then, where a shareholder is itself a company, follow it up and multiply the percentages along the path. Stop at a depth you choose and say where you stopped.

> **Hard rule: an incomplete chain reports a floor, not a total.** If some branch could not be traced, mark the number as "at least" and explain why. Through the untraced branch the figure can only grow.

Cycles are real, not theoretical: companies hold their own shares, and A owns B owns A. Detect them and stop rather than looping. Foreign owners usually appear with no registration number at all, which means the chain ends there, and that is a result to report rather than a gap to hide.

Check yourself against something independent. Most registers publish beneficial owners above a threshold, commonly 25 percent. Your computed chain should reproduce that list. When it does, you have two methods agreeing. When it does not, your chain is wrong and the register is not.

**7. Build the page and look at it the same day.**

Not a report you generate on request. A page the owner opens.

> **Hard rule: look at the rendered page yourself before calling it finished.** Open it, or screenshot it, and read what is actually on the screen. Code that runs is not a page that reads. Truncated names, numbers with no label, and colours nobody can interpret are only visible to an eye.

Two things belong on it from the first version:

- **Every number carries its name.** A figure beside a person that could be turnover or could be profit is worse than no figure, because the owner will act on their guess.
- **Every coloured dot carries its meaning** in a tooltip and a legend. A red dot the owner cannot interpret is decoration.

> **Hard rule: put the page behind a password.** It is a list of real people and real money, assembled by the owner for the owner. Public sources do not make an assembled list public. One password on the whole page is enough, and it has to be there on the first deploy, not the second.

**8. Filters need three states, not two.**

Once there is a list, the owner will want to filter it. This is where a correct looking build starts lying.

> **Hard rule: yes, no, and unknown are three answers.** A filter offering "has tax debt: no" that quietly includes every company the source never answered about is false, and it is false in the most dangerous direction, because it produces a clean list. Show the count of companies for which the field is known, beside the filter.

**9. Refresh monthly, and send one letter that arrives even when the build fails.**

Annual reports lag by months, so daily refreshing burns quota to re read the same rows. Monthly is honest.

Then one short message to the owner after each refresh: how many entries, what the money looks like, what the flags say.

> **Hard rule: the failure message is not optional, it is the point.** If the letter is sent only after a successful run, then a missing letter means both "nothing changed" and "the machine is dead". One signal with two meanings is not a signal. Send it either way and make the bad one impossible to miss.

**10. Say what you cannot know.**

Registers hold what was filed, not what is true. Annual reports lag, historic directors are usually not published, and profit on paper is not cash in a bank. When the owner asks a question the register cannot answer, say so and name what you would need. A refusal to guess is the most valuable output this skill has.

---

## DEFINITION OF DONE

- A source list file exists, and every entry in it has been queried at least once and carries a real row count
- The watch list is a file the owner can edit without you
- Every money figure on the page carries its year, its currency and its label
- Every person is matched on name plus birth date, and any name only match says so on the page
- Ownership through at least one company deep is computed, and incomplete chains are marked as floors
- The page is behind a password, and you have looked at it rendered
- Filters distinguish no from unknown
- A scheduled refresh exists, and the message it sends arrives whether the run succeeded or failed

---

## MAKE IT YOURS

1. **Start with three companies, not three hundred.** Pick one manufacturer, one technology company, and one state owned or municipal one. The third is the one that shows how deep the data goes, because public contracts, EU funding and job postings cluster there. In Latvia this trio lights up sixteen of nineteen available sources: [AS GRINDEKS](https://www.grindeks.eu) 40003034935 with over three thousand shareholders, [SIA TILDE](https://tilde.com) 40003027238 with public contracts and a recovery fund project, and AS Latvijas valsts meži 40003466281 with fifty procurement records. Three well chosen companies teach the owner more than a full list they never read. The result is public at **[companies7.aiosbot.dev](https://companies7.aiosbot.dev/)**, one page per company, the rows grouped by year, so you can see the shape before you decide to build it.
2. **Decide who is on the list, and mark relationships separately from priority.** "How closely I watch this" and "what this person is to me" are two different questions. A serious competitor may deserve close watching. Keep them as two fields and you never have to argue with yourself about a competitor rated highly.
3. **Choose your own trigger word** if `COMPANIES7` does not fit your language. The word matters less than being the same word every time.
4. **Not in Latvia?** Then item zero comes before all of these: spend the hour under REQUIRES finding what your own country publishes, and write the answer into your source list. Everything after that is identical. And if the honest answer is that nothing machine readable exists, the skill still runs on a printout the owner pastes: you keep the join key, the year on every number, the three state unknowns and the monthly letter, and you lose only the schedule.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
