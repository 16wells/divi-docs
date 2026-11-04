---
title: "Why the Hamburger Menu Icon Is Invisible or Unclickable in Divi 5"
description: "Fix a Divi 5 mobile menu whose hamburger icon is missing or does nothing when tapped, caused by icon color or overflow clipping."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15323758-why-the-hamburger-menu-icon-is-invisible-or-unclickable-in-divi-5"
---

# Why the Hamburger Menu Icon Is Invisible or Unclickable in Divi 5

!!! abstract "Quick Reference"
    **Symptom:** The mobile menu shows only the logo, or the hamburger icon is there but tapping does nothing.
    **Cause 1:** The icon color matches the header background (Menu module, Design tab, Icons).
    **Cause 2:** A parent element clips the icon with Hidden overflow (Advanced tab, Visibility).

Check your site on a phone or in device preview and decide which symptom you have:

- **The icon is missing entirely.** You see only the logo or an empty bar, and nothing reacts to a tap.
- **The icon seems present but the dropdown never opens.** You may faintly see three lines, or know they should be there.

## Fix 1: The icon color matches the header background

The most common cause. The icon renders, but a black icon on a black header looks identical to a missing one.

1. Open the page in the Visual Builder, or the header layout in Theme Builder.
2. Click the **Menu** module to open its settings.
3. On the **Design** tab, open the **Icons** option group.
4. Change **Hamburger Menu Icon Color** to a value that contrasts with the header background.
5. Save.

While in the Menu module, also check the **Dropdown Menu** option group on the Design tab. If **Mobile Menu Background** or **Mobile Menu Text Color** hides the menu items, the dropdown opens but looks empty.

!!! tip
    Use a contrast checker. A subtle difference that looks fine on desktop can vanish on a phone in bright light.

## Fix 2: The header is clipping the icon

If the color is fine but the icon still does not appear or cannot be tapped, the **Visibility** option group on a parent element may be clipping it. **Horizontal Overflow** and **Vertical Overflow** set to **Hidden** cut off anything extending past the element's box. These settings live on the header's parent section or the page, not on the Menu module.

1. Open the header template in Theme Builder, or the page in the Visual Builder.
2. Click the **Section**, **Row**, and **Column** that contain the Menu module.
3. On the **Advanced** tab, open the **Visibility** option group.
4. Set **Horizontal Overflow** and **Vertical Overflow** to **Visible**, or remove the overrides so they inherit the default.
5. Save.

If the header is inside a Row or wrapped in a Group, repeat the check on those too, since clipping can come from any ancestor. Also check the page itself: open page settings (the three-dots menu in the Visual Builder), go to the **Advanced** tab, and review the **Visibility** group. A page-level overflow setting clips everything inside.

## Still not working

- Clear the cache at **Divi > Theme Options > Clear CSS Cache** (top right), then reload in a private window.
- Enable **Safe Mode** under **Divi > Support Center** to rule out a plugin or custom code conflict.
- Check **Divi > Theme Options > General > Custom CSS** for rules targeting `.mobile_menu_bar` or `.et_mobile_menu` with `display: none`, `visibility: hidden`, or `opacity: 0`.

If the icon appears in Safe Mode, the cause is custom code.

## Official documentation

[Why the Hamburger Menu Icon Is Invisible or Unclickable in Divi 5](https://help.elegantthemes.com/en/articles/15323758-why-the-hamburger-menu-icon-is-invisible-or-unclickable-in-divi-5)
