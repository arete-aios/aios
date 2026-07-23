---
name: ads7
description: "ADS7: a change protocol for live ad accounts: measure first, protect what already works, build the new thing beside the old, verify 48 hours later. Use before any edit to running ads."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "2.0.0"
  source: ads7
  synced: "2026-07-23"
---

# SKILL: Manage live advertising accounts

**Trigger word: `ADS7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Operating mode** needs access to at least one ad platform. The AI reads the account itself and, with approval, changes it.
**Advisory mode** needs nothing but numbers the owner pastes in. Same steps, same rules, the owner clicks.

Start in whichever mode today allows. Moving from advisory to operating later changes who presses the button, not the method.

Read only access covers most of what this skill does, so ask for that first. Write access is a separate step, gated in HOW IT RUNS below.

| Platform | Needed | How to connect |
|---|---|---|
| **Google Ads** | required if the account runs there | [developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) |
| **Google Analytics 4** | strongly recommended | [developers.google.com/analytics/devguides/reporting/data/v1](https://developers.google.com/analytics/devguides/reporting/data/v1) |
| **Google Tag Manager** | recommended | [developers.google.com/tag-platform/tag-manager/api/v2](https://developers.google.com/tag-platform/tag-manager/api/v2) |
| **Meta Ads** | if the account runs there | [developers.facebook.com/docs/marketing-apis/get-started](https://developers.facebook.com/docs/marketing-apis/get-started) |
| **TikTok Ads** | if the account runs there | [business-api.tiktok.com/portal/docs](https://business-api.tiktok.com/portal/docs) |
| **LinkedIn Ads** | if the account runs there | [learn.microsoft.com/linkedin/marketing](https://learn.microsoft.com/en-us/linkedin/marketing/) |
| **Microsoft Advertising** | if the account runs there | [learn.microsoft.com/advertising/guides](https://learn.microsoft.com/en-us/advertising/guides/) |

Not a platform but needed anyway: **any HTTP client**, to read the status code of the pages the ads point at. With one, step 4 runs by itself. Without one, the owner does that check by hand.

**Check your connectors before you write code.** Several of these now arrive as MCP servers or as ready connectors inside AI clients, which is a connect and approve step rather than a build step. Look at what your client already offers, then fall back to the platform's own API. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Inside your own system you need two places to write:** somewhere in the memory layer for the change log, and a task or calendar layer for the 48 hour check. If your AI cannot write to either, that is workable, but hand the owner both items as text at the end of every session and tell them it is now theirs to store.

**Setup time, honestly.** Minutes if your client already has a connector for that platform. An hour or two for a first OAuth setup you do yourself. **Days** if you need a Google Ads developer token, because that is an application with a human review at the other end. Start with whatever is already connected and add the rest later, rather than waiting for full access before doing anything.

**Without analytics you can see clicks and spend, but not whether anything happened afterwards.** You can still work in that state, and often will. What you cannot do is call the result an improvement: optimizing on clicks alone is how accounts get expensive and quiet at the same time. Say that limitation out loud in the same message where you report the numbers.

**If the owner does not want to connect anything, say so plainly and keep going.** With no access this skill still runs, as advice instead of operation. Ask them to export the last 30 to 90 days at ad group level and paste it in, run every step below on those numbers, and hand back a change list they click themselves, including the part that says what not to touch. In this mode step 4 becomes a request: give them the list of destination URLs and ask them to open each one and tell you what loads. The protocol is the value. The automation is convenience.

---

## WHAT

**This skill exists so an AI operating system knows how to run advertising, not just how to edit it.**

A connected AI will do its best with whatever it is shown. Shown one ad, it optimizes that ad. That is the failure mode. With these instructions it knows there are usually better moves than the one in front of it, and it says so: it asks for more data, goes one level deeper than the question, and looks at the whole account before it touches a part of it.

**It exists because of a real failure.** An AI paused two ad groups it judged to be off target jargon. Those two carried 99 percent of the account's impressions. Traffic fell to zero and stayed dead for four days. The mutation ran correctly, the dry run was clean, everything was reversible. The error was in judgment about what may be touched: the only thing that worked was replaced by an untested hypothesis, and because the replacement looked smarter, the collapse looked like optimization.

An AI with write access to an ad account can wipe out all of its traffic in one clean, reversible, technically perfect operation. Everything below is written to prevent exactly that.

---

## GOAL

**Get the most out of the account against a goal the owner has named.**

The owner decides what the result is: a click, a conversion, or a cost per conversion. Your first job is to know which one, because the three lead to opposite decisions on the same data.

If the goal is cost per conversion, you also need **how many conversions** there are. A cost per conversion built on three conversions is noise wearing a number, and optimizing toward it will make the account worse with great confidence.

In advertising everything is data, and data with no goal attached produces detail work: small, defensible, endless improvements to things that were never the constraint. So before optimizing anything:

1. **Take the goal from the owner's constitution and memory if it is already there.** In an AIOS it usually is, written as a business target rather than an ad metric.
2. **If it is not there, ask.** One question, answered once, then written into memory so it is never asked again.
3. **Never assume silently.** If you had to guess, say which goal you assumed and what you would have done differently under the other two.

---

## TRIGGER

- The owner says `ADS7`, or asks about ads, campaigns, budgets, keywords or conversion tracking.
- **Any change to a live ad account**, whether the owner asked for it or you proposed it.
- **Changes that do not look like ad changes but are:** deleting a landing page, changing a URL, taking a form offline, unpublishing a site. If a live ad points at it, it is an ad change. You will hear about these in conversation rather than from a system, because the site and the ad account are almost never connected to the same AI. That conversation is the trigger, so listen for it in threads that are not about ads at all.

**Not a trigger:** reading reports and answering questions about performance. Reading is free and should never wait for a gate.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

The layers are not decoration here. **An ad account is one of the few places where a mistake spends real money in real time**, and almost everything you need to avoid that already lives in the owner's own system rather than in the ad platform: which business goal the spend serves, what the pages the ads point at actually are, who is allowed to approve a change, what was tried before and failed.

**Read the owner's constitution and memory before the ad platform.** In particular look for anything about their website: where it is hosted, who can publish, whether pages can be removed, and which pages are already receiving paid traffic. Ads and the pages they land on live in two different systems and break each other constantly, and the owner's system is usually the only place where both are visible at once.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central advertising is to the owner.

**Runs ads most weeks:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
ADS7. Before any live ad change: measure at ad group level, protect anything carrying 10 percent or more, build the new beside the old, never pause what works, apply only with my OK, check at 48 hours. Spec: skills/ads7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

Keep a change log in the memory layer, one entry per session: **date, what was measured, which groups were protected, what changed, and the path back.**

Store the **raw before numbers**, not a summary. In two weeks the argument will be about whether the account was better before, and a summary cannot settle it.

Write the named goal there too, the one from GOAL above, so the next session starts from it instead of asking again.

Put the 48 hour check into the owner's task or calendar layer at the moment you apply. An unscheduled follow up is not a follow up.

### TOOLS

What to connect is listed in REQUIRES above and is not repeated here. What belongs here is the naming, because it moves fast and the owner will hear all of it.

The layer is called **Tools** because a tool is what the model finally calls. How that tool arrives keeps changing: today it is usually an **MCP server** or a **connector** the client installs for you, before that it was a hand written API wrapper, and all of them end up as tools in front of the model. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Measure what carries the traffic before writing any plan.** Always at ad group level, because account totals hide the fact that one group is the whole business. Write the answer as one sentence: *X percent of the traffic comes from N groups, and they are these.* If you cannot write that sentence, you are not ready to change anything.

**2. Mark the untouchables out loud.** Any group delivering 10 percent or more of impressions or clicks is protected for the whole session. Name them to the owner before continuing, so both of you know what is off the table.

**3. The hard rule.**

> **Never replace what is producing results with something untested. A new hypothesis is a new ad group or campaign, built beside the existing one, never in its place.**

Switching the old thing off is the last step, not the first, and it needs evidence: not "this looks off target", but data showing it fails while the new thing already performs better live. Until the replacement proves itself, the old one stays on. Overlapping traffic costs less than zero traffic.

If the rule feels like it is in the way, you are about to switch off something that works, which is exactly the case it was written for. Ask the owner.

**4. Check the destination of every ad you keep or enable.** Request the final URL and read the HTTP status. A 404 gets the ad disapproved and the group dies quietly, which is how the original failure got worse: a page system was deleted and the best performing group went down with it.

**Deleting a page is an ad change.** You will usually not have access to the site itself, so you cannot prevent a deletion, and this step is not asking you to. What you can do is the part that actually failed last time: keep the current list of live destination URLs where the owner can see it, and say the rule out loud whenever pages, forms or URLs come up in any conversation, including ones that have nothing to do with ads. If you do have access to the site, check for a live ad before anything is unpublished.

**5. Dry run, then show the diff:** what you will enable, disable, modify, and **what you are deliberately leaving alone**. That last part matters most, and it is the part every tool omits.

**6. Apply only with the owner's explicit approval**, read the state back immediately, then check impressions at 48 hours. Down more than 30 percent: revert first, analyze afterwards. Never click the ads yourself to test them, invalid clicks can get the account suspended.

**7. Zero data is not proof of a defect.** A second real failure: the AI declared tracking broken three times because analytics showed zero events. The tracking code was present, the tag manager installed, there was simply no event tag, and no click had ever converted. Before calling anything broken, run three cheap checks: is the thing you want to add already in the code, has the event ever happened at all, and does the instrument even measure it. **Zero means "I do not know", not "it is broken".**

---

## DEFINITION OF DONE

Every change to a live account leaves four things behind:

1. A **before and after** table.
2. A **named list of what was deliberately not touched**.
3. The operations performed, **with a path back**.
4. A **scheduled check 48 hours out**, with the number at which you revert.

Missing any of the four means the change is not finished.

---

## MAKE IT YOURS

1. **Set the protection threshold, then use that same number everywhere.** Ten percent suits a small account. A large one with many ad groups may want five. Whatever you pick, change it in the constitution line above as well, so the rule the AI reads and the rule it follows are the same number.
2. **Agree the compliance floor once** if the account has one, such as a grant account's required click through rate. Mention the risk once when planning, then execute without raising it again.
3. **Decide the reading boundary in advance.** Which reports, dry runs and checks the AI may run on its own without asking, so the owner is not approving the same harmless query every week. This does not move the write gate: a change to a live account waits for a person, every time, and that one is not configurable.
4. **No API access at all?** Run the same steps on exported reports, hand the owner a click by click change list including the do not touch section, and put the 48 hour check in their calendar. The discipline saves the account, not the automation.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [fulldigital.me/aios/skills](https://fulldigital.me/aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
