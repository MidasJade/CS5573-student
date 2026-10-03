# L04 — Phishing Anatomy & ATT&CK Mapping

## Student Lab Guide

**Time:** ~75 minutes · **You need:** Docker Desktop running, and this lab folder.
**Submit:** the Canvas quiz (five findings) **and** the worksheet, exported to PDF.

**Open the worksheet now** — `L04_Worksheet.docx`, from Canvas — and fill it in *as you
go*. It asks for the exact header lines you based each verdict on, so writing it
afterwards from memory is harder and worse.

> **Which terminal do I use?**
> **Windows:** **PowerShell** (Start → "PowerShell"). If you already have WSL set up,
> that works too. Avoid the old `cmd.exe`.
> **macOS / Linux:** **Terminal**.
> Everything in this guide runs the same way in all three.

---

### Why this lab exists

Last week a machine handed you confident statements and you had to decide which ones
were real. This week the statements were written **by a person who was trying to fool
somebody**, which is a different problem.

It is also the problem you will actually be handed. Somebody forwards you a message and
asks "is this real?" You have minutes, you have no threat intelligence, and the answer
matters in both directions: clear a real lure and someone types their password into it;
escalate a legitimate message from a customer and you have cost your company a
relationship and your own credibility.

Here is what makes it tractable. **The part of an email designed to persuade you is the
part you can see. The part that records what actually happened is the part you have to
go looking for.** The body is an argument. The headers are evidence.

So this lab does almost nothing with the body. You will read delivery paths,
authentication records, link targets and attachment bytes — and you will find that the
most useful conclusions come from **comparing two messages**, not from staring at one.

One warning up front, because it is the whole lesson: **three of the five messages pass
every authentication check email has.** Two of those three are malicious. A check that
passes has answered the one question it was built to answer, and no other question.

---

### 0. Bring up the environment (~8 min — the gate)

Open a terminal, change into this lab's folder (the one containing
`docker-compose.yml`), and run:

```bash
docker compose up -d --build
```

The first run pulls a Python base image and builds one container; expect a minute or
two. Then confirm it:

```bash
docker compose ps
```

You should see **one** service, `analyst`, with state `Up`.

> **Nothing is listening and nothing is being scanned.** L04 has no targets, no network
> services, and no authorization boundary to restate — the messages are ordinary files
> on a disk, and every step below is offline. If you unplugged your network right now
> the lab would still work.

Now get a shell inside it:

```bash
docker compose exec analyst bash
```

Your prompt changes to:

```
root@analyst:/workbench#
```

**If your prompt does not say `analyst`, you are still on your own machine**, and
everything below will look empty. This is the single most common way to lose five
minutes in this lab. Run the `exec` line again.

Confirm the messages are there:

```bash
ls -l /cases/
```

Five files: `case01.eml` through `case05.eml`. They are mounted **read-only**, so you
cannot damage them — experiment freely.

One tool is installed, a small parser called `eml`. Check it:

```bash
eml --help
```

Read what it says about itself, because it tells you something about the exercise:

> *It renders nothing and it judges nothing. There is no "suspicious" verdict in this
> program, because deciding that is the analyst's job.*

Same principle as last week's scanner. The tool points; you decide.

---

### 1. What a message actually contains (~7 min)

Start with the one that is easiest to get right, so you learn the output format on an
easy case:

```bash
eml /cases/case01.eml
```

You get:

```
SUMMARY  /cases/case01.eml
------------------------------------------------------------------------
  From:         Arbor Ridge IT Service Desk <no-reply@arborridge-it.example>
  Reply-To:     Password Recovery Desk <recovery.desk@mailrelay-services.example>
  Return-Path:  <bounce-9914@mailrelay-services.example>
  To:           r.calder@arborridge.example
  Subject:      Action required: your password expires in 24 hours
  Date:         Mon, 17 Aug 2026 07:02:36 -0500
  Message-ID:   <20260817120236.6F1D3B1177@relay14.mailrelay-services.example>
  X-Mailer:     PHPMailer 6.6.3
  Auth results: (see --headers for the full record)
  Received:     2 hop(s)   (see --headers)
  Links:        1          (see --links)
  Attachments:  0          (see --attachments)
```

Four different address fields, and **they are four different things.** This is the first
thing to internalise, because mail clients show you only the first one:

| Field | What it is | Who controls it |
|---|---|---|
| **`From:`** | the name and address your mail client displays | **whoever composed the message** |
| **`Return-Path:`** | the *envelope* sender — where bounces go | the sending server |
| **`Reply-To:`** | where your reply goes if you hit Reply | whoever composed the message |
| **`To:`** | who it was addressed to | whoever composed the message |

**`From:` is not authenticated by anything in the message itself.** It is a label. You
can put whatever you like in it, the same way you can write any return address on an
envelope. Nothing in the email format prevents it.

Now look at what those four fields say *here*. The company in this exercise is **Arbor
Ridge Supply Co.** — you can read its real domain straight off the `To:` line, which was
written by the receiving organisation's own systems and is the one field in this message
nobody outside the company got to choose.

Compare it, character by character, to the domain in `From:`.

> **Worksheet B.1** asks you to write down both domains and say what the difference is.
> Do that now, before you read on — once you have seen it you cannot un-see it, and the
> exercise is noticing it unprompted.

Then notice `Reply-To:`. If you hit Reply on this message, your answer does not go to
the address shown in `From:`. It goes somewhere else entirely. **A `Reply-To:` on a
different domain from `From:` is not proof of anything by itself** — mailing lists and
ticketing systems do it legitimately all day. It is a question worth asking, not an
answer.

---

### 2. The delivery path (~10 min)

```bash
eml --headers /cases/case01.eml
```

The first section is the **`Received:` chain**. Every mail server that handles a message
adds a line at the *top* describing what it just received and from where. Nobody removes
earlier lines. So the chain is a stack, and the parser tells you how to read it:

```
  Each server prepends its own line, so the LAST line below is the
  earliest hop and the FIRST line is the most recent. Read bottom-up
  to follow the message forward through the network.
```

**Bottom-up is forward in time.** Bottom line = where it started. Top line = your own
mail server, last.

This matters because of who wrote each line. The `From:` header was written by the
sender. **The `Received:` lines were written by the servers that handled the message** —
including yours, which the sender does not control. The last few hops are as close to
tamper-proof as anything in email gets. An attacker can forge lines at the *bottom* of
the chain (they can claim anything about where their message came from before it reached
a real server), but they cannot rewrite what your own infrastructure recorded.

Read case01's chain now. Two hops: your company's inbound mail server, and the thing
that handed it over.

Now the second section, **`AUTHENTICATION RESULTS`** — what your receiving server
concluded when it checked the sender. The parser prints the record and then reminds you
what each check is for:

```
    SPF   - was this sending server permitted to send for the
            envelope domain? (Return-Path, not necessarily From.)
    DKIM  - is there a valid signature, and which domain signed it?
    DMARC - does the From domain line up with an SPF or DKIM pass,
            and what did that domain ask receivers to do on failure?
```

Spelled out, since the abbreviations are everywhere and rarely explained:

- **SPF — Sender Policy Framework.** A domain publishes a list of servers allowed to
  send mail for it. SPF asks: *is the server that just connected on that list?* Note
  carefully which domain it checks — the **envelope** sender (`Return-Path:`), which is
  often not the domain in `From:`.
- **DKIM — DomainKeys Identified Mail.** The sending domain cryptographically signs
  parts of the message. DKIM asks: *does the signature verify, and which domain signed
  it?* That second half is the part people skip.
- **DMARC — Domain-based Message Authentication, Reporting and Conformance.** Ties the
  other two to the thing users actually see. DMARC asks: *does the domain in `From:`
  line up with a domain that passed SPF or DKIM?* And it carries the From domain's own
  instruction for failures — `p=none` (do nothing), `p=quarantine`, `p=reject`.

For case01, all three have an opinion and it is not a flattering one. Write the three
results into **Worksheet B.2**.

---

### 3. Three checks, five messages (~12 min)

Now do all five at once. This loop runs the parser over each message and pulls out just
the authentication lines:

```bash
for f in /cases/*.eml; do echo "== $(basename $f)"; eml --headers "$f" | grep -E 'spf=|dkim=|dmarc='; done
```

That prints, exactly:

```
== case01.eml
  spf=fail (sender IP is 192.0.2.211) smtp.mailfrom=mailrelay-services.example;
  dkim=none (message not signed);
  dmarc=fail (p=none) header.from=arborridge-it.example
== case02.eml
  spf=pass (sender IP is 198.51.100.24) smtp.mailfrom=callowayfreight.example;
  dkim=pass header.d=callowayfreight.example header.s=cfl2024;
  dmarc=pass (p=quarantine) header.from=callowayfreight.example
== case03.eml
  spf=softfail (sender IP is 192.0.2.88) smtp.mailfrom=parcel-trace-intl.example;
  dkim=none (message not signed);
  dmarc=none (p=none) header.from=parcel-trace-intl.example
== case04.eml
  spf=pass (sender IP is 198.51.100.142) smtp.mailfrom=swiftmail-free.example;
  dkim=pass header.d=swiftmail-free.example header.s=sm1;
  dmarc=pass (p=none) header.from=swiftmail-free.example
== case05.eml
  spf=pass (sender IP is 198.51.100.24) smtp.mailfrom=callowayfreight.example;
  dkim=pass header.d=callowayfreight.example header.s=cfl2024;
  dmarc=pass (p=quarantine) header.from=callowayfreight.example
```

**Three of the five pass all three checks: case02, case04 and case05.**

Fill in **Worksheet C.1** — the grid of five messages against three checks — before
reading further. It is a transcription exercise and it takes ninety seconds, and it is
the thing you will refer back to for the rest of the lab.

Now the important part. If authentication were a verdict, you would be nearly done: two
messages to worry about, three to clear. **By the end of this lab you will have
established that two of those three passing messages are malicious.**

That is not a flaw in the exercise and it is not a flaw in SPF, DKIM or DMARC. They are
doing exactly what they were designed to do. The trouble is what people believe they
do. So be precise about it:

- A **DKIM pass** proves a private key held by some domain signed the message. It says
  nothing about whether that domain's owner wanted this particular message sent, and
  nothing at all about the person named in the display name.
- An **SPF pass** proves a server was on a list. Free mail providers' servers are on
  their own list, permanently, for everybody who signs up.
- A **DMARC pass** proves the `From:` domain is consistent with one of the above — so it
  tells you *the From domain is probably not forged.* It does not tell you that domain
  is one you should trust, or that the account behind it is in the right hands.

**Everything that can go wrong from here goes wrong in one of two ways:** the domain is
authentic and *the account is not in the right hands*, or the domain is authentic and
*it was never your company's domain in the first place.* One of each is waiting for you
in cases 02 and 04.

---

### 4. Where a link actually goes (~10 min)

```bash
eml --links /cases/case01.eml
```

```
LINKS  (href, and the text it was displayed as)
------------------------------------------------------------------------
  shown as : https://portal.arborridge.example/password
  goes to  : http://arborridge-sso.account-verify.example/reset?u=r.calder&id=9914
```

The visible text of a link and its destination are **two independent pieces of data**.
Nothing enforces a relationship between them. The text can be any string at all,
including a different URL — which is exactly what is happening here, and it is the
oldest trick in the format.

Read the destination from the right-hand end inward, because that is how a hostname is
actually structured: the rightmost labels are the registered domain and everything to
the left is a subdomain chosen by whoever controls it. `account-verify.example` is the
domain. `arborridge-sso` is a subdomain of it — a string the operator picked to make the
left-hand end of the URL look familiar. **Anyone can create a subdomain with your
company's name in it.** It costs nothing and proves nothing.

Note the destination is also plain `http`, while the displayed text claims `https`.

Now run the same command on the other four. One of them has a link whose displayed text
and destination are **different hosts** while the message's authentication is **entirely
clean**:

```bash
eml --links /cases/case02.eml
eml --links /cases/case05.eml
```

Those two messages claim the same sender. Both pass everything. One of their links goes
where it says it does. Record both in **Worksheet C.2**.

---

### 5. The attachment (~13 min)

One message in the set has an attachment. Find it from the summaries, then inspect it:

```bash
eml --attachments /cases/case03.eml
```

```
ATTACHMENTS
------------------------------------------------------------------------
  filename       : Delivery_Notice_7730184412.htm
  declared type  : text/html
  decoded size   : 1344 bytes
  sha256         : 8bf7f01d……………………………………………………………4b4bd6c
```

*(The digest is abbreviated here on purpose — the full 64 characters are on your
screen, and copying them from your own output is the point. It is finding **F4**.)*

Three things worth naming here.

**The declared type is a claim, like everything else.** `Content-Type` is written by the
sender. It is a hint about how to handle the bytes, not a statement of fact about them.

**The digest is how you talk about a file without sending it.** That SHA-256 is the same
idea you built in L01: a short, fixed-length name for an exact sequence of bytes. It is
how you ask a colleague "have you seen this one before?" or search a malware repository,
without forwarding the thing itself to anybody. Note that it is a digest of the
**decoded** bytes, not of the base64 text in the message — which is why two messages
carrying the same attachment with different line wrapping still produce the same digest.

**It was `base64`-encoded**, which is not encryption and not obfuscation. Mail was
specified for plain text, so binary content gets re-expressed in a 64-character alphabet
that survives the trip. Anybody can reverse it; the parser already did.

Now write the decoded bytes out and read them:

```bash
eml --attachments --save /workbench /cases/case03.eml
cat /workbench/Delivery_Notice_7730184412.htm
```

> ⚠️ **Read it as text. Do not open it in a browser.** It is a working HTML page and it
> will behave like one, including submitting whatever you type into it. Inside this
> container there is nothing it can reach, and the habit is the point: **you examine
> artifacts, you do not operate them.**

It is a login form. Find the `<form>` tag and read its `action` attribute — that is the
address the browser would send the contents to when the button is pressed. If you would
rather pull it out directly than read the whole file:

```bash
grep -oE 'action="[^"]*"' /workbench/Delivery_Notice_7730184412.htm
```

**That host is finding F3.** Note what the page is asking for, and what the two hidden
fields carry.

Last, verify the digest a second way, with a completely different tool:

```bash
sha256sum /workbench/Delivery_Notice_7730184412.htm
```

The same 64 characters, from a program that knows nothing about email. **That is what
corroboration looks like** — and it is worth noticing how different this is from last
week, when `whatweb` and `nmap` "agreed" because they were both reading the same banner.
Two tools reaching the same answer by the same route is one observation, not two.

---

### 6. The one you don't escalate (~12 min)

You now have four of your five findings within reach. The last one is a judgment call,
and it is the one that would actually be your job.

**Two of these messages claim to come from the same person at the same partner company.
Both pass every authentication check. One is fine. One is not.**

Put them side by side:

```bash
eml --headers /cases/case05.eml
eml --headers /cases/case02.eml
```

Look at the **earliest hop in each** — the bottom line of each chain, the one describing
how the message first entered the partner's mail system.

For case05 it is:

```
      from WIN-CFL-MAIL01.callowayfreight.local ([10.20.4.18])
      by mx1.callowayfreight.example with ESMTP id 7a41c9;
```

For case02 it is:

```
      from [203.0.113.77] (unknown [203.0.113.77])
      by mx1.callowayfreight.example with ESMTPSA id 2f88e1
      (authenticated sender o.brantley@callowayfreight.example);
```

Both were genuinely handled by `mx1.callowayfreight.example`. That is *why* both pass
SPF and DKIM — the partner's real infrastructure really did send both, and really did
sign both. The authentication is not lying.

The difference is where each message **entered** that infrastructure:

- `ESMTP` from a host inside the partner's own network, named like a company mail
  server, on a private address. That is mail originating in their office.
- `ESMTPSA` — the `A` is for *authenticated* — from an unremarkable public address, with
  the server noting which account signed in. That is somebody logging into a mail
  account from somewhere else and submitting a message through it.

Submitting mail with a username and password from an arbitrary address is a completely
normal thing to do; it is how every phone and laptop sends mail. **On its own it means
nothing.** What makes it evidence here is that you have the comparison: the *same
account*, days apart, and only one of the two arrived the way this person's mail
normally arrives.

> This is why the lab gave you two messages from the same sender. A single message's
> headers are often not conclusive. **A baseline turns a header into a finding** — and
> in real work, building that baseline is most of the job.

Now read both bodies and both links, and ask the practical questions: what is each one
asking the recipient to do, where does each link go, and does it make sense that this
person would need the recipient to do that?

Then decide. **One of the five is legitimate and should not be escalated** — that is
finding F5, and the worksheet asks you to justify it with specific header evidence, not
an impression. Clearing a message is a claim, and it needs support exactly like
accusing one does.

**And do not stop at four.** Before you submit, you should have a verdict on **all
five**, including case04 — which passes everything, is not finding F1, and is not
legitimate either. Worksheet D asks you about it directly. The question to ask of
case04 is not *"did the checks pass?"* but *"what domain did they pass for, and what has
that got to do with the person this message claims to be from?"*

---

### 7. Map it to ATT&CK (~8 min, worksheet only)

Tuesday gave you the vocabulary; this is where you use it. For each message you judged
malicious, give the **tactic** and the **technique with its identifier**, looked up
yourself at **attack.mitre.org** — not copied from the lecture slides.

All of these messages sit in one tactic: **Initial Access**. The interesting part is the
technique, and in particular the sub-technique, because the three lures here use
genuinely different mechanisms to accomplish the same goal. Start from **T1566,
Phishing**, read its sub-techniques, and pick the one that matches what each message
actually did.

Two notes, both of which are the real-world experience of doing this:

**More than one mapping can be defensible, and that is fine** — say which you chose and
why in one line. This section is read by a human, not matched against a string. What is
*not* defensible is a mapping that doesn't fit the evidence you collected.

**And ATT&CK has no severity ratings**, so there is nothing to rank here. If you find
yourself wanting to say one technique is worse than another, notice that the judgment is
coming from you and your environment — which is precisely the argument from Tuesday.

Worksheet **§E** has the table.

---

### 8. Submit

Two things, both due **Sunday 11:59 PM**:

1. **The Canvas quiz** — five findings, short answer. Matching is case-insensitive and
   ignores surrounding spaces; a pasted URL or an email address is accepted where a
   hostname is asked for. One question is read by a human.
2. **The worksheet**, exported to **PDF** from `L04_Worksheet.docx`.

Everyone's five values are the same — the messages are identical for the whole class, so
identical findings are expected and are not treated as collusion. **What is yours is the
reasoning**: the header line you cite for each verdict, your case04 answer, and your
ATT&CK mappings.

---

### Optional extension (ungraded)

If you have time and want to go further, in rough order of effort:

- **`eml --raw /cases/case02.eml`** — the header block exactly as stored. Find the
  `References:` header and confirm that case02 really does point at case05's
  `Message-ID`. The thread is genuine; only the newest message in it isn't.
- **Count the hops.** `eml` reports a hop count in each summary. **Two messages have
  three hops; three have two** — and the two with the extra hop are the pair from the
  partner company. Work out why, from their chains: a message that really originated
  inside another company's office has to cross that company's own mail server before it
  reaches theirs and then yours. The messages injected straight at your mail server from
  a rented host have one fewer. **A longer path can be the more trustworthy one**, which
  is the opposite of most people's instinct — and note it does not separate case02 from
  case05, because case02 abused that same real path.
- **Look up the IP addresses** used in these fixtures — `192.0.2.211`, `198.51.100.24`,
  `203.0.113.77`. They are all in ranges reserved by **RFC 5737** for documentation, so
  none of them belongs to anybody. Finding that out yourself is a small lesson in
  checking the thing in front of you rather than assuming it is real.
- **Write the `From:` header you would have to forge** to make case04 convincing, and
  then work out which of the three authentication checks would have stopped it. This is
  the fastest way to understand what DMARC is actually for.

---

### Shutting the lab down (when you're finished — not graded)

Nothing in this section is submitted or graded. Do it once you're done, so the lab isn't
running on your machine for the rest of the semester.

> ⚠️ **Submit first.** Shutting down removes the container, and anything you saved
> inside `/workbench` goes with it. Get your five findings into the Canvas quiz and your
> worksheet filled in **before** you run this.

Leave the container (`exit`), make sure you're in the `L04_Phishing_Anatomy` folder, and
run:

```bash
exit                  # only if you're still at root@analyst:/workbench#
docker compose down
```

Expect it to remove one container and the lab's default network.

**What survives:** the image it pulled and built, and the five message files — those
live in this folder on your own disk, not in the container, so they are still here
afterwards. Coming back is just `docker compose up -d --build`, and it'll be much faster
the second time.

**Why bother?** The service here is set to restart itself whenever Docker Desktop
starts — which means every reboot. Left alone, it quietly runs all semester.

**If you'd rather pause than remove it:**

```bash
docker compose stop      # pause it; it survives
docker compose start     # resume later
```

**Reclaiming disk space (optional).** At the **end of the semester** — not before —
`docker compose down --rmi local` removes the image too; it re-downloads if you come
back.

---

### Troubleshooting

**`docker: error during connect` / `cannot connect to the Docker daemon` / a named-pipe
or socket error.**
Docker Desktop isn't running. Start it and wait for **"Engine running"** in its window
before retrying. Same fix as L01 Step 2.
*Windows:* if it stays stuck, quit Docker Desktop, run `wsl --shutdown` in PowerShell,
and start it again.
*macOS:* quit and reopen Docker Desktop from Applications.
*Linux:* `sudo systemctl start docker`.

**`no such service: analyst` or `no configuration file provided`.**
You're in the wrong folder. `cd` into `L04_Phishing_Anatomy` — the one containing
`docker-compose.yml` — and try again.

**`ls /cases/` says no such file or directory, or prints nothing.**
You are on your own machine, not inside the container. Run
`docker compose exec analyst bash` first; your prompt must read
`root@analyst:/workbench#`. This accounts for most lost time in this lab.

**`eml: command not found`.**
You're outside the container (see above). Inside it, `eml` is on the path; the long form
`python3 /opt/eml.py` also works everywhere.

**`eml.py: no such file: case01.eml`.**
Give the full path: `/cases/case01.eml`. The messages are not in your working directory.

**The `for` loop in §3 prints nothing.**
Check you are inside the container, and that you typed `/cases/*.eml` with the leading
slash. On Windows, run it **inside** the container as shown — PowerShell does not
understand this loop syntax, which is one more reason to get the prompt right first.

**`Permission denied` writing to `/workbench`.**
You are somewhere else in the filesystem. `cd /workbench` and retry. `/cases` is
read-only by design and you cannot write there.

**I want to start over.**
```bash
docker compose down
docker compose up -d --build
```
The messages are read-only and mounted from this folder, so nothing you did can have
changed them.

**No Docker at all?**
You can do this entire lab without it. The five messages are plain files in
`env/analyst/cases/`, and the parser is `env/analyst/eml.py` — pure Python standard
library, no packages to install. From this folder, on any machine with Python 3:

```bash
python3 env/analyst/eml.py env/analyst/cases/case01.eml
python3 env/analyst/eml.py --headers env/analyst/cases/case02.eml
```

Every command in this guide works that way; substitute the paths. The findings are
identical. **L04 is the one lab in this course with no real dependency on Docker** —
tell me if you take this route, but you are not at any disadvantage.
