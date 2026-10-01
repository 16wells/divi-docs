# Decisions Log — Divi 5 Technical Documentation

> **This is the living document.** Any Claude agent working on this project should update this file as decisions are made or new open questions surface. Check it at the start of any work session to see current state.

## How to Use This File

- **Closed Decisions:** Things we've decided and committed to. Don't revisit without a good reason.
- **Open Decisions:** Things we're deliberately leaving unresolved. Do not force closure on these without the user.
- **Outstanding From Client:** Items we're waiting on the client to provide.

Every entry should have a date, a short description, and ideally a one-line rationale.

---

## Closed Decisions

| Date | Decision | Rationale |
|---|---|---|
| 2026-05 | Retrofit this repo with project-memory scaffold files only | Preserve website behavior while enabling cross-session continuity |
| 2026-05-22 | Ship 5 new-module pages as stubs now rather than waiting for full scrapes | Sandbox network policy blocks `elegantthemes.com` / `help.elegantthemes.com`; stubs preserve nav + ET blog linkage, full settings tables fill in via next monitor run when network access is restored. |
| 2026-08-10 | Bulk-apply the 2026-08-10 settings-diff backlog via `auto_update_page()`, create the 2 new ET stub pages, fix confirmed broken links, and merge directly to `main` | Skip explicitly authorized: "Apply all changes and push to production, then merge everything to main." Found and fixed a real duplicate-row bug in the auto-updater first (see `insights.md`) rather than run it blind. |
| 2026-10-01 | Fix the 36-file malformed-AUTO-ADDED-table defect via option A (delete redundant rows) — but applied per-row, not per-file | Skip said "go ahead, option A." Before applying, found 2 of the 36 files (`the-svg-module-in-divi-5.md`, `the-timeline-module-in-divi-5.md`) don't fit option A — their AUTO-ADDED rows are the only real content, not redundant duplicates. Deleted the genuinely-redundant rows (420, across 34 files) per option A; for the 2 exceptions plus a few other genuinely-new rows elsewhere, padded/reformatted them to fit their table instead of deleting (125 rows) rather than destroy real documentation to satisfy the letter of the instruction. See `insights.md` for the full reasoning. |

---

## Open Decisions

| Opened | Decision | Notes |
|---|---|---|
| 2026-05 | Should memory files live in this repo long-term or a separate ops repo? | Keep in this repo for now; revisit after workflow trial period. |
| 2026-05 | Should this project adopt optional marketing-context.md? | Deferred; current engagement is technical/docs-led. |

---

## Outstanding From Client

| Item | Status | Notes |
|---|---|---|
| Confirm canonical project start date | ⏳ Pending | Needed to replace TODO markers in README/context files. |

---

## Change Log

| Date | What changed |
|---|---|
| 2026-05-06 | Initial decisions log created |
