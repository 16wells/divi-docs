---
title: "Stacked & Nested Presets"
description: "How Divi 5 stacked presets layer several presets on one element and nested presets embed option group presets inside element presets."
category: builder
tags: [builder, presets, stacked-presets, nested-presets, design-system]
related: [option-group-presets, preset-manager, presets]
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/12817235"
---

# Stacked & Nested Presets

!!! abstract "Quick Reference"
    **What it is:** Stacking applies several presets to one element; nesting places option group presets inside an element preset.
    **Where to find it:** Stacking via the **Module Preset icon** in an element's settings; nesting inside the element preset editor.
    **Key behavior:** When stacked presets set the same option, the later one in the stack wins. Editing a preset updates every element linked to it, including through nesting.

A preset is a collection of styles for modules, columns, rows, and sections. Editing a preset updates every element using it. Presets cover structure and behavior as well as appearance, so they are more than CSS classes.

## Stacked presets

Stacking lets you layer design attributes from more than one preset on a single element. For example, a "Dark Mode" preset that turns text white can sit alongside a "Left Image" preset that aligns images left, so the element inherits both.

1. Click the section, row, column, or module to open its settings.
2. Click the **Module Preset icon**.
3. Select one or more existing presets.
4. Check the result. Order matters: Divi applies presets in the order you add them, and later presets override earlier ones for overlapping options.

## Nested presets

Nested presets place option group presets (which style a single group such as borders or title text) inside an element preset.

For example, a "Rounded Corners" option group preset with a consistent border radius can be nested in a Blurb element preset. Applying the Blurb preset applies the rounded corners too. If you later change the Rounded Corners preset, everything using it updates, even when it is nested inside other presets.

1. **Create an option group preset:** in any module's settings, style an option group (for instance Border with an 8 px radius) and save it as a preset.
2. **Nest it:** edit or create an element preset and add the option group preset in the matching group of the preset editor.
3. **Apply the element preset:** the nested option group presets come along. You can still apply the option group preset directly elsewhere.

## Combining the two

Nested presets hold a component's core rules (typography, borders, backgrounds), and stacked presets add context-specific variations on top. Because linked elements update when a preset changes, edits propagate site-wide.

## Tips

- Identify base styles (dark mode, light mode, primary button) and build presets around them; keep option group presets focused on one design property.
- If two stacked presets set the same option, such as text color, the later one takes precedence.
- Combine presets with Divi 5 design variables to adjust colors, fonts, and spacing globally.
- Try stacking and nesting on a staging site before using them on a live one.

## Official documentation

[Stacked & Nested Presets](https://help.elegantthemes.com/en/articles/12817235){:target="_blank"}
