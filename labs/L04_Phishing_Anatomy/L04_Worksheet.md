# L04 Worksheet — Phishing Anatomy & ATT&CK Mapping

**Name:** ________________________  **Date:** ______________

Fill this in **as you go** — several questions ask for the exact header line you based a
verdict on, which is much harder to reconstruct afterwards.

**Submit:** this worksheet exported to **PDF**, *and* the five findings in the Canvas
quiz. Both due **Sunday 11:59 PM**.

> Everyone's five findings are the same — the messages are identical for the whole
> class, so matching values are expected and are not treated as collusion. **What is
> yours is the reasoning** in sections D, E, F and G.

---

## A. Environment

**A.1** Paste the output of `docker compose ps` (or write the service name and state):

```
```

**A.2** How many message files are in `/cases/`? _______

**A.3** This lab involved no scanning and no network targets. In one sentence, why did
that make the authorization question from L03 inapplicable this week?

```
```

---

## B. Reading one message

All of section B is about **case01**.

**B.1** Two domains, copied exactly:

| | Domain |
|---|---|
| The domain in the `To:` line (the company's real one) | |
| The domain in the `From:` line | |

What is the difference between them, in your own words?

```
```

**B.2** Record case01's three authentication results:

| Check | Result |
|---|---|
| `spf=` | |
| `dkim=` | |
| `dmarc=` | |

**B.3** The `Reply-To:` address is on a different domain from the `From:` address. Name
one **legitimate** reason a real business message might do that.

```
```

**B.4** In the `Received:` chain, which line was written by a server **your own
organisation controls** — the top one or the bottom one? Why does that make it harder to
forge than the `From:` header?

```
```

---

## C. Findings

**C.1** The grid. One row per message, from the loop in §3 of the guide:

| Message | `spf=` | `dkim=` | `dmarc=` |
|---|---|---|---|
| case01 | | | |
| case02 | | | |
| case03 | | | |
| case04 | | | |
| case05 | | | |

How many of the five pass **all three**? _______

**C.2** Links — displayed text vs. actual destination:

| Message | Shown as | Goes to | Same host? |
|---|---|---|---|
| case01 | | | |
| case02 | | | |
| case05 | | | |

**C.3** The five findings you'll enter in Canvas:

| | Finding | Your answer |
|---|---|---|
| **F1** | The malicious message that is a **reply inserted into a real existing thread** | |
| **F2** | The `From:` domain in the password-expiry message that **imitates the company's own domain** | |
| **F3** | The **host the decoded attachment submits credentials to** | |
| **F4** | The **SHA-256 of the decoded attachment** | |
| **F5** | The message that is **legitimate** and should **not** be escalated | |

**C.4** For **F4**, give the two different commands you used to arrive at the same
digest:

```
1.
2.
```

---

## D. Verdicts and reasoning *(graded)*

A verdict with no evidence attached is an impression. For **each** message: malicious or
legitimate, and **the specific header line, link, or file content** that supports it.
One or two sentences each.

**D.1 — case01**

```
```

**D.2 — case02**

```
```

**D.3 — case03**

```
```

**D.4 — case04.** This one passes SPF, DKIM **and** DMARC, it is not F1, and it is not
legitimate. Explain why every check passing tells you nothing useful here. Your answer
should name **which domain** the checks passed for.

```
```

**D.5 — case05.** This is F5. Justify **clearing** it with specific evidence — not
"nothing looked wrong." What did you check, and what did it show?

```
```

**D.6** Two of these messages claim the same sender and both pass every authentication
check. Quote the **one line from each** that separates them, and say what the difference
means.

```
case05:
case02:
Difference:
```

---

## E. ATT&CK mapping *(graded)*

For each message you judged malicious. Look the technique up yourself at
**attack.mitre.org** — do not copy from the lecture slides. More than one mapping can be
defensible; the one-line reason is what's being read.

| Message | Tactic | Technique (name + ID) | Why this one, in one line |
|---|---|---|---|
| case01 | | | |
| case02 | | | |
| case03 | | | |
| case04 | | | |

**E.1** All four sit in the same tactic. Name it, and say in one sentence why the
*tactic* is the same when the *mechanisms* are so different.

```
```

**E.2** You were told not to rank these by severity. Why can't you — what is it about
ATT&CK that makes the request impossible to satisfy?

```
```

---

## F. Limits — what header analysis does **NOT** tell you *(graded)*

Every technique has an edge. Name **three** things you could **not** determine about
these messages from the evidence available in this lab, even in principle.

```
1.
2.
3.
```

**F.1** You cleared case05 on header evidence. Describe one scenario in which that
verdict would be **wrong** anyway — i.e. the headers look exactly like this and the
message is still hostile.

```
```

**F.2** Suppose you had been handed only **case02**, with no case05 to compare it
against. Could you still have reached the same verdict? What would you have had to do
instead?

```
```

---

## G. How this feeds the security program

Nothing from this lab goes on your risk register or into your threat profile as a
**fact** — these messages are from a different, fictional company, and
`arborridge.example`, `case02.eml` and that SHA-256 digest have no place in a document
about your employer. What transfers is the **method** and the **classes of finding**: a
sender that isn't who it displays as, a check that passes and proves less than it
appears to, and a judgment call about what not to escalate.

Where it belongs is **§4 of the program report**, as part of the threat profile you're
writing this week — specifically the *"would it work here, and would we know"* columns.

**G.1** Name **one** thing you would need to know about **your own company** before you
could say whether a message like case02 would have worked there — and name the
questionnaire item (or packet section) that would tell you.

```
```

**G.2** Now the second column. If a message like case02 arrived at your company and
somebody clicked the link, **what would have to be true for anyone to find out?** Name
one thing, and whether your company currently has it.

```
```
