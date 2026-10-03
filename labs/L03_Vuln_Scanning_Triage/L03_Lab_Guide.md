# L03 — Vulnerability Scanning & Triage

## Student Lab Guide

**Time:** ~75 minutes · **You need:** Docker Desktop running, and this lab folder.
**Submit:** the Canvas quiz (five findings) **and** the worksheet, exported to PDF.

**Open the worksheet now** — `L03_Worksheet.docx`, from Canvas — and fill it in *as you
go*. It asks for the exact commands you ran, so writing it afterwards from memory is
harder and worse.

> **Which terminal do I use?**
> **Windows:** **PowerShell** (Start → "PowerShell"). If you already have WSL set up,
> that works too. Avoid the old `cmd.exe`.
> **macOS / Linux:** **Terminal**.
> Everything in this guide runs the same way in all three.

---

### Why this lab exists

Last week you built an asset inventory — *what exists*. This week you find out *what's
wrong with it*, and then do the part that actually matters.

Running a scanner is not a skill. You type one command and a tool hands you back dozens
of confident-looking statements. **Every one of them is the tool's opinion**, formed
without knowing anything about your company, your data, or what else is in place. Some
will be real and urgent. Many will be true and worthless. Some will describe files that
do not exist. And one set of them will be **flatly wrong about the host it's
describing** — not vague, not hedged: specific, detailed, and wrong.

Your job is to tell them apart. That's triage.

---

### 0. Bring up the environment (~10 min — the gate)

Open a terminal, change into this lab's folder (the one containing
`docker-compose.yml`), and run:

```bash
docker compose up -d --build     # first run pulls images + builds (~2–4 min)
docker compose ps                # you should see FOUR containers, all "Up"
```

Expect `l03-web01`, `l03-app01`, `l03-devbox` and `l03-scanner`, all **Up**.

> ### ⚠️ "Cannot connect to the Docker daemon" / pipe / socket error
>
> If `docker compose up -d --build` fails with something like:
>
> **Windows:** `open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.`
> **macOS / Linux:** `Cannot connect to the Docker daemon at unix:///var/run/docker.sock.`
>
> …then **Docker Desktop isn't running.** In order:
>
> 1. Start Docker Desktop and wait for it to say **"Engine running."** Re-run the
>   command.
> 2. Still failing? Quit Docker Desktop fully and reopen it.
> 3. Wedged backend — **Windows:** Docker Desktop → ⚙ → *Troubleshoot* → **Restart**.
>   **macOS:** same menu, *Restart*. **Linux:** `sudo systemctl restart docker`.
>
> If none of that works, bring the exact error to Thursday's session.

**Fewer than four Up?** Re-run `docker compose up -d --build`, then check the one that
didn't start with `docker compose logs <name>` (for example
`docker compose logs l03-web01`). Don't start scanning a half-up environment — you'll
get results that are wrong in ways that are hard to spot.

Now step **inside** the scanner container. Right now your terminal is talking to your
own computer (Windows, macOS, or Linux); this command opens a shell — a command prompt —
*inside* the scanner workstation, which is a small Linux machine running on your
computer with all the tools already installed:

```bash
docker compose exec scanner bash
```

Reading it: `docker compose exec` = run something inside a running container,
`scanner` = which one, `bash` = the program to run (a shell). Your prompt changes to:

```
root@scanner:/work#
```

That's how you know you're inside. Everything for the rest of this lab runs **there**.
Type `exit` to come back to your own machine.

Quick check that your tools are present:

```bash
nmap --version
whatweb --version
curl --version
```

> **A tool missing or erroring?** Not fatal. Tell your instructor and use
> `nmap -sV --script http-enum,http-headers <target>` wherever this guide says "run the
> scanner." **Every value this lab asks for comes from the targets themselves, not from
> a scanner's output**, so the answers do not change.

---

### 1. Authorization, and why it's the first heading (~2 min)

You are authorized to scan **`172.29.0.0/24` and nothing else.** Not your home network,
not your employer's, not a website you're curious about, not the other lab's segment.

This is not a formality. Running a vulnerability scanner against a host you don't have
written permission to test is, depending on where you are, a contract violation, a
firing offence, or a crime. The scanner does not know or care whose machine it is
pointed at. **You are the control.**

In real engagements this boundary is written down before anyone touches a keyboard —
scope, addresses, dates, and who signed. Tonight it's one line, and it's the same idea.

The three targets:


| IP            | What it appears to be          |
| ------------- | ------------------------------ |
| `172.29.0.10` | intranet web server            |
| `172.29.0.20` | internal application front end |
| `172.29.0.30` | developer utility box          |


---

### 2. Look before you scan (~8 min)

Start by finding out what's actually listening. From inside the scanner:

```bash
nmap -p- --open 172.29.0.10-30
```

`-p-` scans **all 65,535 ports** rather than nmap's default top-1000 — slower, and the
only way to be sure you haven't missed a service parked somewhere unusual. `--open`
hides the closed ones so the output is readable.

You should find **three** open ports across the three hosts. Write them into your
worksheet's target table now, with which host each belongs to.

Then look at each one by hand, before any scanner tells you what to think:

```bash
curl -sI http://172.29.0.10/            # -s = quiet, -I = headers only
curl -sI http://172.29.0.20:8080/
curl -sI http://172.29.0.30:9090/
```

Read the `Server:` header on each. **Write all three down exactly as they appear** —
you'll need one of them later, and you'll need to distrust another one.

> **Why by hand first?** Because in ten minutes a scanner is going to hand you a page of
> conclusions, and it is much easier to evaluate those conclusions if you have already
> formed a few of your own. Going in cold makes you a reader of the tool's output
> instead of its reviewer.

---

### 3. Run the scanner (~10 min)

Now let the tools talk. You have two, and they work differently — which matters later.

**`whatweb`** fingerprints a web service from what it *says about itself*: response
headers, page markup, cookie names. **`nmap -sV`** fingerprints from how a service
*responds to probes*, and `--script http-enum` additionally guesses at paths that
commonly exist.

```bash
whatweb -v http://172.29.0.10/
whatweb -v http://172.29.0.20:8080/
whatweb -v http://172.29.0.30:9090/

nmap -sV --script http-enum,http-headers,http-methods -p80   172.29.0.10
nmap -sV --script http-enum,http-headers,http-methods -p8080 172.29.0.20
nmap -sV --script http-enum,http-headers,http-methods -p9090 172.29.0.30
```

The nmap runs take a minute or two each. **Don't read them yet** — let them all finish,
then come back. (To keep the output: `nmap ... -oN web01.txt`.)

Now read what came back, and notice the *shape* of it before the content.

**Most of what you got is description, not judgment.** Look at the whatweb reports:
`Status: 200 OK`, `Title`, `IP`, `Country: RESERVED, ZZ`, a dump of the response
headers, `HTML5` detected from the doctype. Every line is true. `Country: RESERVED, ZZ`
is whatweb geolocating a private lab address and finding, correctly, that there is no
country — a finding that is accurate and worth nothing. `IP: 172.29.0.10` restates what
you typed. None of this tells you whether anything is wrong.

**Then look at `http-enum` on `172.29.0.10`.** It returned about **seventy-seven
lines**, and they look alarming:

```
/admin/account.php: Possible admin folder (401 Unauthorized)
/admin/download/backup.sql: Possible database backup (401 Unauthorized)
/admin/upload.php: Admin File Upload (401 Unauthorized)
/admin/CiscoAdmin.jhtml: Cisco Collaboration Server (401 Unauthorized)
/admin/environment.xml: Moodle files (401 Unauthorized)
```

A database backup. A file upload. Cisco. Moodle. **None of those exist.** That host
serves a handful of static HTML files — there is no PHP on it, no ASP, no JSP, no
ColdFusion, no CMS, no `backup.sql`.

**So why did the scanner report them?** Two commands will show you. Ask for a file under
`/admin/` that does exist, then ask for one that obviously doesn't:

```bash
curl -sI http://172.29.0.10/admin/index.html
curl -sI http://172.29.0.10/admin/there-is-no-such-file.php
```

Both come back **`401 Unauthorized`**, with an identical
`WWW-Authenticate: Basic realm="Restricted"` header. The same response for a file that
is there and a file that never was.

> **Mind the trailing slash.** If you ask for `http://172.29.0.10/admin` — no slash —
> you get a **`301 Moved Permanently`** instead, pointing you at `/admin/`. That isn't
> the access control; it's the web server noticing you asked for a directory by the
> wrong name and redirecting you to the right one, which happens *before* the password
> rule applies. Request the two files above, not the directory, and the comparison is
> exact.

That's the whole explanation. `/admin/` is password-protected, and the server asks for
credentials **before** it looks to see whether the file exists — so it never gets as far
as `404 Not Found`. You failed the first check, and the request stops there.

Which means that from the outside, **"protected" and "absent" look identical.** A
scanner guessing filenames gets `401` for every guess, reads each one as *"something is
here and it's locked,"* and reports it. Seventy-odd times.

**The tool is not broken. It is reasoning correctly from a misleading signal** — which
is worth sitting with, because it is the same failure you are about to meet in a
completely different form in step 4.2.

Three more things to notice:

- **`http-methods` says `Supported Methods: GET HEAD`.** True, and completely fine.
  Nothing risky is enabled. The script reports the list either way, because reporting
  is its job — deciding whether `GET HEAD` is a problem is yours.
- **`http-enum` found nothing at all on `.20` and `.30`.** Not because they're safer —
  because neither has a password-protected directory to produce the 401 cascade. **The
  host that looks worst in the scan is the one with a working access control on it.**
- **Exactly one line in those seventy-seven matters**, and it is not formatted any
  differently from the sixty wrong ones:

  ```
  /backup/: Backup folder w/ directory listing
  ```

That is this lab in one screen. The tool reported a true and important thing, in the
same typeface, at the same severity, in the same list, as dozens of things that are
false. It had no way to tell them apart. **You do** — and that is the entire job.

---

### 4. Triage: verify before you believe (~20 min)

Work through the four findings below. For each one, the scanner may or may not have
mentioned it — that's not the point. **The point is that you confirm each one yourself,
from the target, and record what you observed separately from what you concluded.**

#### 4.1 — A directory that shouldn't be listable

Your scan already told you about this one — `/backup/: Backup folder w/ directory
listing`, one line in seventy-seven. Plenty of people skim past it, and on its own
"directory indexing enabled" really is just an informational finding. Don't skim. The
question is never *"is indexing on?"* — it's ***"what does it expose?"***

```bash
curl -s http://172.29.0.10/backup/
```

You'll get an HTML listing. Look at what's in it. One of those files is not a file you'd
want a stranger reading, and you can fetch it with no credentials at all:

```bash
curl -s http://172.29.0.10/backup/<the filename>
```

**Finding F1: what is that file called?** (Just the filename.)

Notice the difference between what the scanner said and what you now know. "Directory
indexing enabled" is a configuration observation. "Anyone on this network can download
a file containing our staff's names, departments, extensions and desk locations" is a
**risk** — the kind of sentence you learned to write on Tuesday.

#### 4.2 — A server that says what it isn't

Look again at what `172.29.0.20:8080` claims to be:

```bash
curl -sI http://172.29.0.20:8080/ | grep -i '^server:'
```

**Finding F2: what exactly does that `Server:` header say?**

Now look at what your **tools** concluded from that header. Check what `whatweb` said
about this host, and what `nmap -sV` called the service. Both of them will have named
that software — and the version is genuinely ancient, which means anything either tool
goes on to say about known weaknesses in it would be serious.

Notice how far each tool ran with it. `nmap -sV` reports the service as
`Apache httpd 2.2.14 ((Unix))`. `whatweb` goes further — it loads its **Apache** plugin,
reports `Version: 2.2.14 (from HTTP Server Header)`, infers `OS: Unix`, links you to
httpd.apache.org, and offers you **Google dorks** for finding more hosts like it. An
entire chain of confident, specific, useful-looking conclusions, every link of which
rests on one string the server chose to send.

> **Two tools agreed. That is not corroboration.** They read the *same banner*.
> Agreement between two tools that share a source tells you nothing you didn't already
> know from the source. This matters more than it looks: *"we confirmed it with a second
> tool"* is a sentence people write in real reports, and it is often worth exactly
> nothing.
>
> Compare `172.29.0.30`, where both tools say Python and both are right. The tools
> aren't bad at this. They are **exactly as reliable as what they're reading.**

Before you write any of that into a report, get a **second, independent signal.** A
banner is a string the server chooses to send. It is a *claim*, not evidence. Ask the
server to do something instead:

```bash
curl -s http://172.29.0.20:8080/this-path-does-not-exist
```

Look carefully at that error page. Compare it with what you know about the software the
banner named. **Does this host look like it's running what it says it's running?**

#### 4.3 — A service with no front door

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://172.29.0.30:9090/
curl -s http://172.29.0.30:9090/
```

No username. No password. No prompt. **Finding F3: what TCP port is that service on?**

Have a look at what it's serving. It's not catastrophic — but ask yourself the inventory
question from last week: *who decided to expose this, and does anyone know it's here?*

#### 4.4 — The one the scanner got wrong

Put 4.2 together. One of your three hosts produced scanner findings that are
**confidently, specifically wrong** — not "low severity," not "probably fine," but
describing software the host is not running at all.

**Finding F4: which host is it?** (Its IP, or its name.)

> **This is the most transferable thing in the lab.** Banner-based fingerprinting is the
> largest single source of scanner false positives in real work. If you hand a
> remediation ticket to an engineer telling them to patch software they don't have, you
> will be wrong in front of someone who can check — and the next finding you bring them,
> the real one, gets less attention than it deserves.
>
> **And be careful what you conclude.** "The finding is false" does **not** mean "the
> host is fine." Think about what it means that a server on your network is
> misreporting its own software — to you, to your scanner, and to whatever inventory
> you were planning to build from that data.

---

### 5. Decide what to fix first (~8 min)

You now have real findings across three hosts, and finite time. Tuesday's question,
made concrete:

**Finding F5: which single host would you remediate first?** Submit the host, and write
your justification on the worksheet in 2–3 sentences.

Weigh, as you did in the lecture:

- **Is it confirmed or potential?** Something you downloaded with no credentials is
confirmed exposure. Something a tool says *might* be possible is not.
- **What's actually at stake?** Personal data about employees is not the same as
operational metadata about a build server.
- **Is anything currently in the way?** A control that already exists changes the answer.
- **What does the fix cost?** High exposure plus a cheap fix is the easiest argument you
will ever make to a busy person.

There is more than one defensible answer here, and you are graded on the **argument**,
not on matching a key.

---

### 6. Submit

1. **The Canvas quiz.** Five findings, F1–F5. One item asks you to paste the exact
  command you ran and say in one sentence what its output showed.
2. **The L03 worksheet.** Finish `L03_Worksheet.docx` (sections A–E), then save it as a
  **PDF** — in Word: **File → Save As**, choose **PDF** — and upload the **PDF**, not
   the `.docx`.

---

### Optional extension (ungraded)

- **See how thin a banner is.** `curl -sI http://172.29.0.10/` — nginx tells you its
exact version, because `server_tokens` is on. What would an attacker do with that,
and what would turning it off actually buy you? (Careful: less than people think.)
- **Try the admin door.** `curl -sI http://172.29.0.10/admin/` returns 401. That's a
control doing its job. Now ask the harder question: what would you need to know to
decide whether it's a *good* control?
- **Make a tool contradict itself.** Fetch the banner with `curl -sI`, ask `whatweb`
and `nmap -sV` about the same host, then request a page that doesn't exist. Three views,
one of which disagrees with the other two. Which would you put in a report, and why
that one?

Nothing here is submitted; it's for the curious.

---

### Shutting the lab down (when you're finished — not graded)

Nothing in this section is submitted or graded. Do it once you're done, so the lab isn't
running on your machine for the rest of the semester.

> ⚠️ **Submit first.** Shutting down removes the containers, and anything you typed or
> saved inside them goes with them. Get your five findings into the Canvas quiz and your
> worksheet filled in **before** you run this.

Leave the scanner (`exit`), make sure you're in the `L03_Vuln_Scanning_Triage` folder,
and run:

```bash
exit                  # only if you're still at root@scanner:/work#
docker compose down
```

Expect it to remove four containers and the `l03net` network.

**What survives:** the images it pulled and built. Coming back is just
`docker compose up -d --build`, and it'll be much faster the second time. Nothing on
your own computer is touched.

**Why bother?** Every service here is set to restart itself whenever Docker Desktop
starts — which means every reboot. Left alone, it quietly runs all semester.

**If you'd rather pause than remove it:**

```bash
docker compose stop      # pause all four; they survive
docker compose start     # resume later
```

**Reclaiming disk space (optional).** At the **end of the semester** — not before —
`docker compose down --rmi local` removes the images too; everything re-downloads if you
come back.

And the same point as last week, which matters more in this lab than any other: **you
are finished scanning.** The authorization covered `172.29.0.0/24` for this exercise.
The exercise is over. Take it down.

---

### Troubleshooting

- **`docker compose` says the daemon isn't running:** start Docker Desktop and wait for
"Engine running," then retry. The single most common issue.
- **`docker compose exec scanner bash` says "no such service":** you're not in the
`L03_Vuln_Scanning_Triage` folder (the one with `docker-compose.yml`). Run `pwd` to
check, then `cd` there.
- **Fewer than four containers `Up`:** re-run `docker compose up -d --build`, then
`docker compose logs <name>`. Don't scan a half-up environment.
- **A scanning tool is missing or errors:** use
`nmap -sV --script http-enum,http-headers <target>` instead, and tell your instructor.
**None of the five findings change** — they come from the targets, not the scanner.
- **A `curl` returned `301 Moved Permanently` instead of what the guide said:** you
probably dropped a trailing slash on a directory. `/admin` redirects to `/admin/`;
`/backup` redirects to `/backup/`. Add the slash, or request a file inside it.
- **`curl` returns nothing at all for a host:** check you used the right port. 80 for
`.10`, 8080 for `.20`, 9090 for `.30` — a `curl` to the wrong port on a live host
hangs or returns empty rather than saying "wrong port."
- **A scan seems to hang:** `nmap -p-` takes a while — all 65,535 ports. Give it a
minute or two before assuming something's wrong.
- **Accessibility path:** if you can't run the interactive session, an annotated
transcript of the whole lab is on Canvas; the worksheet and quiz are identical either
way.

