# L02 Worksheet — Reconnaissance & Asset Inventory

**Name:** ______________________  **Date:** ____________

**How to submit:** type your answers into this document, then save it as a **PDF**
(Word: *File → Save As*, choose **PDF**) and upload the PDF to Canvas. Fill it in
*as you work* — it asks for the exact commands you ran.

Graded for completeness with randomized spot checks. Keep it tight — this should
feel like ~2 pages. Values go in the Canvas quiz; this worksheet is where you
show *method*, *judgment*, and *limits*.

---

## A. Environment & verification

1. Command you ran to confirm the segment was up, and how many containers were `Up`:

   `______________________________________`  → containers Up: ____ / 6

2. Your recon box's own IP on the segment (from `hostname -I`): `172.28.0._____`

3. In one line: why does your own recon box show up in a host-discovery sweep,
   and why shouldn't it go in the asset register?

   ______________________________________________________________________

---

## B. Findings

For **each** finding: the exact command, what you *observed* (raw output),
what you *inferred* from it (observation ≠ inference), and the value you
submitted.

| # | Finding | Command used | Observation (what the tool showed) | Inference (what it means) | Value submitted |
|---|---|---|---|---|---|
| F1 | Live **asset** hosts on the segment | | | | |
| F2 | Service **+ version** on `172.28.0.10` : 80 | | | | |
| F3 | TCP **port** of the legacy cleartext remote-login service | | | | |
| F4 | TCP **port** of the uninventoried message/telemetry broker | | | | |
| F5 | **Biggest-risk** host (value + justification below) | | | | |

**F5 justification (2–3 sentences).** Which host, and *why* is it the biggest
risk — weigh what it exposes, whether it requires credentials, and the host's role:

____________________________________________________________________________

____________________________________________________________________________

---

## Asset register (all hosts — the boring ones too)

| IP | What it appears to be | Open port(s) | Service / version |
|---|---|---|---|
| 172.28.0.10 | | | |
| 172.28.0.20 | | | |
| 172.28.0.30 | | | |
| 172.28.0.40 | | | |
| 172.28.0.50 | | | |

---

## C. Corroboration

Pick **one** finding and confirm its value a **second, independent way** (a
different tool or signal than the one in section B). Name the finding, the
second method, and whether the two agreed.

- Finding: ____   Second method: ______________________________
- Agreed? ☐ yes ☐ no — if no, what did you do about it? ______________________

---

## D. Limits — what this recon does **NOT** show *(graded)*

Answer at least **two**:

1. You found open ports and versions. Name one thing about these hosts a port
   scan **cannot** tell you about their actual security. ____________________

2. Your host count is a point-in-time snapshot. Give one reason it could be
   **wrong tomorrow** even if the scan was correct today. ____________________

3. A version banner can lie or be absent. How much confidence should you attach
   to a service version from `-sV`, and why? ______________________________

---

## E. How this feeds the security program

This register is raw material for **§4 — Risk Assessment** of the Security Program
Report, and Week 3's risk register is built directly on top of it: you cannot score
a risk against an asset you never listed.

1. Your register records IP, apparent role, open ports, and service/version. Name
   **one thing a risk assessment will need about these hosts that a port scan
   cannot tell you** — and say how you would actually find it out.

   ____________________________________________________________________________

2. One sentence: what's the first *governance* action this register makes
   possible? ______________________________________________________________
