---
name: site-lovable7
description: "SITE-LOVABLE7: rules for letting an AI manage a site built in an AI website builder, which path each change takes, what needs an OK, and a credit cap. Use before editing a live site."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: site-lovable7
  synced: "2026-07-23"
---

# SKILL: Let an AI manage a site built in an AI website builder

**Trigger word: `SITE-LOVABLE7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Operating mode** needs the builder account plus an AI client that can reach the builder's MCP server. You read the project, hand work to the builder's own agent, and deploy with approval.
**Drafting mode** needs nothing connected. You produce the exact page copy, the section structure, the prompt the owner pastes into the builder chat, and the checklist for preview and deploy. **The routing rules and the permission tiers pay off just as much when the human is the hands.**

Start in whichever mode today allows. Moving from drafting to operating changes who clicks, not which change is allowed.

| What | Needed | How to connect |
|---|---|---|
| **A builder account** | required for operating mode | [lovable.dev](https://lovable.dev) · docs: [docs.lovable.dev](https://docs.lovable.dev/) |
| **The builder's MCP server** | required for operating mode | [docs.lovable.dev/integrations/lovable-mcp-server](https://docs.lovable.dev/integrations/lovable-mcp-server). What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| **Credits** | required, every agent change spends them | [docs.lovable.dev/introduction/credits-and-usage](https://docs.lovable.dev/introduction/credits-and-usage) |
| **A paid plan, for a live custom domain** | required to ship on the owner's own address | [docs.lovable.dev/features/custom-domain](https://docs.lovable.dev/features/custom-domain) |
| **Direct database or CMS access** | optional, second and narrower path | [docs.lovable.dev/features/cloud](https://docs.lovable.dev/features/cloud). Reads data and edits existing text without spending credits |
| **A route out** | recommended to check on day one | [ownership and hosting](https://docs.lovable.dev/tips-tricks/deployment-hosting-ownership), so the owner knows how the code leaves if they ever want it to |

**Setup time, honestly.** Minutes if the AI client already lists the builder as a connector: connect, approve, done. An hour if you set the connection up yourself. The optional direct database path is a separate credential and a separate afternoon, and it is worth it only for a site that changes text often.

Free tiers exist for building. **A live site on the owner's own domain is a paid plan**, and every change the builder's agent makes costs credits that are real money. Say that before the first task, not after the first invoice.

**Where it lives.** Every page needs an address, and there are two honest choices. Take the free subdomain the builder hands you, a name on its own publish domain, and the page is reachable the moment it goes live. Or point your own domain at it, so the address is one you keep no matter which builder sits under it. The builder's own domain needs a paid plan and is the address you truly own: [docs.lovable.dev/features/custom-domain](https://docs.lovable.dev/features/custom-domain).

**Behind a password, when it should not be public.** Some pages are dashboards, drafts or client work, not things a stranger should read. Be honest about what the builder actually protects. Its project access setting guards the editor and the source, private to your workspace by default and restrictable to invited users only on a paid plan: [docs.lovable.dev/features/project-visibility](https://docs.lovable.dev/features/project-visibility). The published site is a separate question, and by default anyone with the published link can open it. To gate the live page, build real login into the app itself, or keep the address unlisted and share it only with the people who need it. **Unlisted is not private:** anyone the link reaches, and any crawler that finds it, can open the page, so never rely on a bare unlisted link for anything that would hurt to leak.

---

## WHAT

**An AI with access to the builder that made the owner's website can rewrite the homepage, spend their credits and push it live, all inside one helpful sounding reply.**

Once the AI can reach the builder, the distance between "fix this typo" and "the signup form is gone" is one confident action. Two things go wrong, reliably.

**It hand edits code where the builder's own agent should do it.** The files look editable, so the assistant edits them, and the next agent run regenerates that area and overwrites the change. Nobody sees the moment it reverts. The fix simply is not there a week later.

**It touches pages that carry money without asking.** The homepage, the signup, the waiting list, the checkout. From inside the project these look like any other page, because nothing in the file tree says which one the ads point at. This skill sets which path each change takes and where the owner's OK is mandatory.

---

## GOAL

**Every change to a live site ends the same way.**

The owner saw what would change before it happened, it went through the correct path, a preview link was shown, deploy came only after an OK, and the result was verified on the live URL. Plus one line saying what it cost in credits.

What counts as a money page is the owner's call, not yours. Take it from their constitution and memory if it is written there, ask once if it is not, and write the answer down so it is never asked again.

---

## TRIGGER

- The owner says `SITE-LOVABLE7`, or asks to read, add or change something on a site built with the builder.
- **Indirect work that lands there:** a blog post, a campaign landing page, a text fix, a new section for something being launched.
- **Before anything that spends credits**, including a long agent message that will run for several minutes.

**Not a trigger:** discussing what the site should say. That is writing, and it costs nothing until someone touches the project. Do the thinking outside the builder, where thinking is free.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**The builder cannot tell you which page matters.** It shows projects, files, diffs and analytics, and every page in that list looks equally safe to edit. What it does not show is which page an ad campaign points at, which form is the only inbound path the owner has, which project belongs to a client rather than to them, and whose credits are being spent. All four live in the owner's own layers, and all four decide whether a change is routine or expensive.

So read the constitution and memory before the builder. The constitution carries the approval rules and the owner's voice, which matters because everything published here goes out in their name and a page that sounds like a stranger is worse than a page with a typo. Memory carries the project map and the log of what was changed and what it cost, which is the only place the answer to "what did we do last time" actually exists. The builder keeps its own history, and finding anything in it during an incident is a different task entirely.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Works on the site most weeks:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
SITE-LOVABLE7. Code and design go through the builder agent, content and reads go direct. Money pages and deploys need my OK, never delete a page, credit cap per task. Spec: skills/site-lovable7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**Keep a short project map:** which projects exist, which workspace each belongs to, who owns the credits, and which pages carry conversions. Refresh it when it surprises you, not on a schedule.

**Log every write:** date, project, what changed, credits spent, deployed or not. When a change touches a signup or a payment flow, log the previous state in enough detail to restore it by hand. The builder keeps history, your log makes it findable in a hurry.

**What does not belong in memory:** a copy of the page contents, which the project already holds, and any credential, which belongs where credentials live. **What rots:** the project map itself, because projects get renamed and archived by people who are not you, and any note about pricing or plan limits.

### TOOLS

**Two connections with different jobs, and mixing them is the failure this section exists to prevent.**

The builder's own MCP server reaches the whole account: list and read files, view diffs, check analytics, query the database, deploy. Its message tool hands work to the builder's agent, which writes the code. **That is the default path for anything visual or structural**, because a hand edited file invites the next agent run to overwrite you.

The second connection, optional, is direct database or CMS access. Worth using only where it beats the builder chat: reading signups, editing existing page text with no credits and no deploy step. With only the builder MCP everything still works, it just costs credits.

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing, today usually an MCP server or a connector the client installs. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **Three gates that do not relax.** **Money pages** (homepage, signup, waiting list, navigation, any form or payment flow) need the owner's explicit OK with a description of exactly what will change, shown first. **Deploying to production** needs an OK after preview, unless the owner already said publish in the task. **Never delete a page**, unpublish instead, and never delete a project, change its visibility, or alter workspace settings.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Route the change before touching anything.** Code, layout, components, new sections: builder agent. Existing page text, blog bodies, images in existing posts, database reads: the direct path if you have one. In doubt, builder agent. **Never mix them**, a hand edit plus an agent run is how content silently reverts.

**2. See the whole account before claiming something does not exist.** Listing tools often hide private projects behind a default filter, so ask for all visibility explicitly. A missing set of projects is usually a filter, not a fact.

**3. Respect the permission tiers.** Reading anything is free and unrestricted. Adding something new, a page, a section, a post, you do and report, in preview and not in production. Editing existing content you do and report. Money pages and production deploys are the gated ones above, and the gate is a description shown before, not a summary after.

**4. Watch the money.** Every agent message spends credits. Set a cap you may spend per task without asking, ten is a sane start, and give an estimate before anything larger or before working in a workspace whose credits belong to someone else. **Report the amount spent in every summary, unasked.** An owner who has to check the billing page has already lost trust.

**5. Close the loop on the live URL.** Preview link to the owner, OK, deploy, then fetch the live page and confirm the change is really there. Note that direct CMS edits go live instantly with no deploy step, which is exactly why they must never be used on money pages.

**6. Keep the practical traps in mind, they cost hours the first time.** Long agent messages can exceed the client's timeout, so run them without waiting and poll for the result. **A timeout is not a failure**, check the message list before retrying and paying twice. Content APIs usually want the internal record id, not the readable slug, and image fields want a full public URL, not a hashed asset path. Campaign landing pages sit on their own path with the form embedded and stay out of the menu, organic articles live in the blog and stay indexed. Ads point at the landing page, never at an article.

---

## DEFINITION OF DONE

1. **The path is named:** builder agent or direct, and why that one.
2. **The owner saw what would change** before it changed, for anything touching a money page.
3. **A preview link was shown**, and production came only after an OK.
4. **The live URL was fetched** and the change confirmed there, not in the diff.
5. **The cost is stated in credits**, in the same message, without being asked.
6. **One log entry exists:** date, project, what changed, credits, deployed or not, and for anything touching a signup or payment flow, the previous state in enough detail to restore by hand.

Missing the fourth means you verified your own intention. Missing the sixth means the next incident starts from zero.

---

## MAKE IT YOURS

1. **Name the owner's money pages explicitly on day one.** Everything else is safe to edit, those are not, and the list is short enough to write in one sitting.
2. **Set the credit cap and the estimate threshold with the owner once**, then stop asking about small jobs.
3. **Decide who owns each workspace.** Spending someone else's credits, even correctly, is a conversation you want to have before the invoice rather than after.
4. **Agree the reading boundary.** Which reads, listings and analytics checks you may run unasked. Reading is free, and permission theatre around free operations trains the owner to approve without looking, which is exactly what you do not want when a real gate arrives.
5. **No MCP access at all?** Degrade to drafting: exact page copy, section structure, and the prompt to paste into the builder chat, plus a checklist for preview and deploy.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
