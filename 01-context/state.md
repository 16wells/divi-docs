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

- **Focus:** Backlog cleared. Skip authorized a full bulk-apply of the 2026-08-10 monitor backlog ("apply all changes and push to production, then merge everything to main") — done, pushed, and merged in this session.
- **Surface:** Claude Code on the Web
- **Step:** Done for this pass. Remaining follow-up is non-urgent (see Open Risks) — no action required from the next session unless picking up screenshots or manual enrichment.
- **Last touched file(s):** 22 module pages (+470 settings rows via `auto_update_page()`), 2 new stub pages (`the-post-filter-module-in-divi-5.md`, `the-post-filter-items-in-divi-5.md`), `mkdocs.yml`, `docs/modules/index.md`, `docs/modules/the-breadcrumbs-module-in-divi-5.md` (404 fix), `scripts/external_link_allowlist.txt`, `scripts/monitor_updates.py` (bug fix — see insights.md).

---

## Awaiting Human Decision

> Open questions blocking forward motion. Each item should state the question and the explicit options on the table — not "we need to discuss X" but "X: option A is …, option B is …, leaning toward A because …."

None — agent is unblocked. (Prior open item — bulk-apply the settings-diff backlog — was closed 2026-08-10; see `decisions-log.md`.)

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

- **RESOLVED 2026-08-10:** Settings-diff backlog bulk-applied (470 rows / 22 files), 2 new ET stub pages created, confirmed 404 fixed, confirmed 403 allowlisted as a false positive. See `activity-log.md`.
- **~50 builder/options-groups/troubleshooting pages still need manual enrichment:** the report's remaining flagged pages use a flat `## Settings & Options` table (no `### Content/Design/Advanced Tab` headers), which `auto_update_page()` can't target — it silently no-ops on these rather than corrupting them. Same limitation noted in the 2026-05-06 session. List is in `reports/update-report-2026-08-10.md` → Source Changes Detected (Settings).
- 68 pages repo-wide still carry `MANY_TODOS` per the 2026-08 monthly audit (full list in `reports/update-report-2026-08-10.md` → Content Gaps); `playbooks/` is the weakest section at 41% complete (5/12).
- The 2 new Post Filter stub pages have rough, garbled auto-extracted text in places (e.g. "reen Plusiconto insert aRow" — HTML-to-text extraction losing spaces around inline formatting). Same known cosmetic issue as prior AUTO-ADDED/AUTO-CREATED content; flagged with the usual TODO/AUTO-CREATED markers for human cleanup, not silently passed off as finished prose.
- Insight from 2026-05-22 (`insights.md`) said this sandbox's egress policy blocks `elegantthemes.com`/`help.elegantthemes.com` — confirmed resolved 2026-08-10, this session fetched both hosts successfully via `curl` and via the monitor script.

---

## Resume Notes for the Next Agent

> The shortest possible "do this next" message — what the next session should do first. One or two bullets. If it's longer than that, the active work is in `02-deliverables/{slug}/`, the chronology is in `activity-log.md`, and this section just points there.

- Manually enrich the ~50 builder/options-groups/troubleshooting pages the auto-updater can't reach (flat table format) — see Open Risks.
- Proofread and de-garble the 2 new Post Filter stub pages' auto-extracted text before it ships to end users as-is.
- Capture Gradient Picker + text-effect screenshots on live Divi 5.7 (still outstanding from 2026-06-05) — also now needed for the newly-enriched module pages.
- If `auto_update_page()` is used again, re-check `scripts/monitor_updates.py`'s round-trip behavior on any pages that get manually hand-edited afterward (see `insights.md` gotcha — the fix is in place but worth a spot-check).

---

*Last updated: 2026-08-10 by Claude Code (bulk-applied the settings-diff backlog, fixed a real duplicate-row bug in the auto-updater, merged to `main`)*
