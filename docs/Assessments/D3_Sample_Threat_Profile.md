# D3 — Sample Threat Profile

**Handed out with the D3 assignment. This is a model of *form*, not of content.**

Same firm as the **D1** and **D2** samples — Thorne & Balch, structural engineers — one
week after the register. **Not** Wumpus Telehealth; nothing to do with our scenario.

Read the **change log** most carefully. That table is the whole reason D3 exists: it is
where a threat profile stops being an essay and starts being a revision of work you
already turned in.

Fields and layout: `D2_D3_Register_Template.md`. Graded on `Program_Memo_Rubric.md`.
**250–400 words** of memo; the three tables are exempt.

---

## The memo

**To:** Ellis Thorne, President; Warren Ochoa, CFO
**From:** R. Keene, Security Program Lead
**Date:** March 24
**Subject:** Threat profile — who would actually come at us, and four changes to the register

Ellis, you asked whether we are a target, and the insurer's renewal form asks the same
thing in worse English. The honest answer is **no, and it does not help us.**

Nobody has chosen Thorne & Balch. What is happening is that a large number of criminal
operations are checking a large number of small professional firms, continuously, at
almost no cost, and the only thing that distinguishes us from the firm across the street
is what they find when they try ours. That is a better problem to have than being
targeted, because it is one we can change.

**Who I am planning against** is the financially motivated crew in the table below, for
one reason I can evidence: the opportunity is documented in our own inventory, and the
intent is established at industry scale by the insurer's loss data. I am also planning
against the careless insider — not the malicious one, which is the correction below.

**Who I am not planning against**, on the record: a competitor after our detailing work,
and activists opposed to the transit alignment. Both get raised in this office. Neither
has shown any intent toward this firm, and the controls that would address them are
already on the register for better reasons. If either of you disagrees, I would rather
argue about it now than discover in October that you assumed I had it covered.

**What changed.** Walking the chain step by step produced one finding I did not expect
and did not want: **the "would we know" column is empty at every step.** That is a
different and worse result than any single row of my register showed, and it is why I am
**withdrawing my own recommendation to accept R7.** Four rows move; the change log says
which and why.

**What this profile cannot tell me:** the right-hand column assesses systems nobody has
instrumented, so every cell in it is an inference, not an observation.

---

## Table 1 — who we plan against

| Actor | Capability (basis) | Intent (basis) | Opportunity (basis) | Plan against? |
|---|---|---|---|---|
| **Financially motivated criminal crew** | Low and cheap — a lure and a password. Assumed, not evidenced. | **Established at industry scale.** Insurer renewal questionnaire Q9/Q14 names credential theft and ransomware as the most frequent and most costly losses in our professional class. | **Documented in our own inventory.** No second factor on email (§4); servers reachable from every workstation (§2); no retained logs (§6). | **Yes — primary.** All three present, and two of the three are evidenced from our own documents rather than assumed. |
| **Careless insider** (not malicious) | By definition present — it is our own staff. | Not applicable; there is no intent. The mechanism is convenience. | Four unmanaged branch drives (§3); nine unassessed collaboration services (vendor inventory); no offboarding checklist (§5). | **Yes — secondary.** The volume case. Someone emailing a drawing set to a personal account to work on it Sunday does more damage per year than a saboteur would. |
| **A competitor seeking proprietary detailing work** | Moderate, if they wanted to. | **No evidence toward this firm.** And much of the work product becomes visible in permitted public filings regardless, which undercuts the premise. | Would exist — see the careless-insider row; the same gaps serve both. | **No.** Declined. The exposure is real, the adversary is not evidenced, and the treatments are already funded under R4 and R5 for reasons I can defend. |
| **Activists opposed to the transit alignment** | Low against systems; their demonstrated methods are public and physical. | **No demonstrated intent toward us**, and no monetisation path. We are a subcontractor, not the project sponsor. | Limited. Public-facing exposure is a website Facilities does not even own. | **No.** Declined, and I want the reason recorded: this gets raised in this office because it is easy to picture, which is not evidence. |

---

## Table 2 — the chain

Primary actor: the financially motivated crew. **Five steps** — enough to be an analysis,
not a transcription. Technique identifiers looked up at **attack.mitre.org**; confirm
them yourself, because sub-technique names move between releases.

| Step | Tactic | Technique (ID) | Would it work here? (source) | Would we know? (source) |
|---|---|---|---|---|
| **1** | Initial Access | Phishing: Spearphishing Link (**T1566.002**) | **Yes.** Email has no second factor, so one engineer's password is the whole barrier. *(Inventory §4; register R2)* | **No.** We have no mail-reporting process and no retained mail logs; a reported lure goes to whoever opens the shared mailbox. *(Inventory §6)* |
| **2** | Credential Access | Valid Accounts (**T1078**) | **Yes.** With a working password they are not attacking anything — they are signing in. *(Inventory §4; register R2)* | **No.** No retained authentication logs, so a successful sign-in from anywhere looks like Tuesday. *(Inventory §6; register R7)* |
| **3** | Discovery | Network Service Discovery (**T1046**) | **Yes.** The drafting servers are reachable from every office workstation and from the branch VPN. *(Inventory §2; register R1)* | **No.** No network or host detection of any kind. *(Inventory §6 — "nothing to inventory")* |
| **4** | Collection | Data from Network Shared Drive (**T1039**) | **Yes.** Calculation records and full drawing sets, no access control beyond share permissions. *(Inventory §2, §3)* | **No.** The servers generate no retained access logs. **This is register R7**, and it is why R7 changed. *(Inventory §6)* |
| **5** | Impact | Data Encrypted for Impact (**T1486**) | **Yes**, and we would not recover quickly — the backup appliance is in the same building as the servers. *(Inventory §7; register R1, R8)* | We would know *immediately* — this is the one step that announces itself. **Which is the problem: the only step we detect is the last one.** |

> **Techniques, not procedures.** I cannot tell you which email it will be. I can tell
> you today that email with no second factor behind it is a working front door, and that
> is the part a profile written in March is allowed to claim.

---

## Table 3 — register change log

Four rows move. The updated register is attached with these changes applied.

| ID | Change | From → To | Why the profile changed my mind |
|---|---|---|---|
| **R2** | Re-ranked | **#2 → #1** | The chain shows R2 is *how R1 arrives*. Funding ransomware mitigation while email has no second factor is buying a better lock for a door somebody is opening with a key. R2 is also the cheaper of the two. R1 stays funded; it moves to second. |
| **R7** | **Re-scored and re-treated** | Moderate / **Accept** → Serious / **Mitigate** | I recommended accepting this two weeks ago and I was wrong. Read down the right-hand column of the chain: we would not detect steps 1 through 4. R7 is not a standalone investigative risk — it is **the reason every other row's duration is unbounded.** Withdrawing my own acceptance, with Ellis's agreement, and asking for basic authentication and file-access logging before the renewal. |
| **R4** | Re-ranked | **#4 → #7** | I ranked the departing engineer who deliberately takes files on how vividly I could picture it. The evidence says the *careless* insider dominates by volume and the deliberate one is rare. The row stays — it is still real — but lower, and the treatment now addresses accidental egress first, which is the same fix and covers both. **This is a row I moved down, and it was the hardest one to write.** |
| **R10** | **Added** | — → added | The actor analysis asked a question the register never had: what does the crew *do* with mailbox access? For a firm that sends invoices, change orders and seal authorisations by email, the answer is fraud conducted in our name against our own clients — a contractual and reputational loss distinct from anything R2 described. That consequence had no row. It does now, owned by me, treatment Mitigate, sourced to client agreements TB-204/211/230. |

---

## Why this profile works

Keyed to the five rubric items.

**1. Answers the actual ask.** All five elements present: actors with a basis, a declined
actor (two, in fact), a five-step chain with both columns cited, a change log with four
entries, and a stated limitation. **And the register actually changed** — which is the
element most often missing. A D3 submitted next to an untouched D2 has not been done.

**2. Decision-ready.** The subject line names the deliverable *and* the consequence
("four changes to the register"). The first paragraph answers the President's actual
question in six words — *"no, and it does not help us"* — and then explains why that is
the better answer. Nothing defines what a threat actor is.

**3. Calibrated.** Three places to look. The limitation paragraph is one sentence and it
is a real limitation, not a disclaimer: *"every cell in it is an inference, not an
observation."* The capability column for the primary actor says **"assumed, not
evidenced"** — labelling the weakest of the three legs instead of dressing it up. And
step 5's detection cell refuses the easy claim: we *would* know, and that is stated as
bad news rather than reassurance.

**4. Specific to that firm.** Permitted public filings undercutting the competitor
premise. A transit alignment. A website Facilities doesn't own. Invoices and seal
authorisations sent by email. Three client agreements by number. **The declined actors
are the ones people in that office actually raise** — which is the test of whether the
declining was real work or a formality.

**5. Usable in the report.** The change log *is* §4's required change log. It pastes in.
Permanent IDs are what make that possible; a profile that said "the one about the file
server" would not survive a second revision.

### Three things worth stealing

**Withdrawing your own recommendation.** R7 is the best row in the change log because the
author argued for accepting that risk two weeks earlier, in writing, to the same two
readers — and then said *"I was wrong,"* in one clause, with the evidence that changed it,
and moved on. No defensiveness and no paragraph of explanation. That is what calibrated
confidence looks like when it costs something.

**The declined actors are specific and unflattering.** *"This gets raised in this office
because it is easy to picture, which is not evidence."* The memo declines the two
adversaries that are socially expensive to decline, and invites disagreement **now**
rather than discovering an assumption in October. Declining nation-states nobody
mentioned would have been free and worth nothing.

**The chain's second column is the finding.** Step by step, the "would it work here"
answers are ordinary — plenty of firms look like that. The "would we know" column is
empty four times out of five, and **that result is not visible in any single register
row.** It only appears when you walk the steps in order, which is the entire argument for
doing this exercise rather than just listing threats.
