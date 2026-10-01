# State — Divi 5 Docs

> **What is happening right now.** This file is the single source of truth for the project's *in-flight* reality. A fresh agent reading just `CLAUDE.md` + this file should be able to pick up where the last session left off, without consulting any chat history.
>
> Keep this file lean — **~200 lines max.** When detail ages out, move it to `activity-log.md` (chronology) or to the relevant deliverable file. This file is not a second activity log.

---

## Active Sub-Project

**Sub-project:** none-yet
**Folder:** `02-deliverables/none-yet/`
**Per-sub-project state file:** `02-deliverables/none-yet/state.md` *(if multiple sub-projects exist on this engagement, each has its own; this top-level file is the meta-pointer)*

*(Sections below are empty awaiting first iterative-memory checkpoint. The agent populates them as work happens.)*

---

## In-Progress Work

> What is actively being worked on right now — the next concrete action, the surface it's happening on, and the step within that work.

- **Focus:** The 2026-10-01 malformed-table defect (36 files) is fixed, pushed, and deployed. `state.md` itself is still stale on everything else (last full refresh 2026-08-10; ~8 weeks of unaudited bot commits — see Resume Notes).
- **Surface:** Claude Code on the Web
- **Step:** Done for this pass. No action required unless picking up the broader state.md refresh, the ~50-page manual enrichment, or screenshots.
- **Last touched file(s):** 36 module pages (table fix), `01-context/insights.md`, `01-context/decisions-log.md`, this file.

---

## Awaiting Human Decision

> Open questions blocking forward motion. Each item should state the question and the explicit options on the table — not "we need to discuss X" but "X: option A is …, option B is …, leaning toward A because …."

None — agent is unblocked. (Prior item — the 36-file malformed-table fix — was closed 2026-10-01, option A as Skip directed; see `decisions-log.md`.)

---

## Most Recent Commit

- **SHA:** `90d458c`
- **Subject:** Fix malformed AUTO-ADDED tables across 36 module pages (option A)
- **Date:** 2026-10-01
- **What it landed:** Deleted 420 redundant AUTO-ADDED settings rows across 34 files (rows that restated settings already documented above them, just with a mismatched column count). Padded 125 rows across the-svg-module-in-divi-5.md, the-timeline-module-in-divi-5.md, button-styling-reference.md, and a handful of genuinely-new procedural rows in other files to match their table's column count instead of deleting — those rows were the only real content in that spot, not redundant. Deleted the "Save"/"Exit" boilerplate garble pattern (`k on the{X}button.`) everywhere it appeared. Verified zero remaining column-count mismatches in all 36 files; `mkdocs build` clean; spot-checked rendered HTML. Pushed straight to `main` (no PR — matches the 2026-08-29 policy change) and deployed via the "Deploy Divi Docs" GH Actions workflow.
- **What it intentionally did NOT land:** 11 more mismatched-table instances found in *unrelated* files during the verification sweep (no AUTO-ADDED marker — different root cause, not part of this bug). Flagged, not fixed — see Open Risks.

---

## External Systems State

> For technical projects, an inventory of real-world resources the project has touched. The file system alone won't show you what's live in AWS, what's stored in Secrets Manager, or whether the cron is currently scheduled. This section bridges that gap.
>
> If the project is purely advisory (strategy, copy, audits) and touches no external systems, write "None — engagement is advisory."



### Deployed Services
| Service | Environment | Identifier | Status | Notes |
|---|---|---|---|---|
| | | | | |

### Cloud Resources
| Resource | Provider | Identifier (ARN / ID / name) | Region | Notes |
|---|---|---|---|---|
| | | | | |

### Third-Party API State
| API | Account / tenant | What's configured | Notes |
|---|---|---|---|
| | | | |

### Secrets / Environment Variables
| Name | Where stored | Purpose | Last rotated |
|---|---|---|---|
| | | | |

### Scheduled / Recurring Jobs
| Job | Cadence | Mode (live / dry-run / paused) | Last run | Next run |
|---|---|---|---|---|
| Weekly monitor (`scripts/monitor_updates.py` + external link check) | Weekly (Mon) | Live — commits report + hash updates automatically, does not auto-edit `docs/` | 2026-08-10 (`3dcd98b5`) | ~2026-08-17 |
| Monthly audit (with auto-update) | Monthly (first Mon) | Live — this one *does* auto-apply some settings updates via `auto_update_page()` | 2026-08-03 (`8256d17`) | ~2026-09-07 |

### Production Data State
> If the project mutates real data, what state is it in? Any in-flight regression, partial recovery, or known divergence between source and target.

---

## Open Risks / Known Mid-Recovery Items

> Things that are explicitly half-done. The "I bumped into this and it's not fixed yet" list. Resolve and remove items as they get cleaned up.

- **RESOLVED 2026-10-01:** 36-file malformed AUTO-ADDED table defect fixed (420 rows deleted, 125 padded/reformatted) and deployed. See `activity-log.md` + `insights.md`.
- **NEW 2026-10-01 — not yet investigated:** 11 mismatched-table instances found in files *outside* the 36-file AUTO-ADDED set during this fix's verification sweep (e.g. `advanced-field-types-for-module-settings.md`, `how-to-change-server-s-maximum-upload-file-size.md`, `using-the-divi-theme-options.md`, `using-extra-s-theme-options.md`, `the-divi-woo-product-meta-module.md`, `how-to-load-a-page-with-a-certain-tab-opened.md`, `how-to-troubleshoot-mailchimp-connection-issues.md`). No AUTO-ADDED marker present — different root cause (looks like unescaped literal `|` characters in cell text, same class as the one confirmed-fine false positive in `the-breadcrumbs-module-in-divi-5.md`, but these haven't been individually verified). Needs its own look before concluding whether they're real breaks or more false positives.
- **RESOLVED 2026-08-10:** Settings-diff backlog bulk-applied (470 rows / 22 files), 2 new ET stub pages created, confirmed 404 fixed, confirmed 403 allowlisted as a false positive. See `activity-log.md`.
- **~50 builder/options-groups/troubleshooting pages still need manual enrichment:** the report's remaining flagged pages use a flat `## Settings & Options` table (no `### Content/Design/Advanced Tab` headers), which `auto_update_page()` can't target — it silently no-ops on these rather than corrupting them. Same limitation noted in the 2026-05-06 session. List is in `reports/update-report-2026-08-10.md` → Source Changes Detected (Settings).
- 68 pages repo-wide still carry `MANY_TODOS` per the 2026-08 monthly audit (full list in `reports/update-report-2026-08-10.md` → Content Gaps); `playbooks/` is the weakest section at 41% complete (5/12).
- The 2 new Post Filter stub pages have rough, garbled auto-extracted text in places (e.g. "reen Plusiconto insert aRow" — HTML-to-text extraction losing spaces around inline formatting). Same known cosmetic issue as prior AUTO-ADDED/AUTO-CREATED content; flagged with the usual TODO/AUTO-CREATED markers for human cleanup, not silently passed off as finished prose.
- Insight from 2026-05-22 (`insights.md`) said this sandbox's egress policy blocks `elegantthemes.com`/`help.elegantthemes.com` — confirmed resolved 2026-08-10, this session fetched both hosts successfully via `curl` and via the monitor script.

---

## Resume Notes for the Next Agent

> The shortest possible "do this next" message — what the next session should do first. One or two bullets. If it's longer than that, the active work is in `02-deliverables/{slug}/`, the chronology is in `activity-log.md`, and this section just points there.

- Investigate the 11 mismatched-table instances found in unrelated files (see Open Risks) — verify which are real breaks vs. more escaped-pipe false positives before touching anything.
- `state.md` has drifted stale on the broader picture (bot-only commits from 2026-08-10 through 2026-09-28, plus a September monthly audit, were never logged here). Worth a full audit-and-refresh pass like the 2026-08-10 one.
- Manually enrich the ~50 builder/options-groups/troubleshooting pages the auto-updater can't reach (flat table format) — see Open Risks.
- Proofread and de-garble the 2 new Post Filter stub pages' auto-extracted text before it ships to end users as-is.
- Capture Gradient Picker + text-effect screenshots on live Divi 5.7 (still outstanding from 2026-06-05) — also now needed for the newly-enriched module pages.

---

*Last updated: 2026-10-01 by Claude Code (fixed the 36-file malformed AUTO-ADDED table defect — option A as directed — pushed and deployed)*
