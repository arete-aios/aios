---
name: site-cloudflare7
description: "SITE-CLOUDFLARE7: publish web pages that stay plain files the owner keeps, live on their own address with one command. Use for landing pages, one-pagers, decks and small static sites."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: site-cloudflare7
  synced: "2026-07-23"
---

# SKILL: Publish a web page the owner actually keeps

**Trigger word: `SITE-CLOUDFLARE7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Publishing mode** needs a free static host account and a deploy token. You write the files and send a copy to a live address in one command.
**Files only mode** needs nothing connected. You still write the complete page as plain files on the owner's disk, they open it in a browser, and it publishes the day an account exists. **The files were always the valuable half.**

Start in whichever mode today allows. Moving from files only to publishing adds an address, it does not change how the page is built.

| What | Needed | How to connect |
|---|---|---|
| **A static host account** | required for publishing | Cloudflare Pages, free tier is enough: [developers.cloudflare.com/pages](https://developers.cloudflare.com/pages/) |
| **One project per site** | required | [get started guide](https://developers.cloudflare.com/pages/get-started/) |
| **A deploy command line tool** | required | Wrangler, run through `npx` so nothing installs globally: [developers.cloudflare.com/workers/wrangler](https://developers.cloudflare.com/workers/wrangler/) |
| **Node, so `npx` exists** | required | [nodejs.org/en/download](https://nodejs.org/en/download) |
| **An API token with Pages deploy permission** | required | [how to create one](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/). Store it as the environment variable `CLOUDFLARE_API_TOKEN`. Never paste it into a page, a chat or a repository |
| **A domain or subdomain** | optional | [developers.cloudflare.com/pages/configuration/custom-domains](https://developers.cloudflare.com/pages/configuration/custom-domains/). Without one the page still gets a working address on `pages.dev` |

**Any static host with a command line deploy works the same way.** Cloudflare Pages is the default here because the free tier carries a custom domain and unlimited bandwidth, not because the method depends on it.

**Setup time, honestly.** About fifteen minutes once: account, project, token. A custom domain adds a DNS change and anything from minutes to a couple of hours before every resolver agrees it exists. Every deploy after that is one command and a few seconds.

**Where it lives.** Every page needs an address, and there are two honest choices. Take the free subdomain the host hands you, here a name on `pages.dev`, and the page is reachable the moment it deploys. Or point your own domain, or a subdomain of it, at the host, so the address is one you keep no matter which host sits under it. The free name works for the life of the account, your own name outlives the host. Custom domains on Pages: [developers.cloudflare.com/pages/configuration/custom-domains](https://developers.cloudflare.com/pages/configuration/custom-domains/).

**Behind a password, when it should not be public.** Some pages are dashboards, drafts or client previews, not things a stranger should read. Three honest options, ordered by how much they actually protect. Put a login in front with the host's own access control, here Cloudflare Access, which can email a one-time PIN to the addresses you allow: [developers.cloudflare.com/cloudflare-one/applications/configure-apps/self-hosted-public-app](https://developers.cloudflare.com/cloudflare-one/applications/configure-apps/self-hosted-public-app/). Build a simple gate into the page itself. Or keep the address unlisted and send the link only to the people who need it. **Unlisted is not private:** anyone the link reaches, and any crawler that finds it, can open the page, so never put behind a bare unlisted link what would actually hurt to leak.

---

## WHAT

**A page built inside a website builder is the owner's only while the subscription lasts.**

This skill makes the page a folder of plain files they keep, and publishing it one command. Instead of a builder that holds the pages inside its product, you write HTML, CSS and a little JavaScript into a folder the owner controls, and publish a copy to a static host.

It prevents three failures: content that cannot leave the tool that made it, a page nobody can rebuild because the source only ever existed in a browser, and a monthly fee for the privilege of editing a paragraph.

**Without this an AI with deploy access fails in two quiet ways.** It publishes the wrong folder into a live project, because a deploy replaces what was there and nothing asks whether you meant it. Or it fixes something by editing the live site directly, which works for exactly as long as it takes for the next deploy to overwrite the fix with the unchanged source. Both look successful in the moment. Both are found later by someone else.

---

## GOAL

**One page exists as a folder of files on the owner's own disk, an identical copy is live at an address they control, and the owner has seen the real URL.**

If every tool involved disappeared tomorrow, the folder would still open in a browser and still be publishable somewhere else. That is the test, and it is the only one that matters here.

The owner decides what the page is for and what it must say. Take that from their constitution and memory if it is written there, ask once if it is not, and never guess at a claim that goes out under their name.

---

## TRIGGER

- The owner says `SITE-CLOUDFLARE7`, or asks to build, publish or update a standalone page or a small static site: a landing page, a one-pager, a deck, a microsite.
- **Any change to something already live at one of these addresses**, including a one word fix.
- **When a page is about to be deleted or renamed.** Addresses get linked to from places you cannot see. Removing one is a decision, not cleanup.

**Not a trigger:** a page that belongs inside an existing app or CMS. Publish that through the system that owns it. **Two publishing paths to one site is how a site starts contradicting itself.**

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**Deploy is one of the few operations in a personal system that is public the second it finishes.** A file written to the wrong folder is a private mistake. A page pushed to a live address is a public claim in the owner's name, readable by anyone with the link, including people who already had it. That is why the owner's own layers get read before the host: their constitution carries how they speak and what they are willing to say in public, and no page should go out sounding like a stranger wearing their domain.

The memory layer carries the part the host cannot tell you: **which addresses already exist, what each is for, and which of them is receiving traffic right now.** Ad campaigns, printed material, email footers and other people's links all point at these addresses from outside the system. Without that registry the third page is already a guess, and guessing is how a live one gets overwritten.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Publishes most weeks:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
SITE-CLOUDFLARE7. Static pages I own, published to my own addresses. The AI writes the files, I preview, I approve the deploy, one page one address, never overwrite a live project unchecked, never delete. Spec: skills/site-cloudflare7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**The source folder is the single source of truth. The live site is a published copy of it.**

Keep a small registry in the memory layer, one line per live page: **address, what it is, where its source folder lives, when it was last deployed.** That is the whole record and it is enough.

**Never edit the live site by hand.** Change the source and publish again, or the next deploy silently reverts the fix and nobody will connect the two events.

**What does not belong in memory:** the page contents, which already live in the source folder, and the token, which belongs in the environment and nowhere else. **What rots:** deploy notes about a page that was replaced, and any registry line for an address that no longer answers. Check the registry against reality when it surprises you, not on a schedule.

### TOOLS

What to connect is in REQUIRES above and is not repeated here. What belongs here is the naming.

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper, and here a plain command line program. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **The deploy gate.** Nothing reaches a live address before the owner has seen the rendered page, and no deploy goes into an existing project until you have said out loud which folder is going to which project name. **A deploy replaces what was there.** When unsure, deploy to a new project or a preview instead. Deleting a live page is almost never the right move: replace it or unpublish it, and say which one you did.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Write the files locally.** Build the page as plain files in a dedicated folder, one folder is one deployable site. Keep it self contained: local or inline CSS, fonts and images, no dependency on an external service that can disappear or block. **A page that needs someone else's server to render is not a page the owner owns.**

**2. Preview before you publish.** Open the file in a browser or serve the folder locally, and have the owner look at the real rendered thing, not at a description of it. Nothing reaches the live address before the owner has seen it.

**3. Deploy with one command.**

```
npx wrangler pages deploy ./your-folder --project-name your-project
```

The output gives the live URL. This publishes a fresh copy and does not touch the source folder.

**4. Verify on the live URL.** Open it. Check it on a phone as well, most visitors are on one. **Two things routinely look like a broken deploy and are not:** an edge cache can serve the previous version for a short while, and a brand new subdomain needs a few minutes before every DNS resolver agrees it exists. Check from outside the machine you deployed from before concluding anything failed.

**5. Guard the live projects.** Before deploying into an existing project, confirm you are sending the right folder to the right project name. When unsure, deploy to a new project or a preview first.

**6. Update the registry in the same breath as the deploy.** A registry updated later is a registry that is wrong by the time it matters.

---

## DEFINITION OF DONE

1. **A self contained source folder** on the owner's disk that opens correctly in a browser with no network.
2. **The owner has seen the rendered page** before anything went live.
3. **The live address verified from outside the deploying machine**, and once on a phone.
4. **One registry line written or updated** in the same session: address, purpose, source folder, deploy date.
5. **Nothing on the live site edited by hand**, so the source and the published copy still say the same thing.

Missing the first means the owner rents the page rather than owns it. Missing the fourth means the next deploy is a guess.

---

## MAKE IT YOURS

1. **Name the skill and the trigger to fit the owner's own index.** `SITE-CLOUDFLARE7` is one label. Use whatever their system already speaks, and change the constitution line to match.
2. **Decide the address scheme up front**, for example one parent domain with a subdomain per project, and keep it. Every page then has one clear address that can be cited, and no page ever needs a second one.
3. **Set the reuse rule.** A shared header, footer and stylesheet copied into each folder keeps every page standalone. Sharing them from one hosted place is tidier and quietly makes each page depend on another one staying alive.
4. **Agree what the AI may publish without asking.** A preview address, almost always yes. The address a real visitor sees, almost always no. Write both sides, so the owner is not approving a preview every week.
5. **No account or token yet?** Build the files anyway, tell the owner exactly where they are and how to open them, and publish the moment the account exists.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
