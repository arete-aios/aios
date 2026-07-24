---
name: slides7
description: "SLIDES7: build presentations as HTML the AI writes directly. 16:9, one URL per slide, notes on a second screen, opens with no wifi. Use when the owner needs a talk or a deck."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: slides7
  synced: "2026-07-23"
---

# SKILL: Build a presentation your AI can actually produce

**Trigger word: `SLIDES7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Published mode:** the deck lives at an address, so a link can be sent and a single slide can be quoted.
**Local mode:** the same folder opens from disk with a `file://` address. No account, no host, no network. You lose the shareable link and nothing else.

Local mode is not the fallback. It is the copy that has to exist anyway, because it is the one that works at the venue.

| What | Why | Where |
|---|---|---|
| **A presentation framework, copied into the deck's own folder** | Turns HTML into slides, keyboard and remote navigation, notes view | [revealjs.com/installation](https://revealjs.com/installation/) |
| **A static host** (optional) | Gives the deck a real address on a domain the owner controls | [Cloudflare Pages](https://developers.cloudflare.com/pages/) · [Netlify](https://docs.netlify.com/) · [GitHub Pages](https://pages.github.com/) · [Vercel](https://vercel.com/docs) |
| **An AI app builder** (alternative) | Same result if that is where the owner already publishes | [docs.lovable.dev](https://docs.lovable.dev/) |
| **A browser you can look through** | So the rendered slide gets seen, not described | Any browser or screenshot tool |

**Check your connectors before you build anything.** Hosts and app builders increasingly arrive as MCP servers or ready connectors inside AI clients, which turns publishing into an approve step rather than a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Setup time, honestly.** Copying the framework into a folder, about five minutes, once. A first deploy to a static host, fifteen to thirty minutes including the domain, once. Every deck after that is content time only. With no host at all, zero setup, and you still get everything except the link.

**In the owner's own system you need two places to write:** the memory layer for the source document and a small register of decks, and wherever their tasks live for the offline check before the event.

---

## WHAT

**An AI builds a good HTML presentation far more reliably than it drives PowerPoint or Google Slides, because HTML is text it can write directly and then look at.**

That is the whole argument. Through a slides API the model works blind: it posts requests at an object it cannot see, gets back identifiers instead of a picture, and finds out that the text overflowed the box only when a human opens the file. In HTML it writes the layout, renders it, and reads the result. The feedback loop closes. Every rule below is enforceable because of that, and none of them are enforceable through an API that answers in element IDs.

**The tradeoff, stated plainly, because the owner will meet it in the first meeting.** The receiver gets a link or a folder, not a `.pptx` they can open and edit in the tool they know. For most audiences that is fine or better: a link opens on a phone, needs no software, and can point at one slide. For an audience that genuinely edits the file afterwards, a corporate template, a co-authored deck, a client who wants to change slide four, this is the wrong format and you should say so before you build, not after. A printed PDF covers "send me the slides" ([revealjs.com/pdf-export](https://revealjs.com/pdf-export/)) but it does not cover "let me edit it".

**Without this skill an AI makes three predictable messes:** a wall of bullet text nobody can read from row eight, a new scattered address for every event, and a deck that loads its framework from someone else's server. That last one has a story. A deck built against a CDN went to a venue whose wifi died, and a CDN deck with no network is a white page in front of a room. That is why the rule below is a rule and not advice.

---

## GOAL

**A finished presentation, addressable slide by slide, that opens on the presenter's machine with the network switched off.** When it is published, the same folder also sits at a live address the owner controls, so a link can be sent and one slide quoted. The offline, addressable copy is the requirement. The live address is the usual way to make it shareable, not a second requirement.

When it is done: the deck is 16:9, every slide has its own address that can be pasted into a message, whether that is a URL on the live host or a `file://` path carrying the same slide hash, the opening page is a title a stranger can read, and the presenter sees notes the audience never does.

**Who decides the content is not you.** Audience, purpose and what may be said publicly come from the owner's constitution and memory if they are written there. If they are not, ask once, then write the answer into memory so the next deck starts from it.

---

## TRIGGER

- The owner says `SLIDES7`, or asks for a talk, a deck, a slide set, a workshop, a pitch, or a slide link they can send.
- **When a talk gets a date.** The offline copy and the notes are not last-day work.
- **When someone asks for the slides.** That is a publishing decision, and it has a route below.

**Not a trigger:** an existing deck you decided to improve. You do not redesign or republish a deck on your own initiative, and never on the day of the event without the owner saying so. A deck that changes under the presenter is worse than an outdated one. Also not a trigger: a document with headings. Not everything long is a talk.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

A deck is one of the few things the owner's AI makes that **a room full of people sees, in the owner's name, with the owner standing next to it.** So the constitution decides more here than the framework does: how they speak, what claims they are willing to make in public, what is private, whose names may appear. And the content is almost never new. Most of a good deck is already in memory as work the owner did, with real numbers attached. Read both before opening a single template.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how often the owner speaks.

**Presents most weeks:** put it in the always loaded core, the part read at the start of every session.
**Occasional:** do not spend core context on it. Put it in the skills index the core already links to, and let it load when the trigger fires.

Either way the line is the same:

```
SLIDES7. Presentations are HTML I own: 16:9, one address with a path per deck, one URL per slide, switcher bottom right, a title page that describes the talk, speaker notes in a second window, framework shipped locally never from a CDN, offline copy tested before every event. Spec: skills/slides7.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**The source document is the archive. The published HTML is a rendering of it.** If the HTML is lost the deck can be rebuilt. If the source document is lost, nothing can. Keep the source in the sphere or project it belongs to, not in the publishing folder.

Keep a short register, one row per deck: slug, event, date, audience, live address, where the source lives. Without it the third talk is already a guess, and guessing is how a live deck gets overwritten by the wrong folder.

**Do not store** the framework copy as if it were the owner's material, and do not treat the rendered file as the record of what was said.

**What rots:** anything on a slide that was true on the day. Numbers, prices, team size, "current" status. Put the date beside any number that will age, so a deck reused next year gets caught before the audience catches it.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **Never load the presentation framework, fonts, or any asset from a CDN.** Every file ships inside the deck's own folder. A deck that needs someone else's server is a deck that dies with the venue wifi, in front of the room, with no recovery. Local copy, every time, no exceptions for "it is just the font".

> 🔒 **Publishing over a live deck is a change to something in use.** Confirm the folder and the target before you deploy, and never republish inside the twenty four hours before a talk without the owner's explicit approval.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Write the content before you write any HTML.** Plain literal headlines, not marketing hooks. Roughly 45 words a slide at most, because a slide is an anchor and not a handout. Real numbers instead of "many". Sources in small type under any checkable claim, verified against the real source and never from memory. No em dash, no filler vocabulary. Pitch it at the actual audience in the room.

**2. One address, one path per deck.** All decks live under a single address the owner controls, and each deck is a path under it. Slug of event plus date, so it sorts and never collides. Set the whole site to noindex through the meta tag, headers and robots. Talks are not search results.

**3. The address opens on a title page, and that page has to work alone.** Someone gets the link three weeks later with no context. The page tells them what the talk is, who gave it, when, and to whom, in a few lines they can read cold. Then a single clear button through to the slides. This is also where the agenda, a QR code and any handout live.

**4. 16:9, always, with the switcher bottom right.** Set the deck to 1920 by 1080. Not 4:3, not square. Projectors and screens are 16:9, and a mismatched deck either loses a strip of every slide or grows black bars the room reads as amateur. Show the on-screen navigation in the bottom right corner, because the presenter clicks with a mouse or a remote and should not be hunting a keyboard shortcut in front of an audience.

**5. Every slide gets its own URL.** Turn on hash routing so slide seven is `/{slug}/#/7`. A slide that can be pasted into a chat, an email or a follow-up message is a citable object. Without it the deck is one blob and every reference becomes "scroll to about the middle".

**6. Speaker notes, and the second window is the part most tools get wrong.** Write the notes, they are half the deck. Then get the arrangement right: **the present control opens a second window, that window goes to the projector, and the first window stays with the presenter carrying the notes, the timer and the next slide.** The audience sees only the second window. Keep the two in sync through a browser channel between windows, both loaded from the same folder, so it works offline as well ([BroadcastChannel](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel), [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open)). Frameworks ship a version of this ([revealjs.com/speaker-view](https://revealjs.com/speaker-view/)); check which window it puts the notes in and adjust, because the default is often backwards for this setup. Test it on a real second screen before the event, and test what happens when the presenter closes one window by accident.

**7. Ship the framework locally, then prove it offline.** Copy the framework and every asset into the deck's folder. Before every event, put the folder on the presenter's machine, switch the network off, open it with a `file://` address, and click through it. An offline copy that has never been opened offline is a guess.

**8. Publish through whatever route the owner already has, and keep the folder identical in all of them.** A static host with a deploy command, an AI app builder that hosts what it builds, an ordinary web host with file upload, or no host at all, in which case you hand over the folder and the exact path to open. Deploy to the production target, not a preview one, because that mistake leaves the live address on the old version while every log looks green.

**9. Look at the rendered result before you call it ready.** Open the live address. Read the last row of text at projector resolution. Click a couple of the per-slide links. Open it on a phone. A deck nobody has looked at is not a finished deck, it is a hopeful folder.

---

## DEFINITION OF DONE

1. **The opening page is a title page** a stranger can read cold, with a button through to the slides, working the same from the live address and from the `file://` copy.
2. **The deck is 16:9**, the switcher is bottom right, and opening one slide's address, a live URL when published or a `file://` path with that slide's hash, lands on that slide.
3. **Speaker notes exist**, and the two-window arrangement has been tested on a second screen with the notes on the presenter's side.
4. **An offline copy has been opened offline** on the machine that will be used, with the network off.
5. **The source document is in memory** and the register has a row: slug, event, date, audience, live address if published, source location.

Missing the fourth is the one that costs a talk. Missing the fifth is how the same deck gets rebuilt from scratch next year.

---

## MAKE IT YOURS

1. **Swap the framework freely.** Anything that produces static HTML with per-slide addresses and a notes view satisfies every rule here. Markdown-first tools that compile to HTML ([Marp](https://marp.app/), [Slidev](https://sli.dev/)) fit the same shape and suit an owner who would rather write text than markup.
2. **Build the house theme once.** Colors, typography, logo placement, a title layout, a section layout, a quote layout. Then every deck inherits it and no talk starts from a blank page.
3. **Decide the editable-file question up front.** If this owner's audiences genuinely edit decks afterwards, agree now who converts and to what, or agree that a PDF is the deliverable. Discovering it after the deck exists is the expensive order.
4. **Fix the address scheme before the second deck**, not after. One parent address, a path per talk, a slug format that sorts by date.
5. **Decide what the present control does on one screen**, when there is no projector and no second display. Mirroring, a merged view, or a plain notice. Someone will click it in a coffee shop.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
