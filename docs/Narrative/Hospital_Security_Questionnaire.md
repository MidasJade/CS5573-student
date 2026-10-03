# St. Ansgar Health System — Vendor Security Questionnaire

*Forwarded to you by Bhargavi with the onboarding packet. Part 1 is St. Ansgar's document, exactly as received. Part 2 is internal only — do not send.*

---

## Part 1 — As received from St. Ansgar

**ST. ANSGAR HEALTH SYSTEM**
Office of Third-Party Risk Management

**To:** Dana Okafor, Chief Executive Officer, Wumpus Telehealth, Inc.
**From:** Ruth Kaplan, Director, Third-Party Risk Management
**Date:** January 12, 2027
**Re:** Vendor Security Assessment — Wumpus Telehealth (Engagement VRA-2027-0114)

Dear Ms. Okafor,

Thank you for your continued engagement with St. Ansgar Health System. As Wumpus Telehealth would create, receive, maintain, and transmit protected health information (PHI) on behalf of St. Ansgar, our vendor risk program classifies this engagement as **Tier 1 (Critical)**. Contract execution is contingent on completion of our security assessment.

Please note the following:

1. **The completed questionnaire is due by Friday, March 12, 2027.** This date is set by our Q2 contracting calendar; responses received after it will move the engagement to the Q3 review cycle, which we understand is incompatible with the launch timeline discussed with your sales team.
2. Answer each item **Yes**, **No**, or **In progress**. "In progress" answers must include an owner and a committed date. Where evidence is requested, reference the document you would furnish; we may request any referenced evidence.
3. **Accuracy matters more than the answer.** A candid "No" with a credible remediation plan is acceptable in a Tier 1 review; an inaccurate "Yes" discovered during verification ends the engagement.
4. Execution of a Business Associate Agreement is a separate, mandatory workstream proceeding in parallel with your counsel.
5. Certain controls (identified during review) must be verified — by evidence or independent assessment — before any PHI flows in production.

We look forward to your response.

Respectfully,

Ruth Kaplan
Director, Third-Party Risk Management
St. Ansgar Health System

---

### Instructions

For each item: answer **Yes / No / In progress**; provide a brief description of the control as implemented; and reference available evidence (policy, report, screenshot, attestation). "In progress" requires an owner and date.

### Section A — Governance & Security Program

| # | Question |
|---|---|
| GOV-01 | Does your organization have a named individual responsible for information security, with documented authority and reporting line to executive leadership? |
| GOV-02 | Do you maintain a written information security policy set, approved by executive management and reviewed at least annually? |
| GOV-03 | Is your security program aligned to a recognized framework (e.g., NIST Cybersecurity Framework, HITRUST, ISO 27001)? Identify the framework and current state of alignment. |

### Section B — Risk Management

| # | Question |
|---|---|
| RSK-01 | Have you completed a documented information security risk assessment within the past 12 months covering the systems that would store or process St. Ansgar PHI? |
| RSK-02 | Do you maintain a risk register with identified risks, owners, and treatment decisions, reviewed by management on a defined cadence? |
| RSK-03 | Is there a documented process for formally accepting risks, including who is authorized to accept risk on behalf of the organization? |

### Section C — Access Control & Identity Management

| # | Question |
|---|---|
| IAM-01 | Is multi-factor authentication (MFA) enforced for all remote access to your corporate environment (VPN, remote desktop, or equivalent)? |
| IAM-02 | Is MFA enforced for all access to email and to any system storing or processing PHI? |
| IAM-03 | Are user accounts individually assigned (no shared credentials), with access provisioned on a least-privilege, role-based basis? |
| IAM-04 | Are user access rights — including contractor and third-party accounts — reviewed on a documented, periodic basis (at least quarterly for privileged access)? |
| IAM-05 | Is there a documented offboarding process ensuring all access (accounts, VPN, tokens, third-party apps) is revoked within one business day of separation? |

### Section D — Network Security

| # | Question |
|---|---|
| NET-01 | Are systems storing or processing PHI segmented from general-purpose corporate networks and from guest/visitor networks? |
| NET-02 | Are firewalls (or equivalent controls) deployed at network boundaries with rulesets that are documented, justified, and reviewed at least annually? |
| NET-03 | Do you employ intrusion detection or prevention capabilities at network or host level? |
| NET-04 | Is remote access to your environment restricted to managed, authenticated endpoints, with access limited to the resources required by role? |

### Section E — Encryption & Data Protection

| # | Question |
|---|---|
| ENC-01 | Is PHI encrypted at rest on all systems that store it, including servers, databases, backups, and end-user devices? |
| ENC-02 | Is PHI encrypted in transit over all networks, using current, industry-accepted protocols and configurations (e.g., TLS 1.2+)? |
| ENC-03 | Are cryptographic keys managed under a documented process (generation, storage, rotation, revocation) with access restricted to authorized personnel? |
| ENC-04 | Is full-disk encryption enforced and verifiable on all laptops and mobile devices that may access PHI? |

### Section F — Logging, Monitoring & Detection

| # | Question |
|---|---|
| LOG-01 | Are security-relevant logs (authentication, access to PHI, administrative actions, network events) collected centrally and retained for at least 12 months? |
| LOG-02 | Are logs monitored — by personnel or tooling — such that anomalous or unauthorized activity would generate a timely alert to a defined responder? |
| LOG-03 | Do you have a documented process for triaging and responding to security alerts and employee-reported security concerns, with defined response times? |

### Section G — Incident Response

| # | Question |
|---|---|
| IR-01 | Do you maintain a written incident response plan with defined roles, severity levels, and escalation paths, tested at least annually (e.g., tabletop exercise)? |
| IR-02 | Does your incident response process include contractual and regulatory notification obligations, including notifying affected customers within a defined timeframe? |
| IR-03 | In the past 24 months, has your organization experienced a security incident involving unauthorized access to, or acquisition of, customer or patient data? If yes, describe the incident and remediation. |
| IR-04 | Do you have a retained or identified incident response provider (internal team or external firm) capable of forensic investigation? |

### Section H — Business Continuity & Disaster Recovery

| # | Question |
|---|---|
| BCP-01 | Are systems storing PHI backed up on a defined schedule, with backups protected against unauthorized modification or deletion (e.g., offline or immutable copies)? |
| BCP-02 | Have you performed a successful, documented restoration test of those backups within the past 12 months? |
| BCP-03 | Do you maintain business continuity and disaster recovery plans with defined recovery time and recovery point objectives (RTO/RPO) for services delivered to customers? |

### Section I — Compliance & HIPAA Readiness

| # | Question |
|---|---|
| HIP-01 | Have you conducted a HIPAA Security Rule risk analysis (45 CFR §164.308(a)(1)(ii)(A)), and do you maintain documentation of it? |
| HIP-02 | Do all workforce members receive security and privacy training at hire and at least annually, with completion tracked? |
| HIP-03 | Do you have documented breach assessment and notification procedures consistent with the HIPAA Breach Notification Rule and applicable state law? |
| HIP-04 | Are you prepared to execute a Business Associate Agreement, including flowing down equivalent obligations to any subcontractors that handle PHI? |

### Section J — Third-Party & Vendor Management

| # | Question |
|---|---|
| VND-01 | Do you maintain an inventory of third parties (cloud providers, SaaS platforms, subcontractors) that store or process your customers' data, with security assessments proportionate to risk? |
| VND-02 | Have you undergone an independent security assessment (audit, penetration test, or certification) within the past 12 months? If yes, identify the type and provide the report or attestation summary. |
| VND-03 | Do your agreements with subcontractors handling PHI include security and breach-notification obligations at least as protective as those in your customer agreements? |

*— End of questionnaire (33 items) —*

---

## Part 2 — INTERNAL ONLY: Gus's first pass (January 18, 2027)

*Bhargavi's note: I asked Gus to take an honest first cut before your start date so you'd have ground truth, not marketing. His words below, lightly cleaned up. This does not leave the building — the answers St. Ansgar gets are the ones you'll build over the next several weeks, with committed dates we can actually hit.*

| # | Honest answer today | Gus's notes |
|---|---|---|
| GOV-01 | **In progress** | As of this week: our new Security Program Lead. Authority/reporting line needs to be written down somewhere official. |
| GOV-02 | **No** | We have an acceptable-use paragraph in the employee handbook from 2023. That's it. |
| GOV-03 | **No** | I've read the NIST CSF. Reading isn't alignment. |
| RSK-01 | **No** | Never done one. |
| RSK-02 | **No** | No register. Risks currently live in my head and my stomach lining. |
| RSK-03 | **No** | Risks get "accepted" by nobody deciding anything. |
| IAM-01 | **No** | VPN is username + password. MFA has been on my wish list since 2025; never funded. |
| IAM-02 | **No** | Same for the office suite. Engineering has MFA on some cloud admin consoles — genuinely, credit to them — but not org-wide and not on email. |
| IAM-03 | **Partially** | Accounts are individual, yes. Least-privilege, no — access accumulates and nobody prunes. There's a shared login for the shipping-label machine; don't judge me. |
| IAM-04 | **No** | Never done a formal access review. I could not tell you today that every ex-employee and ex-contractor account is disabled. That's an honest answer and it makes me sweat. |
| IAM-05 | **No** | Offboarding is me remembering. Usually I remember. |
| NET-01 | **No** | One flat network: laptops, printers, guest Wi-Fi, WMP-FS01, badge system, all of it. VPN users land on the same segment. |
| NET-02 | **Partially** | There's an edge firewall. The ruleset is... archaeological. Never formally reviewed. |
| NET-03 | **No** | Nothing at the office. Cloud side has provider defaults only. |
| NET-04 | **No** | Any device with the VPN client and a valid password gets in. We have no MDM, so "managed endpoint" isn't a thing we can even say. |
| ENC-01 | **Partially** | Burrow production: yes, cloud-provider encryption at rest — engineering is solid here. WMP-FS01: no. Laptops: whatever the OS did by default; unverified. Backups: mixed, see BCP-01. |
| ENC-02 | **Mostly yes** | Burrow is TLS everywhere; the SaaS suite is TLS by nature. Inside the office network, file-share traffic is another story. |
| ENC-03 | **No** | Engineering manages cloud keys sensibly but nothing's written down as a process. |
| ENC-04 | **No** | Can't enforce, can't verify. No MDM. |
| LOG-01 | **No** | Logs exist in the cloud/SaaS consoles at default retention. Nothing centralized. WMP-FS01 logs roll over and vanish. |
| LOG-02 | **No** | Nobody's job is to look, so nobody looks. |
| LOG-03 | **No** | People forward weird emails to the helpdesk queue and Marisol or I answer when we can. There's no defined process or response time. |
| IR-01 | **No** | No plan. If something happened tomorrow it would be improvisation. |
| IR-02 | **No** | I assume Simone knows what we'd be required to do. I don't. |
| IR-03 | **No** | Nothing we're aware of. Knock wood. |
| IR-04 | **No** | No retainer. I wouldn't know who to call first. |
| BCP-01 | **Partially** | Burrow: cloud-side backups, engineering-managed, decent. WMP-FS01: a nightly copy to a USB drive attached to the same server. I know. I *know.* |
| BCP-02 | **No** | Never tested a restore of the office stuff. Burrow side, engineering has restored dev databases but never as a documented exercise. |
| BCP-03 | **No** | No BC/DR plan, no RTO/RPO anyone's agreed to. |
| HIP-01 | **No** | Never conducted. (RSK-01's answer, wearing a tie.) |
| HIP-02 | **Partially** | Ad-hoc onboarding slideshow from People. No annual cycle, no tracking. |
| HIP-03 | **No** | Simone flagged this during BAA drafting. Needs to exist. |
| HIP-04 | **In progress** | Simone is negotiating the BAA now. Subcontractor flow-downs need a look — see VND-01. |
| VND-01 | **No** | I can name our big providers off the top of my head, but there's no inventory and no assessments. Marketing signs up for new SaaS tools like it's free samples at the grocery store. |
| VND-02 | **No** | Never had one. |
| VND-03 | **No** | Nobody has ever read our subcontracts with security in mind. |

*Gus, closing note: reading this back, the pattern is that nothing here is broken because somebody chose wrong — it's all defaults nobody ever revisited while we grew 4x. That's not an excuse. It's the to-do list. Glad you're here.*
