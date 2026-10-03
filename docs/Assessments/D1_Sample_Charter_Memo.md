# D1 — Sample Program Charter Memo

**Handed out with the D1 assignment. This is a model of *form*, not of content.**

The company below is **not** Wumpus Telehealth and has nothing to do with our scenario.
That's deliberate: you should be able to see exactly what a charter memo does without
being able to borrow a single sentence of it. Read it for shape, length, and tone —
then write yours about the company you actually work for.

Graded on `Program_Memo_Rubric.md`. **250–400 words** of body text.

---

## The memo

**To:** Ellis Thorne, President; Warren Ochoa, CFO
**From:** R. Keene, Security Program Lead
**Date:** March 3
**Subject:** Security program charter — what I own, and the first three months

Recommendation: approve this charter as written. It commits me to a defined scope and
gives you a single accountable owner before the insurance renewal in June.

**Mandate.** I am responsible for protecting the firm's ability to deliver sealed
engineering work on schedule — the drawings, the calculation records, and the client
data behind them — and for producing the evidence that we do. Where protection and
delivery conflict, I bring you the tradeoff rather than deciding it alone.

**Scope.** In: all firm-managed systems, the drafting file servers, email, and the
vendor relationships that touch project data. Explicitly out: the physical security of
our four offices, which remains with Facilities, and safety compliance, which is
Engineering's. I would rather own less and actually do it.

**Authority.** I can require changes to how firm systems are configured and accessed.
I cannot unilaterally stop a project deliverable; if I believe one carries
unacceptable risk, I escalate to Ellis, and Ellis decides. Spending above $5,000 goes
to Warren. If someone tells me no, that is a legitimate answer — it just has to be
recorded as a decision rather than a silence.

**Framework alignment.** We are using NIST CSF 2.0. My honest first read: we are
partially there on PROTECT, weakest on GOVERN and IDENTIFY, and we have no DETECT
capability I would claim in writing. That assessment is inferred from two weeks of
conversations, not yet verified against the systems themselves; I will confirm it
during the asset inventory and correct this memo if I am wrong.

**First priorities.** One, a complete asset and vendor inventory — we cannot insure or
defend what we have not counted, and the renewal application asks. Two, multi-factor
authentication on email, because credential theft is the loss our insurer prices most
heavily. Three, a written access-review cadence.

I will report monthly, and flag anything that changes this scope.

---

## Why this memo works

Keyed to the five rubric items. Read this part as closely as the memo.

**1. Answers the actual ask.** All five required elements are present, and each says
something specific. Note what scope does: it names what is **out** — Facilities,
safety compliance — and gives a reason. "I would rather own less and actually do it"
is a real position, not a hedge.

**2. Decision-ready.** The first line is the recommendation. A busy executive who
stops reading after one sentence still knows what they're being asked to do and why
now. Nothing is defined that the reader didn't ask about; there is no paragraph
explaining what a security program *is*.

**3. Calibrated.** Look closely at the framework paragraph. It states a conclusion,
labels it **inferred**, says what it's based on, says what would confirm it, and
commits to correcting the memo if it's wrong. It also refuses to claim a DETECT
capability — *"no DETECT capability I would claim in writing"* is a stronger sentence
than any score would have been. That is what calibration looks like in a memo, and
it's rarer than you'd think.

**4. Specific to that company.** Sealed drawings. Four offices. A June insurance
renewal. Facilities versus Engineering. Swap the firm's name out and several sentences
stop making sense — which is the test.

**5. Usable in the report.** It could drop into a governance section and be edited
rather than rewritten. The authority paragraph in particular gives the report
something to point back to when later decisions go a way the program didn't recommend.

**What it does not do:** ask for a single product, tool, or license. Priority two says
*"multi-factor authentication on email"* and stops — a capability and a reason, not a
purchase order. Your charter should do the same.

**One more thing worth stealing:** *"If someone tells me no, that is a legitimate
answer — it just has to be recorded as a decision rather than a silence."* That
sentence is the whole point of governance, and it will matter more later in this
course than it looks like it does now.
