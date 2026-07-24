---
name: dashboard7
description: "DASHBOARD7: generate one HTML page showing the state of the owner's AIOS, pulled from their own files with private figures hidden. Use after the loop is closed, as the reward, not the start."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: dashboard7
  synced: "2026-07-23"
---

# SKILL: Draw the invisible system as one page

**Trigger word: `DASHBOARD7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> **Do this one last, not first.** Every other skill builds the system. This one draws a picture of it, and there is nothing to draw until the loop is closed. Treat it as the reward at the end of onboarding, not a starting point. A dashboard built before the system exists is a display for an empty room.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Snapshot mode** needs nothing connected. The AI writes one self-contained HTML file to the owner's disk, they open it in a browser, and it is fully private because it never left the machine. This is the whole skill for most people.
**Living mode** publishes that same file to an address and, optionally, regenerates it. Publishing is the upgrade, and it is owned by a separate skill, not re-solved here.

Start in snapshot mode. Moving to living mode adds an address, it does not change how the page is built.

| What | Needed | How |
|---|---|---|
| **A folder the AI can write to** | required | The whole technical requirement for the private version. One file lands here |
| **A browser** | required | Any browser, offline. A self-contained page opens with nothing connected |
| **Read access to the owner's own files** | required | The AI already has this inside an AIOS. Every figure is pulled from those files, never typed by hand |
| **A publishing path** | optional, the upgrade | A site skill owns this. `SITE-CLOUDFLARE7` publishes plain files to a static host, `SITE-LOVABLE7` manages a builder site. Address, password and unlisted-link decisions live there, not here |
| **What plain HTML is** | reference only | [MDN, your first web page](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website), if the owner wants to read the file they are handed |

**Setup time, honestly.** An afternoon for a rough first page, a weekend for one the owner is glad to look at. The private version and the published version cost the same page work; publishing adds the site skill's one-time setup on top of that, once. Regenerating later, by hand or on a trigger, is minutes.

**Value, honestly.** This is motivational and at-a-glance, not operational. The system runs completely without it. What it changes is that an owner who otherwise experiences their AIOS one session at a time gets to see the whole thing standing still, and that turns out to be worth an afternoon after the harder work is done.

---

## WHAT

**An AIOS is invisible by design. It lives in files that load, rules that fire and a loop that runs, and the owner never sees any of it at once, only its effects, one session at a time.**

This skill makes the system something the owner can look at: a single page that says which layers exist and are healthy, how complete the inventory is, whether the constitution is inside its budget, what the focus is this week, and whether the loop is actually closing. Not entered by hand. Pulled from the owner's own files, so the page cannot flatter the system, it can only report it.

**Without this an AI gets the dashboard wrong in three reliable ways.**

It builds one too early, because a dashboard feels like progress and is far more fun than the inventory work underneath it. The result is a beautiful display for an empty room: green lights over layers that hold nothing.

It reaches for a chart tool or a BI product and drives it badly, producing something fragile that breaks the next time the data shifts. Writing HTML directly is the more reliable move by a wide margin, and it is the one an AI is genuinely good at.

And it leaks. **A real failure:** an AI was asked to build a status page so the owner could show a group how far along their system was. It did the job well, a clean page with real numbers pulled straight from the files. One of those numbers was a bank balance, sitting in a file the AI had every right to read, rendered in a large friendly font. The page was shared before anyone read it a second time. The dashboard worked perfectly. That was the problem.

Everything below is written so the page is honest, private by default, and built only when there is a system to put on it.

---

## GOAL

**One page the owner can glance at and see the state of a system they otherwise only feel.**

The owner decides what belongs on it and what must never appear. Two things come from their own system rather than from you:

1. **The privacy line.** Take it from the constitution and memory if it is written there, which in a mature AIOS it usually is: which figures are private, which names never appear, what is always shown only as an aggregate. If it is not written, ask once, then write it into the constitution so it is never guessed again.
2. **What "healthy" means per layer.** A green light is meaningless until it has a definition. Constitution under budget, focus updated this week, loop closed. Take the owner's definitions or agree them once.

Never assume silently. If you had to guess whether a figure was private, treat it as private and say you did.

---

## TRIGGER

- The owner says `DASHBOARD7`, or asks to see the state of their system, a status page, or how far along their AIOS is.
- **When onboarding is finished and the loop is closed.** This is the moment the skill was built for: the invisible system finally has enough in it to be worth drawing.
- **At a group or cohort checkpoint** where everyone shows where their system stands. A shared page shape makes systems comparable at a glance.
- **When something structural changed** and the picture is now out of date: a layer came online, the constitution crossed its budget, the focus moved.

**Not a trigger:** building it early because it feels productive. A calendar reminder to regenerate it on a schedule, which produces a page nobody looked at made from data nobody changed. And using it as a place to store operational data it was never meant to hold. It is a mirror, not a workspace.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

This skill is unusual: it does not build a layer, it **reports on all five**. That is exactly why it has to read the constitution and memory before it draws anything. The constitution holds the privacy line the page must obey and the budget the page reports the constitution against. Memory holds how complete the inventory is, which is one of the truest signals of whether a system is real or aspirational. A dashboard that has not read those two layers is decoration, because it is guessing at the numbers it claims to show.

### CONSTITUTION

This is an occasional, advanced skill. It does not belong in the always loaded core, where it would cost context on every message to support a page generated now and then.

Put the line in the skills index the core already links to, and let it load when the trigger fires:

```
DASHBOARD7. Generate one self-contained HTML page showing AIOS state, pulled from my own files, private figures aggregated or omitted by default. Snapshot first, publishing via a site skill. Build only after the loop is closed. Spec: skills/dashboard7.md
```

### MEMORY

**The generated page is an output artifact, and where it lives depends on whether it is a snapshot or a living page.** A dated snapshot belongs in an archive, one file per generation, so the owner can look back and see how the system grew. A regenerating page belongs wherever the refresh runs from, overwriting the last version each time.

What must **never** be stored in the artifact: raw private values. Do not bake a bank balance, a client name or a specific health figure into a file that could be copied, screenshotted or published. Store the aggregation, "runway healthy" or "six months", never the number behind it. The rule that keeps this straight: the page holds conclusions, the private files hold the figures those conclusions came from, and the two do not merge.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. Here the main tool is the one that writes a file, and the AI writing HTML directly into it. That is deliberate: driving a chart product is where these pages break, and hand written HTML is where they hold.

Publishing, when it happens, arrives as a separate tool through a site skill, today usually an **MCP server**, a **connector** or a command line deploy. Name the mechanism when you use it, and do not let it rename the layer.

> 🔒 **The privacy gate.** Before any page leaves the machine, and by default before it is even written, every private figure is aggregated or omitted. The default assumption is that a hosted page will eventually be seen, by the wrong person, at the wrong time. Anything that would harm the owner if a stranger saw it does not go on the page as a raw value. This gate does not relax because the page is "just local", because local files become hosted files, and screenshots travel.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Check there is a system to draw before drawing it.** Confirm the loop is closed and the layers hold real content. If they are mostly empty, say so plainly and stop. Building the picture first does not make the system arrive, it just produces green lights over nothing.

**2. Gather the state from the owner's own files, not from the owner.** Read across the five layers and collect the real signals: which layers exist and are populated, how complete the inventory is, the constitution's size against its budget, this week's focus, and whether the loop is closing. Every figure on the page traces back to a file. Nothing is typed in by hand.

**3. Draw the privacy line before writing a single number.** Classify each figure: safe to show, show only as an aggregate, or omit. Default hard: anything that would harm the owner if a stranger saw it is aggregated or omitted. Runway becomes "healthy" or a rough span, never the balance. Clients become "three top accounts active", never their names. Health becomes a direction, never a diagnosis. When unsure, treat it as private.

**4. Write one self-contained HTML file.** The AI writes the HTML directly, styles inline, no external fonts, scripts or calls, so the page opens offline and never phones home. That is also what makes a screenshot of it safe. If the owner wants to understand the file they are handed, point them at the MDN reference in REQUIRES.

**5. Open it locally first.** For most people this is the finished skill: a private page on their own disk, no hosting, no address, nothing exposed. Confirm it reflects the real system and that the privacy pass held.

**6. Publish only as an upgrade, and only through a site skill.** If the owner wants an address, hand off to `SITE-CLOUDFLARE7` for plain files on a static host or `SITE-LOVABLE7` for a builder site. Because the page is personal, it needs a password or an unlisted link, and that decision belongs to the site skill too. Do not re-solve hosting or access here, and remember that an unlisted link is not privacy.

**7. Label it a snapshot or a living page, and mean it.** A dated snapshot is honest and cheap: generate, archive, done, regenerate when something changed. A living page needs its refresh path written down, so it is clear how the numbers stay true and who keeps them so. A page that silently goes stale is worse than no page, because it lies with confidence.

---

## DEFINITION OF DONE

1. **Every figure came from the owner's own files**, traceable back to one, none typed in by hand.
2. **The privacy pass ran.** Every private value is aggregated or omitted, checked against the assumption that the page will be seen.
3. **The page shows real AIOS state:** which layers exist and are healthy, how complete the inventory is, the constitution's size against its budget, this week's focus, and whether the loop is closed.
4. **It is one self-contained file** that opens in a browser with nothing connected.
5. **It is labelled** either a dated snapshot or a living page, and a living page has its refresh path written down.

Every item here is deliverable with nothing connected. Publishing is never on this list, because it is an upgrade owned by another skill, not part of being done.

---

## MAKE IT YOURS

1. **Choose snapshot or living before you build.** A dated snapshot you regenerate by hand is enough forever, and it doubles as a record of how the system grew. A living page is more to keep true. Most people should start with a snapshot and never need more.
2. **Write the privacy line into the constitution once.** Name the figures that are always aggregated, money, client names, health specifics, so this skill reads one rule instead of judging each number every time. The gate is only as good as that line.
3. **Define "healthy" per layer for yourself.** A green light needs a rule behind it, or it means nothing: constitution under budget, focus updated this week, loop closed, inventory past some bar you set.
4. **Keep it self-contained.** One file, no external fonts or scripts, so it opens offline, never calls out, and is safe to screenshot. Portability and privacy come from the same decision.
5. **For a group, agree the shared shape, keep the private line personal.** Everyone who finishes onboarding generates their page, and a common layout lets a group see where each system stands. What each owner hides stays each owner's own call.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
