---
title: "The Gravity Form Module in Divi 5"
description: "The Divi 5 module that embeds any Gravity Forms form and gives every part of it its own styling group."
category: modules
tags: [modules]
related: []
divi_version: "5.11+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15945400-the-gravity-form-module-in-divi-5"
---

# The Gravity Form Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A module that displays a form built with the Gravity Forms plugin and lets you style each part of it.
    **Requires:** The Gravity Forms plugin installed and activated. Any form you create there becomes selectable in the module.
    **Division of labor:** Fields, logic, notifications, and confirmations stay in Gravity Forms; the module handles design and embedding.

## Add the module

1. In the Visual Builder, click the green plus icon to insert a Row into the Section.
2. Click the gray plus icon inside the Row to open the module list.
3. Find **Gravity Form** (or search for it) and click it.

## Use cases

- **Style existing forms** without rebuilding them.
- **Advanced logic with Divi design:** keep Gravity Forms' conditional logic, multi-page forms, and integrations while matching the look of your site.
- **Multi-step forms:** show a paged form with a styled progress bar and next/previous buttons.

## Content tab

### Gravity Form group

| Setting | Description |
|---|---|
| Form | Dropdown of the forms created in Gravity Forms; choose the one to display |
| Use Ajax | Submits the form without a page reload using Gravity Forms' built-in Ajax. Off by default (standard page-reload submission) |
| Show Validation Messages (Builder Preview) | Visual Builder only: renders the real validation summary and field messages so you can style them. Does not change the live form |
| Show Confirmation Message (Builder Preview) | Visual Builder only: replaces the form preview with a sample confirmation message so you can style it. Does not change the live form |

### Other Content settings

| Setting | Description |
|---|---|
| Elements | Add [nested modules](https://help.elegantthemes.com/en/articles/12672584-nested-module-in-divi-5) |
| Background | Background styles |
| Loop | Enables the Loop Builder |
| Order | Position in a Flexbox or Grid layout |
| Meta | Label text and forced visibility inside the Visual Builder |

## Design tab

Styles here apply to the rendered form. Each part of a Gravity Forms form has its own group.

| Setting | Styles |
|---|---|
| Layout | Layout Style: Block, Flex (default), or Grid |
| Title Text | The form title |
| Description | The form description |
| Section Heading Text | Headings created by Gravity Forms' Section field |
| Legend Text | The heading above grouped fields (radio and checkbox groups, Name and Address fields) |
| Input | Input and textarea fields |
| Checkbox | Checkbox fields |
| Radio | Radio button fields |
| Required Marker Text | The marker flagging required fields, such as an asterisk |
| Progress Bar Text | The progress bar on multi-page forms |
| Submit button | The submit button |
| Next page button | The next-page button on multi-page forms |
| Previous page button | The previous-page button on multi-page forms |
| Validation Summary | The summary shown at the top of the form when submission fails |
| Field Validation Text | The messages shown under individual fields |
| Confirmation Text | The message shown after a successful submission |
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
| Interactions | Custom interactions such as showing or hiding the module |
| Visibility | Visibility per device |
| Transitions | Duration of animations |
| Position | Precise placement |
| Scroll Effects | Behavior during scrolling |

Save the page with `CMD + S` (Mac) or `CTRL + S` (PC), or use the **Save** and **Exit** buttons.

## Official documentation

- [The Gravity Form Module in Divi 5](https://help.elegantthemes.com/en/articles/15945400-the-gravity-form-module-in-divi-5)
