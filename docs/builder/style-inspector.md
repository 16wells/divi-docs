---
title: "Style Inspector"
description: "Divi 5 Style Inspector — audit and edit all colors, fonts, numbers, media, code, attributes, and presets on a page or element from one panel."
category: builder
tags: [builder, style-inspector, debugging, design-audit, design-system]
related: [presets, design-variables]
divi_version: "5.x"
last_updated: 2026-03-16
source_url: "https://help.elegantthemes.com/en/articles/12457386"
---

# Style Inspector

The Style Inspector is a panel in the Divi 5 Visual Builder that shows all styles, content, and presets applied to a page or individual element, and allows direct editing from a single consolidated view.

!!! abstract "Quick Reference"
    **What it does:** Displays and allows editing of every style, content attribute, and preset on the page or selected element.
    **Where to find it:** Left sidebar → Inspector icon.
    **Key features:**

    - Three tabs: Styles (colors, gradients, numbers, fonts), Content (media, code, attributes, text), Presets
    - Page-level or element-level inspection scope
    - Hover any value to highlight all fields sharing it across the page
    - Direct inline editing — changes apply immediately

    **ET Docs:** [Style Inspector](https://help.elegantthemes.com/en/articles/12457386){:target="_blank"}

## Overview

The Style Inspector acts as an audit and editing tool for your design. At the page level, it displays every color, font, number value, media asset, code snippet, attribute, and preset used across the entire page. At the element level, it narrows the view to show only what affects the selected section, row, column, or module. Changes made within the inspector apply immediately.

This makes the Style Inspector useful for identifying inconsistencies (stray font sizes, off-brand colors), consolidating one-off values into global variables or presets, and quickly editing content attributes like alt text without opening each module individually.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12457386) and the [detailed usage guide](https://help.elegantthemes.com/en/articles/13002652).

## Accessing the Style Inspector

1. Open the Visual Builder on any page
2. Locate the **Inspector icon** in the left sidebar
3. Click to activate the Style Inspector panel
4. To inspect a specific element, select it first, then open the inspector

## Inspection Levels

| Level | Scope | How to Activate |
|-------|-------|-----------------|
| Page-level | All styles, content, and presets on the entire page | Open the inspector without selecting any element |
| Element-level | Only the styles, content, and presets for the selected element | Select a section, row, column, or module, then open the inspector |

## Tabs

The Style Inspector organizes information into three tabs:

### Styles Tab

Displays all design values used in the current scope, grouped by type.

| Group | Description |
|-------|-------------|
| Colors | Global colors sorted by usage count, followed by static (one-off) colors |
| Numbers | Font sizes, line heights, spacing values, and other numeric settings |
| Fonts | Font families and weights in use |

Hovering over any value highlights all fields across the page (or element) that share that value. This makes it easy to spot where a specific color or font size is applied.

### Content Tab

Lists all non-style content in the current scope.

| Group | Description |
|-------|-------------|
| Media | Background images and media assets |
| Code | Custom CSS snippets |
| Attributes | IDs, classes, alt text, and title attributes |
| Text | Module text content |

### Presets Tab

Shows all presets applied within the current scope.

| Group | Description |
|-------|-------------|
| Module Presets | Element presets applied to modules, rows, sections, or columns |
| Option Group Presets | Button, typography, background, and other option group presets |

## Direct Editing

The Style Inspector is not read-only. You can modify values directly within the panel:

- Click a color to change it or map it to a global color
- Adjust font sizes and numeric values inline
- Edit attributes like alt text and CSS classes
- Changes apply immediately to the current scope and auto-save

## Common Use Cases

| Task | Workflow |
|------|----------|
| Color audit | Open page-level inspector, review the Colors group to identify off-brand or inconsistent colors |
| Font consistency | Check the Numbers group for one-off font sizes that should be standardized |
| Alt text cleanup | Open the Content tab, review the Attributes group, fix missing or incorrect alt text |
| Preset coverage | Check the Presets tab to see which elements use presets and which have only static styles |
| Value consolidation | Identify frequently repeated static values and convert them to global variables |

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    The Style Inspector is a read/edit UI tool that surfaces data already stored in element attributes, presets, and global variables. It does not introduce its own data storage layer. Edits made through the inspector modify the same underlying data as editing through element settings.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Layout JSON inspection or Divi REST API | Needs Testing | The inspector aggregates data from element attributes, presets, and global variables |
| Modify | Layout JSON update or Divi REST API | Needs Testing | Modifications through the inspector are equivalent to modifying the underlying element/preset data directly |
| Create | N/A | N/A | The inspector does not create new data structures — it surfaces existing ones |


## Related

- [Presets](presets.md) — Element presets surfaced in the Presets tab
- [Design Variables](design-variables.md) — Variables that appear in the Styles tab as global values
- [Option Group Presets](option-group-presets.md) — Option group presets shown in the Presets tab
