# L03 Worksheet — Vulnerability Scanning & Triage

**Name:** ______________________  **Date:** ____________

**How to submit:** type your answers into this document, then save it as a **PDF**
(Word: *File → Save As*, choose **PDF**) and upload the PDF to Canvas. Fill it in
*as you work* — it asks for the exact commands you ran.

Graded for completeness with randomized spot checks. Keep it tight — ~2 pages.
Values go in the Canvas quiz; this worksheet is where you show *method*,
*judgment*, and *limits*.

---

## A. Environment & authorization

1. Command you ran to bring the lab up, and how many containers were `Up`:

   `______________________________________`  → containers Up: ____ / 4

2. What range were you authorized to scan? `____________________`

3. In one line: name one thing that could go wrong if you ran tonight's scanner
   against a host outside that range. ____________________________________

---

## B. What's listening

Fill this in from `nmap -p- --open` **and** your own `curl -sI` of each host.
The `Server:` column is what the host *says* about itself.

| IP | Open TCP port | `Server:` header, exactly as returned |
|---|---|---|
| 172.29.0.10 | | |
| 172.29.0.20 | | |
| 172.29.0.30 | | |

---

## C. Findings

For **each** finding: the exact command, what you *observed* (raw output), what
you *inferred* from it (observation ≠ inference), and the value you submitted.

| # | Finding | Command used | Observation (what the tool showed) | Inference (what it means) | Value submitted |
|---|---|---|---|---|---|
| F1 | File exposed by directory indexing | | | | |
| F2 | `Server:` banner on `172.29.0.20` | | | | |
| F3 | Port of the unauthenticated status service | | | | |
| F4 | Host whose scanner finding is **wrong** | | | | |
| F5 | Host to remediate **first** (justify below) | | | | |

**F4 — how do you know?** The scanner believed a banner. You didn't. Name the
**second, independent signal** you used, and say what it showed:

____________________________________________________________________________

**F4 — what it does *not* mean (graded).** The finding was false. In 1–2
sentences: does that make that host *fine*? What, if anything, is still wrong
there?

____________________________________________________________________________

**F5 justification (2–3 sentences).** Which host, and why first? Weigh confirmed
vs. potential exposure, what's actually at stake, whether anything is already in
the way, and what the fix would cost:

____________________________________________________________________________

____________________________________________________________________________

---

## D. Limits — what a scan does **NOT** tell you *(graded)*

Answer at least **two**:

1. Your scanner reported a severity for each finding. Give one reason a tool
   **cannot** know how severe something is for *this* organization.
   ____________________

2. A scan came back clean for a host. Name one reason that is **not** the same
   as "that host is secure." ____________________

3. You scanned from inside the lab network. Name one thing that tells you
   **nothing** about — and one thing it might **overstate**. ____________________

---

## E. How this feeds the security program

Tonight's triaged findings are evidence for **§4 — Risk Assessment**, and they
are the kind of thing your **D2 risk register** is built from: each one can
become a row, with an owner and a treatment decision.

1. Pick **one** of tonight's findings and write it as a **risk statement** in the
   form Tuesday's lecture used — *[threat source] does [threat event], which
   works because of [vulnerability], causing [impact]* — plus a likelihood, and
   the reason that anchors it.

   ____________________________________________________________________________

   ____________________________________________________________________________

2. For that same finding, which treatment do you recommend — **mitigate,
   transfer, avoid, or accept** — and who should own it? One sentence.

   ____________________________________________________________________________
