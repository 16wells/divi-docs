# Activity Log — Divi 5 Technical Documentation

> **Cross-surface handoff file.** This is how a Claude agent in Cowork knows what a Claude agent in Chat (or Claude Code) already worked on, and vice versa. Every session appends one entry. Read the most recent 5–10 entries at the start of a work session before doing anything.

## How to Use This File

**At the start of a session** — scan the last few entries to see:
- What was the previous agent working on?
- What's in progress but not finished?
- Were any decisions logged that I should know about?
- Is anything queued up for me specifically?

**At the end of a session** — append a new entry with:
- Date (ISO format: `2026-04-17`)
- Surface (Cowork, Claude Code, Claude.ai Chat, or Claude.ai Project)
- What you did (brief — one or two sentences per item)
- What's in progress / partial
- What's queued for next session

**Keep entries short.** This file is read at the top of every session. If it gets bloated, it stops getting read. Aim for 5–10 lines per entry max. Details belong in the decisions log or the actual deliverable file.

**Do not duplicate the decisions log.** If a decision was made, log it in `decisions-log.md` and reference it here — don't restate it.

---

## Session Entries (newest first)

### 2026-05-22 — Claude Code on the Web — Five New Modules announcement stubs

- Digested the ET *Five New Modules for Divi 5* announcement (Timeline, Breadcrumbs, Table of Contents, SVG, Instagram Feed). Created stub pages for the four missing modules (`docs/modules/the-timeline-module-in-divi-5.md`, `the-svg-module-in-divi-5.md`, `the-table-of-contents-module-in-divi-5.md`, `the-instagram-feed-module-in-divi-5.md`) plus the related builder page (`docs/builder/aspect-ratio-image-framing-and-image-presets-in-divi-5.md`). Added `## Elegant Themes tutorials` sections linking the blog post on each new page and on the existing Breadcrumbs page. Added the blog row to `planning/et-blog-tutorials-map.md`. Updated `mkdocs.yml` nav and ran `mkdocs build` cleanly. Stubs have TODO settings tables because the sandbox network policy blocks `elegantthemes.com` / `help.elegantthemes.com` (see insights). Next weekly monitor run with network access should fill them in.
- See decision: stubs-vs-full-pages (2026-05-22).

### 2026-05-21 — Claude Code — Re-template from `client-project` to `internal-product`

- Renamed `01-context/client-profile.md` → `01-context/product-charter.md` via `git mv` and substantially expanded the content into the internal-product charter schema (One-liner, Stage, Why We're Building It, The User with three audiences, Anti-persona, Content Layers table, Scope Boundaries, Success/Kill Criteria, Editorial Voice, Trust Signals). Original positioning preserved and built out.
- Updated `CLAUDE.md` with surgical additions only (CLAUDE.md was previously highly customized for the MkDocs task-doc shape and is intentionally not template-shaped):
  - Added "Who You're Working For" section establishing internal-product framing (16Wells-owned, public users = Divi 5 implementers + AI assistants).
  - Updated "How to Get Oriented" table to reference `product-charter.md`.
  - Added Karpathy "Working Style" section with one Divi-doc-specific tweak (verification step calls out `mkdocs build`).
  - Added Git Operations + File Editing sections (these were previously absent from this CLAUDE.md).
- Preserved the entire Content Types table, Common Tasks, Rules, and Task Files sections — they are project-specific operational content and out of scope for the re-templating.
- README.md is already well-shaped and doesn't reference `client-profile.md`, so no README changes needed.

### 2026-05-06 — Cowork — Filterable Gallery plugin + recipe page + standalone GitHub repo
- Built the Divi 5 Filterable Gallery WordPress plugin from chunk 1 → v1.2.5 across three feature chunks plus several rounds of bug fixes (final zip: `divi5-filterable-gallery-v1.2.5.zip` in `02-deliverables/`).
- Five notable bugs caught and fixed during the build: (1) Python escape collision in patch tooling produced broken PHP echo statement in v1.1.0 (fixed via single-quoted PHP strings for static HTML); (2) "Unsaved changes" indicator on page load — root cause was CSS specificity, not JS event timing chased through three versions (display:inline-flex on indicator span overrode the [hidden] attribute's user-agent default); (3) gallery items leaving layout gaps when filtered out — switched from opacity+height:0 to display:none !important; (4) live preview pane needed to be in same column as CSS editor with maximize-toggle (v1.2.4 layout restructure to grid-template-areas); (5) class reference sidebar overflowing preview in maximized mode — fixed in v1.2.5 by JS-pinning reference's max-height to editor's measured height + ResizeObserver to keep them in sync.
- Wrote `docs/recipes/divi5-filterable-gallery.md` documenting the v1.2.5 feature set; integrated 5 screenshots Skip captured (overview, categories-admin, tag-image, filter-row, settings-editor); updated `mkdocs.yml` Recipes nav and `docs/recipes/index.md`. `mkdocs build` succeeds cleanly with zero recipe-related warnings.
- Built standalone GitHub repo at `02-deliverables/divi-filterable-gallery/` ready to push to `git@github.com:16wells/divi-filterable-gallery.git`: README.md (GitHub-flavored, links back to docs site + 16wells.com), full GPL-2.0 LICENSE, .gitignore, CONTRIBUTING.md, plus complete plugin source. Initialized as git repo, committed, tagged v1.2.5. Added `02-deliverables/divi-filterable-gallery/` to divi-docs's `.gitignore` to prevent nested-repo conflicts.
- **In progress:** none.
- **Queued:** Skip needs to: (1) `cd 02-deliverables/divi-filterable-gallery/ && git remote add origin git@github.com:16wells/divi-filterable-gallery.git && git push -u origin main --tags` to push the plugin repo; (2) on GitHub, create a v1.2.5 Release with the zip attached; (3) commit the recipe page + nav update + index update + screenshots + activity log to the divi-docs repo via standard `git add docs/ mkdocs.yml 01-context/ .gitignore && git commit -m "Add Divi 5 Filterable Gallery recipe" && git push`.

### 2026-05-06 — Cowork — Settings-table update pass (May 4 monitor report)
- Ran `auto_update_page()` directly from bash for all 59 pages flagged in the May 4 monitor report, bypassing hash detection (hashes were already updated by the monitor run).
- Added **438 settings rows** across **20 module files**: tabs, woo-product-price, woo-product-tabs, text, code, woo-checkout-billing, icon, woo-breadcrumbs, login, woo-related-products, woo-product-images, testimonial, audio, blog, blurb, contact-form, woo-product-title, woo-product-reviews, heading, bar-counter.
- 39 builder/css-reference/options-groups/troubleshooting pages skipped ("no new settings") — most were fully rewritten from ET source earlier in the session and already had complete tables.
- Final `mkdocs build`: 0 broken cross-reference links. Screenshot-placeholder warnings only (expected).
- **In progress:** none
- **Queued:** User needs to commit: `git add docs/ && git commit -m "Add 438 settings rows to 20 module files via auto_update_page" && git push`. Screenshot capture still needed for all new pages (requires live Divi 5 site).

### 2026-05-06 — Cowork — Full backlog clear from May 4 monitor report
- Reformatted 9 raw-scraped ET pages to proper SKILL.md template (Contact Form 7 Styler, Canvas Portal, Breadcrumbs, Variable Generator, New Form Field Options, Fields/Checkbox/Radio Option Groups, Ken Burns Effect).
- Enriched 47 TODO stub pages across `docs/builder/`, `docs/modules/`, and `docs/troubleshooting/` — worked in 5 parallel batches. Every stub replaced with full settings tables, step-by-step instructions, screenshot placeholders, tips, and related links.
- Fixed all broken cross-reference links site-wide (two Python batch-replacement passes + manual edits); build ends with 0 errors, 0 broken-link warnings.
- mkdocs.yml nav was already complete from a Cursor session earlier that day — no nav changes needed.
- **In progress:** none
- **Queued:** 41 pages in the monitor report have settings-table additions to incorporate (lower priority — individual page updates). Screenshot capture still needed for all new pages (requires live Divi 5 site).

### 2026-05-06 — Cowork — Retrofit project-memory scaffold
- Added `01-context/` files: `activity-log.md`, `decisions-log.md`, `insights.md`, `client-profile.md`, and `project-scope.md`.
- Added `02-deliverables/kickoff-notes.md` plus folder readmes for `03-assets/`, `04-research/`, and `05-build/`.
- Added `.claude/commands/` files and `.claude/skills/project-setup/SKILL.md`.
- Added continuity sections to root `CLAUDE.md`: orientation table, `activity-log.md`/`insights.md` guidance, and cross-surface handoff instructions.
- Created empty subfolders with `.gitkeep`: `03-assets/copy/`, `03-assets/photos/`, `03-assets/brand/`, `04-research/competitors/`, `05-build/wireframes/`.
- Refined `01-context/client-profile.md` and `01-context/project-scope.md` to project-native language and removed generic scaffold TODOs.
- **In progress:** none
- **Queued:** Use these files as the baseline for future decision and session logging.

### 2026-05-06 — Cowork — Project setup
- Created retrofit context files from the template and filled placeholders for this documentation repo.
- Kept existing site/runtime files untouched while adding only project-memory scaffolding.
- **In progress:** _(nothing yet)_
- **Queued:** First working session

---

## Entry Template (copy this when adding a new entry)

```
### YYYY-MM-DD — [Surface] — [Short topic]
- [What you did — bullet per item, one sentence each]
- **In progress:** [Anything left partial — or "none"]
- **Queued:** [What the next session should pick up — or "none"]
```

---

## What Belongs Here vs. Elsewhere

| If it's... | Log it in... |
|---|---|
| A concrete decision (closed or open) | `decisions-log.md` |
| Something the client owes us | `decisions-log.md` → Outstanding From Client |
| Working state / what I did today | **This file** |
| A draft copy or asset | The actual file in `03-assets/` |
| Research findings | The appropriate file in `04-research/` |

If you're ever unsure, err toward logging it here briefly with a pointer to where the full artifact lives.
