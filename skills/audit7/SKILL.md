---
name: audit7
description: "AUDIT7: two read-only audits of your AI operating system, the machinery and the library, alternating so both are covered monthly. Use when nobody has checked what loads, costs or leaks."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: audit7
  synced: "2026-07-23"
---

# SKILL: Audit the system you are running on

**Trigger word: `AUDIT7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **Two passes, one skill.** Pass one is **the machinery**: what loads, what it costs, what still answers, where the holes are. Pass two is **the librarian**: whether the content underneath is honest. One pass every two weeks, alternating, so both are covered monthly. Never both in one sitting, the second one gets skimmed.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**With access:** you read the files, configuration and connector list yourself, and test every tool with a live call. This is the audit, and it finds what nobody would have thought to mention.
**Without access there is no audit, only its preparation.** You cannot test a tool you cannot call, and reading the pasted tools file is exactly the document review this skill exists to replace, so do not name it one. Turn the paste into a numbered checklist of live tests the owner runs on their own machine, hand it over, and let the audit happen when they run it. The word is earned by the live call, not by the paste.

| What | Why | Where |
|---|---|---|
| **Read access to the content folder** | Pass two is impossible without it | Whatever your client already reaches |
| **A token counter** | Turns "the core feels heavy" into a number | [token counting](https://docs.claude.com/en/docs/build-with-claude/token-counting) · [tiktoken](https://github.com/openai/tiktoken) |
| **The client config and connector list** | Where tools and auto-approvals actually live | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| **Whatever runs scheduled jobs** | A job that died three weeks ago is the classic finding | [crontab reference](https://man7.org/linux/man-pages/man5/crontab.5.html) |
| **A secret scanner, optional** | Faster than reading every file for keys in plain text | [gitleaks](https://github.com/gitleaks/gitleaks) |
| **A published risk list** | So security is checked against more than your imagination | [OWASP Top 10 for LLM apps](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |

**Setup time, honestly.** Nothing to install if you can already read the system. The run is the cost: **30 to 50 minutes on the strongest model available, maximum thinking, parallel agents if your tool has them.** Say that number before starting. A five minute audit is a skim, it comes back mostly clean, and false confidence about security is worse than no audit. Add fifteen minutes of the owner's attention at the end. The first run is the longest and returns the most.

---

## WHAT

**A system like this grows by accretion, and nothing in it announces that it stopped working.**

The always loaded core gains one reasonable line at a time, and it is the only thing the owner pays for on every message. Skills get written, used twice, never fire again. Tools get connected once, then a machine is rebuilt, a key expires, an API changes, and the connection dies quietly.

**The failure worth naming is the tool that keeps answering after it has died.** A health integration returned the last known measurement instead of that day's. Nothing tested it, so a stale number went into a trend and the AI reported a two week improvement that never happened. The arithmetic was right. Nobody had asked the instrument whether it was still measuring. Every dead integration either goes quiet, which gets noticed, or repeats itself confidently, which does not.

**Without this skill an AI audits by asking.** It reads the tools file, reports what that file claims is connected, and calls it a status. That is a document review wearing the word audit. The difference here is a live call against every tool and a real number against every file.

---

## GOAL

**An honest page the owner can act on, and a system in exactly the state it was in before the run started.**

After a machinery pass the owner knows the number that loads on every message, which skills went cold, which tools answer today, and where the holes are. After a librarian pass they know which folders lie about their contents and which layer has drifted.

Both end the same way: one line per item, then one list of what to merge, archive or rewrite. Nothing is fixed during the run.

---

## TRIGGER

- The owner says `AUDIT7`, optionally naming which pass.
- **The rhythm: one pass every two weeks, alternating.** Machinery, then the library, then machinery. Monthly coverage of both without a long day nobody schedules.
- **After anything structural:** a machine rebuild, a move to a new client, a large import, a tool migration. Rebuilds are the most reliable producer of dead integrations there is.
- **When the AI said something confidently wrong** and the cause was a stale file or a tool that was not really connected.

**Not a trigger:** one folder needing its index fixed during normal work. Fix that there, one line, same session. This skill walks everything and touches nothing, the opposite job. Also not a trigger: the urge to tidy. Tidying is not measurement, and it destroys the evidence measurement needs.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

An audit has no external standard, so it measures the system against **what it promised itself**. The size budget, the approval gates, the map of which layer holds what, the one index per folder rule: all of it is in the owner's constitution, and that is where a finding has to come from. **Read the constitution first and quote its own numbers back at it.** An audit that invents its own standards produces opinions, and opinions get argued with instead of fixed. Memory carries the other half, the previous runs. One audit is a snapshot, three show whether the core is growing.

### CONSTITUTION

This fires on a rhythm rather than in conversation, so do not spend always loaded context on the method. Put the line in the skills index the core already links to. **What does belong in the core is the budget number this audit measures against**, because a ceiling nobody can see is not a ceiling.

```
AUDIT7. Every two weeks, alternating: machinery pass, then library pass. Read only, test every tool live, propose everything, change nothing during the run. One line per item, OK or the finding, ending in one MERGE / ARCHIVE / REWRITE list. Spec: skills/audit7.md
```

### MEMORY

**One dated report per run, kept, never overwritten.** The trend is the product. Store raw numbers, tokens per file and the actual response or error from each tool test, not a summary saying things looked healthy.

**What never goes in: the value of any credential the security pass finds.** Name the file and its permissions, never the secret. Audit reports get pasted into chats and pushed to repositories, and a report quoting a live key has just published it.

**What rots:** the fix list once the fixes are done, and any conclusion about tool health older than a month.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. Today they usually arrive as **MCP servers** or **connectors** the client installs. Name the mechanism when you use one, and do not let it rename the layer.

> 🔒 **The whole run is read only, and so is every test.** Prove a tool is alive with the cheapest read it offers: list, get, status, whoami. Never send, post, deploy, pay or delete to prove a channel works. If a tool can only be proven by writing, mark it **untested** and say so. An untested line is an honest finding. A test message sent from the owner's account is a change, and this run makes none.

---

## HOW IT RUNS

> **PROPOSE ONLY, CHANGE NOTHING.** Not one file moved, renamed, merged or deleted during the run. Two reasons, and the second is the one that matters. An audit that fixes as it goes destroys its own evidence, so nothing can be verified afterwards. And the owner never learns what was wrong, so the same drift returns next month and the audit quietly becomes a cleaning service.

Steps for you, the assistant. Goal level, not code level. Parallel agents if your tool has them. With access you run these steps. Without it you cannot, so you turn each one into a check the owner runs and hand that over, because a step you cannot execute is a line in a checklist, not a finding.

### Pass one, the machinery

**1. Map what loads at session start and put a number on each file.** Tokens, not impressions. Then for each: lean or bloated, current or stale. Then the question nobody asks, **do any two of them contradict each other?** Two always loaded files disagreeing is the most expensive defect in the system, because the model resolves it silently and differently every time.

**2. List every skill and trigger word, then name the ones that never fire.** Unused for a month means either the trigger is missing from where the AI actually reads triggers, or it was never a skill. Both are findings, and their fixes are opposites.

**3. List every connected tool and test each one live.** MCP servers, APIs, scheduled jobs, channels. Flag four things: jobs failing silently, expired credentials, channels nobody has spoken in, and tools connected but never once used. **Asking the tools file what is connected is not a test.**

**4. Find the holes. This is the section owners skip and the one that costs most when it is wrong.** Four questions, answered concretely:

- **What can reach this system from outside?** Open ports, tunnels, webhooks, bots that accept a message from any sender. Anywhere a stranger's text lands in the model's context is an instruction channel, not an input field.
- **Which credentials sit in plain text?** File and permissions, never the value. Include config files, environment files, backups and old exports.
- **Which tools can write or send outside without approval?** For each, name what actually stops it: a written gate, a client setting, or nothing. "Nothing" is common and always worth a line.
- **Which scheduled job runs unattended with the widest permissions?** That is the one that will send the wrong thing while everyone is asleep.

Then name **one** thing to tighten first. A list of twelve gets nothing tightened.

**5. Compare with what people publicly build today** and name up to three things this system lacks. For each, say which finding from steps 1 to 4 it would have prevented. If it prevents none, it is novelty.

### Pass two, the librarian

**6. Walk every folder holding more than a handful of files.** Each must have exactly one index. Flag three things: folders with none, folders with two, and orphan files listed in no index. An unlisted file is invisible to the AI no matter how good it is.

**7. Measure every always loaded file against the budget the constitution itself states.** Against that number, not your judgment. Then flag stale dates, finished projects still written as live, and any statement a newer file contradicts.

**8. Check all five layers, present, findable, current.** The defect to hunt is **leakage**: identity written into memory, dated events written into the constitution, a method living inside a project file, a tool documented in three places.

**9. Check the focus file against reality.** Dead dates, finished work still listed, and the harder one, real work in progress the focus file has never heard of. That gap is what makes an AI plan around a life the owner is no longer living.

### Both passes

**10. Report one line per item: OK, or the finding.** Not a paragraph per folder. The owner is scanning for the lines that are not OK, everything else is noise around them.

**11. End with one list, split MERGE / ARCHIVE / REWRITE, one line each.** One list, not one per section, because a fix list scattered across five sections never gets executed. Then stop. The fixes are the next session's work, item by item, with the owner's approval.

---

## DEFINITION OF DONE

1. **A dated report**, one line per item, each either OK or carrying a specific finding.
2. **A number on every always loaded file**, and a total against the stated budget.
3. **A live test result for every tool**, including the ones marked untested and why.
4. **The security section answered concretely**, locations rather than values, with one thing named to tighten first.
5. **One MERGE / ARCHIVE / REWRITE list** at the end, and nothing after it.
6. **A system in exactly the state it was in before the run**, and a date for the next pass, which is the other one.

Missing the third means you reviewed a document. Missing the sixth means you did maintenance and called it an audit. Without access you deliver none of the six, only the checklist that lets the owner produce them, and you call it a checklist, not an audit.

---

## MAKE IT YOURS

1. **Set the always loaded budget before the first run**, in tokens, written into the constitution. Without a number every audit reports the same soft finding, that the core is getting large, and nothing ever crosses a line.
2. **Decide which reads run unattended.** Listing files, counting tokens and calling a status endpoint should never need approval. The read only rule for the run itself does not move.
3. **Put the alternating dates where they will be seen.** In the calendar, not in an intention. An audit whose trigger is remembering it exists happens roughly once.
4. **Match the security questions to the surface that exists.** A laptop with two connectors and a server taking messages from strangers deserve different lists.
5. **Keep the passes separate even when the first one is short.** Finishing both while the context is warm is how the librarian pass turns into a skim, and content drift is the slower and more expensive failure.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
