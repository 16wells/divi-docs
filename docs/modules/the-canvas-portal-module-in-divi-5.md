---
title: "The Canvas Portal Module in Divi 5"
description: "How the Divi 5 Canvas Portal module renders a detached canvas at an exact spot in a page or Theme Builder template, with use cases and settings."
category: modules
tags: ["modules", "canvas", "popup", "overlay", "portal"]
related: ["canvases"]
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14718409-the-canvas-portal-module-in-divi-5"
---

# The Canvas Portal Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A module that renders the content of a detached [canvas](../builder/canvases.md) at the exact place where you put the module.
    **Where it lives:** Gray Plus icon inside a Row, then search for "Canvas Portal".
    **Key setting:** Content tab > Canvas, a dropdown of your existing canvases.
    **Use it when:** Position matters, for example a mega menu tied to a header link or a popup placed relative to a call to action.

## How it works

Normally Divi appends canvas content on its own when an interaction fires. The Canvas Portal replaces that automatic placement: the selected canvas is output where the portal sits, on a page or inside a Theme Builder template.

## Adding the module

1. Click the **Green Plus** icon to insert a Row.
2. Click the **Gray Plus** icon inside the Row to open the module list.
3. Choose **Canvas Portal**, or find it with the search box.
4. In the Content tab, pick the canvas to display.

## Use cases

- **Mega menu anchored to a header link:** build the mega menu on its own canvas and place a Canvas Portal inside the text or link module holding the parent menu item, so the menu renders relative to that link instead of in a default off-canvas position.
- **Newsletter popup with precise placement:** design the popup in a detached canvas and inject it into a chosen section. Pair it with an on-load interaction and a delay to control when it appears.
- **Reusable content blocks:** keep pricing tables, testimonial sliders, or announcement banners in a global canvas and drop a portal wherever they should show. Editing the source canvas updates every portal that points to it.

## Settings

| Tab | Setting | Description |
|---|---|---|
| Content | Canvas | Selects which existing canvas is shown; its content replaces the portal on the front end. |
| Content | Link | Makes the whole portal clickable. |
| Content | Background | Background styles for the portal. |
| Content | Meta | Label text, and forcing visibility inside the Visual Builder. |
| Design | Sizing, Spacing, Border, Box Shadow, Filters, Transform, Animation | Standard design option groups. |
| Advanced | Attributes, CSS, HTML, Conditions, Interactions, Visibility, Transitions, Position, Scroll Effects | Standard advanced groups. HTML sets the semantic tag; Interactions can show or hide the portal. |

## Official documentation

[The Canvas Portal Module in Divi 5](https://help.elegantthemes.com/en/articles/14718409-the-canvas-portal-module-in-divi-5)
