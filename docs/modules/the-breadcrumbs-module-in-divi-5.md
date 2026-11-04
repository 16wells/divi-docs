---
title: "The Breadcrumbs Module in Divi 5"
description: "The Divi 5 Breadcrumbs module shows a clickable trail of the current page's position in the site, with separate styling for the wrapper, links, home link, and separator."
category: modules
tags: ["modules", "breadcrumbs", "navigation", "seo"]
related: ["woo-breadcrumbs", "menu"]
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14852183-the-breadcrumbs-module-in-divi-5"
---

# The Breadcrumbs Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A clickable trail such as Home > Blog > Category > Post that shows where the current page sits in the site.
    **Where it lives:** Gray Plus icon inside a Row, then search for "Breadcrumbs".
    **Key settings:** Content tab > Home Text, Home URL, and Separator.
    **WooCommerce:** For product pages use the Woo Breadcrumbs module instead.

## Adding the module

1. Click the **Green Plus** icon to insert a Row.
2. Click the **Gray Plus** icon inside the Row.
3. Choose **Breadcrumbs**, or search for it.

## Use cases

- **Site-wide navigation aid:** put the module in a Theme Builder header so every page shows the same trail.
- **Deep hierarchies:** blogs, knowledge bases, and documentation sites where visitors land several levels below the home page.
- **Accessibility and SEO:** a visible content trail for visitors and a structured navigation path for search engines.

## Content tab

| Setting | Description |
|---|---|
| Home Text | Label of the first item. Defaults to "Home". Supports Dynamic Content. |
| Home URL | Destination of the first item. Defaults to the site home page. Supports Dynamic Content. |
| Separator | Character between items, for example `/`, `>`, or `|`. |
| Link | Makes the whole module clickable. |
| Elements | Toggles optional pieces of the trail on or off. |
| Background | Color, gradient, image, video, or pattern. |
| Loop | Enables the Loop Builder. |
| Meta | Label text and forced Visual Builder visibility. |

## Design tab

The trail is split into four sub-elements, each with Background, Text, Sizing, Spacing, Border, and Box Shadow groups through Divi 5 Composable Settings. If a group is missing inside a sub-element, hover over the sub-element and click the **Toggle Options** icon to enable it.

| Group | Styles |
|---|---|
| Layout | Block, Flex (default), or Grid. |
| Breadcrumb | The wrapper around the whole trail. |
| Breadcrumb link | Every clickable item except the home item. |
| Home link | Only the first item (set by Home Text and Home URL). |
| Separator | The symbol or icon between items. |
| Sizing, Spacing, Border, Box Shadow, Filters, Transform, Animation | Module-level groups. |

Tip: save a styled module as an Option Group Preset so the same Composable Settings stay enabled wherever you reuse it.

## Advanced tab

Attributes, CSS, HTML (semantic tag, such as `nav` or `div`), Conditions, Interactions, Visibility, Transitions, Position, and Scroll Effects.

## Official documentation

[The Breadcrumbs Module in Divi 5](https://help.elegantthemes.com/en/articles/14852183-the-breadcrumbs-module-in-divi-5)
