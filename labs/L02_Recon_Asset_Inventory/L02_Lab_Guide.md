# L02 — Reconnaissance & Asset Inventory
## Student Lab Guide

**Week 2 · CS5573 · Target time: 75 minutes (core) + optional extension**

**What you turn in — two things, both due Sunday 11:59 PM:**

1. **The L02 Canvas quiz** — the five values you discover in this lab.
2. **The L02 worksheet** — a ~2-page Word document (`L02_Worksheet.docx`, download it
   from Canvas) where you record *how* you got each answer and what it does and doesn't
   prove. Type your answers into it, then **export it as a PDF and upload the PDF.**

> **Open the worksheet now, before you start, and fill it in as you go.** It asks for
> the exact command you ran for each finding. Those are quick to jot down in the moment
> and genuinely annoying to reconstruct an hour later from memory.

---

### The situation (in-world)

You are Wumpus Telehealth's first security lead. Nobody can hand you a list of
what's on the office network — the two-person IT shop has been too busy keeping
the lights on. Before you can protect anything, you have to find out what's
*there*. This week you've been given access to one small network segment and a
recon workstation. Your job: **discover the hosts, catalog what they're running,
and flag anything that looks wrong.** You can't protect what you don't know you
have.

Everything you scan is a lab container on a private, isolated network. You are
authorized to scan **only** the `172.28.0.0/24` lab segment. (Scanning networks
you don't own is a good way to get expelled or arrested — the whole point of the
lab is that this one is yours.)

---

### 0. Setup & verification (~10 min)

You need Docker Desktop running (you proved this worked in L01).

> **Which terminal?** Same as L01: you only need a terminal *on your own computer* for
> the three `docker compose` commands below — everything else runs inside the `recon`
> container, in Linux `bash`, so your operating system stops mattering once you're
> inside. **Windows: use PowerShell** (WSL/Ubuntu also fine if you already run it with
> Docker Desktop's WSL integration; avoid `cmd.exe`). **macOS / Linux: your normal
> Terminal.**

```bash
# from the L02_Recon_Asset_Inventory folder:
docker compose up -d --build      # first run pulls images + builds (~2–4 min)
docker compose ps                 # you should see 6 containers, all "Up"
```

You should see `web01`, `db01`, `files01`, `gateway01`, `printer01`, and
`recon`. Now step onto your recon workstation — **you run every command in this
lab from here**, not from your laptop's own shell:

```bash
docker compose exec recon bash
```

Sanity check that your toolkit works and you can see the network:

```bash
nmap --version          # any version is fine
hostname -I             # your recon box's own IP on the segment — write it down
ping -c1 172.28.0.10    # should get a reply
```

> **Verification gate:** if `docker compose ps` doesn't show 6 containers Up, or
> `ping` fails, stop and fix setup before going on (see the troubleshooting note
> at the end). Everything below assumes you're inside the `recon` shell.

---

### 1. The recon workflow

Real asset discovery is a funnel: **which hosts are alive → which ports are open
→ what's actually running on them → what's out of place.** You'll do exactly
that, in four passes.

#### Pass 1 — Who's alive? (host discovery)

```bash
nmap -sn 172.28.0.0/24
```

`-sn` is a "ping sweep": no port scan, just *which addresses answer*. Read the
output carefully. **Not every address that answers is an asset you care about:**

- `172.28.0.1` is the **network gateway** (the bridge itself) — infrastructure,
  not a host you inventory.
- One address is **your own recon box** (the IP `hostname -I` gave you) — that's
  *you*, holding the flashlight, not a discovered asset.

Knowing your own tool's footprint is part of the skill. Count the **asset
hosts** — the live addresses that are neither the gateway nor yourself.
**(Finding F1.)**

#### Pass 2 — What's open? (port enumeration)

Discovery only told you addresses. Now enumerate open TCP ports. Scan the asset
range and **scan all 65,535 ports** — a service hiding on an unusual port is
exactly the kind of thing an inventory is supposed to catch, and the default
scan would miss it:

```bash
nmap -p- 172.28.0.10-50
```

(`-p-` = all ports. On this tiny local segment it finishes in seconds.) Note the
open port on each host. Some hosts have one; at least one host has more than one.

#### Pass 3 — What's running? (service & version detection)

An open port isn't an asset record yet — you need the *service and version*.

```bash
nmap -sV -p- 172.28.0.10-50
```

`-sV` grabs banners and fingerprints each service. Look closely at the web server
on `172.28.0.10` — you want its **exact product and version string**.
**(Finding F2.)** You can corroborate it without nmap:

```bash
curl -sI http://172.28.0.10/        # read the "Server:" response header
curl -s  http://172.28.0.10/ | grep -i '<title>'   # the page title, for your notes
```

#### Pass 4 — What's out of place? (the judgment pass)

Now walk your results like an auditor. On a modern office segment, some things
should make you stop:

- A **cleartext, interactive remote-login protocol** — the kind of thing that
  went out of style twenty years ago because it sends credentials in the clear.
  One host is running one. **What TCP port is it on? (Finding F3.)** *(nmap labels
  this ancient protocol by its well-known port number.)* Note which host it's on —
  you'll need that for F5 and your asset register.
- A service that **isn't a web page, a database, SSH, or a printer** — something
  a message/telemetry system would use, sitting open with no authentication, that
  nobody wrote down. **What port is it on? (Finding F4.)**

  **What you're looking at.** That service is an **MQTT broker**. MQTT is a
  lightweight messaging protocol built for devices — sensors, thermostats,
  badge readers, medical telemetry. Devices don't talk to each other directly;
  they all connect to a central **broker**, *publish* readings to named channels
  called **topics** (`building/floor2/thermostat`), and *subscribe* to the topics
  they care about. The broker passes messages along. It's the post office.

  **`mosquitto`** is the most common open-source broker — that's the program
  running on port 1883. **`mosquitto_sub`** is its companion *client*: a small
  tool that connects to a broker and subscribes. Both are already installed on
  your recon box. In the command below, `-h` is the broker's host, `-t` is the
  topic to subscribe to, `#` is MQTT's wildcard meaning **every topic**, and
  `-v` prints the topic name alongside each message.

  So the command asks the broker: *"send me everything, from everyone."* Try it:

  ```bash
  mosquitto_sub -h 172.28.0.40 -t '#' -v      # Ctrl-C to stop
  ```

  > ### 📟 What you should see
  >
  > Within a second or two, a burst of **retained device records** — the broker
  > replays these to every new subscriber the moment it connects:
  >
  > ```
  > devices/thermostat-2f/status online fw=1.4.2
  > devices/badge-reader-lobby/status online fw=2.1.7
  > ...
  > ```
  >
  > Then live readings every few seconds — temperatures, badge scans, a
  > heartbeat. **Ctrl-C** to stop.
  >
  > **Sit with that for a moment.** You are a machine nobody at this company
  > configured, on a network you were handed this morning. You asked a device
  > broker for *every message on it*, and it said yes. No password. No prompt.
  > No record that you did it.
  >
  > And look at what the retained records gave you: **a list of devices, with
  > firmware versions, that appears in no asset register anywhere.** You are
  > building an inventory this week — and the broker just handed you part of one
  > that nobody knew existed. That's not a bonus. That's the problem.
  >
  > **Nothing printed?** Give it about ten seconds. If it's still silent, the
  > connection may still be fine — add `-d` and look for the client **receiving
  > `CONNACK`** (broker accepted the connection) and **`SUBACK`** (subscription
  > granted):
  >
  > ```bash
  > mosquitto_sub -h 172.28.0.40 -t '#' -v -d
  > ```
  >
  > For contrast, point the same command at a host with no broker on it:
  >
  > ```bash
  > mosquitto_sub -h 172.28.0.10 -t '#' -v      # .10 is the web server
  > ```
  >
  > That errors out immediately instead of connecting. **An error = refused; a
  > quiet open session = accepted.**
  >
  > **For your worksheet, keep the two columns honest.** What you *observed*: the
  > broker accepted an anonymous subscription and sent device telemetry. What you
  > *inferred*: any host on this segment could read this traffic — and, since the
  > broker asks nothing of anyone, could **publish** to it too. You did not test
  > publishing. Don't write that you did.

- Finally, step back: **of everything you found, which single host is the biggest
  risk to Wumpus, and why?** Weigh what a service exposes, whether it needs
  credentials, and what the host's role is. **(Finding F5 — this one needs a
  2–3 sentence justification, not just an answer.)**

---

### 2. Build your asset register

As you go, fill in the asset table in the worksheet — **every** host you found,
including the boring ones (the database, the file server, the printer). An
inventory that only lists the scary things isn't an inventory. For each host
record: IP, what it appears to be, open port(s), and service/version.

---

### 3. Submit

1. **The L02 Canvas quiz.** Enter your five findings. Values are numeric or
   short-answer; the quiz tells you the form it wants (an integer, an IP, a port,
   a `product version` string). For one finding — chosen at random, so you won't know
   which in advance — the quiz also asks you to paste the command you used and 2–3
   sentences of reasoning, so keep notes as you work.
2. **The L02 worksheet.** Finish `L02_Worksheet.docx` (download it from Canvas), then
   save it as a PDF and upload the PDF. In Word: **File → Save As**, and choose **PDF**
   as the file type. Upload the PDF, not the `.docx`.

**Everyone's answers will be identical — that's expected.** All students scan the same
lab segment, so the five values come out the same across the class. Matching values are
not evidence of collusion and won't be treated that way.

---

### Optional extension (ungraded)

Recon never really ends. If you have time:

- Pull the actual contents out of that unauthenticated message broker
  (`mosquitto_sub -h 172.28.0.40 -t '#' -v`) and skim what a stranger on the
  segment could read. Does it change your F5 argument?
- Point `redis`/`psql`-style curiosity at the database (`172.28.0.20:5432`): does
  it demand a password? How does "open but authenticated" change its risk versus
  the broker?
- Run `nmap -sV -O` (OS detection) and notice how confident (or not) the guesses
  are inside containers — a lesson in **calibrated claims** you'll use all
  semester.

Nothing here is submitted; it's for the curious.

---

### Shutting the lab down (when you're finished — not graded)

Nothing in this section is submitted or graded. It matters more here than in L01:
this lab runs **six** containers and a private network, and they're configured to
restart themselves whenever Docker Desktop starts — so every reboot brings the whole
segment back up until you tell it otherwise.

> ⚠️ **Submit first.** Shutting down removes the containers, and anything you typed
> or saved inside them goes with them. Get your five values into the Canvas quiz and
> your worksheet filled in **before** you run this.

Leave the recon box (`exit`), make sure you're in the `L02_Recon_Asset_Inventory`
folder, and run:

```
exit                     # only if you're still inside the recon container
docker compose down -v
```

Expect it to remove six containers and the `wumpuslab` network.

**What the `-v` is for.** The database creates a scratch data volume while it runs;
`-v` cleans that up too, so nothing is left behind. It does **not** touch anything in
your lab folder — the lab's own files are mounted read-only from `env/`, and they stay
exactly where they are.

**What survives:** the images it pulled. Coming back is just
`docker compose up -d --build`, and it'll be much faster the second time.

**If you'd rather pause than remove it:**

```
docker compose stop      # pause all six; they survive
docker compose start     # resume later
```

Use `stop`/`start` while you're mid-lab, and `down -v` when you're finished.

**Reclaiming disk space (optional).** This lab pulls several images and is the
largest one so far. At the **end of the semester** — not before —
`docker compose down -v --rmi local` removes the images too; everything re-downloads
if you come back.

One more reason to shut it down: you're finished scanning. The authorization you were
given covered `172.28.0.0/24` **for this exercise**. When the exercise is over, take
the range down.

---

### Troubleshooting

- **`docker compose ps` shows fewer than 6, or a container keeps restarting:**
  `docker compose logs <name>` (e.g. `gateway01`). Then `docker compose down -v &&
  docker compose up -d --build` for a clean rebuild.
- **`nmap -sn` shows nothing / permission errors:** make sure you're inside the
  `recon` container (`docker compose exec recon bash`), not your laptop shell.
- **A scan feels slow:** you're probably scanning the whole `/24` with `-p-`.
  Scan the asset range `172.28.0.10-50`, not `0.0/24`, for port work.
- **Accessibility path:** if you can't run the interactive session, an annotated
  transcript of the four passes and the asset table is available on Canvas; the
  worksheet and quiz are identical either way.
