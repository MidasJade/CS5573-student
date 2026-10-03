# Wumpus Telehealth — Security Program Lead Onboarding Packet

**From:** Bhargavi Pandey, Chief Technology Officer
**To:** Our new Security Program Lead (you)
**Date:** Tuesday, January 19, 2027
**Re:** Welcome, and everything I wish someone had written down for me

---

## 1. Welcome — and your charge

Welcome to Wumpus Telehealth. I'm Bhargavi, co-founder and CTO, and as of this morning you report to me.

Let me tell you why this job exists. Three weeks ago we signed a term sheet with **St. Ansgar Health System** — a regional hospital network and, if we close it, far and away our largest customer. Their contract requires three things we do not currently have: a signed Business Associate Agreement, a completed vendor security questionnaire (it's in your inbox; read it after this), and *evidence of a real security program*. Not a firewall. A program.

You are the first security hire this company has ever made. Your charge, in one sentence: **build Wumpus a security program that is honest about where we are, credible to a hospital's risk office, and fundable by a startup's budget.** You will do that mostly by writing — assessments, proposals, policies, and decision memos that leadership can act on. Around here, if it isn't written down, it doesn't exist.

I hired you because I know what I don't know. I can architect a telehealth platform; I cannot tell you whether our risk posture would survive a hospital's scrutiny, and I've stopped pretending otherwise. You'll get candor from me, and I expect it back — especially when the news is bad.

## 2. About Wumpus

**What we are.** Wumpus Telehealth is a Kansas City startup, about **140 employees**, roughly half in our KC office and half remote. We do two things, both through our platform, **Burrow**:

1. **Virtual urgent care** — video visits connecting patients with our clinician network, mostly evenings and weekends when their own doctors are closed.
2. **Remote patient monitoring (RPM)** — connected devices (blood pressure cuffs, glucose meters, pulse oximeters) that stream readings into Burrow, where our clinical team watches trends and escalates.

**How we make money.** Health systems and insurers pay us per-member and per-visit fees to extend their coverage after hours and keep chronic patients out of the ER. Patients are their patients; we're the connective tissue. That's why the St. Ansgar deal matters so much — it's the model working at hospital-system scale, and every future deal will look at how this one went.

**What we hold.** Patient health data. Video visit records, device telemetry, clinical notes, insurance identifiers. If you take one thing from this section: we are a healthcare company that happens to run on software, and the data we hold is the kind people get very serious letters about.

## 3. The team, and who's who

The people you'll actually work with, and — more useful — what each of them cares about:

| Who | Role | What they care about (my honest read) |
|---|---|---|
| **Dana Okafor** (she/her) | CEO & co-founder | Growth. Dana is not hostile to security, but she is allergic to spending without a business case. Tie a risk to revenue — especially the St. Ansgar deal — and she will listen. Hand her fear without a number attached and she will move on. |
| **Bhargavi Pandey** (she/her) | CTO & co-founder — *your boss* | Making this program real without stalling the product. I will back your recommendations when they're written well enough to defend in a leadership meeting. Help me help you: bring me memos, not vibes. |
| **Howard Feld** (he/him) | CFO | Runway. Howard scrutinizes every dollar because his job is making sure we exist next year. He is fair, he is rigorous, and he will ask "what happens if we don't?" about everything you propose. Have an answer. |
| **Tucker Malone** (he/him) | VP Sales | Closing St. Ansgar. Tucker will ask you weekly whether the questionnaire is "handled." He's an optimist by trade, not an adversary — but he will happily promise a customer anything you don't explicitly tell him we can't do. |
| **Gus Terrell** (he/him) | IT Manager | Keeping the lights on. Gus *is* IT here, along with Marisol — two people for 140 employees. He knows where everything is buried, including the things he's not proud of. He asked Dana for a security hire before I did. Treat him as the ally he is. |
| **Marisol Vega** (she/her) | IT Technician | The ticket queue. Marisol is junior, sharp, and drowning in password resets and printer exorcisms. If your program adds work to her plate, design it so it's *less* work than the chaos it replaces. |
| **Simone Adler** (she/her) | Fractional General Counsel | Our obligations. Simone is outside counsel on a monthly retainer; she's leading the BAA negotiation with St. Ansgar right now. When your work touches HIPAA, contracts, or anything with the word "notification" in it, she's your first call — before, not after. |

### Org chart

```
Dana Okafor — CEO & co-founder
├── Bhargavi Pandey — CTO & co-founder
│   ├── VP Engineering — Burrow platform & RPM teams (~45)
│   ├── Gus Terrell — IT Manager
│   │   └── Marisol Vega — IT Technician
│   └── ★ YOU — Security Program Lead
├── VP Clinical Operations — clinicians & care coordinators (~50)
├── Howard Feld — CFO
│   └── Finance, People & Admin (~15, incl. accounting/AP)
└── Tucker Malone — VP Sales
    └── Sales & Customer Success (~20)

    Simone Adler — fractional General Counsel (external; engaged by Dana)
```

Roles without names above are real people you'll meet; the names that matter to your first quarter are the seven in the table.

## 4. The environment as you'll find it

This section is the truth, written down once, so you don't have to discover it by stepping on it. None of it is a judgment of Gus or Marisol — two people kept a 140-person company running through hypergrowth. It *is* the honest starting line, and your first assessments should treat it that way.

**The office network is flat.** One network at the KC office. Staff laptops, printers, the badge system, guest Wi-Fi, the clinic demo gear, and the file server all sit on the same segment. Everything can reach everything. This wasn't a decision anyone made; it's the absence of a decision, compounded annually since we were eleven people.

**Remote access is a VPN that lands you on that same flat network.** About half the company works remotely and connects through our VPN concentrator. Once you're on, you're *on* — same reach as a desk in the office.

**Burrow runs in the cloud; the office runs on SaaS — mostly.** The Burrow platform and RPM telemetry live with a major cloud provider, managed by engineering. Email, documents, calendars, and identity live in a SaaS office suite. That migration was declared finished two years ago. It wasn't, which brings us to:

**WMP-FS01.** A legacy Windows file server in the office, the one machine that never got migrated. It holds years of accumulated files — HR records, finance archives, old operational exports, things departments swear they need and never open. Nobody has a complete inventory of what's on it. It is backed up in a way Gus describes as "technically." Ask him about it early; he'll be relieved someone finally did.

**Identity is single-factor.** Everyone signs into the SaaS suite and the VPN with a username and password. **MFA is not enforced anywhere.** It's been on Gus's wish list for over a year; it has never been funded or scheduled.

**Endpoints are unmanaged.** No MDM. Laptops run whatever the built-in OS antivirus does by default. Some are encrypted because the OS shipped that way; nobody verifies. Remote employees' machines have never been seen by IT after day one.

**Offboarding is informal.** When someone leaves — employee or contractor — their accounts get disabled when someone remembers to ask. The checklist exists primarily in Gus's head. Neither of us can currently tell you, with confidence, that every departed person's access is gone. Expect your first access review to find things.

**Logging exists but nobody's watching.** The cloud and SaaS consoles keep their default logs. Nothing is centralized, nothing alerts, and no one's job includes looking.

### Network sketch

```
                          INTERNET
                              │
      ┌───────────────────────┼───────────────────────────┐
      │                       │                           │
 Cloud provider          SaaS office suite         KC office edge
 (Burrow platform,       (email, docs, identity,   (single firewall/router)
  RPM telemetry)          single-factor sign-in)          │
                                                ┌─────────┴──────────┐
                                                │  ONE FLAT NETWORK  │
                                                │  staff laptops     │
                                                │  guest Wi-Fi       │
                                                │  printers, badge   │
                                                │  system, demo gear │
                                                │  WMP-FS01 (legacy  │
                                                │    file server)    │
                                                │  VPN concentrator ─┼── remote staff
                                                └────────────────────┘
```

> **TODO (course build):** replace this ASCII sketch with the rendered network-diagram asset for the student packet. The sketch above is authoritative for topology until then.

## 5. Why you're here now: St. Ansgar

St. Ansgar Health System operates hospitals and clinics across the region. Their term sheet makes them our first true hospital-system customer, worth more than our next several deals combined — and their vendor risk office does not sign on charm.

Before contract signature they require:

1. **A completed security questionnaire** — attached to this packet, with their cover memo and a deadline you should read today. Spoiler: we cannot currently answer most of it the way they'd like. Your job is not to make the answers sound better than they are. Your job is to make the *true* answers better, and to show a credible, dated plan for the rest.
2. **An executed BAA.** Simone is negotiating it. The BAA will commit us to specific safeguards — encryption expectations, breach-notification duties, subcontractor flow-downs. What she signs, you and Gus have to make true.
3. **Evidence of a program.** Named security lead (that's now you), written policies, a risk assessment, and eventually independent verification. The questionnaire is the map of what "evidence" means to them.

Tucker wants this closed yesterday. Howard wants it closed without lighting money on fire. Dana wants both. Welcome to security leadership.

## 6. How we'll work together

Here's the rhythm I'm setting, and I'll hold up my end:

- **Monday:** I'll send you a short memo — where we stand, what I need from you that week, and where it fits in the larger program. When something happens at the company that you need to know, this is where you'll hear it.
- **Tuesday evening:** you and I meet to work through that week's problem domain. Bring questions; I'd rather untangle your thinking live than edit it after.
- **Thursday evening:** hands-on time. Gus is standing up a lab environment for you — a safe replica of the kinds of systems we run — so you can verify things with your own hands instead of taking anyone's word, including his. First task: make sure your environment actually works. Tell us Thursday if it doesn't, while it's still easy to fix.
- **Before the following Tuesday:** your written deliverable for the week lands on my desk. Short — a page or so — and decision-ready. These memos are not homework filed and forgotten; they accumulate into the company's **Security Program Report**, the document that will eventually go in front of Dana and the board, and before that in front of St. Ansgar. Write every one as if it will be re-read months later by someone deciding whether to trust us. It will be.

## 7. Your first deliverables

This week:

1. **Read this packet and the St. Ansgar questionnaire**, including Gus's candid first-pass answers attached to it. Come Tuesday with your questions — there are no stupid ones yet; you've been here a day.
2. **Get your lab environment running** by Thursday's session, per Gus's setup guide. This gates everything else.
3. **Start your own notes on the environment.** Section 4 above is my summary; verify it, extend it, and disagree with it in writing where I'm wrong.

Next week, expect Dana to ask you — directly, in her way — what exactly we hired you to do. Your answer will be your first formal memo: a **program charter**. Start thinking about it now.

## 8. A note on mindset

Three things I need you to internalize before your first meeting:

**The mess is the job.** Everything in section 4 stayed unfixed because fixing it competed with keeping a growing company alive, and lost. You will not be graded — by me, by Dana, by anyone serious — on how loudly you gasp at it. You'll be graded on whether, six months from now, the important parts are measurably better and everyone understands why we fixed those parts first.

**Write what you know, and how well you know it.** When you tell me a risk is likely, I will ask how you know. "Confirmed," "probably," and "I haven't verified" are three different sentences; a security lead who blurs them loses the room exactly once. Overclaiming will cost you more credibility here than any gap in our defenses.

**Blame systems, not people.** When you find something broken — and you will, weekly — the question is never "who screwed up." It's "what process let this happen, and what would have caught it." A program built on that question gets told the truth by its coworkers. The other kind gets managed around, and finds things out too late.

Glad you're here. There's a lot to do.

— Bhargavi

---

*Attachments: St. Ansgar Health System vendor security questionnaire (with cover memo); lab environment setup guide (from Gus).*
