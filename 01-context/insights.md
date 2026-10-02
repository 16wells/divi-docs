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

### 2026-10-01 — Live-site check found a second, pre-existing `auto_update_page()` defect: AUTO-ADDED rows appended to the wrong table

- Verified the live site (homepage, a new stub page, the modules index) renders cleanly. But `docs/modules/code.md` on production shows a malformed Design/Advanced tab table — settings appear to repeat with the second instance missing its description.
- Root cause is **not** the round-trip bug fixed 2026-08-10. It's a separate, older structural bug: when a tab section's only table is a 2-column `| Options Group | Description |` summary table (linking out to shared `options-groups/*.md` docs, no per-setting `Setting | Type | Description` table), `auto_update_page()`'s insertion logic still appends 3-column AUTO-ADDED rows after it — it finds "the last `|`-delimited line in this tab" without checking it's the right table shape. Result: a single malformed table with inconsistent column counts, which `mkdocs`/python-markdown renders as entries with blank/misaligned descriptions.
- This predates the 2026-08-10 session — traced to `286ec90` (the original 2026-05-06 `auto_update_page()` run) via `git log -- docs/modules/code.md`. The 2026-08-10 bulk-apply didn't touch `code.md` (it correctly saw nothing new to add), so it neither caused nor caught this.
- **Scope: confirmed in 36 of the ~37 module files** that have ever had AUTO-ADDED rows (found via a script comparing cell-count of each table row against the row before it). Same list as the 2026-08-10 `auto_update_page()`-touched files, which makes sense — it's a property of the tool, not any one page.
- Caveat for next time: the 2026-08-10 "spot-check for duplicates" only grepped for literal repeated row text — it would not have caught this (these rows aren't textually identical, they're structurally mismatched against the table they landed in). A real check needs to diff column counts within each contiguous table block, not just look for repeated strings.
- Not fixed yet — flagged to Skip rather than unilaterally editing 36 files, since the right fix is a content judgment call (delete the redundant AUTO-ADDED rows since the Options Group table above already covers the same ground, vs. give them their own properly-labeled table) as much as a mechanical one.

### 2026-10-01 — Fixing it: "redundant vs. net-new" isn't a per-file call, it's per-row — and 2 of the 36 files were the opposite case

- Skip said "go ahead, option A (delete)." Before applying it file-by-file, checked each of the 4 files that showed an *unusual* mismatch direction in the earlier scan (not the common 2-col-header/3-col-row pattern) — and found that `the-svg-module-in-divi-5.md` and `the-timeline-module-in-divi-5.md` are categorically different from the other 34: their AUTO-ADDED rows are the **only** real settings documentation on those stub pages (the table above them is empty/TODO-only, not a duplicate reference). Blindly deleting "option A" everywhere would have gutted the one piece of real content Divi's five-new-modules initiative produced for those two modules.
- Built the fix as a per-row rule, not a per-file one: for every AUTO-ADDED row, check whether its setting name (normalized — strip markdown links/bold, trailing `-`/dash artifacts from garbled extraction, generic "Content"/"Design"/"Advanced" tab-name restatements) already appears earlier in the *same table*. Match → redundant → delete. No match → genuinely new → keep, but reformat to the table's actual column count (pad short rows, collapse long ones by dropping empty middle cells) instead of leaving the structural mismatch in place.
- This correctly reproduced "delete" for the 34 common-pattern files (420 rows) and "keep + pad" for SVG/Timeline (plus `button-styling-reference.md`, which turned out to have real design-group settings — Filters/Transform/Animation — that weren't covered anywhere else in its very detailed hand-written table; 125 rows total reformatted-not-deleted).
- A universal near-duplicate junk pattern showed up in almost every file: a `Save`/`Exit` row pair with description `k on the{X}button.` — a cut-off fragment of generic "Click on the Save/Exit button" Visual-Builder chrome instructions, present identically file after file. Deleted unconditionally wherever it matched exactly, regardless of the redundancy check — it's boilerplate, not per-module content.
- **Takeaway for any future auto-extraction cleanup on this repo:** never assume uniform treatment across a flagged file list. The two outlier files here only got caught because a human (not the script) looked at the *direction* of the column mismatch before deciding what "fix" meant — a purely mechanical "delete everything AUTO-ADDED" pass would have silently deleted real content.
- Also surfaced in the cleanup's own verification pass: 11 more files (outside the 36) have column-count mismatches with no AUTO-ADDED marker — different, unrelated root cause (looks like unescaped literal `|` in cell text, same class as one confirmed-harmless false positive found in `the-breadcrumbs-module-in-divi-5.md`'s own pre-existing content). Not investigated — flagged in `state.md` Open Risks.

### 2026-10-01 — The 11 "unrelated" mismatches were 6 genuine-content pipes + 1 scrape artifact — and my own verification script had the same blind spot

- Checked each of the 11 flagged mismatches individually rather than batch-processing them, since they weren't one bug — each file needed to be read. 6 of 7 files turned out to be **genuine content that legitimately contains a literal `|`**: a CSS border-radius format example (`link|top-left|top-right|...`), Divi's own tab-anchor URL syntax (`#dt-tabs|1`), Mailchimp's merge-tag syntax (`*|MERGE|*`), and a "separator character" example (`Common values are|or-.`) that appears identically in 4 rows across 2 files because the Extra and Divi theme options share the same SEO settings copy. None of these were bugs in the writing — they were correct example text that nobody had escaped for markdown table syntax. Fixed by escaping each as `\|`, matching the pattern already correctly used elsewhere in `the-breadcrumbs-module-in-divi-5.md`.
- The 7th (`how-to-change-server-s-maximum-upload-file-size.md`) was genuinely different: a scrape-garbling artifact (a stray empty cell splitting one logical value, "Increase Execution Time," across two table columns). That whole file's prose is truncated throughout (every row is missing its opening words — e.g. "k on theInfotab" instead of "Click on the Info tab"), a pre-existing scrape-quality problem distinct from the table-structure bug. Fixed only the structural break (merged the empty cell away) without touching or trying to "fix" the surrounding garbled prose — inventing cleaner wording would be fabrication, and a full rewrite of that file is a separate, larger task, not this one.
- **Gotcha caught before committing:** my own verification script (written 2026-10-01 to check for remaining mismatches) didn't know about `\|` escaping — it counted raw `|` characters, so after escaping the 6 genuine-content pipes, it still flagged all 7 fixed rows as "broken," because escaped pipes look identical to unescaped ones under naive `.split("|")`. Had to fix the detector itself (split on unescaped `\|` only, matching how python-markdown's table extension actually parses it) before trusting a "zero remaining" result. Any future table-structure check on this repo should split on `(?<!\\)\|`, not `|`.
- Confirmed via `mkdocs build` + rendered HTML spot-checks: all 4 non-trivial cases render as single clean rows with the pipe characters visible as literal text, not split into phantom columns.

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
