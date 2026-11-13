---
name: cc7
description: "CC7: build a private Command Center or selected view from existing AIOS sources, or optionally set up and update starter B Health."
license: CC-BY-4.0
metadata:
  version: "1.1.0"
---

# CC7 · Command Center and Health

## Choose the requested work

- **Build my Command Center** or **copy this demo/view**: follow
  [the portable Command Center recipe](references/command-center.md). It reuses
  existing sources, a fictional EN/LV template and local-first checks. This
  explicit request authorises preparing the selected view; it does not opt in
  to starter B Health, connect accounts or publish private data.
- **Set up CC7 Health**, **B + YES + CC7**, or an update to an existing Health
  register: follow the unchanged Health workflow below.
- **Open/read Health** remains read-only and never triggers setup.

## Starter B Health

CC7 is an optional local view for starter **B**. It shows the last recorded
audit for Constitution, Memory, Skills, Tools, Focus, and the EXIT7 feedback
loop. The source files retain the actual work and decisions.

## Set up once

1. Wait for an explicit choice: `B + YES + CC7` during onboarding or
   **Set up CC7** after a B install. Finish the five onboarding steps first.
   Asking to open Health is a read request. If it is absent, give the setup
   command and prerequisite instead of creating files.
2. From the AIOS folder, run this with Python 3.9 or newer:

   ```sh
   python3 00-system/aios/skills/cc7/health.py --init
   ```

3. Read back `04-tools/cc7/audits.json` and `04-tools/cc7/health.html`. Check
   all six sections and their source links. Record CC7 as installed in the
   existing `ONBOARDING.md` with `[Health](04-tools/cc7/health.html)` and
   add `[Health](cc7/health.html)` to `04-tools/_tools-CONTEXT.md`. A failed
   run leaves CC7 pending. If this client cannot run Python, give the command
   and wait for a successful read-back before reporting it installed.
4. Give the owner a clickable Health link to `04-tools/cc7/health.html` from
   the AIOS root. They can open the HTML file directly. It works offline, and
   `#exit7` goes straight to the feedback loop.

Setup creates the audit register and page. Empty rows show **Not yet audited**.
Opening the page or finding a source file does not count as an audit.

## Record and refresh

Use the existing audit or project source. For each section actually checked,
edit just its entry in `04-tools/cc7/audits.json`:

- `audited_on` is the actual check date in `YYYY-MM-DD`. Leave it `null` if
  no check has been done.
- `scope` states what was checked and `result` states what happened, including
  any problem or limit. Keep both short.
- `evidence` lists the existing evidence files, using paths from the AIOS
  root. The page links to those files without copying their contents.
- `open_decisions` can record an approval that is pending or the next check.

For EXIT7, link to the improvement and the follow-up that showed its effect.
While an improvement is proposed or applied and awaiting verification, use
`open_decisions` for its current state and next check. Keep any earlier verified
date, result, and evidence. After the next relevant task confirms the effect,
record the actual verification date and evidence and update the pointer in
`ONBOARDING.md`. See [EXIT7 feedback loop](../exit7/SKILL.md#feedback-loop).

Regenerate and read back Health after an authorised status update:

```sh
python3 00-system/aios/skills/cc7/health.py
```

If validation fails, correct the register or its missing link and rerun. The
last generated page is preserved on validation failure. The constitution
governs status updates and approvals. CC7 reads the register and checks file
paths locally. It does not publish the page or schedule audits.
