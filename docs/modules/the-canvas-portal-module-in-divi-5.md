---
title: "The Canvas Portal Module in Divi 5"
category: modules
tags: ["modules", "canvas", "popup", "overlay", "portal"]
related: ["canvases"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/14718409-the-canvas-portal-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# The Canvas Portal Module in Divi 5

The Canvas Portal module injects content from a detached canvas into a specific spot on your main canvas or Theme Builder template. Instead of letting Divi auto-append canvas content when an interaction triggers, the Canvas Portal renders that canvas exactly where you place it.

## Overview

This makes the module essential when position matters: mega menus anchored to a header link, popups placed relative to a CTA, or reusable content blocks dropped into specific layout spots.

## Adding the Canvas Portal Module

When you load the Visual Builder, Divi automatically adds a **[Section](https://intercom.help/elegantthemes/en/articles/9996489-the-divi-regular-section)**.

1. Click the **Green Plus** icon to insert a **[Row](https://intercom.help/elegantthemes/en/articles/10316106-the-divi-row)**.
2. Click the **Gray Plus** icon inside the Row, which will show the list of all available Divi modules.
3. Find the **Canvas Portal Module** and click on it to load it. Alternatively, you can use the Search option to find it.

![Adding the Canvas Portal Module](../assets/screenshots/modules/canvas-portal/add-module.png){ loading=lazy }
*Click the gray plus icon to insert the Canvas Portal module.*

## Use Cases

1. **Mega menu anchored to a header link**: Build an off-canvas mega menu on its own canvas, then drop a Canvas Portal inside the text or link module that holds the parent menu item. The mega menu renders relative to the link, so it opens exactly where you need it instead of appearing in a default off-canvas position.
2. **Newsletter popup with precise placement**: Design a newsletter popup in a detached canvas and use a Canvas Portal to inject it into a specific section of the page. Combine it with an on-load interaction and a delay, and the pop-up appears in the right spot at the right time while staying out of your way in the builder.
3. **Reusable content blocks across pages**: Build global content such as pricing tables, testimonial sliders, or announcement banners inside a global canvas. Drop a Canvas Portal into any page or Theme Builder template to display that canvas wherever you need it. Update the source canvas once, and every Canvas Portal reflects the change.

## Settings & Options

Once you've added the Canvas Portal Module, the module settings automatically pop up. These settings are organized into three tabs: **Content**, **Design**, and **Advanced**.

### Content Tab

The Content tab is where you pick the canvas the module displays, along with link and background styling.

![Canvas Portal Module Content tab](../assets/screenshots/modules/canvas-portal/settings-content.png){ loading=lazy }
*The Content tab showing canvas selection and link options.*

| Setting | Type | Description |
|---------|------|-------------|
| [Canvas](https://help.elegantthemes.com/en/articles/13249775-divi-5-canvases-off-canvas-menus-popups-canvas-portals) | select | Select an existing canvas from the dropdown to display inside the module. The canvas content renders in place of the Canvas Portal on the front end. |
| [Link](https://help.elegantthemes.com/en/articles/10066994-understanding-the-link-option-group-in-divi-5) | group | Make the entire Canvas Portal clickable, creating a seamless way to direct users to another page, section, or external site. |
| [Background](../options-groups/background.md) | group | Choose the Canvas Portal's background styles. |
| [Meta](https://help.elegantthemes.com/en/articles/10066900-understanding-the-meta-option-group-in-divi-5) | group | Set the Canvas Portal's Label text and force its Visibility inside the Visual Builder. |
| Canvas |  | Select an existing canvas from the dropdown to display inside the module. The canvas content renders in place of the Canvas Portal on the front end. <!-- AUTO-ADDED --> |
| Link |  | Make the entire Canvas Portal clickable, creating a seamless way to direct users to another page, section, or external site. <!-- AUTO-ADDED --> |
| Background |  | Choose the Canvas Portal's background styles. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Canvas Portal's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

All the design styles and options for the **Canvas Portal Module** are in this tab.

![Canvas Portal Module Design tab](../assets/screenshots/modules/canvas-portal/settings-design.png){ loading=lazy }
*The Design tab with sizing and styling options.*

| Setting | Type | Description |
|---------|------|-------------|
| [Sizing](../options-groups/sizing.md) | group | Choose the Canvas Portal's sizing (width, height, alignment). |
| [Spacing](../options-groups/spacing.md) | group | Choose the Canvas Portal's spacing (margin, padding). |
| [Border](../options-groups/border.md) | group | Choose the Canvas Portal's border styles. |
| [Box Shadow](../options-groups/box-shadow.md) | group | Choose the Canvas Portal's Box Shadow styles. |
| [Filters](../options-groups/filters.md) | group | Choose the Canvas Portal's filters, such as hue shifts, saturation changes, and blending modes. |
| [Transform](../options-groups/transform.md) | group | Choose the Canvas Portal's advanced design effects, such as scaling, rotating, skewing, and translating. |
| [Animation](../options-groups/animation.md) | group | Choose the Canvas Portal's animation styles, adding personality and interactivity while keeping a polished, professional feel. |
| Sizing |  | Choose the Canvas Portal's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Canvas Portal's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Canvas Portal's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Canvas Portal's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Canvas Portal's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Canvas Portal's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Canvas Portal's animation styles, adding personality and interactivity while keeping a polished, professional feel. <!-- AUTO-ADDED --> |

### Advanced Tab

The **Advanced tab** provides tools for experienced designers, including options for adding CSS IDs and Classes, controlling visibility, managing transitions, adjusting element positions, and creating scroll effects.

![Canvas Portal Module Advanced tab](../assets/screenshots/modules/canvas-portal/settings-advanced.png){ loading=lazy }
*The Advanced tab with CSS and conditional logic options.*

| Setting | Type | Description |
|---------|------|-------------|
| [Attributes](https://help.elegantthemes.com/en/articles/10102703-understanding-the-attributes-option-group-in-divi-5) | group | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. |
| [CSS](https://help.elegantthemes.com/en/articles/10102722-understanding-the-css-option-group-in-divi-5) | text | Add custom CSS code to fine-tune your Canvas Portal, enabling advanced styling that perfectly aligns with your vision. |
| [HTML](https://help.elegantthemes.com/en/articles/13284097-semantic-elements-custom-html-wrappers-for-divi-5) | select | Choose the semantic HTML tag for the Canvas Portal module. |
| [Conditions](https://help.elegantthemes.com/en/articles/10102758-understanding-the-conditions-options-in-divi-5) | group | Create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. |
| [Interactions](https://help.elegantthemes.com/en/articles/11666517-interactions-in-divi-5) | group | Create custom interactions, such as showing or hiding the Canvas Portal, and many more. |
| [Visibility](https://help.elegantthemes.com/en/articles/10102735-understanding-the-visibility-option-group-in-divi-5) | group | Choose the Canvas Portal's visibility based on different devices. |
| [Transitions](https://help.elegantthemes.com/en/articles/10102770-understanding-the-transitions-option-group-in-divi-5) | group | Choose how long the Canvas Portal's animation takes, adding subtle, impactful animations that enhance user experience and make your module stand out. |
| [Position](https://help.elegantthemes.com/en/articles/10102783-understanding-the-position-option-group-in-divi-5) | group | Choose precise control of the Canvas Portal's placement and create dynamic, visually engaging designs. |
| [Scroll Effects](https://help.elegantthemes.com/en/articles/10102792-understanding-the-scroll-effects-option-group-in-divi-5) | group | Control how the Canvas Portal behaves and transforms during scrolling. |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS code to fine-tune your Canvas Portal, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| HTML |  | Choose the semantic HTML tag for the Canvas Portal module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Interactions |  | Create custom interactions, such as showing or hiding the Canvas Portal, and many more. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Canvas Portal's visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Canvas Portal's animation takes, adding subtle, impactful animations that enhance user experience and make your module stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Canvas Portal's placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Canvas Portal behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

```css
/* TODO: Add CSS targeting .et_pb_canvas_portal for portal-specific styling */
```

```php
// TODO: Add PHP hooks for canvas portal output filtering
```

## Common Patterns

<!-- TODO: Add 2-3 real-world use cases -->

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

<!-- TODO: Add common issues and solutions -->

## Related

- [Canvases](../builder/canvases.md)
- [Toggle Module](toggle.md)
