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

- **Focus:** Live-site spot-check (2026-10-01) found a real, pre-existing rendering defect on production — see Awaiting Human Decision. `state.md` itself is stale again (last full refresh was 2026-08-10; ~8 weeks of unaudited bot commits since, same pattern as before — see Resume Notes).
- **Surface:** Claude Code on the Web
- **Step:** Reported the defect; waiting on Skip's call on the fix approach before touching the 36 affected files.
- **Last touched file(s):** `01-context/insights.md` (new finding logged), this file.

---

## Awaiting Human Decision

> Open questions blocking forward motion. Each item should state the question and the explicit options on the table — not "we need to discuss X" but "X: option A is …, option B is …, leaning toward A because …."

| Opened | Question | Options on the table | Leaning |
|---|---|---|---|
| 2026-10-01 | 36 module pages have malformed Design/Advanced-tab tables on the live site (AUTO-ADDED settings rows appended to a 2-column Options Group summary table instead of their own table — see `insights.md`). How to fix? | A: delete the AUTO-ADDED rows in affected tabs — the Options Group table above them already covers the same options via links to shared docs, so they're redundant noise, not missing information; B: give the AUTO-ADDED rows their own properly-labeled table/subsection instead of deleting; C: something else | Leaning A — the AUTO-ADDED rows add no information the Options Group table doesn't already give (generic one-liners vs. real docs), so deleting is lower-risk than restructuring |

---

## Most Recent Commit

- See `activity-log.md` 2026-08-10 entries for the full backlog-clear + merge-to-main session.
- **What it landed:** +470 settings rows across 22 module pages; 2 new stub pages (Post Filter, Post Filter Items) + nav/index entries; fixed the confirmed 404 in `the-breadcrumbs-module-in-divi-5.md`; allowlisted the confirmed-false-positive `16wells.com` 403; fixed a real duplicate-row bug in `scripts/monitor_updates.py` (see `insights.md`). Merged to `main` — this is the current production state.
- **What it intentionally did NOT land:** The ~50 builder/options-groups/troubleshooting pages the tool can't auto-insert into (different table structure — needs manual enrichment, same limitation as the 2026-05-06 session). Screenshots still outstanding.

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

- **NEW 2026-10-01 — confirmed broken on production:** 36 module pages (same set the 2026-05-06/2026-08-10 `auto_update_page()` runs touched) have a malformed table in their Design and/or Advanced tab — AUTO-ADDED settings rows (3 columns) appended directly after a 2-column `Options Group \| Description` summary table, with no table boundary between them. Renders with misaligned/missing descriptions on the live site (confirmed via WebFetch on `/modules/code/`). Pre-existing since 2026-05-06 (`286ec90`) — not caused by the 2026-08-10 session, and not caught by its duplicate-row check (that check only looked for literal repeated text, not column-count mismatches). See `insights.md` for the full root cause and file list derivation. Awaiting Skip's direction — see Awaiting Human Decision.
- **RESOLVED 2026-08-10:** Settings-diff backlog bulk-applied (470 rows / 22 files), 2 new ET stub pages created, confirmed 404 fixed, confirmed 403 allowlisted as a false positive. See `activity-log.md`.
- **~50 builder/options-groups/troubleshooting pages still need manual enrichment:** the report's remaining flagged pages use a flat `## Settings & Options` table (no `### Content/Design/Advanced Tab` headers), which `auto_update_page()` can't target — it silently no-ops on these rather than corrupting them. Same limitation noted in the 2026-05-06 session. List is in `reports/update-report-2026-08-10.md` → Source Changes Detected (Settings).
- 68 pages repo-wide still carry `MANY_TODOS` per the 2026-08 monthly audit (full list in `reports/update-report-2026-08-10.md` → Content Gaps); `playbooks/` is the weakest section at 41% complete (5/12).
- The 2 new Post Filter stub pages have rough, garbled auto-extracted text in places (e.g. "reen Plusiconto insert aRow" — HTML-to-text extraction losing spaces around inline formatting). Same known cosmetic issue as prior AUTO-ADDED/AUTO-CREATED content; flagged with the usual TODO/AUTO-CREATED markers for human cleanup, not silently passed off as finished prose.
- Insight from 2026-05-22 (`insights.md`) said this sandbox's egress policy blocks `elegantthemes.com`/`help.elegantthemes.com` — confirmed resolved 2026-08-10, this session fetched both hosts successfully via `curl` and via the monitor script.

---

## Resume Notes for the Next Agent

> The shortest possible "do this next" message — what the next session should do first. One or two bullets. If it's longer than that, the active work is in `02-deliverables/{slug}/`, the chronology is in `activity-log.md`, and this section just points there.

- Resolve the 2026-10-01 malformed-table finding first (36 files, see Awaiting Human Decision) — it's live on production.
- `state.md` has drifted stale again (bot-only commits since 2026-08-10: weekly monitors through 2026-09-28 plus a September monthly audit, none logged here). Worth a full audit-and-refresh pass like the 2026-08-10 one before assuming this file reflects reality.
- Manually enrich the ~50 builder/options-groups/troubleshooting pages the auto-updater can't reach (flat table format) — see Open Risks.
- Proofread and de-garble the 2 new Post Filter stub pages' auto-extracted text before it ships to end users as-is.
- Capture Gradient Picker + text-effect screenshots on live Divi 5.7 (still outstanding from 2026-06-05) — also now needed for the newly-enriched module pages.

---

*Last updated: 2026-10-01 by Claude Code (live-site spot-check; found and logged a pre-existing malformed-table defect affecting 36 production pages, not yet fixed)*
