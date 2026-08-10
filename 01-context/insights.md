# Insights — Divi 5 Technical Documentation

> **Working-memory scratchpad for learnings that aren't decisions yet.** Things you noticed. Patterns that showed up. Quirks of the client. Half-formed observations that might matter later. This file catches what would otherwise evaporate between sessions.

## How to Use This File

**Add to this file when you:**
- Notice a pattern in the client's behavior, market, or content
- Learn something from a call, document, or piece of research that isn't a formal decision
- Spot a gotcha, risk, or assumption worth flagging
- Have a half-formed observation that might matter later but isn't ready to act on yet

**Do *not* use this file for:**
- Formal decisions → go to `decisions-log.md`
- Session handoff notes → go to `activity-log.md`
- Finished deliverables → they live in `02-deliverables/` or `03-assets/`
- Outstanding items owed by the client → go to `decisions-log.md` under Outstanding From Client

**When an insight graduates:** If an insight turns into a concrete decision, move it (or a summary of it) to `decisions-log.md` and note the date. Keep this file as the record of how you got there.

**Keep entries dated and short.** One or two bullets per insight. If an insight needs a full page, it probably belongs in a proper deliverable.

---

## Setup Notes

- *(Initial assumptions, constraints, or observations from project start. Filled in during scaffolding — may be updated as the project progresses.)*

- The repository already has substantial active doc edits, so memory scaffolding must remain operational-only and additive.
- Avoid modifying `docs/` content during setup tasks unless explicitly requested.
- Cross-session continuity is likely high value given work spans multiple tools/surfaces.

---

## Dated Insights (newest first)

*(Add entries with a short heading. Keep bullets tight.)*

### 2026-08-10 — `auto_update_page()` had a round-trip bug that silently duplicates rows on re-run

- `scripts/monitor_updates.py` wrote AUTO-ADDED settings rows as `| Setting | Type | Description | <!-- AUTO-ADDED -->` — no trailing pipe. Its own reader, `parse_local_settings()`, requires a line to both start **and** end with `|` to be recognized as a table row, so every previously-auto-added row was invisible to the parser on the next run.
- Practical effect: re-running `auto_update_page()` on a file that already had AUTO-ADDED rows from an earlier pass (e.g. the 2026-05-06 session's files) treated all of them as "new," and would have appended a second copy of every row. Caught this before committing by diffing the first bulk-apply attempt — 13 of 74 flagged files showed exact-duplicate rows.
- Fixed by moving the marker inside the description cell with a closing pipe (`| Setting | Type | Description <!-- AUTO-ADDED --> |`) and stripping trailing `<!-- ... -->` comments when parsing descriptions back out, so re-runs correctly recognize existing rows and skip them.
- Also had to normalize 434 already-committed old-format rows across 20 files (cosmetic-only: moved the pipe, no content change) so they'd be visible to the fixed parser too — otherwise the fix only protects rows added going forward.
- **Takeaway:** any future change to `auto_update_page()`'s row-writing template must stay round-trippable through `parse_local_settings()` — write it, then immediately re-parse the same content and confirm the row comes back, before trusting a bulk run.

### 2026-05-22 — Claude Code on the Web sandbox blocks ET hosts

- The remote-execution environment's egress proxy returned 403 `host_not_allowed` for both `elegantthemes.com` and `help.elegantthemes.com` (and for `web.archive.org` + `r.jina.ai`). That blocks `scripts/scrape_docs.py`, `scripts/monitor_updates.py`, and the weekly external-link check unless the environment's network policy is widened.
- This is environment-level, not Claude Desktop or local-machine — easy to misdiagnose. Fix is at claude.ai/code → environment → network policy.
- Implication for weekly monitor: until policy is widened, run the monitor and scrape scripts from a local machine (or a session with a permissive policy), not the default Claude Code on the Web environment.

<!-- Example format:

### YYYY-MM-DD — [Short topic]
- [One-line observation]
- [Optional second bullet with context or next-step hint]

-->

---

## Entry Template (copy this when adding)

```
### YYYY-MM-DD — [Short topic]
- [Observation or pattern]
- [Why it might matter]
```

---

## What Belongs Here vs. Elsewhere

| If it's... | Log it in... |
|---|---|
| A formal decision (closed or open) | `decisions-log.md` |
| Session-by-session "what I did" | `activity-log.md` |
| A pattern, quirk, gotcha, or half-formed observation | **This file** |
| Something the client owes us | `decisions-log.md` → Outstanding From Client |
| A finished draft or asset | The actual file in `03-assets/` |

---
*Last updated: 2026-05-06*
