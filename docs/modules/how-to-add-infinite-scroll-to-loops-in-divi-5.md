---
title: "How to Add Infinite Scroll to Loops in Divi 5"
description: "Add infinite scrolling to a Divi 5 Loop Builder layout using the YITH Infinite Scrolling plugin, three class attributes, and four selector settings."
category: modules
tags: [modules, loop-builder, pagination, infinite-scroll]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15338539-how-to-add-infinite-scroll-to-loops-in-divi-5"
---

# How to Add Infinite Scroll to Loops in Divi 5

!!! abstract "Quick Reference"
    **Problem:** The Loop Builder has no built-in infinite scroll.
    **Solution:** The free YITH Infinite Scrolling plugin, wired up through three CSS class attributes in Divi and four selectors in the plugin.
    **Recommended structure:** One Section with two Rows: the first holds the looped item (a Group module works well), the second holds the Pagination module.
    **Gotcha:** Class attribute values in Divi have no leading dot; the plugin selectors do.

## Prerequisites

- YITH Infinite Scrolling installed and activated (Plugins, Add Plugin, search, Install Now, Activate).
- Loop enabled on a section, row, column, or module.
- The Section/two-Row structure above.

## Tag the loop item

1. Open the page in the Visual Builder and open the looped element's settings.
2. Go to **Advanced tab, Attributes**.
3. Click **+ Add Attribute**, choose **class**, and enter `dt-loop-item`.

## Configure the Pagination module

1. Add a Pagination module after the looped element.
2. In **Content tab, Target, Target Loop**, select the looped element.
3. In **Advanced tab, Attributes**, add a **class** attribute with the value `dt-looped-pagination`.
4. Save.

## Tag the wrapping Section

1. Open the Section settings (the one containing both Rows).
2. In **Advanced tab, Attributes**, add a **class** attribute with the value `dt-loop-wrapper`.

Any valid class names work, as long as the plugin settings below match them.

## Set the plugin selectors

In the WordPress dashboard, open the **YITH** menu and set:

| Option | Value |
|---|---|
| Navigation Selector | `.dt-looped-pagination` |
| Next Selector | `.dt-looped-pagination .nav-next a` |
| Item Selector | `.dt-loop-item` |
| Content Selector | `.dt-loop-wrapper` |

Click **Save Option**.

## Notes

- The page needs enough content to scroll, otherwise infinite loading never triggers.
- Remember the dot rule: no dot in Divi attribute values, dot in the plugin selectors.

## Official documentation

[How to Add Infinite Scroll to Loops in Divi 5](https://help.elegantthemes.com/en/articles/15338539-how-to-add-infinite-scroll-to-loops-in-divi-5)
