---
title: "The Breadcrumbs Module in Divi 5"
category: modules
tags: ["modules", "breadcrumbs", "navigation", "seo"]
related: ["woo-breadcrumbs", "menu"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14852183-the-breadcrumbs-module-in-divi-5"
---

# The Breadcrumbs Module in Divi 5

The Divi **Breadcrumbs Module** displays a clickable trail that shows visitors where the current page sits inside your site - for example, **Home → Blog → Category → Post**. It helps visitors orient themselves, makes it easy to step back up the hierarchy, and gives search engines a clear signal about your content structure.

## Overview

This article covers how to add the Breadcrumbs Module to a page, walks through every setting on the **Content**, **Design**, and **Advanced** tabs, and explains how the module's sub-element design groups work alongside Divi 5's [Composable Settings](https://help.elegantthemes.com/en/articles/14332889-composable-settings-in-divi-5). If you're building breadcrumbs specifically for a WooCommerce product page, use the [Woo Breadcrumbs Module](https://help.elegantthemes.com/en/articles/12032985-the-woo-breadcrumbs-module-in-divi-5) instead.

![Breadcrumbs module displayed in the Visual Builder](../assets/screenshots/modules/breadcrumbs/overview.png){ loading=lazy }

## Adding a Breadcrumbs Module

When you load the Visual Builder, Divi automatically adds a **[Section](https://intercom.help/elegantthemes/en/articles/9996489-the-divi-regular-section)**.

1. Click the **Green Plus** icon to insert a **[Row](https://intercom.help/elegantthemes/en/articles/10316106-the-divi-row)**.
2. Click the **Gray Plus** icon inside the Row, which will show the list of all available Divi modules.
3. Find the **Breadcrumbs module** and click on it to load it. Alternatively, you can use the Search option to find it.

![Adding the Breadcrumbs Module](../assets/screenshots/modules/breadcrumbs/add-module.png){ loading=lazy }
*Click the gray plus icon to insert the Breadcrumbs module.*

## Use Cases

- **Site-wide navigation aid**: Place the module inside a **[Theme Builder](https://help.elegantthemes.com/en/articles/12022773-build-custom-templates-using-the-theme-builder-in-divi-5)** header so every page on your site shows the same breadcrumb trail.
- **Deep content hierarchies**: Use breadcrumbs on blogs, knowledge bases, or documentation sites where visitors land on pages several levels below the home page.
- **Accessibility and SEO**: Give visitors a visible content trail and search engines a structured navigation path that mirrors your site's information architecture.

## Settings & Options

Once you've added the Breadcrumbs Module, its settings panel opens automatically. The settings are organized into three tabs: **Content**, **Design**, and **Advanced**.

### Content Tab

The Content tab is where you set the home item's text and link, choose a separator, and configure background, link, and other shared options.

![Breadcrumbs Module Content tab](../assets/screenshots/modules/breadcrumbs/settings-content.png){ loading=lazy }
*The Content tab showing home text, URL, and separator options.*

| Setting | Type | Description |
|---------|------|-------------|
| Home Text | text | The label for the first item in the trail. Defaults to "Home." Supports [Dynamic Content](https://help.elegantthemes.com/en/articles/13627810-advanced-content-management-using-dynamic-content-in-divi-5). |
| Home URL | url | The destination URL for the first item. Defaults to your site's home page. Supports [Dynamic Content](https://help.elegantthemes.com/en/articles/13627810-advanced-content-management-using-dynamic-content-in-divi-5). |
| Separator | text | The character or symbol that appears between each item in the trail (for example, **/** , **>** , or **\|** ). |
| [Link](https://help.elegantthemes.com/en/articles/10066994) | group | Make the entire Breadcrumbs Module clickable, sending visitors to a page, section, or external URL when they click anywhere on the module. |
| [Elements](https://help.elegantthemes.com/en/articles/12672584-nested-module-in-divi-5) | toggle | Toggle on or off any optional pieces of the breadcrumb trail. |
| [Background](../options-groups/background.md) | group | Choose the Breadcrumbs Module's background color, gradient, image, video, or pattern. |
| [Loop](https://help.elegantthemes.com/en/articles/11863867-loop-builder-in-divi-5) | group | Enable the Loop Builder to repeat the module across a set of items. |
| [Meta](https://help.elegantthemes.com/en/articles/10066900-understanding-the-meta-option-group-in-divi-5) | group | Set the module's label inside the Visual Builder and force its visibility while editing. |

### Design Tab

All the design styles for the **Breadcrumbs Module** live on this tab.

The Breadcrumbs Module breaks the trail into four sub-elements:
- the **Breadcrumb** wrapper
- the clickable **Breadcrumb link** items
- the **Home link**
- the **Separator** between items

Each sub-element exposes its own **Background**, **Text**, **Sizing**, **Spacing**, **Border**, and **Box Shadow** option groups through Divi 5's **[Composable Settings](https://help.elegantthemes.com/en/articles/14332889-composable-settings-in-divi-5)**. If one of those option groups isn't visible inside a sub-element, hover over the sub-element and click the **Toggle Options** icon to enable it.

![Breadcrumbs Module Design tab](../assets/screenshots/modules/breadcrumbs/settings-design.png){ loading=lazy }
*The Design tab with sub-element styling options.*

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose the visual style for the breadcrumb trail and how items align inside the module. |
| Breadcrumb | group | Style the wrapper that contains the entire trail. Available sub-options: [Background](../options-groups/background.md), [Text](../options-groups/text.md), [Sizing](../options-groups/sizing.md), [Spacing](../options-groups/spacing.md), [Border](../options-groups/border.md), [Box Shadow](../options-groups/box-shadow.md). |
| Breadcrumb Link | group | Style every clickable item in the trail except the home item. Available sub-options: [Background](../options-groups/background.md), [Text](../options-groups/text.md), [Sizing](../options-groups/sizing.md), [Spacing](../options-groups/spacing.md), [Border](../options-groups/border.md), [Box Shadow](../options-groups/box-shadow.md). |
| Home Link | group | Style only the first item in the trail (the one set by Home Text and Home URL). Available sub-options: [Background](../options-groups/background.md), [Text](../options-groups/text.md), [Sizing](../options-groups/sizing.md), [Spacing](../options-groups/spacing.md), [Border](../options-groups/border.md), [Box Shadow](../options-groups/box-shadow.md). |
| Separator | group | Style the symbol or icon that sits between each item. Available sub-options: [Background](../options-groups/background.md), [Text](../options-groups/text.md), [Sizing](../options-groups/sizing.md), [Spacing](../options-groups/spacing.md), [Border](../options-groups/border.md), [Box Shadow](../options-groups/box-shadow.md). |
| [Sizing](../options-groups/sizing.md) | group | Set the Breadcrumbs Module's overall width, height, and alignment. |
| [Spacing](../options-groups/spacing.md) | group | Adjust the module's outer margin and inner padding. |
| [Border](../options-groups/border.md) | group | Add or style the module's border and rounded corners. |
| [Box Shadow](../options-groups/box-shadow.md) | group | Apply a shadow around the module. |
| [Filters](../options-groups/filters.md) | group | Apply visual filters such as hue shifts, saturation changes, and blending modes. |
| [Transform](../options-groups/transform.md) | group | Scale, rotate, skew, or translate the module. |
| [Animation](../options-groups/animation.md) | group | Add an entrance or hover animation to the module. |

**Note**: Save a styled Breadcrumbs Module as a Preset using **[Option Group Presets](https://help.elegantthemes.com/en/articles/10725144-how-to-use-option-group-presets-in-divi-5)** so the same Composable Settings stay enabled everywhere you reuse it.

### Advanced Tab

The Advanced tab gives experienced designers extra control - custom CSS, semantic HTML, conditions, interactions, visibility, transitions, position, and scroll effects.

![Breadcrumbs Module Advanced tab](../assets/screenshots/modules/breadcrumbs/settings-advanced.png){ loading=lazy }
*The Advanced tab with CSS and conditional logic options.*

| Setting | Type | Description |
|---------|------|-------------|
| [Attributes](https://help.elegantthemes.com/en/articles/10102722-understanding-the-custom-css-options-in-divi-5) | group | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the module. |
| [CSS](https://help.elegantthemes.com/en/articles/10102722-understanding-the-custom-css-options-in-divi-5) | text | Add custom CSS to fine-tune the Breadcrumbs Module beyond the built-in design options. |
| [HTML](https://help.elegantthemes.com/en/articles/13284097-semantic-elements-custom-html-wrappers-for-divi-5) | select | Choose the semantic HTML tag wrapping the module (such as **nav** or **div** ). |
| [Conditions](https://help.elegantthemes.com/en/articles/10102758) | group | Show or hide the module based on conditions like logged-in status, post category, or date. |
| [Interactions](https://help.elegantthemes.com/en/articles/11666517-interactions-in-divi-5) | group | Trigger custom behaviors, such as showing or hiding the Breadcrumbs Module when another element is clicked. |
| [Visibility](https://help.elegantthemes.com/en/articles/10102735) | group | Hide the Breadcrumbs Module on phone, tablet, or desktop. |
| [Transitions](https://help.elegantthemes.com/en/articles/10102770) | group | Set how long the module's hover and state animations take. |
| [Position](https://help.elegantthemes.com/en/articles/10102783) | group | Pin the module to a specific spot on the page or relative to its container. |
| [Scroll Effects](https://help.elegantthemes.com/en/articles/10102792) | group | Animate the Breadcrumbs Module as the visitor scrolls. |

## Code Examples

```css
/* TODO: Add CSS targeting .et_pb_breadcrumbs for custom styling */
```

```php
// TODO: Add PHP filters for breadcrumb trail manipulation
```

## Common Patterns

<!-- TODO: Add 2-3 real-world use cases -->

## Elegant Themes tutorials

- [Five New Modules for Divi 5 (Timeline, Breadcrumbs, Table of Contents, SVG, Instagram Feed)](https://www.elegantthemes.com/blog/theme-releases/five-new-modules){:target="_blank"} — release announcement; calls out the Breadcrumbs module as simple but well-suited to Theme Builder templates.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

<!-- TODO: Add common issues and solutions -->

## Related

- [Woo Breadcrumbs Module](woo-breadcrumbs.md)
- [Menu Module](menu.md)
