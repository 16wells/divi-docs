---
title: "The SVG Module in Divi 5"
description: "The Divi 5 module for placing vector graphics from pasted SVG code or an uploaded SVG file, with Fill and Stroke controls."
category: modules
tags: ["modules", "svg", "icons", "graphics"]
related: ["icon", "image"]
divi_version: "5.5+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15081438-the-svg-module-in-divi-5"
---

# The SVG Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A module that places a vector graphic on the page, from pasted SVG markup or an uploaded SVG file.
    **Why use it:** Vectors stay sharp at every size and can be recolored through Fill and Stroke inside the Visual Builder.
    **Prerequisite for uploads:** WordPress blocks SVG uploads by default; enable them first (see Elegant Themes' [How to Upload SVG and JSON Files](https://help.elegantthemes.com/en/articles/11982083-how-to-upload-svg-and-json-files)).

## Add the module

1. In the Visual Builder, click the green plus icon to insert a Row into the Section.
2. Click the gray plus icon inside the Row to open the module list.
3. Find **SVG** (or search for it) and click it.

## Use cases

- **Logos and brand marks** that stay sharp on retina screens and large sizes.
- **Decorative shapes** such as dividers and blobs that can be recolored and resized without quality loss.
- **Custom illustrations** pasted as raw markup, including animated graphics or ones styled directly with Fill and Stroke.

## Content tab

| Setting | Description |
|---|---|
| SVG Source | How the SVG is supplied (see below) |
| Link | Makes the whole module clickable: Link URL, Link Target (same or new tab), and Link Rel such as `nofollow` or `noopener` |
| Elements | Toggle which sub-elements of the module are shown |
| Background | Background styles for the module |
| Loop | Enables the Loop Builder |
| Order | Position in a Flexbox or Grid layout |
| Meta | Label text and forced visibility inside the Visual Builder |

### SVG Source

- **SVG Code:** paste valid SVG markup. It must be a well-formed `<svg>` element; broken or partial markup will not render.
- **Uploaded SVG:** choose an SVG file from the WordPress Media Library (requires SVG uploads to be enabled).
- **Title:** the SVG's title text, used for accessibility and shown as a tooltip when a visitor hovers over the graphic.

## Design tab

| Setting | Description |
|---|---|
| Layout | Flexbox or CSS Grid layout for the module's contents |
| Fill | Fill color for closed shapes; overrides any `fill` values inside the SVG markup |
| Stroke | Stroke color, width, and style (such as a dashed pattern) for the outlines along the SVG's paths |
| Sizing, Spacing, Border, Box Shadow | Standard option groups |
| Filters | Hue shifts, saturation changes, blend modes |
| Transform | Scale, rotate, skew, translate |
| Animation | Animation styles |

## Advanced tab

| Setting | Description |
|---|---|
| Attributes | CSS ID, reusable CSS classes, or custom HTML attributes |
| CSS | Custom CSS for the module |
| HTML | Semantic HTML tag |
| Conditions | Show content based on conditions |
| Interactions | Custom interactions such as showing or hiding the SVG |
| Visibility | Visibility per device |
| Transitions | Duration of animations |
| Position | Precise placement |
| Scroll Effects | Behavior during scrolling |

Save the page with `CMD + S` (Mac) or `CTRL + S` (PC), or use the **Save** and **Exit** buttons.

## Official documentation

- [The SVG Module in Divi 5](https://help.elegantthemes.com/en/articles/15081438-the-svg-module-in-divi-5)
