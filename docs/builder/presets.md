---
title: "Divi Presets"
description: "Overview of Divi 5 element presets: creating, applying, editing, defaulting, stacking, and nesting reusable module styles."
category: builder
tags: [builder, presets, global-styles, design-system]
related: [visual-builder, global-elements, library]
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/13349150"
---

# Divi Presets

!!! abstract "Quick Reference"
    **What it is:** An Element Preset saves a module's design so it can be reused on any element of the same type and updated in one place.
    **Where to find it:** The Preset icon next to the element name at the top of its settings panel.
    **Key behavior:** Each element type has its own preset list, and each type can have one default preset that new elements start with.

Element Presets are part of Divi 5's preset-based design system, alongside Default Presets, Option Group Presets, and Design Variables.

## Where presets live

Open the settings of any element (section, row, column, or module) and use the Preset dropdown. From it you can apply a preset, create one from the element's current styles, edit one, or set a default with the star icon. Button presets apply only to buttons, blurb presets only to blurbs, and so on.

## What a preset holds

A preset stores the modified settings for that element type: colors and typography, spacing and alignment, borders, shadows and effects, and interactions, hover states, and responsive adjustments. Applying it to another element of the same type copies those settings, and editing the preset updates all elements using it. Presets can use [Design Variables](design-variables.md) and can include [Option Group Presets](option-group-presets.md).

## Create a preset

**From scratch**

1. Add the module (for example a Button).
2. Open the **Preset dropdown** and click **Add New Preset**.
3. In **Content tab → Preset Settings → Preset name**, enter a descriptive name.
4. Style it in the Design tab.
5. Click **Save Preset**.

**From existing styles**

1. Style the module in the Design tab.
2. Open the Preset dropdown and choose **New Preset From Current Styles**.
3. Name it (for example "Primary Button") and click **Save Preset**.

## Default presets

Every element type has a Default Preset that new elements use. Click the star icon on a preset to set it. Editing the default updates every element using it. A simple baseline: a neutral Section preset, a Row preset with your usual grid spacing, and defaults for Text, Heading, Button, Image, and Blurb.

## Stacked presets

[Stacked presets](stacked-nested-presets.md) apply several element presets to one element. Divi combines their styles, and when two define the same property the last one applied wins, as in CSS. Examples: a base Row preset plus a second preset that changes padding, or a Column preset plus a "Background / Dark" preset.

## Nested presets

Nested presets put Option Group Presets inside an element preset, keeping them linked.

1. Open a module that uses the preset to edit.
2. In the preset dropdown, hover over the preset and click the gear icon.
3. In the preset editor, go to a group such as Spacing, Borders, or Shadows.
4. Apply existing Option Group Presets instead of manual styles.
5. Save the preset.

Editing an option group preset later updates every element preset using it, and every element using those presets.

Nesting defines a component's core rules (such as a card's spacing, corners, and shadow); stacking adds variations (light vs. dark, hero vs. compact).

## Edit and maintain presets

To edit globally: open a module using the preset, open the Preset dropdown, hover over the preset name, click the gear icon, adjust styles, and click **Save Preset**. To change the default, click the star icon on the chosen preset. To opt a single module out, uncheck any selected element preset in its dropdown.

## Suggested workflow

1. Define Global Variables for colors, fonts, and spacing.
2. Create one clean base preset per core element and set the most-used as defaults.
3. Turn repeated design decisions into Option Group Presets.
4. Nest those into your Module Presets.
5. Stack one or two variation presets for special cases.

## Examples

- **Button system:** a base Button preset, Option Group Presets for text, spacing, and border, and stacked "Hero" or "Ghost" variations.
- **Card grid:** Row and Column presets with nested padding, radius, and shadow presets, plus "Dark" and "Compact" stacked variations.
- **Typography:** base Text and Heading presets, typography Option Group Presets for H1, H2, and Body, reused in other modules.

## Official documentation

[Element Presets in Divi 5](https://help.elegantthemes.com/en/articles/13349150){:target="_blank"}
