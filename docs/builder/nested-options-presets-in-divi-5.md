---
title: "Nested Options Presets in Divi 5"
description: "How Divi 5 lets you apply presets to sub-options and nest option presets inside other option presets, so one change propagates through every layer."
category: builder
tags: [builder, presets, nested-presets, design-system]
related: [option-group-presets, element-presets, stacked-nested-presets, composable-settings-in-divi-5]
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14734094-nested-options-presets-in-divi-5"
---

# Nested Options Presets in Divi 5

!!! abstract "Quick Reference"
    **What it is:** An extension of Divi 5 presets that works on sub-options (such as the Border inside a Button group) and lets one option preset live inside another.
    **How to use it:** Hover a nested option in the Design tab, click its **Preset icon**, and pick or create a preset.
    **Key behavior:** Edit an inner preset and every preset that nests it, and every element using those presets, updates.
    **Availability:** Divi 5 only.

## What it adds

Divi 5 already had element presets and option group presets. Nested Options Presets add two things:

- **Presets on sub-options.** Sub-options inside an option group (for example Call To Action > Button > Border) now accept presets. Before, presets applied only to whole elements or top-level option groups.
- **Option presets inside option presets.** An option preset can contain another option preset, adding a third layer of nesting beneath element and option group presets.

The payoff is reuse: one Border preset can sit inside a Button preset, inside a Call To Action preset, and directly on an Image module. Change it once and every use follows.

## Where it fits in the preset system

| Preset type | What it does |
|---|---|
| Element presets | Apply a set of styles to one element type, such as a Blurb. |
| Option group presets | Style a single option group (Border, Button) across any module that has it. See [Option Group Presets](option-group-presets.md). |
| Stacked presets | Apply several presets to the same element or group at once. See [Stacked and Nested Presets](stacked-nested-presets.md). |
| Nested presets (element level) | Nest an option preset inside an element preset; covered in the stacked and nested article. |
| Nested options presets | This feature: presets on sub-options, and presets inside other option presets. |

It also works with [Composable Settings](composable-settings-in-divi-5.md): any sub-element you enable there can have its own option preset.

## Apply a preset to a nested option

1. Open the Visual Builder and click a module to open its settings.
2. Go to the **Design** tab.
3. Expand an option group that has sub-options, such as **Button**.
4. Hover the nested option (for example **Border**) and click the **Preset icon**.
5. Choose an existing option preset, or click **Add New Preset**.
6. Set the styles and click **Save Preset**.

The same preset can then be reused on any matching nested option across the site.

## Nest one option preset inside another

1. Create a standalone option preset first, for example a **Border** preset with your default border style.
2. Open a module's settings, hover the option group to edit (such as **Button**), click the **Preset icon**, and open an existing Button preset for editing or create one.
3. In the preset editor, expand the nested option (for example **Border**).
4. Click that nested option's **Preset icon** and pick the Border preset from step 1.
5. Click **Save Preset**.

The Button preset now holds the Border preset as a reference. Any change to the Border preset flows into every Button preset that nests it, and into every element using those Button presets.

## Worked example

Goal: two element presets, **Dark Blurb** and **Light Blurb**, sharing one button style and one pill-shaped border.

1. Create a **Pill Border** option preset with a high border radius.
2. Create a **Solid Button** option group preset and nest **Pill Border** on its **Border** sub-option.
3. Create the **Dark Blurb** and **Light Blurb** element presets, and nest **Solid Button** inside each.

Every button inherits the Solid Button style and every button border inherits Pill Border. Changing the radius on Pill Border updates every button, whichever blurb preset it sits in.

## FAQ

- **How is this different from the nested presets in Stacked and Nested Presets?** That feature nests an option preset inside an element preset. This one adds option presets inside other option presets, plus presets on sub-options that could not take them before.
- **Is Composable Settings required?** No, not for sub-options that already existed. Sub-elements you enable through Composable Settings gain preset support too.
- **What happens when I change a nested preset?** Every preset that nests it updates, and so does every element using those presets. Changes pass through all layers.
- **Can I override a nested preset on one element?** Yes. Static styles set directly on an element override preset values, as before.
- **Does it work in Divi 4?** No. It is exclusive to Divi 5.

## Official documentation

- [Nested Options Presets in Divi 5](https://help.elegantthemes.com/en/articles/14734094-nested-options-presets-in-divi-5){:target="_blank"}
