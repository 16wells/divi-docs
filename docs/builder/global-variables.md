---
title: "Global Variables"
description: "Divi 5 Global Variables — site-wide design tokens for colors, gradients, fonts, numbers, images, text, and links referenced across all pages and templates."
category: builder
tags: [builder, global-variables, design-system, design-tokens, site-wide]
related: [design-variables, presets, relative-colors-hsl]
divi_version: "5.x"
last_updated: 2026-06-05
source_url: "https://help.elegantthemes.com/en/articles/13348842"
---

# Global Variables

Global variables are site-wide design tokens in Divi 5 that let you define colors, gradients, fonts, numbers, images, text, and links once and reference them on every page, template, and Theme Builder layout.

!!! abstract "Quick Reference"
    **What it does:** Defines site-wide design tokens available on every page, template, and Theme Builder layout.
    **Where to find it:** Variable Manager icon in the Visual Builder toolbar → organized by type tabs.
    **Key features:**

    - Seven types: Color, Gradient, Font, Number, Image, Text, Link
    - **Variable Generator** (in the Variable Manager) can bulk-create relative **color** palettes and **`clamp()`**-based **number** scales — same UI as [design variables](design-variables.md#variable-generator)
    - Number variables support `calc()`, `clamp()`, `min()`, `max()` for responsive values
    - Embedded in layout JSON exports for portable design systems
    - Three-tier system: Variables → Option Group Presets → Element Presets

    **ET Docs:** [Global Variables](https://help.elegantthemes.com/en/articles/13348842){:target="_blank"}

## Overview

While [design variables](design-variables.md) can be created and used on individual pages, global variables are explicitly site-wide in scope. A global variable created on any page is immediately available on every other page, in Theme Builder templates, and in new pages. When you change a global variable's value, the update propagates everywhere it is referenced.

Global variables are the backbone of a Divi 5 design system. By defining your brand palette, typographic scale, and spacing values as globals, you ensure consistency across the entire site and make sweeping design changes trivial — update the variable once instead of editing dozens of individual elements.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13348842).

## Variable Types

Global variables support the same seven types as design variables, each managed in a dedicated tab within the Variable Manager.

| Type | Description |
|------|-------------|
| Color | Brand palette colors, text colors, background colors, border colors |
| Gradient | Reusable linear and radial gradients for backgrounds, text fills, and any gradient-enabled field (Divi 5.7+) |
| Font | Reusable typeface definitions for headings, body text, and custom uses |
| Number | Sizes, spacing values, and responsive units; supports `calc()`, `clamp()`, `min()`, `max()` |
| Image | Logos, patterns, and other visual assets referenced by URL |
| Text | Static strings used across the site (phone numbers, addresses, business hours) |
| Link | Frequently used URLs for CTAs, landing pages, social profiles |

## Managing Global Variables

The Variable Manager is accessed from the Visual Builder toolbar. Global variables are organized into tabs by type.

### Creating a Global Variable

1. Open the Visual Builder on any page
2. Click the **Variable Manager** icon in the toolbar
3. Select the appropriate type tab (e.g., Colors, Numbers)
4. Click the **"+ Add"** button for that type
5. Enter a descriptive name (e.g., "Brand Primary" rather than "Blue")
6. Set the value using the appropriate input (color picker, number field, media selector, etc.)
7. Click **"Save Variables"** to persist the changes site-wide

### Applying a Global Variable

1. Open any element's settings panel
2. Navigate to the target option (background color, font size, etc.)
3. Hover the field to reveal the **dynamic content icon**
4. Click the icon and select the desired global variable from the popup
5. The field now references the global variable instead of a static value

## Integration with Presets

Global variables and presets work together as complementary layers of a design system:

| Layer | Role | Description |
|-------|------|-------------|
| Global variables | Define raw values | Colors, fonts, spacing scales |
| Option Group Presets | Bundle option groups | Reusable typography, button, or background configurations |
| Element Presets | Style full elements | Complete module/row/section designs |

The recommended workflow is: define your global variables first, use them inside presets, then apply presets to pages. This creates a chain of inheritance that makes updates efficient.

## Responsive Number Variables

Number-type global variables support advanced CSS functions, making them especially useful for responsive design:

| Function | Use Case | Description |
|----------|----------|-------------|
| `clamp()` | Responsive typography | Define a minimum, preferred, and maximum value in a single variable |
| `calc()` | Computed values | Perform arithmetic with mixed units |
| `min()` / `max()` | Bounded values | Set floor or ceiling constraints |

A single number variable using `clamp()` can handle responsive font sizing without separate breakpoint overrides.

## Export and Portability

Global variables are embedded in the layout JSON when you export layouts from the Divi Library. When those layouts are imported to another Divi 5 site, the variables come along automatically. This makes global variables part of a portable design system.

## Best Practices

- Start by defining core brand elements: primary/secondary colors, heading and body fonts, base spacing
- Use descriptive names that reflect purpose, not value (e.g., "Section Padding Large" instead of "40px")
- Prioritize editing variables and presets over tweaking individual modules
- Avoid assigning one variable to unrelated purposes — create separate variables even if values are currently identical

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Global variables persist across all pages, suggesting they are stored in a site-wide location such as `wp_options` or a custom post type rather than per-page post meta. The exact option key or post type needs verification.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | `wp_options` query or Divi REST endpoint | Needs Testing | Look for a serialized array under a Divi-specific option key |
| Modify | `update_option()` or Divi REST endpoint | Needs Testing | Changes should propagate on next page render to all references |
| Create | `update_option()` or Divi REST endpoint | Needs Testing | Must specify type, name, and value; color variables integrate with the global color system |


## Elegant Themes tutorials

- [New Gradient Editor, Gradient Variables, Text Effects and More](https://www.elegantthemes.com/blog/theme-releases/new-gradient-editor-gradient-variables-text-effects-and-more){:target="_blank"} — Gradient variables and the unified Gradient Picker in Divi 5.7 (June 2026).
- [Divi 5 Sizing System & Color Palette Variable Generator](https://www.elegantthemes.com/blog/theme-releases/variable-generator){:target="_blank"} — Variable Manager generators for site-wide color and fluid sizing tokens (April 2026).

*Maintainers:* also list new posts in [`planning/et-blog-tutorials-map.md`](https://github.com/16wells/divi-docs/blob/main/planning/et-blog-tutorials-map.md){:target="_blank"}.

## Related

- [Design Variables](design-variables.md) — The variable system fundamentals and Variable Manager
- [Presets](presets.md) — Saved design configurations that can reference global variables
- [Gradient Builder](gradient-builder.md) — Gradient Picker and gradient variables
- [Relative Colors (HSL)](relative-colors-hsl.md) — HSL-based color relationships using the color system
- [Option Group Presets](option-group-presets.md) — Reusable style blocks that work with variables
