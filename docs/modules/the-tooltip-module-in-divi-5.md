---
title: "The Tooltip Module in Divi 5"
description: "The Divi 5 Tooltip module: a floating popup panel anchored to a parent element, shown on hover, click, or always."
category: modules
tags: [modules]
related: []
divi_version: "5.8+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15585511-the-tooltip-module-in-divi-5"
---

# The Tooltip Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A nestable container that appears as a floating popup next to another element (a hint, label, or mini-card).
    **How it attaches:** Add it as a child of the element it describes; that parent is the tooltip's *anchor*.
    **Defaults:** Shows on hover, sits outside top center of the anchor, floats on a high z-index, with a solid black background (`#000000`), `3px` rounded corners, and padding of `3px` top and bottom and `6px` left and right.
    **Design tip:** Turn on **Force Visible** (Meta group) while designing so the popup shows on the canvas.

## How it works

- The **anchor** is the parent element (button, image, text, icon, or any module) the tooltip points at.
- The **Tooltip module** is a child of that anchor and holds the popup content: rich text, other modules, or both.
- Because the popup appears only when triggered, use **Force Visible** (Meta > **While In Builder**) to see and style it.

## Add the module

1. In the Visual Builder, click the green plus icon to insert a Row into the Section.
2. Click the gray plus icon inside the Row to open the module list.
3. Find **Tooltip** (or search for it) and click it.

## Use cases

- **Form field hints** explaining what a field expects.
- **Icon and image labels** revealed on hover.
- **Definitions and footnotes** shown inline, on demand.
- **Mini promo cards** with text plus other modules beside a button or product.

## Content tab

| Setting | Description |
|---|---|
| Text | The tooltip's content, edited in the rich text editor |
| Link | Makes the whole module link to a page, section, or external URL |
| Elements | Add nested modules |
| Background | Background color, gradient, image, or video (default is solid black) |
| Loop | Repeats the module's content from a data source |
| Order | Controls the module's order when generated dynamically |
| Meta | Label, plus Force Visible (While In Builder) to preview the popup on the canvas |

## Design tab

### Tooltip group (unique to this module)

| Setting | Description |
|---|---|
| Show Tooltip on | **Hover**, **Click**, or **Always** (always visible, no interaction needed) |
| Tooltip Movement | **Anchored** (shown relative to the target; top by default, changeable with Tooltip Position) or **Follow Cursor** (follows the mouse, following the Show option) |
| Tooltip Position | Where the tooltip appears relative to the target element |
| Tooltip Skid | Shifts the tooltip along the target edge (cross-axis offset) |
| Tooltip Distance | Gap from the target along the placement direction (main-axis offset) |
| Tooltip Open Delay | Delay before the tooltip opens |
| Tooltip Close Delay | Delay before the tooltip closes |
| Show Tooltip Arrow | Displays a small pointer arrow toward the parent module |

### Other Design settings

| Setting | Description |
|---|---|
| Layout | How child modules inside the tooltip are arranged |
| Body Text | Font, size, color, and spacing of the popup text |
| Sizing | Width, max width, height, and alignment |
| Spacing | Padding and margin (default padding `3px` top/bottom, `6px` left/right) |
| Border | Borders and rounded corners (default radius `3px`) |
| Box Shadow | Drop shadow around the popup |
| Filters | Hue, saturation, blend modes |
| Transform | Scale, rotate, skew, move |
| Animation | Motion effect when the popup appears |

## Advanced tab

| Setting | Description |
|---|---|
| Attributes | CSS ID and classes |
| HTML | Custom HTML attributes |
| Conditions | Show or hide based on rules such as login status or device |
| Interactions | Trigger actions in response to visitor interaction |
| Visibility | **Disabled On** for specific screen sizes, and content **Overflow** |
| Transition | Timing and speed of hover transitions |
| Position | Placement and **Z-Index** (high by default) |
| Scroll Effects | Scroll-based motion and sticky behavior |

Save the page with `CMD + S` (Mac) or `CTRL + S` (PC), or use the **Save** and **Exit** buttons.

## Official documentation

- [The Tooltip Module in Divi 5](https://help.elegantthemes.com/en/articles/15585511-the-tooltip-module-in-divi-5)
