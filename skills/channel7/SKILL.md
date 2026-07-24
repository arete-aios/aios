---
name: channel7
description: "CHANNEL7: set up how you actually reach your second brain from your pocket, a chat channel outside the build tool, with voice input if you like talking. Use when your AI only lives at your desk."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: channel7
  synced: "2026-07-23"
---

# SKILL: Reach your second brain from your pocket

**Trigger word: `CHANNEL7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

> Every other skill assumes the owner can reach their AI. This one makes that true when they are not at their desk. A second brain you can only open from one app on one laptop is a filing cabinet with a good search box.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Native surface mode** uses what the owner already has: the build tool at the desk, and the mobile app of whatever AI they use, with its built in voice input. Zero setup, working today. The honest limit is that a vendor's app is usually not wired to the owner's files, so from the phone it is clever but not yet their second brain.

**Dedicated channel mode** puts a bot in a messaging app the owner already checks all day, wired to an agent that loads their constitution and memory when it starts. Now the thing in their pocket answers from the same context as the desk.

Start in whichever mode today allows. Moving from native to dedicated later changes how much of the system the pocket reaches, not the habit it builds.

| Channel | Good when | How to connect |
|---|---|---|
| **Telegram bot** | the owner already lives in Telegram; fastest bot to stand up | [core.telegram.org/bots](https://core.telegram.org/bots) |
| **Slack app** | the owner works in Slack; Socket Mode needs no public web address | [api.slack.com](https://api.slack.com) |
| **The vendor's own mobile app** | zero setup, a fine place to start, voice already built in | already installed |

**Check for a connector before you build anything.** Some clients reach messaging platforms through an MCP server or a ready connector, which turns a build step into a connect and approve step. Look at what the client offers first. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Voice input, ranked honestly, cheapest first.** Native voice in the vendor's mobile app: zero setup. Phone or desktop dictation that converts speech to text before it ever reaches the AI: zero setup, and it works into any channel including a bot. A local speech to text engine such as [faster-whisper](https://github.com/SYSTRAN/faster-whisper): private, the audio never leaves the machine, free after an afternoon of setup and a model download of a few gigabytes. Many people capture far more when they can talk instead of type, and that is often what makes a daily habit stick.

**Voice output is the optional half.** Having it talk back needs a text to speech service, costs money per message, and for some languages only certain voice models work at all. A general reference: [platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech). Leave it for later unless the owner will genuinely listen to spoken replies.

**Setup time, honestly.** The native app is minutes, it is already on the phone. A bot that receives a message and answers is under an hour on Telegram, an hour or two the first time on Slack. An agent that stays **always on** behind the bot, so it answers while the owner is away, is a bigger commitment: a small host that keeps running and stays alive. Voice input is zero if native, an afternoon for the private local engine.

**With nothing set up the owner still talks to the AI inside the build tool.** The channel is an upgrade for reach and habit, not a precondition. Set up the smallest thing that gets them off the desk.

---

## WHAT

**A second brain is only worth what reaches it, and thoughts do not wait for the owner to sit down.**

They arrive walking, driving, standing in a queue, lying awake. A thought has a half life of about a minute. If capturing it means opening a laptop and a specific tool, it does not get captured, and the system fills up with only the thinking that happened at a desk.

**A real failure this is written from.** An owner built an excellent second brain inside a desktop tool and could reach it only there. The structure was clean, the skills worked, and it was empty of exactly the material it existed to hold, because the capture surface was never where the thoughts were. The daily habit never formed, because friction won every time. Then a channel dropped into a messaging app the owner already checked all day, and capture went from a chore to a reflex. Nothing about the brain changed; the door moved into their pocket, and that was the whole difference.

**Two directions, and they are not equal.** Getting messages in and a text answer back is the essential, easy half. Getting spoken answers back is the optional half that costs money and, in some languages, works badly. An AI meeting this without instruction inverts it, reaching for a hosted voice service before the owner can send a plain message from a bus. Get inbound working first. Everything else is decoration on a door that does not open yet.

---

## GOAL

**The owner can reach their second brain in the moment a thought arrives, from wherever they are, and the answer comes back to the same place.**

The result is a channel the owner actually uses, not the most capable one you could build. Who decides which channel: **the owner's existing habit, not the platform's API.** A person glued to one messaging app should get a bot there, even if another platform would be easier to build on; pushing them onto a new app recreates the friction this skill exists to remove.

Read that habit from the constitution and memory if it is there. If not, ask one question, which app is open on your phone all day, then write the answer down so it is never asked again. Never assume the channel silently. The wrong channel is worse than none: it looks done and stays empty.

---

## TRIGGER

- The owner says `CHANNEL7`, or asks how to talk to their AI from their phone, why capture only happens at the desk, or how to send it a voice note.
- **Early, near the start**, because most other skills quietly assume this one is already done.
- **When the owner keeps having thoughts they never manage to record**, which is the symptom that names the missing channel.
- **When typing is the thing stopping them.** That is the moment to add voice input, not a fancier bot.

**Not a trigger:** building the always on host before the owner has sent a single message and felt it answer. Prove the habit with the cheapest surface first. The infrastructure earns its afternoon only after the owner walks through the door.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

The channel is plumbing in the Tools layer, but the value of this skill is not the wiring. It is the decision underneath: which channel fits this owner, unmakeable from inside Tools and answerable from the other two. The constitution and memory hold how the owner behaves, which app they already check, what they have paid for, whether they type or talk. Read those before picking a platform, or you build a fine channel into an app the owner never opens.

There is a second reason the two layers come first. The agent behind the channel must load the constitution and memory when it starts, or the thing answering from the owner's pocket is a generic bot wearing their name, not their second brain.

### CONSTITUTION

The channel is set up once, but which channel exists and how far it reaches is a standing fact worth knowing in every session. So the setup method lives in the skills index, and a short line lives in the always loaded core:

```
CHANNEL7. My second brain is reachable at {channel} from my phone; the agent there loads my constitution and memory at start. Reach: {always-on | at-desk only}. The channel answers only me; any bot token lives in the secrets layer, never in the vault or in chat. Voice in: {on|off}. Voice out: off for now. Spec: skills/channel7/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

Store the shape of the channel, not its traffic: which platform, whether the agent is always on or only alive at the desk, whether voice input is on, what was decided about voice output, and which host runs it if any.

**What does not go in memory.** The bot token or any credential, which belongs in the secrets layer with tight permissions, never in the owned content and never pasted into chat. And the message history itself, which is a pipe passing through, not a filing system. A thought that arrives through the channel is still raw until another skill routes it into the node that owns it. Letting the chat log become a second, unsorted memory is how the owner ends up with two versions of what they think.

### TOOLS

The layer is called **Tools** because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written wrapper around a platform's Bot API. The inbound pipe is the platform's bot interface, the runtime is the vendor's own app or a small always on host, the optional spoken reply is a text to speech service, and voice input is native app voice, phone dictation, or a local engine. Name the mechanism when you use it, and do not let the mechanism rename the layer.

> 🔒 **The channel is a door into the whole system. Lock it to the owner.** A bot wired to a second brain must answer only the owner's verified account, never an open inbox any stranger can message. The token that opens that door lives in the secrets layer with tight file permissions, never in the owned vault and never typed into a chat, because a channel that reaches everything is exactly the credential worth stealing.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level.

**1. Find the app the owner already lives in.** Read it from the constitution and memory, or ask the one question: which app is open on your phone all day. Pick the channel to fit that answer. Do not push a new app on them to save an hour of wiring; the app they already open is the only one a one minute thought will reach.

**2. Get one message in and one real answer back. That is the whole first milestone.** In native surface mode, send from the vendor's app and confirm the loop works away from the desk. In dedicated mode, stand up the bot on the chosen platform, wire it to an agent that loads the constitution and memory at start, and prove the answer carries the owner's own context, not a generic reply.

**3. Lock the channel to the owner before it carries anything real.** The bot answers only known accounts, and the token moves to the secrets layer. A door that opens for strangers is a leak, cheaper to close on day one than after it holds anything.

**4. Add voice input only if the owner likes talking, cheapest path first.** Native app voice or phone dictation both turn speech to text before it reaches the AI, at zero setup, and dictation works into any channel. A local engine is worth its afternoon once the habit exists, not before. Prove it with one voice message that lands as clean text. If the owner is a typer, skip this out loud, not silently.

**5. Decide voice output now, and the honest default is later.** It needs a text to speech service, costs money per reply, and some languages only work on certain voice models. Turn it on only if the owner will really listen to spoken answers; otherwise mark it deferred, so it is a decision on record, not a loose end.

**6. Register the channel and its honest reach in the core.** Which channel, voice in on or off, voice out decided, and the reach stated plainly: always on, or alive only when the desk is. Always on is a promise about when the AI can answer, and a broken promise there is worse than an admitted limit.

---

## DEFINITION OF DONE

1. **One channel is chosen to fit a habit the owner already has**, not a new app they must now remember to open.
2. **A message goes from the owner's pocket and a real answer comes back**, proven once, live. In dedicated mode the answer carries the owner's own context; in native mode it proves the reach and the habit.
3. **If the owner likes talking, one voice message lands as clean text** on that channel, proven once. If they do not, voice input is skipped on the record, not forgotten.
4. **Voice output is decided:** off for now, or on with a reason. Not left ambiguous.
5. **The channel and its honest reach are registered in the core**, and any bot token lives in the secrets layer rather than the vault, with the channel locked to the owner.

Missing the second means you built plumbing nobody has walked through. Missing the fifth means the door exists but the AI does not know its reach, so it promises answers at hours it cannot deliver.

---

## MAKE IT YOURS

1. **Pick the channel by where the owner already is, not by which API is nicest.** The best inbound channel is the boring app they already check, over the elegant one they would have to build a new habit around.
2. **Keep the two commitments separate.** A bot that replies is an hour. An agent always on behind it is a standing thing you keep alive. Ship the first; decide later whether the second is worth the upkeep.
3. **Treat voice input as the habit maker.** If the owner resists typing, the fastest voice path is the whole win. Native app voice or phone dictation today beats a perfect private engine next month.
4. **Leave voice output for later on purpose.** It is the expensive optional half and it rarely earns its cost early. Name it deferred so it stops being an open question.
5. **Remember the channel is a pipe, not a cabinet.** What arrives through it still gets routed into place by your other skills, not left as a growing chat history to reconcile later.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
