# L01 — Environment Setup & Hashing Warmup

## Student Lab Guide

**Week 1 · CS5573 · Target time: 60 minutes (core) + optional extension**

**What you turn in — two things, both due Sunday 11:59 PM:**

1. **The L01 Canvas quiz** — the five values you discover in this lab.
2. **The L01 worksheet** — a ~2-page Word document (`L01_Worksheet.docx`, download it
  from Canvas) where you record *how* you got each answer and what it does and doesn't
   prove. Type your answers into it, then **export it as a PDF and upload the PDF.**

> **Open the worksheet now, before you start, and fill it in as you go.** It asks for
> the exact command you ran for each finding. Those are quick to jot down in the moment
> and genuinely annoying to reconstruct an hour later from memory.

---

### Why this lab exists

Two jobs this week, and they're both foundational.

**First, prove your environment works — now, while it's cheap to fix.** Every
lab for the rest of the semester runs in Docker. If your Docker Desktop is going
to fight you, we find out in Week 1 on a lab where nothing is at stake, not in
Week 6 the night before a deadline. Getting the container up *is* half the grade
of this lab, and it is the "environment verified" gate for the course.

**Second, warm up on the two skills every later lab assumes:** working at a
command line, and **hashing** — the tool that lets you say, with math instead of
faith, "this file is exactly the bytes I think it is." Integrity — the *I* in the
CIA triad from Tuesday — starts here. You can't reason about whether something was
tampered with until you can *fingerprint* it.

Nothing in this lab requires prior Linux experience. If you've never opened a
terminal, this is the on-ramp; go slowly and read the output.

---

### 0. Set up Docker & bring up the workbench (~15 min — the gate)

> **Which terminal do I use?** You only need a terminal *on your own computer* for the
> three `docker compose` commands in this section. **Every other command in this lab
> runs inside the container, in Linux `bash` — so once you're inside, your operating
> system no longer matters.**
>
> - **Windows:** open **PowerShell** (search "PowerShell," or use Windows Terminal).
> The commands below work exactly as written, with no extra setup once Docker Desktop
> is running. *(If you already use WSL/Ubuntu with Docker Desktop's WSL integration
> turned on, that works too — but don't install WSL just for this. Avoid old
> `cmd.exe`.)*
> - **macOS / Linux:** use your normal **Terminal**.

1. **Install Docker Desktop** if you haven't (Windows/macOS: the installer from
  docker.com; Linux: Docker Engine + the compose plugin). Start it and wait
   until it says it's running.
2. From the `L01_Environment_Hashing` folder, build and start the container:
  ```bash
   docker compose up -d --build     # first run downloads a base image (~1–2 min)
   docker compose ps                # you should see ONE container, "workbench", Up
  ```
  > **If `docker compose up -d --build` errors instead of building,** Docker Desktop
  > isn't running yet — the command couldn't reach Docker's **engine**. This is not a
  > problem with the lab, and it is the single most common Week-1 issue. The exact
  > wording depends on your OS:
  >
  > - **Windows:** `error during connect: ... open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified`
  > - **macOS / Linux:** `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
  >
  > Fix it in order (same idea on every OS):
  >
  > 1. **Start the engine.** *Windows / macOS:* launch **Docker Desktop** (Start menu
  >   / Applications) and wait until it reports **"Engine running"** — the tray/menu-bar
  >    whale icon stops animating; the first start after a reboot can take a minute or
  >    two. *Linux:* start Docker Desktop the same way, or if you run Docker Engine
  >    directly, `sudo systemctl start docker`.
  > 2. **Confirm it's up:** run `docker version` and look for a **Server:** section in
  >   the output (not just a *Client:* section). Same check on every OS.
  > 3. **Re-run** `docker compose up -d --build` above.
  >
  > Still failing while Docker says it's running? The backend is wedged — restart it:
  > *Windows,* run `wsl --shutdown` in PowerShell, then relaunch Docker Desktop;
  > *macOS / Linux,* fully quit Docker Desktop and reopen it. (A reboot does the same
  > on any OS.) Wait for "Engine running," then retry.
3. **Step inside the container** — run:
  ```bash
   docker compose exec workbench bash
  ```
   **What that command does.** A *container* is a small, self-contained Linux computer
   running on top of your own machine (Windows, macOS, or Linux). Until now your
   terminal has been talking to *your own* computer; `docker compose exec workbench  bash` opens a shell — a command prompt — *inside* the container. **You run every
   command in the rest of this lab from in there,** not from your laptop's own shell.
   (This is why your operating system stops mattering: inside, it's the same Linux for
   everyone.)
  - **Reading the command:** `docker compose exec` = run something inside an
  already-running container; `workbench` = which container to enter; `bash` = the
  shell (command prompt) to open.
  - **How you'll know it worked:** your prompt *changes* — from your own computer's
  prompt (Windows: `PS C:\...>`; macOS/Linux: something like `you@laptop ~ %` or a
  bare `$`) to the container's, which reads exactly:
  `root@workbench:/workbench#`. That prompt means you are inside. It also tells you
  **where** you are: the part after the `:` is your current folder, which is worth
  watching — a wrong folder is the most common cause of "No such file or directory"
  later in this lab.
  - **To leave (later, when you're done):** type `exit` and press Enter — that returns
  you to your own computer's prompt. The container keeps running in the background,
  and you can step back in anytime by re-running `docker compose exec workbench bash`.
  **Don't exit yet** — stay inside for the rest of the lab.
4. Run the environment self-check:
  ```bash
   verify_env.sh
  ```
   Read the output. If the last lines say `**ENVIRONMENT OK**`, your toolchain
   works and you have cleared the course's environment gate. If anything says
   `MISSING`, or you never reach that line, stop and see **Troubleshooting** —
   this is exactly the problem this week exists to catch.

> **Gate:** clearing `verify_env.sh` with `ENVIRONMENT OK` is the "lab
> environment verified" outcome for Week 1. Do it early; tell us Thursday if it
> won't, while it's still easy.

Everything below assumes you are inside the `workbench` shell, in `/workbench`.

---

### 1. Command-line orientation (~10 min)

You're standing in `/workbench`. Look around:

```bash
pwd                 # where am I?           -> /workbench
ls                  # what's here?          -> evidence  dedup  downloads  incident
ls -l evidence      # long listing of one folder
```

These folders are exported notes from a small company's old file server —
generic working files, nothing real. Your first finding is a plain inventory
question, the kind you'll answer for real in Week 2:

> **Finding F1 — How many files are in the `evidence/` folder?**

```bash
ls -1 evidence          # one name per line
ls -1 evidence | wc -l  # let the machine count lines instead of you
```

`wc -l` counts lines; piping (`|`) feeds one command's output into the next.
Count **files in `evidence/`** (it has no subfolders). **(F1.)**

Peek at a couple of files so the folder isn't a black box:

```bash
cat  evidence/README.txt              # print a whole file
head evidence/quarterly_report.txt    # just the first lines
```

---

### 2. Hashing: fingerprinting a file (~10 min)

A **cryptographic hash** turns any file into a short, fixed-length fingerprint (a
*digest*). Change a single byte and the digest changes completely. Two files with
the same SHA-256 digest are — for all practical purposes — byte-for-byte
identical; two different files have different digests.

Fingerprint the quarterly report:

```bash
sha256sum evidence/quarterly_report.txt
```

The 64-character hex string on the left is your answer.

> **Finding F2 — the SHA-256 digest of `evidence/quarterly_report.txt`.**
> Submit the full 64-character hex string (lowercase). **(F2.)**

Prove to yourself that the fingerprint is about *content*, not *name*:

```bash
md5sum  evidence/quarterly_report.txt   # a DIFFERENT (older, weaker) hash of the same file
```

Same file, two algorithms, two totally different digests — and neither depends on
the filename. Hold onto the idea that MD5 is the *older, weaker* one; it matters
in section 5.

---

### 3. Using hashes to find duplicates (~8 min)

If identical content means identical digest, then hashing is how you spot copies —
even copies with different names. In `dedup/` there's a `reference.txt` (an
approved policy) and several other files. Some are exact copies of it; some just
look similar.

```bash
sha256sum dedup/*        # hash them all at once; compare the left column
```

Line up the digests. Every file whose digest **equals** `reference.txt`'s digest
is an exact duplicate. Files that merely resemble it — say, one value changed —
get a *completely* different digest, which is the whole point: hashing catches the
one-character edit your eyes would skim past.

> **Finding F3 — how many files in `dedup/` are exact duplicates of
> `reference.txt`?** Count the *other* files that match it (don't count
> `reference.txt` itself). **(F3.)**

---

### 4. Verifying a download against a published checksum (~8 min)

This is hashing's most everyday use: a project publishes the digests of its files
so you can confirm your copy arrived intact and untampered. `downloads/` has three
files and a `SHA256SUMS` list of their *official* digests.

```bash
cd downloads
sha256sum -c SHA256SUMS      # check each file against its published digest
cd ..
```

`-c` reads the list and reports `OK` or `FAILED` per file. One file's real
contents no longer match the digest the project published for it — so its line
comes back `**FAILED**`. That's the file you would *not* trust.

> **Finding F4 — which file fails checksum verification?** Give its filename.
> **(F4.)**

---

### 5. The judgment finding: tamper detection and its limits (~10 min)

`incident/` is a small scenario. You hold a **trusted baseline digest** for an
approved firewall configuration, in `baseline.sha256`. On the box you find two
candidate files: `firewall_rules.conf` (what's running now) and
`firewall_rules.conf.bak` (a backup). One of them is the approved, untampered
version — the one whose digest matches the baseline.

```bash
cat incident/baseline.sha256                 # the trusted digest (left column)
sha256sum incident/firewall_rules.conf incident/firewall_rules.conf.bak
```

> **Got `cat: incident/baseline.sha256: No such file or directory`?** Look at your
> prompt. If it reads `root@workbench:/workbench/downloads#` instead of
> `root@workbench:/workbench#`, you are still inside the `downloads/` folder from
> Step 4 — that step ends with `cd ..` to bring you back out, and it's easy to miss
> when you run the lines one at a time. The `incident/` folder lives in `/workbench`,
> **not** inside `downloads/`, so the path can't resolve from where you're standing.
> Fix it:
>
> ```bash
> pwd                # where am I?  -> should be /workbench
> cd /workbench      # return to the lab root, from anywhere
> ```
>
> Then re-run `cat incident/baseline.sha256` and the `sha256sum incident/...` command
> above. **Every path in this lab is written relative to `/workbench`** — so any time a
> command reports "No such file or directory," run `pwd` first. Being in the wrong
> folder is the usual cause, not a missing file.

Compare each candidate's digest to the baseline.

> **Finding F5a — which file matches the trusted baseline?** Give its filename.
> **(F5a — autograded value.)**
>
> **Finding F5b — justification (2–3 sentences, human-read).** The *other* file's
> digest does **not** match the baseline. Explain what that mismatch **does**
> prove and what it **does not**: does it tell you *who* changed the file, *when*,
> or whether the change was even malicious? And why is this entire check only as
> trustworthy as the baseline itself — what if you couldn't be sure where the
> baseline digest came from? **(F5b — this is the graded reasoning.)**

This is the habit the whole course is built on: a tool gives you a fact
(*these bytes differ*), and your job is to state **exactly** what that fact
licenses you to claim — no more. Tuesday's confidence ladder — **confirmed /
inferred / unverified** — lives right here: the observation column is what you
confirmed, the inference column is what you concluded from it.

---

### 6. Submit

Two things, both due Sunday 11:59 PM.

1. **The L01 Canvas quiz.** Enter your five findings: F1, F2, F3, F4, F5a. For one of
  them — chosen at random, so you won't know which in advance — the quiz also asks you
   to paste the exact command you ran and one sentence on what its output told you.
   Your F5b justification is an essay box here.
2. **The L01 worksheet.** Finish `L01_Worksheet.docx` (sections A through E), then save
  it as a PDF and upload the PDF. In Word: **File → Save As**, and choose **PDF** as  
   the file type. Upload the PDF, not the `.docx`.

---

### Optional extension (ungraded)

- **See a collision-prone hash up close.** `md5sum dedup/`* — MD5 still gives each
distinct file a different digest here, but MD5 is *broken*: researchers can
deliberately construct two different files with the **same** MD5. Why does that
make MD5 unsafe for the tamper-check you did in section 5, while SHA-256 is fine?
- **Extensions lie.** `file downloads/app-manual.pdf` — the name ends in `.pdf`,
but what does `file` say it actually is? A lesson you'll reuse all semester:
don't trust the label, check the bytes.
- **Hash from your own text.** `printf 'hello' | sha256sum` — then change one
letter and watch the entire digest change. That's the "avalanche" property.

Nothing here is submitted; it's for the curious.

---

### Shutting the lab down (when you're finished — not graded)

Nothing in this section is submitted or graded. Do it once you're done, so the lab
isn't running on your machine for the rest of the semester.

> ⚠️ **Submit first.** Shutting down **deletes the container**, and everything you
> typed or created inside it goes with it — nothing inside the container is saved to
> your computer. Make sure your five values are recorded in the Canvas quiz and your
> worksheet is filled in **before** you run this.

Leave the container (`exit` gets you back to your own machine's prompt), make sure
you're in the `L01_Environment_Hashing` folder, and run:

```
exit                  # only if you're still at root@workbench:/workbench#
docker compose down
```

You should see it remove the `workbench` container. That's the whole job.

**What that does and doesn't do:**

- **Removes the container.** The lab files inside it are gone — but they were only
  ever copies, and re-creating them takes one command.
- **Keeps the image it built.** Coming back later is just
  `docker compose up -d --build` again, and it'll be quick the second time because
  nothing needs downloading.
- **Touches nothing on your own computer.** Your files, your folders, this guide —
  all untouched.

**Why bother?** This lab is configured to restart itself whenever Docker Desktop
starts, which means every time you reboot. Left alone, it quietly runs all semester.
It's small and harmless, but there's no reason to carry it around.

**If you'd rather pause than remove it** — say you want to come back tomorrow and
pick up exactly where you left off:

```
docker compose stop     # pause it; the container and its contents survive
docker compose start    # resume it later
```

Use `stop`/`start` while you're still working, and `down` when you're finished for
good.

**Reclaiming the disk space (optional).** This lab's image is a small one, so there's
no hurry. If you want the space back at the end of the semester — and you're sure you
won't redo this lab —
`docker compose down --rmi local` removes the image too. Everything then has to
download and rebuild from scratch next time, so don't do this mid-semester.

Quitting Docker Desktop itself is optional; it's fine to leave installed, and you'll
need it again on Thursday of Week 2.

---

### Troubleshooting

- `**docker compose` says the daemon isn't running:** start Docker Desktop and
wait for it to report "running," then retry. This is the single most common
Week-1 issue.
- `**docker compose ps` shows nothing / the build failed:** re-run
`docker compose up -d --build` and read the last lines of output. Then
`docker compose logs workbench`. If it still fails, bring the exact error to
Thursday's session — that's what it's for.
- `**docker compose exec workbench bash` says "no such service":** make sure
you're in the `L01_Environment_Hashing` folder (the one with
`docker-compose.yml`) when you run it.
- **A hash doesn't match what you expected** even though the command ran: you're
almost certainly hashing the wrong file — check the path, and run `pwd` to confirm
which folder you're in. (The lab files are stored so that Windows, macOS, and Linux
all see byte-for-byte identical copies, so the right command on the right file gives
the same digest on every machine.)
- **Accessibility path:** if you can't run the interactive session, an annotated
transcript of all six steps is on Canvas; the worksheet and quiz are identical
either way.

