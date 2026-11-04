---
title: "Relative Colors (HSL)"
description: "Divi 5 HSL color system — derive color variations from base values using relative hue, saturation, lightness, and opacity filters."
category: builder
tags: [builder, colors, hsl, relative-colors, color-system, design-system]
related: [design-variables, global-variables, advanced-units]
divi_version: "5.x"
last_updated: 2026-04-30
source_url: "https://help.elegantthemes.com/en/articles/11631084"
---

# Relative Colors (HSL)

Divi 5's color system uses HSL (Hue, Saturation, Lightness) as its native color model and provides relative color filters that generate variations from a base color — maintaining relationships that update automatically when the base color changes.

!!! abstract "Quick Reference"
    **What it does:** Generates color variations from a base color using HSL offset filters that update automatically when the base changes.
    **Where to find it:** Any color picker → Color Filters drawer (expandable panel within the picker).
    **Key features:**

    - HSL-native color model with Hex, RGB, HSL, and CSS variable input formats
    - Color Filters drawer for relative hue, saturation, lightness, and opacity adjustments
    - Derived colors maintain relationships when the base color changes
    - Four default global colors: Primary, Secondary, Heading Text, Body Text

    **ET Docs:** [Relative Colors (HSL)](https://help.elegantthemes.com/en/articles/11631084){:target="_blank"}

## Overview

Rather than picking every color individually, Divi 5 lets you derive colors from a base value by adjusting its hue, saturation, lightness, and opacity. These adjustments are stored as relative offsets, meaning the relationship between colors is preserved. If you change your primary brand color from blue to green, all derived colors (hover states, lighter backgrounds, darker accents) shift accordingly.

This system integrates tightly with [global variables](global-variables.md) and [design variables](design-variables.md). You can define a base color as a global variable and then apply relative color filters wherever that color is referenced, building an entire dynamic palette from a handful of base values.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11631084).

## Color Picker

Divi 5 replaces the traditional swatch grid with a modal-based color picker that supports multiple input formats and HSL-native controls.

### Supported Input Formats

| Format | Description |
|--------|-------------|
| Hex | Standard hex color codes (e.g., `#3A5BD9`) |
| RGB | Red, Green, Blue values |
| HSL | Hue, Saturation, Lightness values |
| CSS variables | Custom property references (e.g., `var(--brand-primary)`) |

### Adjustment Controls

| Control | Type | Description |
|---------|------|-------------|
| Hue | Slider | Rotates the color around the color wheel (0-360 degrees) |
| Saturation | Slider | Adjusts color intensity from gray to fully saturated |
| Lightness | Slider | Adjusts brightness from black through the color to white |
| Opacity | Slider | Controls transparency from fully transparent to fully opaque |

## Color Filters Drawer

The Color Filters drawer is an expandable panel within the color picker that lets you apply relative HSL modifications to any color. These filters create derived colors that maintain their relationship to the base.

### How Color Filters Work

1. Select a base color (manually or from a global variable)
2. Expand the **Color Filters** drawer
3. Adjust the HSL and opacity sliders to create the desired variation
4. The resulting color is stored as the base color plus the filter offsets

When the base color changes, the filter offsets are reapplied, producing a new result that preserves the same relative relationship.

### Filter Applications

| Use Case | Filter Approach | Description |
|----------|-----------------|-------------|
| Hover state | Decrease lightness by 10-15% | Creates a darker version for hover effects |
| Light background | Increase lightness by 40-50%, decrease saturation by 20% | Creates a tinted background from a bold color |
| Complementary accent | Shift hue by 180 degrees | Generates the complementary color |
| Muted variant | Decrease saturation by 30-50% | Tones down a vivid color for secondary uses |
| Transparent overlay | Reduce opacity to 10-30% | Creates a color wash effect |

## Global Colors

Divi 5 provides four default global colors that serve as the foundation of the site-wide palette. Additional global colors can be created through the Global Variables Manager.

| Default Color | Description |
|---------------|-------------|
| Primary Color | Main brand color |
| Secondary Color | Supporting brand color |
| Heading Text Color | Default color for headings |
| Body Text Color | Default color for body text |

### Managing the Global Palette

1. Open the **Global Variables Manager** from the Visual Builder sidebar
2. Expand the **Colors** section
3. Edit existing global colors or add new ones
4. Changes propagate to every element referencing the modified color

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Color filter offsets are likely stored alongside the base color reference in the element's attribute data. If the base color is a global variable, the element stores a reference to the variable ID plus the HSL/opacity offsets. The exact data format needs verification.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Layout JSON inspection or global variables query | Needs Testing | Look for color values stored as base + offset objects rather than flat hex strings |
| Modify | Layout JSON update or `update_option()` for globals | Needs Testing | Modifying a base global color should cause all filtered derivatives to update |
| Create | Global Variables Manager or color picker UI | Needs Testing | Filters are applied per-field; global colors are created in the Variables Manager |


## Elegant Themes tutorials

- [Divi 5 Sizing System & Color Palette Variable Generator](https://www.elegantthemes.com/blog/theme-releases/variable-generator){:target="_blank"} — **Generate Color Palette Variables** in the Variable Manager builds a full relative palette from the primary color (April 2026).

*Maintainers:* also list new posts in [`planning/et-blog-tutorials-map.md`](https://github.com/16wells/divi-docs/blob/main/planning/et-blog-tutorials-map.md){:target="_blank"}.

## Related

- [Design Variables](design-variables.md) — Variable system that stores base color definitions
- [Global Variables](global-variables.md) — Site-wide variables including the global color palette
- [Advanced Units](advanced-units.md) — Related expression-based value system for numeric fields
