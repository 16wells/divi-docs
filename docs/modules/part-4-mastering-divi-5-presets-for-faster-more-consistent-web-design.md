---
title: "Part 4: Mastering Divi 5 Presets For Faster, More Consistent Web Design"
description: "Part 4 of the Divi 5 Mastery Course: build a preset system from Design Variables using the Preset Manager, Option Group Presets, Element Presets, stacking, and nesting."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15530394-part-4-mastering-divi-5-presets-for-faster-more-consistent-web-design"
---

# Part 4: Mastering Divi 5 Presets For Faster, More Consistent Web Design

!!! abstract "Quick Reference"
    **Goal:** Turn the Design Variables from Part 3 into a reusable preset system before building the homepage in Part 5.
    **Hierarchy:** Design Variables (base) > Option Group Presets (one option group) > Element Presets (a full element) > pages and Theme Builder templates.
    **Where to manage:** The Preset Manager icon in the Visual Builder's left sidebar.
    **Course position:** Part 4 of 16. Previous: Part 3 (Design Variables). Next: Part 5 (homepage).

!!! tip "Divi AI Agent"
    With a Divi AI subscription, the Divi AI Agent can find a repeated combination of settings (for example a border plus shadow on several modules), turn it into an Option Group Preset, and apply it to every module that already matches. It stops for approval before anything destructive.

## Why build presets now

- Applying a full set of styles takes a few clicks instead of adjusting typography, spacing, colors, and borders on every module.
- Styling stays consistent across the homepage, inner pages, and templates.
- Changing a color, spacing value, or button style in one preset updates it everywhere the preset is used.

## The Preset Manager

Open a page in the Visual Builder and click the **Preset Manager** icon in the left sidebar. From here you create, organize, edit, duplicate, reorder, and set default presets. Presets are grouped by type:

- **Element Presets** belong to an element such as Heading, Blurb, or Call to Action.
- **Option Group Presets** belong to an option group such as Background, Heading, or Text.

Expand an element's menu to see its presets. A preset applied to a module appears beside the module title in the settings panel.

To edit one, click its pencil icon to open the **Preset Preview**, adjust it, and save. Saved changes apply everywhere the preset is used.

## Create Option Group Presets

An Option Group Preset saves the styling for one option group and applies wherever that group appears. Create these before Element Presets.

Example, a Heading Text preset:

1. Open the Heading module's settings and go to **Design tab > Heading Text**.
2. Hover over the group title and click the **Option Group Preset** icon.
3. Click **New Preset From Current Styles** (if you already styled it) or **Add New Preset** (to start blank).
4. Give it a descriptive title and make your changes.
5. Click **Save Preset**.

Start with the groups used most:

- **Typography:** style Heading Text and Body Text with the Part 3 font and fluid number variables.
- **Spacing:** keeps rhythm consistent across sections, rows, columns, groups, and modules.
- **Border:** apply your border width and rounded-corner variables for a unified look.
- **Buttons:** buttons live inside many modules, so add a module with a button (such as Email Optin), style its Button group with your variables, and save it as an Option Group Preset.

### Core Option Group Presets used in the course

| Option group | Presets |
|---|---|
| Border | Top Border, Outlined - Dark, Rounded - Regular, Bottom Border |
| Spacing | Padding - Medium, Padding - Large |
| Font Body | Dark Text, Small Text |
| Buttons (inside other modules) | Filled - Primary Color, Filled - Black, Filled - White, Text - Primary Color, Text - White |
| Heading Text | Heading 1 through Heading 6 (each tied to its H1 to H6 variable) |
| Body Text | Dark Text, Small Text |
| Background | Background - Light Gray |

The official article lists the exact variables and values behind each preset; use that table as your build checklist.

## Create Element Presets

An Element Preset saves the full design of one element type (Button, Blurb, Image, Section, Row, Column, or Group). It can nest Option Group Presets, so updating a nested group flows through every Element Preset that uses it. For example, a Blurb preset can nest title typography, body text, spacing, background, and border presets.

Key Element Presets to build:

1. **Primary Button:** your button Option Group Preset plus any extra styling.
2. **Email Opt-In:** the button preset with title typography, description text, and field styling.
3. **Module Group:** a Group module with related modules inside, saved as a reusable container for feature, pricing, or testimonial cards.

### Core Element Presets used in the course

| Module | Presets |
|---|---|
| Heading | Heading 1 - Big, Heading 1 through Heading 6 |
| Text | Dark Text, Light Text, Small Text |
| Button | Filled - Primary Color, Text - Primary Color, Filled - Black, Filled - White |
| Image / Video | Rounded |
| Icon | Dark - Small - Contained, Dark - Small |
| Icon List | Light Text |
| Blurb | Dark Text, Dense |
| Group | Contained - Light, Contained - Dark |
| Countdown Timer | Light Text |
| Accordion | Dark Text |
| Menu | Dark Text |
| Social Media Follow | Isolated Icons - Dark, Isolated Icons - Light |
| Social Network | No Background |

## Stack and nest presets

You can stack several presets on one element, each handling a different job. With a Blurb:

1. Click the preset icon next to the module header and choose a first preset.
2. Click the applied preset to open its options and select a second one.

Divi 5 applies both. When an underlying preset changes, every module using it updates.

## Best practices

- **Preview before saving.** The pencil icon opens a preview where you can test against sample content and background colors. Saved changes are global.
- **Set defaults.** Select the applied preset in the module header and click the star icon so new modules of that type start with it.
- **Name clearly.** Use role-based names for reusable design decisions and component-based names for complete Element Presets.
- **Export your library.** Export as a backup or to reuse on other sites. Make sure any Design Variables a preset references already exist before importing.

## Import the ready-made presets

1. Download the JSON file from the official article.
2. Open any page in the Visual Builder and click the Preset Manager icon.
3. Click the **Import/Export** icon.
4. Choose the JSON file.

## Official documentation

[Part 4: Mastering Divi 5 Presets For Faster, More Consistent Web Design](https://help.elegantthemes.com/en/articles/15530394-part-4-mastering-divi-5-presets-for-faster-more-consistent-web-design)
