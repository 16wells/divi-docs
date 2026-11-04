---
title: "Design Variables"
description: "Divi 5 Design Variables — define reusable color, number, font, image, link, and text tokens and apply them to any field via dynamic content."
category: builder
tags: [builder, design-variables, design-system, dynamic-content, css-variables]
related: [global-variables, option-group-presets, advanced-units]
divi_version: "5.x"
last_updated: 2026-06-05
source_url: "https://help.elegantthemes.com/en/articles/11027601"
---

# Design Variables

Design variables let you define reusable values — colors, numbers, fonts, images, links, and text — and apply them to fields across your Divi 5 site through the dynamic content system.

!!! abstract "Quick Reference"
    **What it does:** Stores named tokens (colors, numbers, fonts, images, links, text) that can be assigned to any compatible field via dynamic content.
    **Where to find it:** Variable Manager icon in the Visual Builder toolbar, or any field's dynamic content icon → Manage Variables.
    **Key features:**

    - Seven variable types: Numbers, Strings, Images, Links, Colors, Gradients, Fonts
    - **Variable Generator:** auto-build a relative color palette from the site primary color, or a full fluid sizing system (`clamp()`-based numbers) from the Numbers group
    - Assign via dynamic content icon on any compatible field
    - Variable chips display the variable name; hover to see the current value
    - Change a variable once to update every field referencing it

    **ET Docs:** [Design Variables](https://help.elegantthemes.com/en/articles/11027601){:target="_blank"}

## Overview

Design variables in Divi 5 act as named tokens that store a single value and can be assigned to any field that supports dynamic content. When you change a variable's value, every field referencing that variable updates automatically. This makes variables the foundation of a scalable design system: define your brand colors, spacing scale, and typography once, then reference those definitions everywhere.

Variables are managed through the **Variable Manager**, accessible from the Visual Builder toolbar or from the dynamic content menu on any compatible field. Each variable has a name and a typed value, and Divi enforces unit compatibility when assigning number variables to fields that expect specific CSS units.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11027601).

## Variable Manager

The Variable Manager is the central interface for creating, editing, deleting, and reordering design variables. You can open it from the toolbar icon in the Visual Builder or by selecting "Manage Variables" from any field's dynamic content menu.

### Accessing the Variable Manager

| Method | Description |
|--------|-------------|
| Toolbar icon | Click the variables icon in the Visual Builder toolbar |
| Dynamic content menu | Hover a supported field, click the dynamic content icon, then select "Manage Variables" |

### Manager Features

| Feature | Type | Description |
|---------|------|-------------|
| Create variable | Action | Add a new variable by specifying a name and value (both required) |
| Edit variable | Action | Change the name or value of an existing variable |
| Delete variable | Action | Remove a variable; it is archived and remains functional until the page is saved |
| Restore variable | Action | Reactivate a deleted variable that is still assigned to fields |
| Reorder variables | Action | Drag and drop variables using the hover handle; no save required |
| Save changes | Action | Explicitly save to persist all edits; closing or cancelling discards unsaved work |

## Variable Generator

Divi 5 can **generate** whole groups of variables from the Variable Manager instead of creating each token by hand. There are two generators: a **relative color palette** (built from your primary color) and a **fluid sizing** system for number variables (typically using `clamp()`). Elegant Themes positions this for beginners (defaults work out of the box) and for advanced users (per-variable and scaling controls in a customization sidebar).

### Color palette generator

| Item | Detail |
|------|--------|
| **Where** | Variable Manager → **Colors** group → hover the group header → **Generate Color Palette Variables** |
| **What it does** | Uses the site **primary** color (and configurable **secondary** relationship) to create a set of **color variables** tied together with Divi’s [relative color](relative-colors-hsl.md) behavior — changing the primary updates derived shades. |
| **Outputs** | Updates base roles such as primary, secondary, body text, header text, and link colors, and adds a spectrum of lighter/darker and transparent variants (per Elegant Themes’ April 2026 announcement). |
| **Typical workflow** | Adjust secondary relationship and how many shade steps you want, then save. |

Each generated color is still a normal color variable in the manager; the generator is a bulk authoring shortcut, not a separate storage type.

### Fluid sizing (numbers) generator

| Item | Detail |
|------|--------|
| **Where** | Variable Manager → **Numbers** group → hover the group header → **Generate Fluid Sizing Variables** |
| **What it does** | Creates many **number** variables at once — by default as **`clamp()`** expressions so values scale between min and max across viewports without switching breakpoints manually. |
| **Variable type menu** | Pick the kind of system to generate (each maps to fields you would normally drive with number variables): |

| Generator type | Intended use (per Elegant Themes) |
|----------------|-----------------------------------|
| Font size | Heading/body type scales with viewport |
| Spacing | Margin and padding scales with viewport |
| Gap | Flex row/column gap scales with viewport |
| Radius | Border radius scales with viewport |
| Border width | Border widths scale with viewport |
| Clamp (generic) | Custom `clamp()`-based tokens |
| Size (generic) | Other sizing tokens not covered above |

**Beginner path:** choose how many variables to create, then confirm (e.g. **Add Variables To My Site** in the UI).

**Advanced path:** open the **customization** sidebar to change scaling function, set the site’s **minimum and maximum width** used to tune `clamp()`, edit individual generated variables, build **non-`clamp`** static scales, or adjust variable name **prefixes/suffixes**.

!!! note "Help Center gap"
    The official Help Center article linked in frontmatter predates the Variable Generator. For UI labels and the full walkthrough, use the blog post and video under [Elegant Themes tutorials](#elegant-themes-tutorials) below.

## Variable Types

Divi 5 supports seven variable types, each suited to different kinds of design data.

| Type | Description |
|------|-------------|
| Numbers | Numeric values with CSS unit support; Divi validates unit compatibility when assigning to fields |
| Strings | Plain text content for any text-supporting field |
| Images | Image URLs selected from the WordPress Media Library |
| Links | Full URLs or relative paths for link fields |
| Colors | Color values that integrate with the global color UI; existing primary/secondary colors are read-only |
| Gradients | Complete gradient definitions (stops, type, direction) editable in the Gradient Picker; site-wide updates when the variable changes (Divi 5.7+) |
| Fonts | Font family selections; includes custom variables plus heading and body fonts from the Theme Customizer |

## Assigning Variables to Fields

To assign a variable to a design field:

1. Open any element's settings in the Visual Builder
2. Hover over the target field to reveal the **dynamic content icon**
3. Click the icon and select a variable from the dropdown
4. The field displays a **variable chip** showing the variable name
5. Hover the chip to see the current value (display varies by type)
6. Click the chip to detach the variable, replace it with another, or open the Variable Manager

## Variable Chips

When a variable is assigned to a field, the field displays a chip instead of a raw value. The chip shows the variable's name, and hovering it reveals the current value. Clicking the chip opens options to detach the variable, swap it for a different one, or jump into the Variable Manager.

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Design variables are likely stored as custom CSS properties at the page or site level. The Variable Manager appears to persist data either in `wp_options` (for site-wide variables) or in the page's post meta / Divi layout JSON. The exact storage mechanism for page-scoped vs. site-scoped variables needs verification.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Divi REST API or `wp_options` query | Needs Testing | Variables may be serialized in a Divi-specific options key or layout JSON |
| Modify | Divi REST API or direct `wp_options` update | Needs Testing | Changing a variable value should propagate to all referencing fields on next render |
| Create | Divi REST API or `wp_options` insert | Needs Testing | Must include name, value, and type; unit validation applies to number variables |


## Elegant Themes tutorials

- [New Gradient Editor, Gradient Variables, Text Effects and More](https://www.elegantthemes.com/blog/theme-releases/new-gradient-editor-gradient-variables-text-effects-and-more){:target="_blank"} — Gradient variable type and Gradient Picker in the Variable Manager (June 2026).
- [Divi 5 Sizing System & Color Palette Variable Generator](https://www.elegantthemes.com/blog/theme-releases/variable-generator){:target="_blank"} — Theme release walkthrough of the color palette and fluid sizing generators in the Variable Manager (April 2026).
- [Variable Generator — video tour](https://www.youtube.com/watch?v=9NhPczWWBng){:target="_blank"} — Same announcement in video form on the Elegant Themes YouTube channel.

*Maintainers:* also list new posts in [`planning/et-blog-tutorials-map.md`](https://github.com/16wells/divi-docs/blob/main/planning/et-blog-tutorials-map.md){:target="_blank"}.

## Related

- [Global Variables](global-variables.md) — Site-wide variables that persist across all pages
- [Option Group Presets](option-group-presets.md) — Reusable style configurations for option groups
- [Advanced Units](advanced-units.md) — CSS functions and custom variables in Divi value fields
- [Presets](presets.md) — Saved design configurations for elements
- [Playbook: Design System Setup](../playbooks/design-system-setup.md) — Build a complete design system with variables and presets
