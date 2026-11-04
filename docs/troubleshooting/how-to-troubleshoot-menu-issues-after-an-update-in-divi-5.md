---
title: "How to Troubleshoot Menu Issues After an Update in Divi 5"
description: "A five-step diagnostic flow for menus that break after a Divi 5, plugin, or theme update."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15324574-how-to-troubleshoot-menu-issues-after-an-update-in-divi-5"
---

# How to Troubleshoot Menu Issues After an Update in Divi 5

!!! abstract "Quick Reference"
    **Typical causes:** Stale cached CSS, custom CSS that no longer fits updated markup, a plugin conflict, or a symptom with its own targeted fix.
    **Order of work:** Clear all caches, match your symptom, test without custom CSS, test in Safe Mode, confirm you are on the latest Divi 5.
    **Quick cache check:** Add `?nocache=1` to the site URL.

## Step 1: Clear every cache layer

Divi 5 keeps generated CSS in a static cache, and after an update it can still hold old styles. This is the most common reason a menu breaks right after updating.

1. Go to **Divi > Theme Options** and click **Clear CSS Cache** (top right).
2. Clear your caching plugin's full cache, including separate CSS and JavaScript caches.
3. Clear any server-level cache from your hosting panel (look for Cache, Performance, or Flush).
4. Clear your browser cache, or test in a private window.

Reload the front end. If the menu works, it was only cache.

## Step 2: Identify the symptom

If the menu is still broken, match what you see:

- **Hamburger icon missing, invisible, or unresponsive:** usually an icon color matching the header background, or an overflow setting on a parent clipping it. See [Why the Hamburger Menu Icon Is Invisible or Unclickable](why-the-hamburger-menu-icon-is-invisible-or-unclickable-in-divi-5.md).
- **Dropdown cut off at an edge or hidden behind content:** an overflow problem on a parent container or a z-index conflict, often from Scroll Effects on the first content section. See [How to Fix the Dropdown Menu That's Cut Off or Hidden](how-to-fix-the-dropdown-menu-that-s-cut-off-or-hidden-behind-page-content-in-divi-5.md).
- **A section, row, or module disappears on mobile:** a visibility, display condition, or custom code problem.

For symptoms that fit none of these, continue below.

## Step 3: Test for custom CSS conflicts

Updates can change markup or class names, so older custom CSS may start hiding or breaking menu elements.

1. Go to **Divi > Theme Options > General** and open the **Custom CSS** field.
2. Copy its contents to a text file as a backup, then clear the field and save.
3. Clear the Divi 5 CSS cache and reload the front end.

If the menu now works, paste the rules back in small chunks, clearing the cache and testing after each, to find the culprit.

Patterns to look for:

- Rules targeting `.et_mobile_menu`, `.mobile_menu_bar`, `.et_pb_menu_inner_container`, or `.et_pb_menu__wrap` that use `display: none`, `visibility: hidden`, `opacity: 0`, or `overflow: hidden`.
- Hardcoded widths or negative margins on `.et_mobile_menu`.
- Z-index overrides on `.et-l-header` or `.et_pb_menu`.

Custom CSS can also live in **Page Settings > Advanced > Custom CSS**, a module's **Advanced > CSS** option group, **Code** modules, and your child theme's stylesheet.

## Step 4: Test for plugin and theme conflicts

1. Go to **Divi > Support Center**, enable **Safe Mode**, and reload on a phone, tablet, or desktop. Safe Mode affects only your user, not visitors.
2. If the menu works, a plugin, child theme, or custom script is the conflict. Disable Safe Mode, deactivate all non-essential plugins, and reactivate them one at a time, clearing caches and testing after each.

The last plugin activated when the problem returns is the conflict.

## Step 5: Confirm the latest Divi 5 version

1. Go to **Dashboard > Updates** and install any Divi update.
2. Repeat Step 1 to clear all caches, then retest the menu.

## Still stuck?

Gather before contacting Elegant Themes support:

- The exact symptom, with screenshots or a short recording.
- Your Divi 5 and WordPress versions.
- A note that you cleared all caches, tested without custom CSS, tested in Safe Mode, and ruled out plugins.
- The URL of an affected page.

## Official documentation

[How to Troubleshoot Menu Issues After an Update in Divi 5](https://help.elegantthemes.com/en/articles/15324574-how-to-troubleshoot-menu-issues-after-an-update-in-divi-5)
