# CS5573 — Security Program Report Rubric

**Issued Week 1 · Governs the final Security Program Report (25% of course grade), due end of finals week · A slimmed version of criteria 2–4 and 8 governs the Week 8 Portfolio v1 checkpoint**

You are receiving this rubric on day one, deliberately. The final report is not written in finals week — it is *assembled* from the memos you write all semester, and every memo is easier to write when you know what the finished document must do. Read this now; reread it at Week 8; audit against it before you submit.

**What you are writing.** The complete Security Program Report for Wumpus Telehealth: the document its leadership and board would use to understand what the security program is, what it has done, what it has learned, and what it needs next. Twelve content-indexed sections (§1–§12, defined in `Program_Report_Template.md`), graded here through eight criteria totaling **100 points**.

**How bands work.** Each criterion below is a four-band table. Your score for a criterion is the band that *best describes the work as a whole* — not an average of features, and not the top band minus quibbles. Read the Developing bands carefully: they describe competent-looking work with a specific missing discipline. That's the trap each criterion is guarding.

---

## Two disciplines graded everywhere

These two themes cut across all eight criteria. Weakness in either drags every band judgment down; strength in both is what the Exemplary bands describe.

### 1. Calibrated claims

A security program's currency is trust in its statements. Every factual and risk claim in your report must signal how well you know it, using this ladder:

| Level | Use when | Sounds like |
|---|---|---|
| **Confirmed** | You (or a source you cite) directly verified it | "Confirmed by the January access review…" |
| **High confidence** | Strong evidence, minor gaps | "The evidence strongly indicates…" |
| **Moderate confidence** | Evidence supports it; alternatives remain plausible | "Most consistent with…, though X can't be ruled out" |
| **Low confidence / possible** | Plausible, thinly evidenced | "It is possible that…; we have not verified" |
| **Unknown** | You don't know | "We do not currently know…" — said plainly |

**Overclaiming is penalized as heavily as underclaiming.** A report that asserts as fact what was never verified fails the same way a report that hedges everything into mush does. "Unknown" stated crisply, with a plan to find out, is a *strong* answer in this course.

### 2. Audience discipline

This is a board report, not a term paper. The board and executive leadership of Wumpus are intelligent, busy, non-specialist readers deciding what to fund and whom to trust. That means: conclusions first, evidence behind them; every technical term earns its place or gets translated; risks tied to business consequences, not enumerated for completeness; recommendations with owners, costs, and dates, not aspirations. No literature reviews, no textbook definitions, no filler. If a paragraph doesn't help a director make a decision or trust your judgment, it's costing you points somewhere below.

---

## The eight criteria

| # | Criterion | Report sections | Points |
|---|---|---|---|
| 1 | Executive Summary & Business Context | §1, §2 | 10 |
| 2 | Governance & Program Charter | §3 | 10 |
| 3 | Risk Assessment & Threat Analysis | §4 | 12 |
| 4 | Control Architecture | §5 | 14 |
| 5 | Security Operations & Detection | §6 | 10 |
| 6 | Incident Retrospective | §7 | 14 |
| 7 | Resilience, Assurance & Compliance | §8, §9, §10 | 15 |
| 8 | Roadmap, Budget Ask & Report Craft | §11, §12, whole document | 15 |
| | **Total** | | **100** |

---

### Criterion 1 — Executive Summary & Business Context (§§1–2) · 10 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 9–10 | The summary stands alone: a director who reads nothing else understands the program's state, the top risks in business terms, what was decided during the year, and what is being asked for. §2 grounds everything in Wumpus's actual business — what it sells, what data it holds, what a security failure costs — so the rest of the report inherits its stakes. Claims are calibrated even here, where the temptation to round up is strongest. |
| **Proficient** | 7–8 | Accurate and complete summary of program state, risks, and the ask, with minor lapses: some findings summarized without their business consequence, or a summary that requires the body to make sense of one or two points. Business context is correct but partly generic. |
| **Developing** | 4–6 | The summary lists activities ("we wrote policies, we assessed risk") rather than telling the decision-maker what matters; or the business context could describe any small company; or the summary's claims are notably more confident than the body supports. |
| **Insufficient** | 0–3 | Missing, boilerplate, or a restated table of contents. No meaningful connection between the business and the program. |

### Criterion 2 — Governance & Program Charter (§3) · 10 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 9–10 | The charter defines the program's mandate, authority, reporting line, and scope in terms leadership demonstrably endorsed; framework alignment (e.g., CSF 2.0) is used as an organizing tool with a candid current-vs-target profile, not a logo. Policy structure is proportionate to a 140-person company. Governance decisions made during the year — including ones that went against the program's recommendation — are recorded accurately and without editorializing. |
| **Proficient** | 7–8 | Sound charter and sensible framework use with minor gaps: authority or escalation paths partially specified, or a target profile asserted without a clear path from the current one. |
| **Developing** | 4–6 | A charter that could be for any company; framework name-dropped without an actual profile; policies listed without evidence any decision-maker adopted them; or governance history sanitized. |
| **Insufficient** | 0–3 | No real charter — a mission statement or a pasted framework summary. |

### Criterion 3 — Risk Assessment & Threat Analysis (§4) · 12 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 11–12 | The risk register reflects Wumpus specifically: its data, its flat network, its two-person IT, its customer obligations. Likelihood and impact judgments are reasoned (methodology visible, e.g., SP 800-30 style) and calibrated — headline fears are not automatically top risks. The threat analysis profiles adversaries economically relevant to a 140-person healthtech and is tied to the risks it justifies. The register shows life: risks re-scored as the year taught the program things, with the changes explained. |
| **Proficient** | 9–10 | Solid, company-specific register and credible threat profile with minor weaknesses: some scores asserted rather than reasoned, or threat analysis correct but loosely coupled to the register. |
| **Developing** | 5–8 | A generic top-risks list; likelihood/impact assigned without visible reasoning; threat section profiles glamorous actors over probable ones; or the register is frozen — untouched by anything that happened all year. |
| **Insufficient** | 0–4 | No usable register, or risk content that contradicts the rest of the report. |

### Criterion 4 — Control Architecture (§5) · 14 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 13–14 | Network, identity, and data-protection architecture presented as *risk decisions with rationale*, not tool lists: what was proposed, what was adopted, what was deferred, and what each choice traded away. The section is honest about partial implementation — what a half-built control does and does not protect — and distinguishes designed state from deployed state at every point. Recommendations were written to be fundable: costed, sequenced, owned. |
| **Proficient** | 10–12 | Sound architecture covering network, identity, and data protection with clear rationale, but minor blurring of proposed vs. implemented, or one domain notably thinner than the others. |
| **Developing** | 6–9 | Controls cataloged without rationale; the architecture describes an idealized end-state without acknowledging what actually existed and when; or identity/data protection treated as afterthoughts to network diagrams. |
| **Insufficient** | 0–5 | A shopping list of products, or an architecture unrecognizable as Wumpus's environment. |

### Criterion 5 — Security Operations & Detection (§6) · 10 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 9–10 | An honest account of what the company could and could not see: logging coverage, monitoring, alert handling, and the path by which a human's "something feels wrong" becomes a response. Detection gaps are stated plainly with their consequences, and the operations design is sized for the real staffing, not an imaginary SOC. |
| **Proficient** | 7–8 | Accurate coverage of logging, monitoring, and triage with minor gaps — e.g., gaps listed without consequence, or a proposed capability not clearly separated from a deployed one. |
| **Developing** | 4–6 | Tool-centric ("deploy a SIEM") without the questions a detection program answers; visibility claims that outrun the evidence; or no treatment of how reported concerns are handled. |
| **Insufficient** | 0–3 | Missing or generic to the point of interchangeability. |

### Criterion 6 — Incident Retrospective (§7) · 14 points

Your report includes a management-view retrospective of security events the program encounters during your tenure: what happened as best the program could establish, what was decided and on what information, which controls held, and what changes follow. It is a decision record, not a forensic report.

> **⚠ Framing rule — hard cap.** If the retrospective attributes an event's root cause to an individual employee's mistake — naming, blaming, or structurally scapegoating the person closest to the failure rather than analyzing the control and process failures that made that mistake possible and consequential — **this criterion is capped at Developing regardless of technical quality.** People clicking, trusting, and erring is the operating environment every control exists for; a retrospective that ends at "an employee erred" has not found a root cause, it has found a headline. This is the single most transferable judgment this course grades.

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 13–14 | A clear, calibrated account: timeline as established (with confidence levels — what was confirmed vs. inferred vs. never determined), decisions with the information available *at the time* they were made, controls that held and failed traced to the decisions that put them there, and systemic causes analyzed without scapegoating anyone — including decision-makers, whose choices are examined as process, not character. The program's own earlier work (assessments, proposals, warnings) is used as evidence, honestly, including where the program itself fell short. |
| **Proficient** | 10–12 | Sound systemic analysis and accurate sequence with minor lapses: hindsight creeping into decision evaluation, some claims outrunning what was established, or a what-held/what-didn't analysis that stops short of the underlying decisions. |
| **Developing** | 6–9 | Chronology without analysis; root cause pinned on a person or a single missing tool rather than the decision chain; confidence levels absent so verified facts and speculation read identically. *(Maximum band if the framing rule above is triggered.)* |
| **Insufficient** | 0–5 | Missing, factually confused, or a dramatized narrative with no management substance. |

### Criterion 7 — Resilience, Assurance & Compliance (§§8–10) · 15 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 14–15 | §8 treats recovery as something *demonstrated*, not owned: RTO/RPO tied to business tolerance, backup and restore posture reported with test evidence, untested recovery labeled as the hope it is. §9 lays out an assurance program that matches verification methods to questions (audit vs. scan vs. pentest) and engages honestly with what independent parties would find. §10 states compliance posture and obligations precisely — what HIPAA and contracts actually require of Wumpus, current gaps, and obligation triggers — legal conclusions attributed to counsel, not improvised. |
| **Proficient** | 11–13 | All three sections present and sound, with minor weaknesses: an RTO asserted without a tolerance argument, assurance methods listed but weakly matched to purpose, or compliance described accurately but generically. |
| **Developing** | 6–10 | One of the three domains missing or perfunctory; recovery claims without test evidence; assurance as a synonym for "we'll get a pentest"; or compliance reduced to a framework checklist with no obligations analysis. |
| **Insufficient** | 0–5 | Two or more domains missing or contentless. |

### Criterion 8 — Roadmap, Budget Ask & Report Craft (§11, §12, whole document) · 15 points

| Band | Points | Description |
|---|---|---|
| **Exemplary** | 14–15 | §11 is something a board could fund at the meeting: prioritized, costed, sequenced, each item traceable to a risk or lesson documented earlier, with the consequence of *not* funding it stated soberly — a roadmap, not a fear appeal. The document reads as one report, not ten stapled memos: consistent facts and terminology, clean cross-references, appendices that support rather than pad. Audience discipline holds start to finish. |
| **Proficient** | 11–13 | A credible prioritized roadmap and a coherent assembled document, with minor seams: some costs or owners missing, occasional redundancy between sections, or appendix material that belongs in the body (or vice versa). |
| **Developing** | 6–10 | A wish list without priorities or costs; asks unconnected to the report's own findings; visible memo-boundaries with contradictions between sections; or a document whose length substitutes for its argument. |
| **Insufficient** | 0–5 | No actionable roadmap, or an assembly so inconsistent the report contradicts itself on material facts. |

---

## Quick self-audit before you submit

Ten minutes with this list is worth more than a re-read for typos.

1. **The one-page test.** Read only §1. Would a director know the program's state, the top three risks in business terms, and the ask? Would they know anything *happened* this year?
2. **The calibration sweep.** Find your five strongest claims. For each: could you name the evidence if challenged in the board meeting? Is its confidence level visible in the sentence?
3. **The "unknown" check.** Does the word appear? A year-one program that never says "we don't know" is overclaiming somewhere.
4. **The framing check.** Search your §7 for every mention of an individual person. For each: are you analyzing a decision or assigning blame? Would you write that sentence if the person were reviewing the report? Does your root cause survive the question "and what would have stopped that from mattering?"
5. **The designed/deployed check.** For every control in §5–§6: does the text make clear whether it was proposed, partially implemented, or fully deployed — and *when*?
6. **The traceability check.** Pick any three roadmap items in §11. Can you point to the section of your own report that justifies each one?
7. **The stapler check.** Read the last paragraph of each section and the first of the next. Does it flow as one document? Do §4's risks, §7's lessons, and §11's asks tell the same story?
8. **The jargon pass.** Find every acronym and term of art. Would the CFO know it, or did you translate it on first use?
9. **The attribution check.** Are legal conclusions attributed to counsel, external findings to their source, and your own analysis owned as yours?
10. **The section-number check.** All twelve sections present, numbered §1–§12 per the template, content-indexed — even those whose honest content is short.
