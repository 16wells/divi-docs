---
title: "Responsive Preview System"
description: "Divi 5 Responsive Preview — test designs across desktop, tablet, and phone viewports with custom widths, fold indicators, and portrait/landscape rotation."
category: builder
tags: ["builder", "responsive", "preview", "mobile"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/responsive-preview-system"
---

# Responsive Preview System

Divi’s responsive preview system allows you to view what your designs will look like on a wide range of devices and viewport configurations. All without having to leave the visual builder!

!!! abstract "Quick Reference"
    **What it does:** Preview and edit your design at desktop, tablet, and phone breakpoints with adjustable viewport widths.
    **Where to find it:** Device icons in the top bar or bottom toolbar of the Visual Builder.
    **Key features:**

    - Three default breakpoints: Desktop (981px+), Tablet (768-980px), Phone (<768px)
    - Drag canvas edges or type a custom pixel width for arbitrary viewport testing
    - Above-the-fold indicator line for each device size
    - Portrait and landscape rotation toggle for tablet and phone previews

    **ET Docs:** [Responsive Preview System](https://www.elegantthemes.com/documentation/divi/responsive-preview-system){:target="_blank"}

Thanks to the Divi responsive preview system, it’s no longer necessary to use a third party software to test how your webpages will render on smaller screen sizes. Mobile devices are utilized by more than 60% of all internet users, so previewing how your pages will look on smaller screens is an important part of web design. Let’s take a look at how to use the repsponsive preview system by demonstrating its capabilities using theStreamer Divi Layout Pack.

There are two ways to access Divi’s responsive preview system. The first is by activating it at the page level. This can be accomplished by viewing the page’s back end or on the front end with the Visual Builder. The second way to activate the responsive preview system is at the module, colum, row, or section level. Let’s start off by loading the preview system at the page level.

<!-- ![Responsive Preview System overview](../assets/screenshots/builder/responsive-preview/overview.png){ loading=lazy }
*The Responsive Preview System interface in Divi 5.* -->

## How To Access the Divi Responsive Preview System

There are two ways to activate responsive preview:

### Page-Level Preview

1. **From the back end**: Go to any page in the WordPress admin and click **Preview** with a device option.
2. **From the Visual Builder**: Click one of the device icons (Desktop, Tablet, Phone) in the top bar or the bottom toolbar. The canvas resizes to the selected breakpoint.

### Element-Level Preview

Within any element's settings panel, use the device selector to switch breakpoints. This lets you preview and edit responsive values for a specific element without affecting the overall canvas view.

## Default Breakpoints

Divi provides three built-in breakpoints:

| Breakpoint | Width Range | Icon |
|-----------|-------------|------|
| **Desktop** | 981 px and above | Monitor icon |
| **Tablet** | 768 px -- 980 px | Tablet icon |
| **Phone** | Below 768 px | Phone icon |

These breakpoints determine which responsive values are applied. Settings cascade downward: a Desktop value is inherited by Tablet and Phone unless overridden.

## Adjusting the Divi Responsive Preview Modes

When you switch to Tablet or Phone preview mode, the canvas resizes to a representative width for that device class. You can fine-tune the preview by:

- **Dragging the canvas edges** to test any width within the breakpoint range.
- **Typing a specific pixel width** in the width input field (if available in the top bar).

This lets you test how your design responds not just at the default breakpoint widths, but at any viewport size in between.

## Customizing the Divi Responsive Preview Widths

For projects that require breakpoints beyond the three defaults, see the [Responsive Options](responsive-options.md) documentation for details on custom breakpoints and how Divi 5 handles the device-first responsive workflow.

## Above The Fold Indicator

When responsive preview is active, Divi displays an **above-the-fold indicator** -- a horizontal line showing where the visible viewport ends before the user scrolls. This helps you ensure that critical content (hero headlines, CTAs, navigation) appears above the fold on each device size.

The fold line adjusts automatically as you change device preview modes, reflecting the typical viewport height for each device class.

## Portrait & Landscape Modes

For tablet and phone previews, Divi provides a **rotation toggle** that switches between portrait (vertical) and landscape (horizontal) orientations. The canvas width and height adjust to reflect the rotated device dimensions.

| Device | Portrait Width | Landscape Width |
|--------|---------------|-----------------|
| **Tablet** | ~768 px | ~1024 px |
| **Phone** | ~375 px | ~667 px |

Use landscape mode to verify that your design works well when users rotate their devices, particularly for full-width sections and hero areas.

## More Resources

- [Responsive Options](responsive-options.md) -- The device-first responsive editing workflow in Divi 5
- [Visual Builder Interface](vb-interface.md) -- Top bar device selector and workspace overview
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Shortcuts for zooming and navigation

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If this feature is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.


## Related

- [Visual Builder](visual-builder.md)
