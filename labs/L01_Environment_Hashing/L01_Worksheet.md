# L01 Worksheet — Environment Setup & Hashing Warmup

**Name:** ______________________  **Date:** ____________

**How to submit:** type your answers into this document, then save it as a **PDF**
(Word: *File → Save As*, choose **PDF**) and upload the PDF to Canvas. Fill it in
*as you work* — it asks for the exact commands you ran.

Graded for completeness with randomized spot checks. Keep it tight — ~2 pages.
Values go in the Canvas quiz; this worksheet is where you show *method*,
*reasoning*, and *limits*.

---

## A. Environment gate

1. Command you ran to start the lab, and how many containers came up `Up`:

   `______________________________________`  → containers Up: ____ / 1

2. Paste the **last line** of `verify_env.sh` output (proof you cleared the gate):

   `______________________________________________________________________`

3. Did any tool report `MISSING`? ☐ no ☐ yes → which, and what did you do? ____________

---

## B. Findings

For **each** finding: the exact command, what you *observed*, what you *inferred*
(observation ≠ inference), and the value you submitted.

| # | Finding | Command used | Observation (what the tool showed) | Value submitted |
|---|---|---|---|---|
| F1 | Files in `evidence/` | | | |
| F2 | SHA-256 of `evidence/quarterly_report.txt` | | | |
| F3 | Exact duplicates of `dedup/reference.txt` | | | |
| F4 | File that **fails** checksum verification | | | |
| F5a | File matching the trusted baseline | | | |

**F5b justification (2–3 sentences).** The other `incident/` file's digest does
**not** match the baseline. What does that mismatch prove — and what does it *not*
prove (who changed it, when, whether it was malicious)? Why is the check only as
trustworthy as the baseline's own provenance?

____________________________________________________________________________

____________________________________________________________________________

---

## C. Same file, two fingerprints

You hashed `evidence/quarterly_report.txt` with **both** `sha256sum` and
`md5sum`. Paste both digests. In one line, why are they completely different even
though it's the same file?

- SHA-256: `__________________________________________________________________`
- MD5:     `__________________________________`
- Why different: ________________________________________________________________

---

## D. Limits — what hashing does **NOT** give you *(graded)*

Answer at least **two**:

1. A file's SHA-256 matches a digest a stranger emailed you. Name one thing this
   still does **not** tell you about whether the file is safe to open. ____________

2. `md5sum` and `sha256sum` both "verify integrity." Give one concrete reason you
   should **not** rely on MD5 to detect deliberate tampering. ____________________

3. Your duplicate count in F3 is a snapshot. Give one reason two files that match
   today could stop matching tomorrow — and why that's the point of re-hashing.
   ____________________

---

## E. How this feeds the security program

1. Integrity is one leg of the **CIA triad**. In one sentence, give a real example
   of something at a company like Wumpus whose *integrity* you'd want to verify
   with a hash (not its confidentiality). ______________________________________

2. One sentence: you now have a working lab environment and can fingerprint a
   file. What's the first thing next week's asset-inventory work needs from you
   that this lab just made possible? ______________________________________
