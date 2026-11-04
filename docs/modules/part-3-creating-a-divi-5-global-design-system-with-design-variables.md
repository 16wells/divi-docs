---
title: "Part 3: Creating A Divi 5 Global Design System With Design Variables"
description: "Build a complete set of Divi 5 Design Variables (colors, fonts, numbers, images, text, links) as the foundation for presets and templates."
category: modules
tags: [modules, design-variables, design-system, course]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15520440-part-3-creating-a-divi-5-global-design-system-with-design-variables"
---

# Part 3: Creating A Divi 5 Global Design System With Design Variables

!!! abstract "Quick Reference"
    **Course position:** Part 3 of the Divi 5 Mastery Course. Previous: [Part 2](part-2-exploring-every-aspect-of-the-divi-5-interface.md). Next: [Part 4](part-4-mastering-divi-5-presets-for-faster-more-consistent-web-design.md).
    **Goal:** A reusable variable set for a sample coworking-space site, covering typography, colors, spacing, borders, layout, buttons, form fields, and repeated content.
    **Where:** Variable Manager icon in the Builder Bar (left side of the Visual Builder).
    **Variable types:** Colors, fonts, numbers, images, text, links (the manager's type filter also lists Gradients).
    **Order matters:** Build variables before presets, because presets bind to variables that already exist.

## Why variables come first

A Design Variable is a named value referenced across the site. Create **Primary Color** once and every module that uses it points back to that single value. Variables are the atoms, presets the molecules, and pages the organisms, so the variables must exist before the [presets in Part 4](part-4-mastering-divi-5-presets-for-faster-more-consistent-web-design.md) can reference them.

Beyond styling, variables can store logos, business details, CTA wording, and external URLs.

## Create a variable

1. Open any page or template in the Visual Builder.
2. Click the Variable Manager icon in the Builder Bar.
3. Use the type dropdown to pick Colors, Fonts, Gradients, Images, Links, Numbers, or Text.
4. Click **+** in that section, name the variable, set its value, and save.

### Naming rule

Name by role. Broad brand values get general names (**Primary Color**, **Body Text Color**). Single-purpose values get functional names (**Border – Fields Dark**, **Background Overlay – Dark**, **Rounded Corners – Buttons**).

## Color variables

Primary, Secondary, Heading Text, Body Text, and Link colors are generated for you; update them to match the design, then add the utility colors. Black and White are mostly used as bases for relative colors.

| Variable | Value |
|---|---|
| Primary Color | `#2176ff` |
| Secondary Color | `#ff5700` |
| Heading Text Color | `#000000` |
| Body Text Color | `rgba(0,0,0,0.7)` |
| Link Color | references Primary Color |
| Black / White | `#000000` / `#ffffff` |
| Background – Light Gray | `#f5f5f5` |

Derived colors use variable referencing with relative color filters, so a section can switch between dark-on-light and light-on-dark schemes by changing presets:

| Variable | Built from |
|---|---|
| Heading Text – Light | White (direct reference) |
| Body Text – Light | White at 90% opacity |
| Text – Dark Transparent | Body Text Color at 40% |
| Text – Light Transparent | Body Text – Light at 60% |
| Background Overlay – Dark / Light | Black / White at 86% |
| Black – Transparent / White – Transparent | Black at 10% / White at 20% |
| Border – Dark / Light | Black at 12% / White at 30% |
| Border – Fields Dark / Light | Black at 30% / White at 50% |
| Drop Shadow | Black at 15% |

## Font variables

Two variables, **Heading** and **Body**, both set to Inter in this build. Using one family keeps a first system simple; hierarchy then comes from size, weight, and line height. Google Fonts and uploaded custom fonts are both supported.

## Number variables

Number variables accept pixels, rems, ems, or CSS functions.

**Heading and eyebrow sizes** use fluid `clamp()` values so text scales between mobile and desktop without per-breakpoint overrides:

| Variable | Value |
|---|---|
| H1 | `clamp(1.75rem, 4.4975vw + 0.6254rem, 3.75rem)` |
| H2 | `clamp(1.5rem, 2.2596vw + 0.9534rem, 2.5rem)` |
| H3 | `clamp(1.25rem, 1.4122vw + 0.9085rem, 1.875rem)` |
| H4 | `clamp(1.0625rem, 0.9831vw + 0.8155rem, 1.5rem)` |
| H5 | `clamp(0.9375rem, 0.7007vw + 0.7588rem, 1.25rem)` |
| H6 | `clamp(0.875rem, 0.2824vw + 0.8067rem, 1rem)` |
| H1 Big | `clamp(3rem, 7.3219vw + 1.1924rem, 6.25rem)` |
| Eyebrow Subheading | `clamp(0.8125rem, 0.2824vw + 0.7442rem, 0.9375rem)` |

**Body text:** Body `clamp(0.875rem, 0.2824vw + 0.8067rem, 1rem)`; Body Small `clamp(0.8125rem, 0.2824vw + 0.7442rem, 0.9375rem)`; Body XS `12px`; Fields Text matches Body Small but stays separate so form text can change independently.

**Line heights:** Headings `1.3em`, Body `1.8em`, Body Small `1.55em`. Large text needs tight leading; body text benefits from more.

**Spacing:** XSmall `10px`, Small `20px`, Medium `30px`, Regular `60px`, Large `100px`, Fluid `clamp(24px, 6vw, 90px)`, and Grid Gap – Fluid `min(4vw, 60px)` (capped for CSS Grid layouts).

**Borders and corners:** Border Width `1px`, Border Width – Fields `1px`, Border Width – Buttons `0px` (filled buttons, no outline). Rounded Corners – Regular/Images/Fields are each `8px` but kept separate so images, containers, and fields can diverge later; Small `4px`, Large `16px`, Buttons `500px` for a pill shape.

**Buttons:** Font Size `14px`, Vertical Padding `16px`, Horizontal Padding `32px` (a 2:1 ratio for a wide, click-friendly shape).

**Layout widths:** Row Max Width `1080px`, plus Max Width – 900, 700, and 510 (`900px`, `700px`, `510px`) for blog posts, forms, and compact centered blocks.

## Image variables

**Logo Dark** (for light backgrounds) and **Logo Light** (for dark backgrounds). Swap a logo once and headers, footers, and templates all update. A placeholder logo generator works if you have no logo yet.

## Text variables

Store repeated business details (Company Name, Address, Phone Number, Email, Opening Hours) and standard CTA wording (Book Tour, View Plans, Learn More, Read More) so the copy stays consistent.

## Link variables

Best for external destinations such as social profiles or scheduling tools; use dynamic content for links inside your own WordPress site. The example stores Elegant Themes and YouTube URLs. When a URL changes, update the variable once.

## The finished system

The example totals 74 variables: 21 colors (8 base, 13 relative), 2 fonts, 38 numbers, 2 images, 9 text, and 2 links. Because everything references these values, changing **Primary Color** flows through every preset that uses it.

## Retrofitting existing pages

The Divi AI Agent (part of a Divi AI subscription) can find hard-coded colors, fonts, and spacing on a page and convert the ones you pick into Design Variables, asking for approval before destructive changes. An example prompt: scan the page for values not yet using a variable and offer to convert repeated ones.

## Official documentation

[Part 3: Creating A Divi 5 Global Design System With Design Variables](https://help.elegantthemes.com/en/articles/15520440-part-3-creating-a-divi-5-global-design-system-with-design-variables)
