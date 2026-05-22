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
