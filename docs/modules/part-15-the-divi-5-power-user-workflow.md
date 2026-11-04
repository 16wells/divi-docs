---
title: "Part 15: The Divi 5 Power User Workflow"
description: "The order of operations experienced Divi 5 builders follow: plan with wireframes, style by reference, navigate quickly, read existing styles, and reuse the design system."
category: modules
tags: [modules, workflow, presets, design-variables, command-center, course]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15704312-part-15-the-divi-5-power-user-workflow"
---

# Part 15: The Divi 5 Power User Workflow

!!! abstract "Quick Reference"
    **Course position:** Part 15 of the Divi 5 Mastery Course. Previous: [Part 14](part-14-mastering-the-divi-5-loop-builder.md). Next: [Part 16](part-16-auditing-polishing-and-launching-your-divi-5-website.md).
    **Theme:** Not a new feature, but the habits and order of work that make builds fast and changes propagate.
    **Chain to remember:** Design Variables, then Option Group Presets, then Element Presets, then modules and layouts.
    **Shortcut:** Command Center opens with Cmd + K (macOS) or Ctrl + K (Windows).

## 1. Plan before you build

Wireframe each page first (Wireframe View is made for this). The goal is not just layout but spotting repeated patterns, because repeated patterns become Presets.

- A module used once or twice (a lone Blurb) needs at most one Element Preset.
- Headings, Text modules, Buttons, Links, Rows, Columns, and Groups appear everywhere and need more variety. A Heading might serve as hero title, section title, card title, post title, and eyebrow, each deserving its own preset when it repeats.
- This is why the course built Design Variables first, then Presets, then pages and templates.
- Do not pre-build every conceivable preset. Build what the wireframe points to and add more when a design needs one (for example a new heading treatment on the Events page). A tight library is faster than a sprawling one.

## 2. Style by reference, not by value

Styling by value means retyping the same hex code, size, or padding in every module. Styling by reference saves the value once and applies it everywhere, so changes propagate.

- **Design Variables** hold colors, fonts, numbers, text, links, and images, and can be used inside Presets.
- **Variable Generator** speeds up real projects: the Color Palette Generator builds a relative color system from primary and secondary colors, and the Sizing Variable Generator builds fluid systems for font sizes, spacing, gaps, widths, border radius, and border width. You still make the design decisions.
- **Build the chain once:**
    1. Design Variables store source values.
    2. Option Group Presets apply them to specific style groups.
    3. Element Presets combine groups into reusable module or container styles.
    4. Modules and layouts use those presets.
- **Extend instead of rebuild:** style the first card carefully, then use Extend Attributes to carry the relevant attributes to the rest. If the cards have different text but should look identical, extend only design attributes and leave content alone.

## 3. Navigate at speed

| Tool | Use |
|---|---|
| Page Manager | Move between pages and posts without leaving the Visual Builder, handy when standardizing something (like testimonial cards) across pages. |
| Command Center | Search-and-action bar for settings, pages, builder tools, and common actions. |
| Layers View | Full page hierarchy for deeply nested layouts: select, rename, and reorder elements directly. |

## 4. Read your own work

- **Modified Filter** reduces the settings panel to values changed from default; the **Modified Indicator** is a small blue dot beside a changed setting or group label. Both are part of the settings search and filtering system.
- **Limitation:** the Modified Filter shows direct edits on the element, not styling that comes from an Element Preset or Option Group Preset. An element that looks heavily styled while the filter shows little is probably styled mostly through presets.
- **Style Inspector** surfaces colors, fonts, styles, and presets across elements, which is how to find a stray off-brand color, a heading missing its preset, or a one-off value that should be a variable.
- Rule of thumb: Modified Filter for one element's direct edits, Inspector for patterns across the layout.

## 5. Reuse the system

Export your Design Variables and Presets and import them into a new project. Because presets reference variables, you start the new site by updating the variables (brand colors, typefaces, spacing, borders, sizing) and every preset adapts. You carry over a reusable structure and repoint its references, rather than copying a finished look and hunting down every place to change.

## Divi AI Agent shortcut

For sites with hand-typed colors, fonts, and spacing, the Divi AI Agent (part of a Divi AI subscription) can find hard-coded values on a page and convert chosen ones into Global Variables, switching each occurrence over after your approval.

## Official documentation

[Part 15: The Divi 5 Power User Workflow](https://help.elegantthemes.com/en/articles/15704312-part-15-the-divi-5-power-user-workflow)
