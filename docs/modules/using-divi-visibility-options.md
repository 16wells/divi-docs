---
title: "Using Divi Visibility Options"
description: "Hide sections, rows, columns, and modules on chosen device breakpoints in Divi 5 and control horizontal and vertical overflow."
category: modules
tags: [modules, options, responsive]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/13722487"
---

# Using Divi Visibility Options

!!! abstract "Quick Reference"
    **What it is:** The Visibility option group, which hides an element on selected devices and sets how overflowing content is handled.
    **Where it lives:** Any section, row, column, or module: settings modal, Advanced tab, Visibility.
    **Key behavior:** In the Visual Builder, an element disabled for the current device preview shows at 50% opacity but stays editable.

For the full option-group reference, see [Visibility Options](../options-groups/visibility.md).

## Hide an element on specific devices

1. Hover over the element and click its gear icon, or click the element, to open its settings.
2. Open the **Advanced** tab, then the **Visibility** option group.
3. Under **Disable On**, check the devices where the element should be hidden (Phone, Tablet, Desktop, or any enabled custom breakpoint).
4. Save your changes.

An element hidden on Phone and Tablet still shows on Desktop.

## Preview hidden elements

Use the device icons in the top bar of the Visual Builder to switch between Desktop, Tablet, Phone, or any custom breakpoint you have enabled. Elements disabled for the active breakpoint fade to 50% opacity, and you can still click them to change their visibility or other styles.

## Breakpoints

Divi 5 supports seven possible breakpoints, with three active by default: Phone, Tablet, and Desktop. Extra ones such as Phone Wide, Tablet Wide, Widescreen, and Ultra Wide can be switched on. You manage active breakpoints and their widths in the Sitewide Responsive Breakpoints modal, and the **Disable On** choices follow whatever ranges you set. See [Custom Breakpoints](../builder/custom-breakpoints.md).

## Settings

| Setting | Description |
|---|---|
| Disable On | Hides the element on each checked device or breakpoint. |
| Horizontal Overflow | How content that exceeds the element's width is handled: Visible, Hidden, Scroll, or Auto. |
| Vertical Overflow | How content that exceeds the element's height is handled: Visible, Hidden, Scroll, or Auto. |

## Best practices

- **Keep versions to a minimum.** Duplicate a section for a separate mobile structure only when the layout truly differs.
- **Label clearly.** Name duplicated sections and rows with admin labels such as "Hero - Desktop" and "Hero - Mobile".
- **Prefer responsive styling for small tweaks.** Use the responsive controls for font size or spacing changes instead of duplicating elements.
- **Check overflow when content is clipped.** Adjust Horizontal and Vertical Overflow so modules behave correctly on small screens.

## Official documentation

- [Using Divi Visibility Options](https://help.elegantthemes.com/en/articles/13722487)
