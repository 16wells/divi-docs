---
title: "Gradient Builder"
description: "Divi 5 Gradient Builder — Gradient Picker, gradient variables, background and text gradient fills, with copy/paste and find/replace support."
category: builder
tags: ["builder", "gradients", "design", "backgrounds", "text-effects", "variables"]
related: ["visual-builder", "presets", "global-variables", "copy-paste-attributes"]
divi_version: "5.7+"
last_updated: 2026-11-04
source_url: "https://www.elegantthemes.com/documentation/divi/gradient-builder"
---

# Gradient Builder

How to add, edit, and reuse gradients throughout your Divi designs — as backgrounds, text fills, and site-wide variables.

!!! abstract "Quick Reference"
    **What it does:** Creates CSS gradients with multiple color stops for backgrounds, text fills, and other design fields.
    **Where to find it:** Any gradient field opens the **Gradient Picker** panel — same UI in Background settings, typography groups, and the Variable Manager.
    **Key features:**

    - **Gradient field type** — one unified attribute you can copy, paste, extend, inspect, and find/replace as a whole
    - **Gradient Picker panel** — consolidated editor (like the color picker) with stops, type, direction, and variables in one place
    - **Gradient variables** — save any gradient in the Variable Manager and reuse it site-wide
    - Linear, Circular (radial), Elliptical, and Conical types, repeating patterns, and background-image layering
    - **Text gradient fills** — apply gradients (including gradient variables) to text in any typography option group

    **ET Docs:** [Gradient Builder](https://www.elegantthemes.com/documentation/divi/gradient-builder){:target="_blank"}

Gradients add depth and visual interest across backgrounds, overlays, and typography. In Divi 5.7, gradient controls were consolidated into a single **Gradient Picker** panel and a new **gradient field type**, so you interact with a gradient as one attribute instead of editing each internal stop and setting separately.

The Gradient Builder is still part of Divi's background design options, but gradients now also appear in **all typography option groups** (Text, Title Text, Heading Text, and related font groups) for gradient text fills. You can manage reusable gradients as **gradient variables** in the [Variable Manager](global-variables.md).

## Gradient Picker Panel

All gradient editing in Divi 5.7 flows through the **Gradient Picker** — a dedicated panel modeled after the color picker. Whether you open a background gradient, a text gradient fill, or a gradient variable in the Variable Manager, you get the same interface and the same controls.

The picker provides:

- Gradient type (Linear, Circular, Elliptical, or Conical), angle, and position
- A visual stop bar for adding, reordering, and positioning color stops
- Access to **gradient variables** and color variables from the same panel
- Consistent behavior across every context where gradients are supported

## Gradient Field Type

Gradients are stored as a **single field value** rather than a collection of separate sub-settings. That unified field type unlocks the same attribute workflows Divi already provides for colors and other design values:

| Workflow | How it applies to gradients |
|----------|----------------------------|
| [Copy & Paste Attributes](copy-paste-attributes.md) | Copy a gradient from one field and paste it onto another compatible gradient field |
| [Extend Attributes](extend-attributes.md) | Propagate a gradient from one element to matching elements in a scope |
| [Find & Replace Attributes](find-replace-attributes.md) | Swap one gradient for another across a module, section, or page |
| [Style Inspector](style-inspector.md) | Inspect which elements use a gradient and edit it inline |

You no longer need to manually recreate stop positions and colors when moving a gradient between elements.

## Gradient Variables

**Gradient variables** are a dedicated variable type in the [Variable Manager](global-variables.md). Any gradient you build in the Gradient Picker can be saved as a variable and referenced anywhere a gradient field accepts dynamic content.

When you edit a gradient variable, every field that references it updates across the site — backgrounds, text gradient fills, and any other gradient-enabled control. This pairs naturally with [presets](presets.md): define gradient variables once, use them inside option group presets and element presets, then apply those presets to pages.

### Creating a gradient variable

1. Open the **Variable Manager** from the Visual Builder toolbar.
2. Select the **Gradients** category and choose **Add Global Gradient** (or right-click an existing gradient field and choose **Convert to Variable**).
3. Build the gradient in the Gradient Picker panel.
4. Name the variable and click **Save Variables**.

### Applying a gradient variable

1. Open any element setting that exposes a gradient field (background gradient, text gradient fill, etc.).
2. Open the Gradient Picker for that field.
3. Choose an existing gradient variable, or click the dynamic content icon to bind the field to a variable.

<!-- ![Gradient Builder overview](../assets/screenshots/builder/gradient-builder/overview.png){ loading=lazy }
*The Gradient Picker panel in Divi 5.7.* -->

## Adding a Background Gradient

To add a gradient to any section, row, column, or module:

1. Open the element's settings.
2. Navigate to the **Content** tab > **Background** option group.
3. Click the **Gradient** tab (next to Solid Color, Image, Video, and Pattern).
4. Open the **Gradient Picker** for the background gradient field.
5. Click **+ Add Gradient Stop** (or the equivalent control in the picker) to add your first color stop.
6. Choose a color or color variable for the stop and adjust its position along the gradient bar.
7. Add a second color stop (at minimum, two stops are needed for a gradient).
8. Adjust the gradient type, direction, and other settings described below.

## Text Gradient Fills

Divi 5.7 extends gradients to **all typography option groups**. In the Design tab, open any text-related group (Text, Title Text, Heading Text, Body Text, or module-specific font groups) and look for **gradient fill** and **image fill** settings alongside the standard text color control.

- **Gradient fill** — opens the same Gradient Picker; supports gradient variables for brand-consistent headline treatments.
- **Image fill** — fills glyph shapes with a background image instead of a solid or gradient color.
- **Text stroke** — outlines letterforms for contrast on busy backgrounds.

See [Text Options](../options-groups/text.md) for the shared typography settings reference. The [Heading](../modules/heading.md) and [Text](../modules/text.md) modules are common starting points for gradient headline effects.

## Gradient Settings Reference

| Setting | Description | Default |
|---------|-------------|---------|
| **Gradient Type** | Linear, Circular (Divi's label for radial), Elliptical, or Conical. | Linear |
| **Direction / Angle** | For Linear and Conical gradients, the angle in degrees (0--360) that controls the gradient line direction. | 180 deg (top to bottom) |
| **Radial Position** | For Circular and Elliptical gradients, where the gradient originates (Center, Top Left, Bottom Right, etc.). | Center |
| **Start Position** | Where the first color stop begins, as a percentage of the element. | 0% |
| **End Position** | Where the last color stop ends, as a percentage of the element. | 100% |
| **Color Stops** | Individual colors placed at specific positions along the gradient. Each stop has a color value and a position (%). | -- |
| **Repeat** | Whether the gradient pattern repeats. See Repeating Gradients below. | Off |
| **Place Above Background Image** | Layer the gradient on top of any background image. | Off |

## Divi Gradient Builder Types

### Linear Gradients

Linear gradients transition between colors along a straight line. The **angle** setting controls the direction of the line:

| Angle | Direction |
|-------|-----------|
| 0 deg | Bottom to top |
| 90 deg | Left to right |
| 180 deg | Top to bottom (default) |
| 270 deg | Right to left |

Any angle between 0 and 360 is supported for diagonal gradients.

### Radial Gradients

Radial gradients transition outward from a central point in a circular or elliptical shape. Use the **radial position** setting to place the center of the gradient at a specific location within the element (center, top-left corner, bottom-right, etc.).

## Repeating Gradients With the Divi Gradient Builder

When the **Repeat** option is enabled, the gradient pattern tiles itself across the element. This creates striped or banded effects. The size of each band is determined by the distance between your color stops. Tighter stop spacing produces thinner, more frequent bands.

Repeating gradients work with both linear and radial types:

- **Repeating linear** produces parallel stripes.
- **Repeating radial** produces concentric rings.

## Repeating Patterns and Interesting Effects

Combine repeating gradients with Divi's **Pattern** background overlay for complex visual effects. A few techniques:

- **Diagonal stripes**: Set a repeating linear gradient at 45 degrees with two alternating color stops spaced 10--20 px apart.
- **Target circles**: Use a repeating radial gradient with sharp color transitions (e.g., transparent-to-color at the same percentage) to create concentric rings.
- **Gradient + pattern overlay**: Place a semi-transparent gradient above a pattern background to tint the pattern with a color wash.

## Divi Gradient Builder Units

Gradient stop positions can be set using several CSS length units:

| Unit | Description |
|------|-------------|
| **%** | Percentage of the element's dimension (most common). |
| **px** | Fixed pixel values. |
| **em** | Relative to the element's font size. |
| **vw / vh** | Relative to the viewport width or height. |

Percentage is the most portable unit since it scales with the element size. Use fixed pixel values when you need precise, non-scaling stop positions.

## Best Practices for Using the Divi Gradient Builder

- **Start with two stops.** Begin with a simple two-color gradient and add complexity only as needed.
- **Use gradient variables for reuse.** Save frequently used gradients as variables instead of rebuilding stops on every element.
- **Use color variables in stops.** Reference global color variables in gradient stops so palette changes propagate into gradients automatically.
- **Mind contrast.** Ensure text placed over a gradient background has sufficient contrast at every point of the gradient, not just the start or end color.
- **Layer gradients over images.** Use the "Place Above Background Image" option to add a gradient overlay that improves text readability on photo backgrounds.
- **Save as presets.** If you create a gradient you reuse frequently, save the element as a [preset](presets.md) so you can apply the same gradient to other elements instantly.

## Elegant Themes tutorials

- [New Gradient Editor, Gradient Variables, Text Effects and More](https://www.elegantthemes.com/blog/theme-releases/new-gradient-editor-gradient-variables-text-effects-and-more){:target="_blank"} — Divi 5.7 theme release: Gradient Picker, gradient field type, gradient variables, and text gradient/image fills with strokes (June 2026).

*Maintainers:* also list new posts in [`planning/et-blog-tutorials-map.md`](https://github.com/16wells/divi-docs/blob/main/planning/et-blog-tutorials-map.md){:target="_blank"}.

## Version Notes

!!! note "Divi 5.7 — Gradient Picker and Variables"
    The unified Gradient Picker panel, gradient field type, gradient variables, and native text gradient/image fills with strokes shipped in Divi 5.7 (June 2026). Earlier Divi 5 builds used per-attribute gradient stops without the consolidated picker or gradient variable type.

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Related

- [Global Variables](global-variables.md) — Gradient variables in the Variable Manager
- [Text Options](../options-groups/text.md) — Text gradient fills, image fills, and strokes
- [Background Options](../options-groups/background.md) — Background gradient tab
- [Copy & Paste Attributes](copy-paste-attributes.md) — Transfer whole gradients between fields
- [Find & Replace Attributes](find-replace-attributes.md) — Bulk gradient swaps
- [Extend Attributes](extend-attributes.md) — Propagate a gradient across elements
- [Style Inspector](style-inspector.md) — Audit gradients used on a page
- [Visual Builder](visual-builder.md)
- [Presets](presets.md)
