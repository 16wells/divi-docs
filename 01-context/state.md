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

- **Focus:** none — no active human/agent editing session since 2026-06-05. Since then the repo has been running unattended on the automated weekly monitor + monthly audit cron (`divi-docs-bot`), which has accumulated a real backlog of unactioned findings (see Open Risks below).
- **Surface:** n/a (bot-only commits for the last 2 months)
- **Step:** Next session should triage the backlog in `reports/update-report-2026-08-10.md` before starting new content work.
- **Last touched file(s) (by a human/content session):** `docs/builder/gradient-builder.md`, `global-variables.md`, `design-variables.md`, `options-groups/{text,heading-text,title-text,background}.md`, `docs/modules/the-{timeline,svg,table-of-contents,instagram-feed}-module-in-divi-5.md`, `planning/et-blog-tutorials-map.md`

---

## Awaiting Human Decision

> Open questions blocking forward motion. Each item should state the question and the explicit options on the table — not "we need to discuss X" but "X: option A is …, option B is …, leaning toward A because …."

| Opened | Question | Options on the table | Leaning |
|---|---|---|---|
| 2026-08-10 | ~70 pages have settings-table diffs detected by monitor since 2026-06-05 but not yet applied — run a bulk `auto_update_page()` pass now, or keep letting weekly runs just report until a dedicated content session? | A: bulk-apply now (mirrors the 2026-05-06 pattern); B: wait, since some diffs may be noise/reordering | Leaning A — backlog is 2 months deep and growing weekly |

---

## Most Recent Commit

- **SHA:** `3dcd98b5`
- **Subject:** Weekly monitor report: 2026-08-10
- **Date:** 2026-08-10
- **Author:** `divi-docs-bot` (automated — not a content session)
- **What it landed:** Refreshed `scripts/et_content_hashes.json`, `reports/update-report-2026-08-10.md`, `reports/external-link-check-2026-08-10.md`. No `docs/` changes — detection only.
- **Most recent human-authored content commit:** `6290d7ef` (2026-06-05, Cursor) — Divi 5.7 gradient picker, gradient variables, text-effect settings.

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

- **Unactioned settings-diff backlog (growing weekly since 2026-06-05):** `reports/update-report-2026-08-10.md` lists ~70 module/builder/options-group/troubleshooting pages with detected settings additions/changes (hashes already advanced, so re-running the monitor won't re-surface these — the diffs must be applied from the report itself or by re-scraping). Five new module stub pages (Timeline, SVG, Table of Contents, Instagram Feed, Canvas Portal) are in this list with real settings tables now available upstream.
- **2 new ET articles not yet created:** "The Post Filter Module in Divi 5" (`help.elegantthemes.com/en/articles/16186978-...`) and "The Post Filter Items in Divi 5" (`.../16187393-...`) — flagged in the 2026-08-10 report, no stub pages exist yet.
- **1 confirmed broken internal reference:** `docs/modules/the-breadcrumbs-module-in-divi-5.md:34` links to `help.elegantthemes.com/en/articles/12022773-build-custom-templates-using-the-theme-builder-in-divi-5`, which now 404s (2026-08-10 external-link-check).
- **1 confirmed broken external link:** `docs/recipes/divi5-filterable-gallery.md:313` → `https://16wells.com` returns 403 (2026-08-10 external-link-check) — check whether this is a real site issue or a bot-detection false positive before editing the doc.
- Note: the bulk of the 2026-08-10 external-link-check failures (127 total) are `429 Too Many Requests` against `help.elegantthemes.com` — link-checker rate-limiting noise, not real breakage. Only the 404 and 403 above are confirmed real.
- 68 pages repo-wide still carry `MANY_TODOS` per the 2026-08 monthly audit (full list in `reports/update-report-2026-08-10.md` → Content Gaps); `playbooks/` is the weakest section at 41% complete (5/12).
- Insight from 2026-05-22 (`insights.md`) said this sandbox's egress policy blocks `elegantthemes.com`/`help.elegantthemes.com` — but the bot has been reaching those hosts successfully every week since, so that block is either resolved or specific to a different execution environment than the one running the cron. Worth confirming which environment the bot actually runs in before assuming this interactive session can reach ET directly.

---

## Resume Notes for the Next Agent

> The shortest possible "do this next" message — what the next session should do first. One or two bullets. If it's longer than that, the active work is in `02-deliverables/{slug}/`, the chronology is in `activity-log.md`, and this section just points there.

- Triage `reports/update-report-2026-08-10.md`: bulk-apply the ~70-page settings-diff backlog (same pattern as the 2026-05-06 `auto_update_page()` session), starting with the five new-module stubs that now have real upstream settings tables.
- Create stub pages for the two new ET articles (Post Filter Module, Post Filter Items) and add nav entries.
- Fix the 1 confirmed 404 (`the-breadcrumbs-module-in-divi-5.md:34`) and check the `16wells.com` 403 on `divi5-filterable-gallery.md:313`.
- Capture Gradient Picker + text-effect screenshots on live Divi 5.7 (still outstanding from 2026-06-05).
- Log a proper `activity-log.md` entry once real content work resumes — the last 2 months of bot commits were not logged there since they're automated, not session work.

---

*Last updated: 2026-08-10 by Claude Code (state.md refresh — audited 2 months of unlogged bot commits since the 2026-06-05 human session)*
