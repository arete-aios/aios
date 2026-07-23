# Layer 4 · Tools

**How the AI reaches anything that is not its own files.**

The layer is called Tools because a tool is what the model finally calls. How they arrive keeps changing: today usually an MCP server or a connector the client installs ([modelcontextprotocol.io](https://modelcontextprotocol.io)), before that a hand written API wrapper, next year something else. **Name the mechanism when you use one, and do not let the mechanism rename the layer.**

---

## What belongs in it

- **Read access to files**, which is the only one most people ever need.
- **Connectors to systems the owner already lives in:** calendar, mail, a spreadsheet, a task tool, a database.
- **Fetching:** a live page, a video, a search result.
- **Publishing:** a static site, a deck, an outgoing message.
- **The credentials, kept beside the content folder and never inside it.** The content folder must survive being copied somewhere else. Keys must not travel with it.
- **An honest note per tool: what happens when it is missing.** Every method should have a mode that runs with no integrations at all, usually by asking the owner for the data instead of fetching it. The method is the value. The automation is convenience.

---

## What does not belong in it

- **The method.** How to decide, judge, structure or write is layer three. Tools are the last inch: the call itself.
- **A tool installed before a skill needs it.** Connectors accumulate faster than they get used, and every one is a permission granted, a surface to maintain, and something to be surprised by later.
- **An assumption that a tool is alive.** Integrations die silently: a token expires, a machine is rebuilt, an API changes a field. A tool whose status was last checked six months ago is a guess.
- **Anything that spends money, sends to another person, or deletes, without a written approval gate.** Gates belong inside the method, stated in words, and they do not relax because a batch is large. A large batch is the reason the gate exists.
- **A shell one liner the owner is asked to run blind.** No method worth having needs that.

---

## How you know it is working

**The honest test is subtraction: turn one off and see whether the method still runs.** If it stops entirely, the method was never written down, only automated, and it will disappear the day the tool does.

Three further signs:

1. **The owner can name every tool that can act in their name**, and every gate on it. If the list is longer than they expected, the layer has outgrown its owner.
2. **Each connected tool has been used in the last month.** Anything older is a dependency without a benefit.
3. **The AI names the mechanism before using it.** *I am about to send this through your mailbox connector.* Not *I will handle it.*

---

## The trap this layer sets

**It is the most visible layer and the least important one.** Integrations are demonstrable, they feel like progress, and they produce the impression of a system where none exists. The constitution needs no tools at all. Memory needs a folder. The daily loop needs nothing but a file that can be written.

When someone's second brain is impressive to look at and nothing has changed in their week, this layer is almost always where the effort went.

**Build the method first, then automate the part that hurts.** Not the other way round.

---

## Which skill maintains it

**No single skill owns this layer, by design.** Each skill carries its own requirements section, stating what it needs, what the setup costs in real time, and what it does when nothing is connected. That keeps the truth about a tool next to the method that uses it, rather than in a list that goes stale.

**`audit7`** is the periodic check: what is connected, what has permission to act, what has not been used, what has quietly died since the last look.

---

**Built by Egils Boitmanis with [FullDigital](https://fulldigital.me), a Latvia registered nonprofit association that teaches people to build an AI operating system they own.**
What an AIOS is: [fulldigital.me/aios](https://fulldigital.me/aios) · The full skill library: [github.com/arete-aios/skills](https://github.com/arete-aios/skills)
Licensed CC BY 4.0. Use it, change it, ship it. Keep the attribution.
