---
title: "Variable Generator in Divi 5"
category: builder
tags: ["builder", "variables", "design-system", "fluid-typography", "color-palette", "global-variables"]
related: ["global-variables", "design-variables", "relative-colors-hsl", "advanced-css-units"]
divi_version: "5.4+"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14851749-variable-generator-in-divi-5"
---

# Variable Generator in Divi 5

The Variable Generator in Divi 5 lets you build a complete sizing system and a complete color palette automatically, without writing a single line of CSS.

## Overview

You launch it from the **Variable Manager** inside the Visual Builder, choose what you want to generate, and Divi creates a set of reusable Global Variables that update everywhere on your site.

This article explains what the Variable Generator does, where to find it, and how to use both of its modes: the **Color Palette Generator** for building a **relative color system**, and the **Fluid Sizing Variable Generator** for building responsive sizing scales like font sizes, spacing, gaps, and more.

![Variable Manager open in the Visual Builder with both generator buttons visible.](../assets/screenshots/builder/variable-generator/overview.png){ loading=lazy }

## What the Variable Generator Does

Most design systems share two foundations: a set of brand colors that work together, and a set of sizing values (font sizes, spacing, radius, etc.) that scale consistently across screen sizes. Building those by hand takes time, and getting the math right (especially for fluid typography) requires an advanced understanding of how `clamp()` math function works.

The Variable Generator does that work for you. It produces:

- **A relative color palette** built from a primary color, with light-to-dark shades and transparent variants that all update together when you adjust the primary.
- **A fluid sizing scale** built with `clamp()`, so values smoothly resize between a minimum and maximum as the viewport (the visible width of the browser) changes.
- **A fixed responsive scale** that outputs separate values per breakpoint (Phone, Tablet, Desktop, etc.).
- **A fixed single scale** that outputs one value across all screen sizes.

Whichever you generate, the output becomes a set of Global Variables in the **Variable Manager**. From there, every variable plugs straight into your design system.

## Where to Find the Variable Generator

![Variable Manager with generator buttons highlighted.](../assets/screenshots/builder/variable-generator/manager-location.png){ loading=lazy }

The Variable Generator lives inside the **Variable Manager**.

1. Open any page in the **Visual Builder**.
2. In the left sidebar, click the **Variable Manager** icon.
3. Hover over the **Colors** group to reveal the **Generate Color Palette Variables** button, or hover over the **Numbers** group to reveal the **Generate Fluid Sizing Variables** button.
4. Click the button for the generator you want to use.

The generator opens in a full-screen modal with a configuration sidebar on the left and a live preview area on the right.

## Using the Color Palette Generator

![Color Palette Generator interface with settings and preview.](../assets/screenshots/builder/variable-generator/color-palette-generator.png){ loading=lazy }

The Color Palette Generator builds a complete color system from a single primary color. It uses Divi's relative color system (a way of defining colors as variations of another color using HSL math) to create shades that stay mathematically linked.

### Generate a Color Palette

1. In the **Variable Manager**, hover over the **Colors** group and click **Generate Color Palette Variables**.
2. Set your **primary color**. Divi uses this as the foundation for the entire palette.
3. Adjust the relationship to your **secondary color** (for example, complementary or analogous).
4. Choose how many shades you want for each color.
5. Click **Add Variables To My Site** to save the palette to your Variable Manager.

### What the Color Palette Generator Produces

The generator updates the four base color slots in your Variable Manager (**Primary**, **Secondary**, **Heading Text**, **Body Text**, and **Link**) and creates a spectrum of light-to-dark shades and transparent versions of those base colors.

Because every shade is defined relative to the primary color, changing the primary later updates every linked shade automatically. You only have to maintain one source color, and the rest of your palette follows.

## Using the Fluid Sizing Variable Generator

![Fluid Sizing Generator interface with token family options.](../assets/screenshots/builder/variable-generator/fluid-sizing-generator.png){ loading=lazy }

The **Fluid Sizing Variable Generator** builds a scale of related size values, like font sizes that step from small to large, or spacing tokens that step from tight to roomy.

You can generate scales for several different design properties (called token families) and pick how those values should respond to different screen sizes.

### Step 1: Open the Generator and Pick a Token Family

![Generator sidebar showing token family options.](../assets/screenshots/builder/variable-generator/token-families.png){ loading=lazy }

1. In the **Variable Manager**, hover over the **Numbers** group and click **Generate Fluid Sizing Variables**.
2. From the **Number variable type** dropdown in the sidebar, choose what you want to generate. The available token families are:

| Token Family | Purpose |
|---|---|
| **Font Size Scale** | Typography sizing |
| **Spacing scale** | Padding and margin values |
| **Gap scale** | Space between flex and grid items |
| **Radius scale** | Border radius values |
| **Border width scale** | Border thickness |
| **Width scale** | Element widths |
| **Clamp (generic)** | Any single fluid value |
| **Size (generic)** | Any single fixed value |

Divi sets sensible defaults for each token family, so beginners can stop here and skip straight to step 4.

### Step 2: Choose a Scale Type

Each token family supports up to three scale types. Pick one based on how you want the values to respond to screen size.

| Scale Type | Behavior | Use Case |
|---|---|---|
| **Fluid** | Uses `clamp()` to smoothly interpolate between min and max as viewport resizes | Modern responsive typography and spacing without breakpoints |
| **Fixed Responsive** | Outputs one value per enabled breakpoint (Phone, Tablet, Desktop, etc.) | Explicit control at each screen size |
| **Fixed Single** | Outputs one value across all screen sizes | Tokens that should not respond to screen size |

### Step 3 (Optional): Customize the Scale

![Scale customization options and live preview.](../assets/screenshots/builder/variable-generator/customize-scale.png){ loading=lazy }

If you want to tune the defaults, the sidebar exposes every aspect of the scale.

| Setting | Description |
|---|---|
| **Variable prefix** | Sets the name prefix for every variable in the scale (for example, `text-` produces `--text-s`, `--text-m`, `--text-l`) |
| **Generated CSS units** | Choose `rem` or `px` for the output |
| **Suffix style** | Switch between t-shirt names (xs, s, m, l, xl) and numeric names (1, 2, 3, 4, 5) |
| **Base size** | Sets which step in the scale is the baseline value |
| **Min. base** and **Max. base** | Define the size of that baseline at the smallest and largest viewport widths (fluid mode only) |
| **Min. ratio** and **Max. ratio** | Control how aggressively each step grows or shrinks. Divi includes preset ratios like 1.125 (Major Second), 1.25 (Major Third), and 1.618 (Golden Ratio), or you can enter a custom ratio or linear step |

You can also toggle special tokens like `gap-0`, `space-0`, `border-none`, `radius-none`, `radius-full`, and `width-full`, which are common values that sit outside the modular scale.

### Step 4: Preview and Add to Your Site

![Results table showing all generated variables with visual previews.](../assets/screenshots/builder/variable-generator/results-preview.png){ loading=lazy }

The right side of the generator shows a live results table with every variable in the scale, the computed values, and a visual preview of how each one will look in practice.

Typography previews show sample text, spacing previews show padded boxes, gap previews show flex rows, and so on.

A few useful controls in the results header:

- **Customize Values** lets you rename individual variables and override specific values without losing the rest of the scale.
- **Show CSS** displays the generated CSS for each variable.
- **Close Sidebar** hides the configuration panel so you can preview the scale at full width.

For fluid scales, a **Resize your browser to preview fluid values** section appears below the table. Drag your browser window narrower or wider to see the values respond in real time.

When you are ready, click **Add Variables To My Site**. If a prefix already exists in your Variable Manager, Divi will ask you to confirm before overriding the previous variables.

## How the Variable Generator Fits with Presets

The Variable Generator only creates Global Variables. To turn those variables into reusable styles, you combine them with the two preset systems in Divi 5.

- **Element Presets** control the default design for an entire module type (every Button, every Heading, every Blurb).
- **Option Group Presets** control specific groups of settings inside a module (for example, the Border group on a Button).
- **Global Variables** (created by the Variable Generator) hold the actual reusable values your presets reference.

A typical workflow looks like this:

1. Use the Variable Generator to create your sizing scale and color palette.
2. Build Option Group Presets that reference those variables for spacing, typography, borders, and color.
3. Stack those Option Group Presets inside Element Presets so each module type pulls from your generated variables by default.
4. When you build pages, drop in modules and let them inherit from the presets.

The result is a layered system: change a generated variable to adjust the raw value, change a preset to adjust how that value gets used, and only override on a single module when you need a one-off.

## Frequently Asked Questions

**Will the generator overwrite my existing variables?**

Only if you tell it to. If a prefix you are generating already exists in your Variable Manager, Divi prompts you to confirm before replacing the previous variables.

**Can I edit values after I add them to my site?**

Yes. Once added, the variables become regular Global Variables. Open the Variable Manager and edit them like any other variable.

**Why does the preview show px values when my unit is set to rem?**

The preview always displays sizes in px for readability. The generated CSS still uses your chosen unit (`rem` or `px`).

**What is the difference between Fluid and Fixed Responsive?**

Fluid outputs one `clamp()` value per token that scales smoothly between a minimum and maximum as the viewport resizes. Fixed Responsive outputs separate values per breakpoint, giving you explicit control at each screen size.

**Can I add more variables to a scale after I generate it?**

Yes. Use the **+ Add smaller variable** and **+ Add larger variable** buttons in the results table to extend the scale before you add it to your site.

## Code Examples

### Using Generated Fluid Sizing Variables

```css
/* Example: Using generated fluid sizing variables in custom CSS */
.my-heading {
    font-size: var(--text-xl);
    margin-bottom: var(--space-m);
}

.my-card {
    padding: var(--space-l);
    border-radius: var(--radius-m);
    gap: var(--gap-s);
}

.my-container {
    width: 100%;
    max-width: var(--width-lg);
    margin: 0 auto;
}
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Related

- [Global Variables](global-variables.md)
- [Design Variables](design-variables.md)
- [Relative Colors & HSL](relative-colors-hsl.md)
- [Advanced CSS Units](../css-reference/advanced-css-units.md)
