---
title: "Part 6: Building a Custom Header and Navigation in Divi 5"
description: "Build a sticky, responsive global header in the Divi 5 Theme Builder with an announcement bar, logo, Menu module, social links, CTA button, and breakpoint Interactions."
category: modules
tags: [modules, theme-builder, header, navigation, flexbox, interactions, course]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15530763-part-6-building-a-custom-header-and-navigation-in-divi-5"
---

# Part 6: Building a Custom Header and Navigation in Divi 5

!!! abstract "Quick Reference"
    **Course position:** Part 6 of the Divi 5 Mastery Course. Previous: [Part 5](part-5-building-a-divi-5-homepage-from-scratch.md). Next: [Part 7](part-7-building-a-custom-footer-in-divi-5.md).
    **Result:** A sticky global header with an announcement bar, logo, Menu module, social icons, and a CTA button, with the social icons and button hidden at Tablet and below.
    **Where:** WordPress dashboard, Divi, Theme Builder, Default Website Template, Add Global Header.
    **Depends on:** Design Variables and presets from earlier parts (Primary Color, Spacing - XSmall, and the Subheading, Dark Text, Isolated Icons - Dark, No Background, and Filled - Black presets).

## Why build a custom header

A Theme Builder header gives more control over layout, styling, responsiveness, and behavior than the default header. You can make it sticky, use semantic HTML, and decide how it changes at each breakpoint. This tutorial uses the Menu module for speed; more advanced navigation can use Link modules, Menu Loops, Dropdown modules, and Interactions. Reusing presets and variables keeps the header in sync with the homepage.

## 1. Open the Theme Builder

1. Go to **Divi, Theme Builder** in the dashboard.
2. Under **Default Website Template**, click **Add Global Header** (or edit the existing placeholder).

## 2. Build the structure

### First Row (announcement bar)

1. Add a single-column Row.
2. **Content tab, Background:** apply the **Primary Color** variable.
3. **Design tab, Layout:** **Justify Content** to Center.
4. **Sizing:** Width 100%, Max Width None.
5. **Spacing:** use the Insert Dynamic Content icon to put **Spacing - XSmall** in top and bottom padding.

For its Column: open it from the Row's **Elements** group, then in **Design, Layout** set Horizontal Gap and Vertical Gap to **Spacing - XSmall** and **Align Items** to Center.

### Second Row (main header)

1. Add a second single-column Row.
2. **Design, Layout:** Horizontal and Vertical Gap set to **Spacing - XSmall**, **Align Items** Center.
3. On its Column, **Design, Layout:** Vertical Gap **Spacing - XSmall**, **Layout Direction** Row, **Justify Content** and **Align Items** Center, **Layout Wrapping** Wrap.

### Section

1. **Design, Layout:** Vertical Gap `10px`.
2. **Spacing:** top padding from the **Border Width - Buttons** variable (0px), bottom padding from **Spacing - XSmall** (10px).
3. **Advanced, Position:** **Z Index** 999 so the header stays above content when sticky.
4. **Advanced, Scroll Effects, Sticky Position:** **Stick to Top**.

## 3. Announcement bar

1. In the first Row, add a **Heading** module.
2. Click **Assign Presets** and choose the **Subheading** element preset.
3. **Design, Heading Text:** set **Heading Text Color** to the global White.

## 4. Logo and navigation

1. In the second Row, add a **Group** module.
2. Inside the Group, add an **Image** module. In **Content, Image**, hover the field, click **Insert Dynamic Content**, and choose **Site Logo**.
3. **Design, Sizing:** Max Height `50px`. (If no logo is set in Divi, Theme Options, assign one later.)
4. Add a **Menu** module to the Group. Select your WordPress menu under **Content, Menu** (or return to this later if the menu does not exist yet), apply the **Dark Text** preset, and optionally delete the module's built-in logo under the **Logo** group since the Image module supplies it.

Then configure the Group's Flexbox settings:

- **Layout:** Vertical Gap **Spacing - XSmall**, **Layout Direction** Row, **Justify Content** Space Between, **Align Items** Center, **Layout Wrapping** Wrap.
- **Sizing, Size:** enable **Grow to Fill**, **Alignment** Stretch.

## 5. Social links and CTA

1. Add a **Social Media Follow** module outside the Group. Add networks under **Content, Elements**, apply the **Isolated Icons - Dark** preset, then edit each network and assign the **No Background** preset.
2. Add a **Button** module and apply the **Filled - Black** preset.

## 6. Hide items on smaller screens with Interactions

For the Social Media Follow module, go to **Advanced, Interactions**:

1. Click **+ Add New Interaction**. Trigger Event: **Breakpoint Enter**, Breakpoint: **Tablet**, Effect Action: **Hide Element**, Target Module: the Social Media Follow module.
2. Add another: **Breakpoint Enter**, Breakpoint **Desktop**, **Show Element**, same target.
3. Repeat both interactions for the Button module (show on Desktop, hide at Tablet and below).

The logo and menu stay visible.

## 7. Test responsiveness

- **Customizable Responsive Breakpoints** (from the top bar): enable extra breakpoints for finer control over when elements hide and spacing tightens.
- **Responsive Editor:** hover a responsive-capable field and click **Edit Responsive Values**, then step through breakpoints.

## Tips

- **Preview in context:** Builder Settings in the Builder Bar, turn on **Show Theme Builder Layouts** to see the header above real page content.
- **Global versus specific:** a Global Header suits most sites; add more specific templates later for pages or post types that need a different header.
- **Back up:** export Theme Builder templates or the header layout from the Theme Builder interface.

## Import the finished header

The course provides a JSON file (Master Course Header Layout.json). Ideally create the WordPress menu first under **Appearance, Menus**, though you can assign it later.

1. Go to **Divi, Theme Builder** and edit or create the **Global Header**.
2. Click the Gear icon (top left) and choose **Import**.
3. Select the JSON file.
4. Make sure **Import Presets** is checked.
5. Click **Import Layout**.

## Divi AI Agent shortcut

The Divi AI Agent (part of a Divi AI subscription) can create the global header, build a WordPress menu, and assign it to the primary location from chat, pausing for approval before destructive changes.

## Official documentation

[Part 6: Building a Custom Header and Navigation in Divi 5](https://help.elegantthemes.com/en/articles/15530763-part-6-building-a-custom-header-and-navigation-in-divi-5)
