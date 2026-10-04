# §4 Templates — Risk Register (D2) and Threat Profile (D3)

**Handed out with the D2 assignment. Used again, unchanged, for D3.**

Both deliverables feed **§4 — Risk Assessment** of your program report. D2 *creates*
that section; D3 *revises* it. These templates exist so that revision is possible.

Graded on `Program_Memo_Rubric.md` (10 pts, five items). **250–400 words of memo** for
each deliverable — **the tables do not count against the word budget.**

---

## Why you're being given columns at all

You could invent your own, and a one-off register would be fine. But §4 gets rewritten
**six times** between February and finals week, and the report rubric requires it to
carry *"a change log: risks added, re-scored, or retired during the year, and why."*

That has one hard prerequisite: **every risk needs a name that doesn't change.** If your
register's rows are identified only by their wording, then the first time you re-score
one you'll be writing "the one about the file server" — and by April you'll have three
rows that could be. So:

> **The point of these columns is that §4 assembles by concatenation, not by rewriting.**
> Fill them in now and your final report's §4 is a paste plus a change log. Don't, and
> you will rebuild it in May from eight memos that don't line up.

Two fields do that work and are easy to miss, so they're called out:

- **ID** (`R1`, `R2`, …) — permanent. **Never renumber and never reuse.** A retired risk
  keeps its ID and gets a status of *Retired*; the gap in the sequence is information.
- **Source** — where the fact came from. One short citation per row. It is the difference
  between a register and a list of worries, and it is the first thing a grader looks at.

**Use these field names.** The layout is up to you (see below); the fields are not.

---

## D2 — the risk register

### The fields

| Field | What goes in it | Why it's there |
|---|---|---|
| **ID** | `R1`, `R2`, … Permanent, never reused. | So D3 and every later revision can refer to this row. |
| **Risk statement** | One arguable sentence with SP 800-30's five parts: threat source · threat event · vulnerability · adverse impact · likelihood. | A topic word ("Phishing") can't be argued with. A sentence can. |
| **Likelihood (why)** | A band — e.g. *Likely* — **and the reason that anchors it.** | So a reader can disagree with the *reason* and one of you can go find out. |
| **Impact (why)** | A band — e.g. *Serious* — **and what it would actually cost**, in business terms. | "Impact 4" is not a consequence. "We lose the contract" is. |
| **Owner** | A person, **by name**. | "IT" is not a person and cannot be asked how it's going. |
| **Treatment** | Exactly one of **Mitigate / Transfer / Avoid / Accept**. | The box being filled is what makes this a register. |
| **Status / next review** | Where it stands, and **a date**. | An unreviewed register is a historical document. |
| **Source** | The questionnaire item ID, packet section, your own asset inventory, or the base-rate citation. | Item 4 of the rubric. An uncited row reads as invented. |

### No multiplied risk score

There is no score column and you should not add one. A 1–5 likelihood times a 1–5 impact
produces a number nobody can interpret — *"a risk score of twelve. Twelve what?"* If you
need to communicate ranking, **rank the rows** and say why the top one is on top. That's
what the memo is for.

### Layout A — a table *(preferred)*

Eight columns is wide. **Set the page to landscape.** Copy this and fill it in:

```
| ID | Risk statement | Likelihood (why) | Impact (why) | Owner | Treatment | Status / next review | Source |
|----|----------------|------------------|--------------|-------|-----------|----------------------|--------|
| R1 |                |                  |              |       |           |                      |        |
| R2 |                |                  |              |       |           |                      |        |
| R3 |                |                  |              |       |           |                      |        |
```

### Layout B — stacked blocks *(equally acceptable)*

If a wide table fights your word processor, use one block per risk. **Same fields, same
grade.** The grader needs the fields, not the shape.

```
R1 · [risk statement — one arguable sentence]
     Likelihood:  [band] — [why]
     Impact:      [band] — [what it costs]
     Owner:       [name]
     Treatment:   [Mitigate | Transfer | Avoid | Accept]
     Status:      [where it stands] · next review [date]
     Source:      [citation]
```

### How many rows

**At least 6–10. More are welcome.** Six to ten is a sensible first pass, not a ceiling —
real registers run to hundreds of rows and nobody calls that a defect. **Thirty rows of
real, owned, decided risk is excellent. Thirty rows of boilerplate is worse than six
honest ones.** The floor is there to discourage padding, not to cap effort.

---

## D3 — the threat profile

D3 adds three tables to §4 and **changes rows in the one you already wrote.**

### Table 1 — who you plan against

| Field | What goes in it |
|---|---|
| **Actor** | The type, not a group name. *"Financially motivated criminal crew."* |
| **Capability (basis)** | What they can do, and how you know. Usually: assumed, and cheap. |
| **Intent (basis)** | Do they want to — **toward a company like this one?** This is where the base-rate citation goes. |
| **Opportunity (basis)** | What in *our* environment lets them. **Cite the document.** |
| **Plan against?** | **Yes / No**, and one line of why. |

```
| Actor | Capability (basis) | Intent (basis) | Opportunity (basis) | Plan against? |
|-------|--------------------|----------------|---------------------|---------------|
|       |                    |                |                     |               |
```

> **At least one row must say No.** Deciding *not* to build the program around an
> adversary is a decision, and it has to be written down for the same reason an accepted
> risk does: so that when somebody asks in six months why your program doesn't address
> it, the answer already exists on paper with your name on it. **It is a graded element.**

### Table 2 — the chain

**4–6 steps**, in the order an adversary would need them. One row per step.

| Field | What goes in it |
|---|---|
| **Step** | 1, 2, 3 … |
| **Tactic** | The adversary's goal at that moment. *Initial Access, Discovery, Impact…* |
| **Technique (ID)** | Name **and** identifier, looked up yourself. |
| **Would it work here? (source)** | Yes/No/Partly — **and the citation.** |
| **Would we know? (source)** | Would anyone detect it — **and the citation.** |

```
| Step | Tactic | Technique (ID) | Would it work here? (source) | Would we know? (source) |
|------|--------|----------------|------------------------------|-------------------------|
| 1    |        |                |                              |                         |
```

**Techniques, not procedures.** A profile written before anything has happened can only
operate at the technique layer — "phishing," not a particular pretext. Nobody can tell
you in advance which email it will be. Everybody can tell you, today, whether email with
no second factor behind it is a working front door.

**"Unknown" is a real answer in the right-hand column**, and often the correct one. If
nobody is assigned to look, say so and cite it. A column confidently filled with "yes,
we'd see it" for an environment nobody has instrumented is the most common way to lose
points on this deliverable.

### Table 3 — the register change log

**This is the table that makes D3 count as a revision**, and the one the final report's
§4 inherits directly. **At least two rows.**

| Field | What goes in it |
|---|---|
| **ID** | The D2 row you're changing — or a new ID, continuing the sequence. |
| **Change** | **Added · Re-scored · Re-ranked · Re-treated · Retired** |
| **From → To** | The old value and the new one. For a new row, "—→ added." |
| **Why the profile changed my mind** | One or two sentences. **This is the graded part.** |

```
| ID | Change | From → To | Why the profile changed my mind |
|----|--------|-----------|---------------------------------|
|    |        |           |                                 |
```

> **A row you move *down* is as good an answer as one you move up** — better, usually,
> because it is harder to write and it proves you re-read your own work instead of
> appending to it.

**Then actually edit the register.** The change log records what you changed; it does not
replace doing it. Submit the updated D2 table with D3, with the changed rows' status
fields current.

---

## Anti-patterns — what loses points

| Looks like | Actually is | Rubric item |
|---|---|---|
| Rows with the Owner or Treatment cell blank | **A list, not a register.** The empty cell is the failure, at any row count. | 1 |
| `Likelihood 4 × Impact 3 = 12` | False precision — arithmetic on labels. | 3 |
| *"Ransomware — High"* | A topic word and a mood, not an arguable sentence. | 3 |
| Rows that would be true of any company in the industry | Padding. Dilutes the real rows and spends the reader's attention. | 4 |
| Every treatment is "Mitigate" | Not decisions — a wish list. Nobody ever chooses Accept, and practitioners use it constantly. | 1 |
| Every treatment is a purchase | A budget request wearing a register's clothing. | 1 |
| A lab hostname, IP, filename or digest in a row | **Category error.** The labs are training ranges; they supply method and finding *classes*, never facts about your employer. | 4 |
| The scariest row on top, with no evidence for its likelihood | Ranked by fear. An unverified likelihood presented as a high one. | 3 + 4 |
| D3 submitted with the register unchanged | D3's element 4 missing — the deliverable didn't do its job. | 1 |

---

## Worked examples

Read these before you draft. Both are set at **the same company as the D1 sample** —
Thorne & Balch, a structural engineering firm that is **not** our scenario and has
nothing to do with it. That continuity is the point: you can watch one program's §4 get
built and then revised, without being able to borrow a sentence of it.

| File | What it shows |
|---|---|
| `D2_Sample_Risk_Register.md` | A full D2 — memo plus a nine-row register — with a breakdown of why it scores where it does. |
| `D3_Sample_Threat_Profile.md` | A full D3 at the same company a week later: actors, chain, **and the change log showing four of those nine rows moving.** |

Read the second one's change log most carefully. It is the part of this course that is
hardest to see the point of in February and most obviously valuable in May.
