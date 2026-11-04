---
title: "Advanced Units"
description: "Divi 5 Advanced Units — use calc(), clamp(), min(), max(), CSS keywords, and custom CSS variables in any numeric field via the unit picker."
category: builder
tags: [builder, advanced-units, css-functions, css-variables, responsive-design, design-system]
related: [design-variables, relative-colors-hsl]
divi_version: "5.x"
last_updated: 2026-04-30
source_url: "https://help.elegantthemes.com/en/articles/10823890"
---

# Advanced Units

Divi 5's advanced unit system separates values from their units in numeric fields and adds support for CSS math functions, keywords, and custom CSS variables — enabling responsive, computed values directly in the Visual Builder.

!!! abstract "Quick Reference"
    **What it does:** Separates value from unit in numeric fields, enabling CSS math functions, keywords, and custom variables.
    **Where to find it:** Unit picker on any numeric field in element settings (spacing, sizing, typography, borders, etc.).
    **Key features:**

    - CSS math functions: `calc()`, `clamp()`, `min()`, `max()`
    - CSS keywords: `auto`, `none`, `inherit`, `unset`
    - Custom CSS variables via `var(--name)` at site, page, or element scope
    - Supports px, em, rem, %, vw, vh, vmin, vmax, and angle units

    **ET Docs:** [Advanced Units](https://help.elegantthemes.com/en/articles/10823890){:target="_blank"}

## Overview

In Divi 5, every numeric field has a dedicated **Unit Picker** that splits the value input from the unit selector. This separation enables features that were previously impossible in a visual builder: you can use `calc()` to mix units, `clamp()` for responsive values, `min()` and `max()` for bounded ranges, CSS keywords like `auto` and `inherit`, and custom CSS variables defined at the site, page, or element level.

The advanced unit system works hand-in-hand with [design variables](design-variables.md). Once you define a CSS variable, it becomes available in any field that supports the unit picker.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10823890).

## Supported CSS Units

| Unit | Supported | Description |
|------|-----------|-------------|
| `px` | Yes | Absolute pixels |
| `em` | Yes | Relative to parent font size |
| `rem` | Yes | Relative to root font size |
| `%` | Yes | Percentage of parent dimension |
| `vw` | Yes | Percentage of viewport width |
| `vh` | Yes | Percentage of viewport height |
| `vmin` | Yes | Smaller of `vw` or `vh` |
| `vmax` | Yes | Larger of `vw` or `vh` |
| `grad` | Yes | Gradians (angle unit) |
| `rad` | Yes | Radians (angle unit) |
| `turn` | Yes | Full rotations (angle unit) |
| `ch` | No | Not currently supported |
| `ex` | No | Not currently supported |

## CSS Math Functions

When you enter a CSS math function into a numeric field, Divi disables the arrow incrementer and scrubber since computed values cannot be adjusted by simple increment/decrement.

| Function | Description |
|----------|-------------|
| `calc()` | Perform arithmetic with mixed units (e.g., `calc(100% - 40px)`) |
| `clamp()` | Define a minimum, preferred, and maximum value (e.g., `clamp(1rem, 2.5vw, 3rem)`) |
| `min()` | Resolve to the smallest of the provided values |
| `max()` | Resolve to the largest of the provided values |

## CSS Keywords

Divi 5 supports CSS keywords in numeric fields. When a keyword is assigned, the unit indicator displays an em dash instead of a unit abbreviation.

| Keyword | Description |
|---------|-------------|
| `auto` | Let the browser determine the value |
| `none` | Remove a property (e.g., `max-width: none`) |
| `inherit` | Inherit the value from the parent element |
| `unset` | Reset to the inherited value or initial value depending on context |

## CSS Variables

Custom CSS properties (variables) can be used in any field that supports the unit picker. Variables are defined using standard CSS `--variable-name` syntax at three levels:

| Scope | Definition Location | Description |
|-------|---------------------|-------------|
| Site-wide | Theme Options > Custom CSS | Available on every page and template |
| Page-specific | Page Settings > Advanced > Custom CSS | Available only on the current page |
| Element-specific | Element Settings > Advanced > Free Form CSS | Scoped to the element and its children |

Once defined, variables are entered into value fields using `var(--variable-name)` syntax.

## Unit Picker Behavior

| Behavior | Description |
|----------|-------------|
| Default units | Applied automatically when possible based on the field type |
| Unit switching | Changing from a math function or keyword to a standard unit clears the field |
| Em dash display | Shown as the unit indicator when no unit is defined or a keyword is active |
| Field layout changes | Spacing fields use a 2x2 grid; border radius fields stack above and below the preview; transform fields show the preview below with range sliders removed |

## AI Interaction Notes

!!! info "Data Storage — Needs Testing"
    Advanced unit values are stored directly in the element's attribute data within the layout JSON. CSS variables defined in Theme Options Custom CSS are stored in the Divi theme options. Page-level and element-level custom CSS is stored in the respective post meta or element attributes.

**Programmatic access:**

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read | Layout JSON inspection or `get_post_meta()` | Needs Testing | Numeric values with functions are stored as strings in the element attributes |
| Modify | Layout JSON update or `update_post_meta()` | Needs Testing | Must preserve the full function syntax (e.g., the entire `clamp()` expression) |
| Create | Custom CSS injection via Theme Options or page/element CSS fields | Needs Testing | CSS variables must be defined before they can be referenced in value fields |


## Elegant Themes tutorials

- [Divi 5 Sizing System & Color Palette Variable Generator](https://www.elegantthemes.com/blog/theme-releases/variable-generator){:target="_blank"} — How Divi’s **Generate Fluid Sizing Variables** flow produces `clamp()`-based number variables for spacing, type, gaps, radius, and more (April 2026).

*Maintainers:* also list new posts in [`planning/et-blog-tutorials-map.md`](https://github.com/16wells/divi-docs/blob/main/planning/et-blog-tutorials-map.md){:target="_blank"}.

## Related

- [Design Variables](design-variables.md) — Divi's built-in variable system (distinct from raw CSS variables)
- [Relative Colors (HSL)](relative-colors-hsl.md) — HSL color functions that use similar expression syntax
- [Global Variables](global-variables.md) — Site-wide variables that can include numeric values with units
