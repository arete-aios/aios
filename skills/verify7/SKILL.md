---
name: verify7
description: "VERIFY7: ask an independent model that never saw your draft answer, then report in three lines whether it changed your mind. Use before confident claims or costly decisions."
license: CC-BY-4.0
metadata:
  author: fulldigital.me
  version: "1.0.0"
  source: verify7
  synced: "2026-07-23"
---

# SKILL: Get a third opinion from a model that does not know you

**Trigger word: `VERIFY7`.**

**Human:** paste this file into your AI. Nothing else is needed from you until it asks.
**Assistant:** everything below is addressed to you. Adapt it to this owner's system. The goal and the hard rules matter, the exact implementation is yours to choose.

---

## REQUIRES

**This skill has two modes, and nothing below is a hard blocker.**

**Automatic mode:** you can reach a second model yourself, through a key or a connector, and you call it without being asked. This is the skill.
**Relay mode:** you hand the owner a clean question in a copy ready block, they paste it into a brand new chat with any other model and bring the answer back verbatim. Same method, same three line report.

**These two are not equal, and pretending otherwise would be dishonest.** The whole value is in the checks nobody requested, and a check that needs the owner to carry a question across two windows only happens when they already doubt. Doubt is exactly the state where verification is least needed. Relay mode is how you prove the idea in an afternoon. Automatic mode is how it survives the month.

| Judge | What it costs | Where to set it up |
|---|---|---|
| **Gemini** | Free tier is enough for daily checks, and it reads images | [ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key) · limits: [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| **DeepSeek** | Prepaid, pennies per call, text only, no images | [api-docs.deepseek.com](https://api-docs.deepseek.com) |
| **Any model the owner is not already talking to** | Whatever it charges | Independence is the requirement, not the brand |

**Check your connectors first.** Some clients already offer a second model as a connector or an MCP server, which turns this into a connect and approve step instead of a build step. What MCP is: [modelcontextprotocol.io](https://modelcontextprotocol.io).

**Inside your own system you need one small thing:** somewhere to write one line per run. Date, question, verdict. Without it nobody ever finds out whether the checks are working.

**Setup time, honestly.** Two minutes for the free key if the owner already has an account with that provider. An hour or two if you write the thin wrapper yourself and want images working as well as text. Longer if someone else controls the owner's billing, in which case start in relay mode today and move over when the key arrives.

---

## WHAT

**You and the owner talk in one bubble, so you can confirm each other's errors.**

They learn what you usually answer. You learn what they want to hear. Two parties who know each other well agree with each other, including when both are wrong, and neither has any way to notice from inside the conversation.

This skill brings in a judge: a separate model that does not know your answer. **Its value is independence, not intelligence.** A weaker model that has never seen your draft is worth more here than a stronger one that has.

**It came out of a real surprise.** A foreign model was asked to describe what it saw in a generated image, with no knowledge of what the image was supposed to be. Its verdict was sharper than the self-criticism written moments earlier, for one reason: it had no intention to protect. It was not hoping the thing was good. That is the entire mechanism, and it generalises well beyond images.

---

## GOAL

**Fewer confident mistakes.**

Every run ends in a three line report, and the third line states plainly whether the check changed your answer. That line is the whole point. The purpose is not to show that verification happened, it is to say what it changed.

**The owner sets the threshold, not you.** What counts as a decision expensive enough to check, and which subjects are off limits, are facts about them. Take both from their constitution and memory if they are written there, ask once if they are not, and never quietly invent a threshold, because an assistant that checks everything is as useless as one that checks nothing.

---

## TRIGGER

- The owner says `VERIFY7 {question}` or `V7 {question}`.
- **More important: you invoke it yourself, without being asked,** in the five moments listed under HOW IT RUNS. Self-invocation is a duty, not a courtesy. The most dangerous moments are the ones where nobody doubts.

**Not a trigger:** anything you can settle directly. If a file read, a command or an API call answers the question, run it. Asking a judge whether a script works when you could simply run it is laziness disguised as diligence. **Verification first, third opinion second, never instead.**

**Also not a trigger:** taste, personal decisions, and anything that lives only inside the owner's own system. A foreign model has no context there and is blinder, not sharper.

---

## AIOS

This skill comes from an **AI operating system**: five layers a person owns and their AI reads. **Constitution** is who they are and the rules that hold in every session. **Memory** is what the system knows. **Skills** are methods like this one. **Tools** are how the AI reaches other systems. **Focus** is what matters right now.

**This skill needs the owner's layers to know when to stay quiet.** The exclusion rule above, do not ask an outsider about anything that lives only in the owner's files, is unenforceable unless you know what their memory actually holds. Get that wrong and you send a stranger a question about their finances, their family or their half finished project, and you get back a confident, generic answer that is worse than your own and now carries the authority of a second opinion.

**The self-invocation threshold has the same problem in the other direction.** "A decision that costs money or is hard to reverse" is not a number until the owner names one, and where that line sits depends on their runway, which lives in memory, not in the question in front of you. Read the constitution for the rule and memory for the amount, then apply both without asking again.

### CONSTITUTION

One line makes this skill exist. Where it goes depends on how central it is to the owner.

**Self-invoking skills belong in the always loaded core.** That is unusual, and it is the case here: a skill that only fires when the owner remembers to ask for it is not this skill, it is a slower version of a search. If it lives only in the skills index, you will never trigger it in the moments that matter, because those are the moments when nothing feels wrong.

**Occasional, owner-invoked only:** if the owner wants it that way, put it in the skills index the core already links to, and tell them plainly what they gave up.

Either way the line is the same:

```
VERIFY7 / V7 {question}, also self-invoked. Ask a foreign judge that never sees my draft answer, report in 3 lines, line 3 = does it change my mind. Spec: skills/verify7/SKILL.md
```

A skill the AI cannot see when the trigger fires does not exist. A core stuffed with lines nobody triggers is broken the other way.

### MEMORY

**This skill barely writes.** Reports live in the conversation. Keep one line per run somewhere the owner can read it: date, question, verdict. That log is not bookkeeping, it is the only way to find out whether the questions are any good, and there is a specific tell in it, described in MAKE IT YOURS below.

**What does not belong in memory:** the judge's answer stored as fact. It is one model's opinion at one moment, and filed as knowledge it will be read later as something the system verified. If a check settles something permanently, write the settled fact and how it was established, not the transcript.

**What rots fastest:** which judge is free, what the limits are, and which one can see images. Those change without notice. Store what you used, so a surprising result a month later can be traced to the model rather than to the question.

### TOOLS

The layer is called Tools because a tool is what the model finally calls. How it arrives keeps changing: today usually an **MCP server** or a **connector** the client installs, before that a hand written API wrapper. Name the mechanism when you tell the owner what you are about to use, and do not let the mechanism rename the layer.

> 🔒 **The independence gate. The judge never sees your draft answer, your conclusion, or the result you hope for.** Models agree with whatever is embedded in the question, so a leading question is worse than no question at all: it returns an answer you want to believe and charges you nothing for it. You may pass facts, numbers and constraints as context. You may not pass the conclusion.

**There is deliberately no approval gate.** The calls cost nothing or pennies, and cheap verification must not become bureaucracy. If every check needed the owner's permission, you would stop checking and the skill would quietly die.

---

## HOW IT RUNS

Steps for you, the assistant. Goal level, not code level. Build the thinnest script or workflow your system allows.

**0. Know your environment first.** If you can run commands or call an API, use a judge directly. If you are in a plain chat with no tools, you cannot call anyone: tell the owner plainly that this is not really installed yet, offer relay mode for this one check, and remind them of the two minute key setup. **Never pretend to verify what you cannot reach.**

**1. First ask: can I check this myself?** Anything a file read, a command or an API call can settle gets checked, not debated.

**2. Invoke yourself in these five moments:** you are about to state something confident that you cannot check directly; a decision costs money or is hard to reverse; there is text inside an image that must be read exactly; the owner asks "is that really true"; you sense you are improvising, the answer coming from form rather than knowledge.

**3. Do not invoke for taste, personal decisions, or anything that lives only in the owner's files.** A foreign model has no context there and is worse, not better.

**4. Write a clean question.** Not "I think the answer is X, do you agree?" but "What is the answer?". Not "Is the text in this image correct?" but "Transcribe the text you see in this image." Strip every judgment and adjective, keep only entities, numbers and constraints. **Test before sending: could a stranger tell from the question alone which answer you hope for?** If yes, rewrite it.

**5. Pick the judge.** Image involved: one that can see images. Everyday check: whichever is free. Expensive or irreversible decision: ask two, because disagreement between judges is information, not a problem to smooth over.

**6. Report in exactly three lines:**

```
Asked {judge}: "{question}"
Answer: {short summary}
Does it change my answer: YES, changing to X / NO, staying, because Y.
```

Line 3 is mandatory. Without it the third opinion is decoration. Say what the check changed, not that it happened.

**7. If two judges disagree, say so openly:** judge A says X, judge B says Y, I stay with Z because.

**8. If the judge is right, say so.** "YES, changing to X" is the skill succeeding, not failing. A check that never changes anything is not proof you were right, it is a sign the questions are leaking your answer.

---

## DEFINITION OF DONE

1. **The direct check ran first**, or you can say why the question could not be settled that way.
2. **The question leaked nothing:** no draft answer, no conclusion, no hoped for result.
3. **Three lines, and the third one exists**, naming what changed or why nothing did.
4. **Disagreement between judges is stated**, never averaged into a smooth summary.
5. **One line in the log:** date, question, verdict, and which judge answered.

Missing the second means you ran a ritual. Missing the third means you ran a ritual and reported it as diligence.

---

## MAKE IT YOURS

1. **Swap judges freely.** Any model works as long as it has not seen the conversation. Independence is the requirement, not the brand.
2. **Add a money threshold.** Auto-invoke on any purchase, subscription or commitment above an amount the owner names once.
3. **Review the log monthly, and watch for one thing.** If line 3 never says YES, your questions are probably leaking the answer. Tighten step 4 rather than congratulating yourself.
4. **Decide the two lists with the owner:** what always gets checked, and what never leaves their system. Both written down, both short.

---

*Assistant, on ingest: save this in the skills layer in your own format, add the trigger line to the skills index, and confirm to the owner in one line what you saved, where, and the trigger.*

---

**Skill by Egils Boitmanis, [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full library: [github.com/arete-aios/aios](https://github.com/arete-aios/aios)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
