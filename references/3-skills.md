# Layer 3 · Skills

**A method written down once, so the AI performs it the same way every time instead of improvising it again.**

A skill is not a prompt and not a document. It is a named procedure with a trigger, a stated goal, and a definition of done, written to the AI rather than to the human.

---

## What belongs in it

**Something the owner has now done three times the same way, badly the first time.** That is the whole entry test. A method earns a file when repeating it from memory has started to produce different results.

A skill file that works contains: what it is for, what it requires and what happens when those requirements are missing, the trigger, what must be true when it is finished, and one line the AI adds to the always loaded core or the skills index so it can be found when the trigger fires.

**The registration line matters more than the method.** A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way and costs context on every message. Rule: **most days into the core, occasional into the index.**

---

## What does not belong in it

- **A thing done once.** Write the outcome to memory and move on. Most one-off work is not a method.
- **Tool instructions.** How to authenticate with a service is not a skill, it is a requirement inside one. When a file is mostly setup steps, it belongs in the tools layer.
- **A behaviour rule.** One line about how to respond is a constitution line, not a skill.
- **Anything that only works for this one owner's exact folders.** If it cannot be handed to another person's AI and rebuilt inside a different system, it is a personal script.
- **Anything that does not actually work.** A method the owner has never successfully run is a demo. Publishing demos beside working methods is how a library stops being trusted.
- **More than three of them, before the loop has closed once.** See [feedback-loop.md](feedback-loop.md). This is the rule everyone breaks and it is the reason most second brains are abandoned.

---

## What is offered here

Twenty-seven, grouped by one rule: **what is different in the world when the skill finishes.**

| Group | After a run | Skills |
|---|---|---|
| **loop** | The loop closes. The ceiling until one has run unasked | `in7` `exit7` `focus7` |
| **start** | The system exists where there was nothing | `constitution7` `braindump7` `deepdive7` `memory7` `channel7` |
| **aios** | The system's own always loaded files have changed | `context7` `focus7` `exit7` `week7` `audit7` `dashboard7` |
| **capture** | Memory holds a record that did not exist | `in7` `inbox7` `voice7` `watch7` `meeting7` `news7` |
| **decide** | A written judgment exists where there was an opinion | `eval7` `evalx` `verify7` `kw7` |
| **people** | You know one named human better | `warm7` |
| **reach** | Something outside your own files has changed | `mail7` `slides7` `site-cloudflare7` `site-lovable7` `ads7` |

`loop` is a cross-section rather than a seventh category: those three also sit in the group that names what they do. It exists because "install only three" is not advice anyone can follow if the command hands them twelve.

Install:

```
/plugin marketplace add arete-aios/aios
/plugin install loop@arete-aios
```

Or take one file and paste it into any assistant, with nothing installed at all. The file tells the AI what to do with itself.

**Nobody needs all twenty-seven.** Three is a working system. The rest are answers to needs that have not happened yet, and installing an answer before the need is the most expensive habit in this whole layer.

---

## How you know it is working

**One skill has run unasked.** The owner did not type a trigger word. The AI recognised the situation from the registration line and ran the method. That is the moment a library becomes a system.

Two further signs:

1. **The owner can name the last three skills they triggered.** If they cannot, the library is decoration, however good the files are.
2. **The count is stable or falling.** A library that grows every week is collecting, not working.

---

## Which skill maintains it

The library itself is the layer. **`audit7`** keeps it honest: what is installed, what has never fired, what overlaps with something else, what quietly stopped working after a tool changed.

`context7` keeps the skills index complete, because an unlisted skill is an invisible one.

---

**Built by Egils Boitmanis with [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
