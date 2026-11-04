---
title: "Part 12: Making Your Divi 5 Website Fully Responsive"
description: "Run a final responsive audit on a Divi 5 site using breakpoints, the Responsive Editor, Structure Templates, Flexbox, CSS Grid, and Design Variables."
category: modules
tags: [modules, responsive, breakpoints, flexbox, css-grid, course]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15703949-part-12-making-your-divi-5-website-fully-responsive"
---

# Part 12: Making Your Divi 5 Website Fully Responsive

!!! abstract "Quick Reference"
    **Course position:** Part 12 of the Divi 5 Mastery Course. Previous: [Part 11](part-11-mastering-css-grid-in-divi-5.md). Next: [Part 13](part-13-creating-interactive-off-canvas-elements-and-popups-in-divi-5.md).
    **Goal:** A final audit of the coworking site (homepage, inner pages, global templates) from phone to ultra-wide.
    **Workflow:** Homepage first, then inner pages, then Theme Builder templates; within each page go Desktop, then Tablet, then Phone.
    **Principle:** Fix site-wide issues in Presets and Variables; use local styles only for one-off adjustments.

## Responsive tools to know

| Tool | What it does |
|---|---|
| Customizable breakpoints | Seven are available: Phone, Phone Wide, Tablet, Tablet Wide, Desktop, Widescreen, Ultra Wide. Click the ellipsis in the Page Bar's responsive menu to enable extras. |
| Canvas scaling | Type an exact width in the responsive width field or drag the Canvas edge to test in real time. |
| Responsive State Picker | Chooses the breakpoint or state being edited: Desktop, Tablet, Phone, Hover, Focus, Checked, Active, Sticky. Check interactive states on buttons, forms, and sticky elements. |
| Responsive Editor | Review and edit a setting across breakpoints in one panel via the Edit Responsive Values icon. Good for typography, spacing, alignment, and column sizing. |
| Structure Templates | Change column layouts per breakpoint (for example three columns on desktop, one on phone). |
| Display Order | In a Column's settings, reorders columns visually on small screens without moving modules or using Visibility. |
| Design Variables | Fluid `clamp()` values already scale between breakpoints; change shared values in the Variable Manager rather than one-off fixes. |
| Flexbox and CSS Grid | Per breakpoint, adjust Layout Direction, Wrapping, Justify Content, Align Items, and gaps (Flexbox), or column/row counts and item placement (Grid). |

## Recommended workflow

1. Start with the homepage, which sets most visual patterns.
2. Review inner pages, reusing earlier decisions.
3. Check Theme Builder templates, especially the global header and footer.
4. Use the Style Inspector and Layers View to catch inconsistencies.

Helpful view tools: drag the Canvas resize handle, use **X-Ray Mode** for structure and spacing, **Wireframe Mode** for long pages, and the Style Inspector for bulk checks.

**Where to change things:** use local styles for one section's needs (for example hero spacing). If a change should apply everywhere (such as button padding on mobile), edit the Preset, then use Extend Attributes to apply it across the page where appropriate.

## Homepage refinements

### Hero

1. Confirm the main headline uses the **Heading 1 Big** element preset so it scales fluidly, and use the Responsive Editor to tune line height at Tablet and Phone.
2. **Stack the hero buttons on Phone:** select the Group holding them, then **Design, Layout, Layout Direction** to Column, Vertical Gap to the **Spacing - XSmall** variable, **Align Items** Center.
3. **Stack the three-column row on Phone:** with Phone selected, open the Row, use **Content, Elements, Apply Structure Template** and choose a 1-column template; set the Row's Vertical Gap to **Spacing - Small**; for each Column set Vertical Gap to **Spacing - XSmall** and Padding Top to `0px`.
4. If headings feel uneven on Tablet, update the Heading 4 preset (for example an H4 Tablet variable at 20px). On Phone, you can use an H2 Mobile variable such as 24px for the Heading Text Size.

### Features grid (CSS Grid)

Confirm the **Number of Columns** goes from three on Desktop to two on Tablet and one on Phone. On mobile, tighten the Vertical Gap with **Spacing – Medium** if cards look too spread out.

### Split features section

1. On Tablet, use **Apply Structure Template** (Row's Elements group) to switch to a single column.
2. To remove extra white space beside the supporting blocks: add a new Group below the intro Group, drag the second and third Groups into it, and set the new parent Group's **Layout Direction** to Row on Tablet so they sit side by side.
3. On Phone, switch that parent Group back to Column.

### Remaining sections

Check Testimonials, Pricing, Countdown, and FAQ for spacing, Row structure, button and form size, touch targets on Phone, and consistent type scaling.

## Inner pages

- **Contact page:** in Phone view, click a form field, then **Design, Sizing, Column Class** and set it to Fullwidth. Reduce extra whitespace by applying **Spacing – Medium** to the first Section's Vertical Gap.
- **Events page:** confirm cards collapse on Tablet and Phone; check date blocks, details, pricing, buttons, and alignment. Fix cramped layouts with Structure Templates, fewer columns, or Flexbox alignment and gap changes at the relevant breakpoint.
- **Moving between pages:** the Page Manager icon in the left sidebar lets you jump to another page by name without leaving the builder; Speculative Prerendering speeds this up when enabled.

### Inner page checklist

- Do multi-column Rows collapse properly with Structure Templates?
- Are buttons and touch targets large enough on mobile?
- Does typography scale like the homepage?
- Any awkward gaps, cramped areas, or overflow?
- Do forms, maps, countdowns, and opt-ins stay usable on Phone?

## Global templates

Turn on **Show Theme Builder Layouts** in Builder Settings to review header, footer, and content together.

**Header:** check the logo scales without using too much vertical space; confirm the menu switches cleanly to the mobile layout at Tablet and Phone; trim bottom padding on the sticky header if needed. Turn off the setting that dims disabled elements to 50% opacity for a preview closer to the front end.

**Footer:** adjust column widths with the Column Class field in Sizing so content flows well on Tablet and Phone; use number variables for typography; check social icon alignment; adjust gaps so the footer is not cramped or too tall.

## Divi AI Agent shortcut

The Divi AI Agent can set a value at one breakpoint without disturbing others, or inspect the page at phone width and list cramped spots (for example a prompt asking it to flag overflowing text or oddly collapsed cards, list only, no fixes).

## Official documentation

[Part 12: Making Your Divi 5 Website Fully Responsive](https://help.elegantthemes.com/en/articles/15703949-part-12-making-your-divi-5-website-fully-responsive)
