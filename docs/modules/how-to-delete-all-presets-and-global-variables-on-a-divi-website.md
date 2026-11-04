---
title: "How to Delete All Presets and Global Variables on a Divi Website"
description: "Use the Reset Divi Presets plugin to wipe Divi 5 element presets, option group presets, and global variables from a site."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/9910009-how-to-delete-all-presets-and-global-variables-on-a-divi-website"
---

# How to Delete All Presets and Global Variables on a Divi Website

Divi has no built-in "reset everything" button for presets and variables. Elegant Themes points to a small helper plugin, **Reset Divi Presets**, that adds reset actions to the WordPress admin bar.

!!! abstract "Quick Reference"
    **Tool:** The Reset Divi Presets plugin (a third-party plugin hosted on GitHub).
    **Can reset:** Element presets, option group presets, or both, plus global variables by type or all at once.
    **Warning:** Resets are permanent. Take a full backup first, and remove the plugin when finished.

!!! warning
    Deleting presets and global variables cannot be undone. Create a full site backup before you start.

## Install the plugin

1. Download the **Reset Divi Presets** zip from the link in the official article.
2. In the WordPress dashboard, go to **Plugins → Add New**.
3. Click **Upload Plugin** at the top and choose the zip.
4. Install, then activate it.

## Reset presets and variables in Divi 5

1. A new **Reset Divi Presets** item now appears in the WordPress admin bar. Hover over it.
2. Pick the action you want.

**Reset Divi 5 Presets**

- **Reset Element Presets** clears presets for elements such as Sections, Rows, and Modules. See [Element Presets](../builder/element-presets.md).
- **Reset Option Group Presets** clears only option group presets and leaves element presets alone. See [Option Group Presets](../builder/option-group-presets.md).
- **Reset All Presets** clears both.

**Reset Divi 5 Global Variables** (see [Global Variables](../builder/global-variables.md))

- **Reset Global Colors**, **Fonts**, **Images**, **Links**, **Numbers**, or **Text** each clear only that variable type.
- **Reset All Global Variables** clears every type.

## Tips

- Choose the narrowest reset that does the job; for example, reset only colors if only your palette is the problem.
- After you finish, deactivate and delete the plugin so the reset actions are not left available.
- The official article's descriptions for Reset Global Numbers and Reset Global Text repeat the wording for links; each button affects its own variable type.

## Official documentation

[How to Delete All Presets and Global Variables on a Divi Website](https://help.elegantthemes.com/en/articles/9910009-how-to-delete-all-presets-and-global-variables-on-a-divi-website)
