---
title: "How to Fix the Dropdown Menu That's Cut Off or Hidden Behind Page Content in Divi 5"
description: "Fix Divi 5 dropdown menus that are clipped by a parent container or stacked behind page content, using Visibility and Position settings."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15324394-how-to-fix-the-dropdown-menu-that-s-cut-off-or-hidden-behind-page-content-in-divi-5"
---

# How to Fix the Dropdown Menu That's Cut Off or Hidden Behind Page Content in Divi 5

!!! abstract "Quick Reference"
    **Cut off at an edge:** An overflow clipping problem. Set Overflow to Visible on parent elements (Advanced tab, Visibility).
    **Partly or fully invisible:** A z-index stacking problem. Raise the header section's Z-index (Advanced tab, Position).
    **Both symptoms:** Apply both fixes, in order.

Hover over a parent menu item on desktop, or tap the hamburger icon on mobile, and look closely:

- **Opens but is sliced off where the header ends:** overflow clipping.
- **Opens but is partly or fully invisible, with page text bleeding through or no dropdown at all:** z-index stacking.

## Fix 1: Let the dropdown overflow its parent

A parent **Section**, **Row**, or **Column** with overflow set to **Hidden** clips anything extending past its box. Dropdowns extend below the Menu module, so a header section with hidden overflow cuts them off.

1. Open the header template in Theme Builder, or the page in the Visual Builder.
2. Click the **Section** containing the Menu module.
3. On the **Advanced** tab, open the **Visibility** option group.
4. Set **Horizontal Overflow** and **Vertical Overflow** to **Visible**.
5. If the dropdown is still clipped, repeat on the parent **Row** and **Column**.

!!! note
    Work outward from the Menu module to the section, changing only elements that actually need it. Do not change overflow on a deeply nested element if the clipping happens at section level.

## Fix 2: Raise the dropdown above page content

If the dropdown opens at full size but disappears behind content below the header, that content sits on a higher stacking layer.

1. Click the **Section** containing the Menu module.
2. On the **Advanced** tab, open the **Position** option group.
3. Set **Z-index** to a high number such as `100`, `999`, or `9999`.
4. Save.

If it is still hidden, another section is usually pushing itself up the stack.

## Scroll Effects on the first content section

**Scroll Effects** on the first section below the header are a common source of z-index trouble. A sticky position or transform effect makes the browser promote the section to its own stacking layer, which can place it above the header menu.

1. Click the first **Section** below the header.
2. On the **Advanced** tab, open **Scroll Effects**.
3. If **Sticky Position** is set or any **Scroll Transform Effects** are active, the dropdown will likely stack behind them.
4. Either disable the effect, or open the section's **Position** option group and set **Z-index** to `0` so the header's higher z-index wins.

!!! tip
    To keep both the scroll effect and the dropdown, make sure the header's Z-index is always higher than any section using Scroll Effects.

## Still not working

- Clear the cache at **Divi > Theme Options > Clear CSS Cache**, then reload in a private window.
- Enable **Safe Mode** under **Divi > Support Center** to rule out a plugin or custom code conflict.
- Check **Divi > Theme Options > General > Custom CSS** for `overflow: hidden` on `.et-l-header`, `.et_pb_menu`, or related selectors, which clip the dropdown regardless of Visibility settings.

## Official documentation

[How to Fix the Dropdown Menu That's Cut Off or Hidden Behind Page Content in Divi 5](https://help.elegantthemes.com/en/articles/15324394-how-to-fix-the-dropdown-menu-that-s-cut-off-or-hidden-behind-page-content-in-divi-5)
