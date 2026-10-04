# D2 — Sample Risk Register

**Handed out with the D2 assignment. This is a model of *form*, not of content.**

The company below is **not** Wumpus Telehealth and has nothing to do with our scenario.
It is the same firm as the **D1 sample** — Thorne & Balch, structural engineers — two
weeks further on. That continuity is deliberate: you can watch one program's §4 get
built, and then watch `D3_Sample_Threat_Profile.md` revise it, without being able to
borrow a sentence of either.

Fields and layout: `D2_D3_Register_Template.md`. Graded on `Program_Memo_Rubric.md`.
**250–400 words** of memo; the register table is exempt.

---

## The memo

**To:** Ellis Thorne, President; Warren Ochoa, CFO
**From:** R. Keene, Security Program Lead
**Date:** March 17
**Subject:** Risk register v1 — the three I want funded before the June renewal

The asset and vendor inventory from my charter is done, and it changed my mind about two
things. The register below has nine risks. Here are the three I am asking you to act on,
and why those three.

**R1 — ransomware on the drafting servers.** This is first because it is the only risk
on the list that can stop us delivering. We seal and submit on dates set by permitting
authorities, not by us; a week of inaccessible calculation records on the Harbor Point
submission is a schedule failure with professional-liability consequences, not an IT
outage. The insurer's own loss data is what lets me call this *Likely* rather than
*Possible*, and I would rather cite theirs than mine.

**R2 — no multi-factor authentication on email.** I flagged this in the charter as a
priority and the inventory confirmed it is worse than I thought: email is where project
correspondence, client data and seal authorisations actually live. This is the cheapest
item on the register by a wide margin.

**R9 — business interruption cover.** Warren, your own figures say we can absorb about
five days. Nothing on this register says five days is the worst case. This is the one
risk I am recommending we **transfer** rather than fix, and June is when we can.

Two notes on what I have *not* done. I have not put a numeric score on anything — a
likelihood times an impact produces a number none of us could defend to the insurer.
And **R7 I am recommending we accept**, in writing, with a date: we have no logging on
the file servers and I do not think it is the best use of the next three months. I want
that on the record as a decision rather than an omission.

I will re-score this register after the renewal, and whenever something material changes.

---

## The register

*(Nine rows. Landscape. Ranked — R1 is the top of the list, not just the first ID.)*

| ID | Risk statement | Likelihood (why) | Impact (why) | Owner | Treatment | Status / next review | Source |
|---|---|---|---|---|---|---|---|
| **R1** | A financially motivated crew encrypts the drafting file servers, which works because the servers are reachable from every office workstation and we have no detection, making sealed calculation records unavailable and causing us to miss a permitted submission date. | **Likely** — our insurer's renewal questionnaire cites it as the most frequent loss in our professional class; two peer firms in the state have disclosed incidents since 2024. | **Severe** — a missed Harbor Point submission is a liquidated-damages exposure plus professional-liability risk, not a cost-of-recovery number. | M. Sowande | **Mitigate** | Segmentation scoped; quote pending · review **Apr 30** | Asset inventory §2 (server reachability); insurer renewal questionnaire Q14 |
| **R2** | An attacker who obtains one engineer's email password through a credential-theft lure reaches project correspondence, client data and seal authorisations, which works because email has no second factor, leading to confidential-information loss and fraud conducted in our name. | **Likely** — the insurer prices this loss most heavily of anything on their form; no second factor exists today. | **Serious** — client confidentiality breach, plus our name on any fraud that follows. | M. Sowande | **Mitigate** | Licensed; rollout starts Apr 7 · review **May 15** | Asset inventory §4 (authentication); insurer renewal questionnaire Q9 |
| **R3** | Calculation records held on unmanaged local drives at the three branch offices are lost to a single disk failure, which works because those drives are in no backup scope, causing permanent loss of the record behind a sealed drawing. | **Possible** — four such drives found; one is seven years old and has never been imaged. | **Severe** — a sealed drawing whose calculation record no longer exists is a defensible-design problem we cannot answer. | D. Pritchard | **Avoid** | Consolidation to the central servers, then wipe · review **Apr 15** | Asset inventory §3 (unmanaged endpoints) |
| **R4** | A departing engineer copies active project files to personal cloud storage on their way out, which works because we have no offboarding checklist and no egress visibility, causing client-confidentiality breach and loss of proprietary detailing work. | **Possible** — two departures last year; neither had a documented access revocation. | **Moderate** — contractual and reputational, concentrated on whichever client's project was taken. | R. Keene | **Mitigate** | Offboarding checklist drafted, unsigned · review **Apr 30** | Asset inventory §5 (account lifecycle); HR separation records |
| **R5** | A compromise at one of the nine project-collaboration services our teams signed up for independently exposes client project data, which works because none has been security-assessed and we hold no inventory of what each contains, causing a breach we would learn about from the vendor or from the client. | **Possible** — nine services found, none assessed; two hold full drawing sets. | **Serious** — notification obligation sits with us under three current client agreements. | N. Haddad | **Mitigate** | Inventory complete; assessment order set · review **May 31** | Vendor inventory (all 9 rows); client agreements TB-204, TB-211, TB-230 |
| **R6** | Anyone with physical access to the large-format plotting workstation can act as the shared drafting account, which works because that account is shared by design and its password is written on the cabinet, making any action taken through it unattributable. | **Likely** — the credential is on a label; the account is used daily. | **Moderate** — no confidentiality loss, but it removes attribution from a system that signs out plots. | M. Sowande | **Avoid** | Replace with per-user access on the queue · review **Apr 15** | Asset inventory §4 (shared accounts) — observed directly |
| **R7** | Unauthorised access to or deletion of files on the drafting servers goes unnoticed, which works because the servers generate no retained access logs and no one is assigned to review them, causing us to be unable to establish what happened or reassure a client that nothing did. | **Likely** — there is no logging, so the condition is certain; what is uncertain is whether anything has used it. | **Moderate on its own** — the harm is investigative and evidentiary rather than direct. | R. Keene | **Accept** | Accepted by E. Thorne, Mar 17, pending renewal · revisit **Jul 1** | Asset inventory §6 (logging) — nothing to inventory |
| **R8** | A fire or flood at the main office destroys both the drafting servers and their backup, which works because the backup appliance is in the same building thirty feet away, causing total loss of active project data. | **Unlikely** — no incident in eleven years; sprinklered building. | **Severe** — this is the one entry on the register that could end the firm. | M. Sowande | **Mitigate** | Offsite replication quoted at $4,100/yr · review **Apr 30** | Asset inventory §7 (backup topology) — observed directly |
| **R9** | A business interruption of more than roughly five days exceeds the cash we can absorb without borrowing, which works because our current policy's business-interruption limit was set when the firm was half this size, causing a liquidity event on top of the original incident. | **Possible** — conditional on R1 or R8 occurring; those are rated above. | **Severe** — a solvency question rather than an IT question. | W. Ochoa | **Transfer** | Raise BI limit at the **June 1** renewal · review **Jun 15** | W. Ochoa's cash-position memo, Mar 11; current policy schedule |

---

## Why this register works

Keyed to the five rubric items. Read this part as closely as the register.

**1. Answers the actual ask.** Nine rows, every cell filled. **No empty Owner and no
empty Treatment anywhere** — that is the single most common way this deliverable fails,
at any row count. The memo answers the question the table can't: *what are your top
three, and why those three.*

**2. Decision-ready.** The subject line is the ask. Three risks are named in the first
paragraph, each with a reason a non-specialist can act on. Nothing explains what a risk
register *is*. Warren is addressed directly where the row is his (**R9**), with his own
figure quoted back to him — which is how you get a CFO to read paragraph three.

**3. Calibrated.** Look at **R7**'s likelihood: *"there is no logging, so the condition is
certain; what is uncertain is whether anything has used it."* That sentence separates a
confirmed fact from an unverified one inside a single cell, which is exactly the Week-1
ladder doing work. Look at **R1**: the likelihood is anchored to **the insurer's** data,
not the author's intuition — *"I would rather cite theirs than mine."* And the memo
refuses to produce a numeric score, out loud, with a reason.

**4. Specific to that company.** Sealed submissions. Permitting dates. The Harbor Point
job. A password on a cabinet label. Four unmanaged drives, one seven years old. Three
client agreements by number. **Swap the firm's name for "Acme" and most of this stops
making sense** — which is the test. There is not one row here that could have been lifted
off a template.

**5. Usable in the report.** It drops into §4 and gets edited, not rewritten. Every row
has a permanent **ID** and a **Source**, which is what lets `D3_Sample_Threat_Profile.md`
come back a week later and move four of them without ambiguity.

### Three things worth stealing

**All four treatments appear.** Mitigate, Transfer (**R9**), Avoid (**R3**, **R6**) and
Accept (**R7**). A register where every row says "Mitigate" is usually a wish list rather
than a set of decisions. Note **R6** in particular: *Avoid* means removing the exposure —
the shared account goes away — which is cheaper than protecting it and almost never what
a security person suggests first.

**The accepted risk is a real decision.** **R7** names who accepted it (E. Thorne), the
date, the reason, and when it gets revisited. *"I want that on the record as a decision
rather than an omission."* Accept with no name and no date is a shrug with better
vocabulary.

**The scariest row is not the top row.** **R8** — the fire that could end the firm — is
rated *Unlikely* and sits eighth, and the register says plainly that it is the one entry
that could end the firm. It is still there, still owned, still funded at $4,100. *Rare is
not the same as ignorable, and frightening is not the same as first.*
