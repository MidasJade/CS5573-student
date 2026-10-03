# CS5573 — Security Program Report Template

**Issued Week 1 · The skeleton your weekly memos fill in · Final assembly due end of finals week**

## How to use this template

This is the structure of your final Security Program Report for Wumpus Telehealth. You do not write this report at the end of the semester — you grow it. Most weeks, your program memo is a draft contribution to one of these sections; each dispatch tells you which section that week feeds. Keep a living copy of this document from Week 1, drop each memo into its section as you write it, and revise earlier sections as the program (and the company's year) teaches you things. Assembly in Week 15 should be editing, not authoring.

**Sections are content-indexed, not week-indexed.** §5 is always Control Architecture no matter when it's written or revised, and section numbers never change. Cite your own report by section ("as assessed in §4") — never by week.

**Revision is expected and graded well.** A §4 risk register that still says exactly what it said in February is a red flag, not a sign of stability. When you revise a section materially, keep the judgment honest: what you believed then, what you know now, what changed your mind.

Grading: see `Program_Report_Rubric.md` (issued alongside this template). The rubric's two cross-cutting disciplines — calibrated claims and audience discipline — apply to every section below. Target lengths are guidance, not quotas; most sections land at one to two pages of decision-ready prose plus any tables.

---

## §1 — Cover & Executive Summary

*The one page a board member actually reads: program state, top risks in business terms, what was decided this year, and the ask.*

**Fed by:** written fresh during Week 15 assembly, from everything below.

- Cover: report title, your name, role (Security Program Lead, Wumpus Telehealth), date.
- Summary: one page, standalone. State of the program; the top three risks and what they mean for the business; the year's most consequential events and decisions; what you are asking leadership to approve. No detail that isn't load-bearing.

## §2 — Business & Risk Context

*What Wumpus is, what it holds, and why security failure is a business event — the stakes the rest of the report inherits.*

**Fed by:** Weeks 1–3 orientation work (onboarding packet, questionnaire gap analysis); revised at assembly.

- The company: product (Burrow: virtual urgent care + RPM), scale (~140 people), customers, how revenue works.
- The data: what PHI and business data exists, roughly where it lives, and who cares (patients, customers, regulators).
- The obligations: the St. Ansgar relationship and its security requirements as the program's founding pressure.

## §3 — Governance & Program Charter

*The program's mandate: authority, scope, reporting line, policy structure, and framework alignment.*

**Fed by:** Week 2 memo **D1** (program charter); revised as governance decisions accumulate.

- The charter itself: what the program is responsible for, what authority it carries, how it escalates, how leadership engages.
- Framework alignment (CSF 2.0): current profile vs. target profile, honestly scored.
- The policy set: what exists, what's adopted vs. drafted, review cadence.
- A record of governance decisions made during the year — including recommendations leadership modified, deferred, or declined, stated factually.

## §4 — Risk Assessment

*The risk register and threat analysis: what can hurt this company, how likely, how badly, and who would bother.*

**Fed by:** Week 3 memo **D2** (risk register v1) and Week 4 memo **D3** (threat profile); re-scored as the year updates your judgments.

- Methodology in brief (SP 800-30 style: sources, likelihood/impact scales, who judged).
- The register: risks specific to Wumpus, each with owner, treatment decision, and status.
- Threat analysis: the adversaries economically relevant to a 140-person healthtech, tied to the risks they justify.
- A change log: risks added, re-scored, or retired during the year, and why.

## §5 — Control Architecture

*Network, identity, and data protection as designed and as actually deployed — the risk decisions, not the tool list.*

**Fed by:** Week 5 memo **D4** (network architecture proposal), Week 7 memo **D5** (access control policy), and Weeks 6 and 8 build work (network defense; encryption/data protection for the BAA); updated whenever deployed reality changes.

- Network: the architecture found, the architecture proposed, what was implemented, and what each boundary does and does not protect.
- Identity & access: authentication posture, authorization model, access review and offboarding process, privileged access.
- Data protection: encryption at rest/in transit, key management, and how the standard meets contractual (BAA) requirements.
- For every control, three timestamps' worth of honesty: proposed, adopted, deployed — never blurred.

## §6 — Security Operations & Detection

*What the company can see and how it responds to what it sees: logging, monitoring, alerting, and the human reporting path.*

**Fed by:** Week 10 memo **D6** (initial assessment & detection gaps); revised as operations mature.

- Logging coverage: which sources exist, retention, centralization — and the gaps, with consequences.
- Monitoring & triage: how an anomaly or an employee's "this feels wrong" becomes a ticket, an owner, and a response, within what time.
- Detection posture sized for real staffing, with the roadmap items it depends on cross-referenced to §11.

## §7 — Incident Retrospective

*A management-view retrospective of security events during your tenure: what happened as established, what was decided on what information, which controls held, and what changes follow.*

**Fed by:** Week 10 memo **D6** and Week 11 memo **D7** (incident decision memo + communications package); finalized once the facts are as settled as they're going to get.

- Timeline as established, with confidence levels — confirmed vs. inferred vs. never determined.
- Decisions made, evaluated against the information available *at the time*, including communications to leadership, customers, and staff.
- What held, what failed, and the earlier decisions each traces to (cross-reference your own §3–§5).
- Systemic root cause and corrective actions. **Mind the rubric's framing rule:** root cause analysis examines controls and decision processes, never a person. If the year passes without a reportable event, this section documents that assessment, near-misses, and the basis for confidence — "nothing happened" is a claim requiring evidence like any other.

## §8 — Resilience (BC/DR)

*Whether Wumpus survives a very bad day: backups, recovery objectives, and the evidence recovery actually works.*

**Fed by:** Week 12 memo **D8** (resilience plan).

- RTO/RPO for the services that matter, tied to business tolerance, not picked from air.
- Backup architecture and protection (including against deliberate destruction); restore test results with dates.
- Continuity beyond IT: people, communications, decision authority during an outage.
- Untested recovery labeled as untested, everywhere it appears.

## §9 — Assurance (Audit & Testing)

*How the program proves its claims — to itself, to leadership, and to outside parties who don't take its word.*

**Fed by:** Week 13 memo **D9** (audit & testing plan).

- The verification map: which claims are verified by which method (config audit, scan, pentest, independent assessment) on what cadence — and why each method fits its question.
- Findings from assurance activity performed during the year, with remediation status.
- Readiness for external scrutiny: what an independent assessor would be shown, and what they would find.

## §10 — Compliance Posture & Obligations

*What law and contract actually require of Wumpus, where the program stands against those requirements, and what triggers what.*

**Fed by:** Week 14 memo **D10** (compliance posture & notification analysis).

- HIPAA posture: Security Rule risk analysis status, safeguard gaps, training, documentation.
- Contractual obligations: the BAA's commitments and the questionnaire's committed dates, tracked honestly.
- Notification obligations: what circumstances trigger duties to whom (individuals, HHS, states, customers) on what clocks — legal conclusions attributed to counsel.
- Other regimes in scope for the business, at survey depth.

## §11 — Roadmap & Budget Ask

*What the program needs next, in priority order, with costs, owners, dates — and the stated consequence of not funding each item.*

**Fed by:** Week 15 assembly work and the board briefing preparation; every item traceable to §§3–§10.

- Prioritized initiatives: what, why (cross-referenced to the risk or lesson that justifies it), cost class, owner, timeline.
- Sequencing logic: what must precede what, and what was deliberately deferred.
- The ask itself, sized for this company's budget reality — a roadmap the board can fund, not a fear appeal.

## §12 — Appendices

*Supporting material that earns its place: referenced, not padding.*

**Fed by:** accumulated artifacts from all weeks.

- Candidates: the completed St. Ansgar questionnaire responses; key policy documents; the full risk register if summarized in §4; selected memos as decision records; glossary if needed.
- Rule of admission: something in §§1–§11 must cite it. Unreferenced appendices are padding and read as such.

---

## Assembly checklist (Week 15)

1. Every section §1–§12 present and content-indexed; no week numbers in headings or cross-references.
2. Facts consistent across sections — names, dates, numbers, and system details agree everywhere they appear.
3. Each section revised to reflect end-of-year knowledge, with honest handling of what changed.
4. §1 written last, from the finished body.
5. Run the rubric's "Quick Self-Audit Before You Submit" — all ten checks — before uploading.
