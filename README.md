# CS5573 — Information Security & Assurance · Student Materials

Lab environments, lab guides, worksheets, and the handouts and rubrics for
**CS5573 Information Security & Assurance** (UMKC, graduate).

Everything here is also posted to Canvas. This repository exists so you can clone the
lab environments directly instead of downloading zip files.

---

## Getting a lab running

You need **Docker Desktop** installed and running. Then:

```bash
git clone https://github.com/<owner>/<this-repo>.git
cd <this-repo>/labs/L01_Environment_Hashing
docker compose up -d --build
```

Each lab folder has a `*_Lab_Guide.md` — **start there.** It assumes no prior Docker
experience and tells you which terminal to use on Windows, macOS and Linux.

> ⚠️ **Clone it, don't download-and-unzip.** Several labs depend on file bytes being
> preserved exactly (one lab has you verify file integrity by hashing). The
> `.gitattributes` files in this repository prevent your operating system from quietly
> rewriting line endings; a zip download or a copy through some editors can break that,
> and then your answers won't match anyone else's.

## Labs

| Lab | Week | What you do |
|---|---|---|
| `L01_Environment_Hashing` | 1 | Prove your Docker toolchain works; fingerprint files with hashes and find out what a hash does and does not prove |
| `L02_Recon_Asset_Inventory` | 2 | Scan a network segment, find what's on it, build an asset register |
| `L03_Vuln_Scanning_Triage` | 3 | Run a vulnerability scanner — then triage: decide what's real, what matters, and in what order |

**Scope.** Each lab names the one network range you are authorized to scan. That
boundary is not a formality, and staying inside it is a graded part of the work.

## Handouts and rubrics

- `docs/Narrative/` — the onboarding packet, the customer security questionnaire, and
  the weekly dispatches
- `docs/Narrative/Program_Report_Template.md` and `Program_Report_Rubric.md` — the
  capstone report's structure and how it's graded. **You get these in Week 1 on
  purpose:** the report is assembled from your weekly memos, and every memo is easier to
  write when you know what the finished document has to do.
- `docs/Assessments/Program_Memo_Rubric.md` — the five-item instrument that grades every
  memo, plus what each one must contain
- `docs/Assessments/D1_Sample_Charter_Memo.md` — a worked example of a charter memo, set
  at a different company on purpose: study the form, write your own content

## Submitting

Values go in the Canvas quiz. The worksheet is where you show **method, judgment, and
limits** — fill it in as you work, since it asks for the exact commands you ran. Export
it to PDF before uploading.

---

*Generated from the course's private source repository. Please report errors to the
instructor rather than opening a pull request — edits here are overwritten on the next
sync.*
