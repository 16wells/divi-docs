---
title: "The Contact Form 7 Styler Module in Divi 5"
category: modules
tags: ["modules", "contact-form-7", "form", "cf7", "third-party"]
related: ["contact-form", "login"]
divi_version: "5.3+"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14716484-the-contact-form-7-styler-module-in-divi-5"
---

# The Contact Form 7 Styler Module in Divi 5

![Contact Form 7 Styler Module Overview](../assets/screenshots/modules/contact-form-7-styler/overview.png){ loading=lazy }

## Overview

The **Contact Form 7 Styler** module lets you display any form built with the **Contact Form 7** WordPress plugin inside the Divi Builder and style it like a native Divi contact form.

You manage fields, logic, and email settings inside Contact Form 7 as usual - the Styler module handles the design.

This module requires the **Contact Form 7** plugin to be installed and activated. Any form you create in Contact Form 7 becomes selectable inside the module.

## Adding the Contact Form 7 Styler Module

When you load the Visual Builder, Divi automatically adds a **[Section](https://intercom.help/elegantthemes/en/articles/9996489-the-divi-regular-section)**.

1. Click the **Green Plus** icon to insert a **[Row](https://intercom.help/elegantthemes/en/articles/10316106-the-divi-row)**.
2. Click the **Gray Plus** icon inside the Row, which will show the list of all available Divi modules.
3. Find the **Contact Form 7 Styler module** and click on it to load it. Alternatively, you can use the Search option to find it.

![Adding the Contact Form 7 Styler Module](../assets/screenshots/modules/contact-form-7-styler/add-module.png){ loading=lazy }
*Click the gray plus icon to insert a new module.*

## Use Cases

1. **Styling Existing Contact Form 7 Forms**: Apply consistent Divi styling to forms you've already built in Contact Form 7 without rebuilding them as Divi contact forms.
2. **Advanced Form Logic with Divi Design**: Use Contact Form 7's advanced validation, conditional fields, and third-party integrations while keeping the form's look aligned with your Divi site.
3. **Migrating Existing Sites to Divi**: Keep the Contact Form 7 forms from a site you're redesigning with Divi and restyle them in place instead of recreating them.

## Settings & Options

Once you've added the Contact Form 7 Styler module, the module settings automatically pop up. These settings are organized into three tabs: **Content**, **Design**, and **Advanced**.

### Content Tab

The Content tab lets you select which Contact Form 7 form to display and configure the module's general content settings.

![Contact Form 7 Styler Module Content tab](../assets/screenshots/modules/contact-form-7-styler/settings-content.png){ loading=lazy }
*The Content tab showing form selection and background options.*

| Setting | Type | Description |
|---------|------|-------------|
| Form | select | Choose which Contact Form 7 form to display from the dropdown of forms you've created in the Contact Form 7 plugin. |
| Elements | toggle | Toggle on/off nested module capability. See [nested modules](https://help.elegantthemes.com/en/articles/12672584-nested-module-in-divi-5) for details. |
| [Background](../options-groups/background.md) | group | Choose the Contact Form 7 Styler module's background color, gradient, image, or video. |
| [Loop](https://help.elegantthemes.com/en/articles/11863867-loop-builder-in-divi-5) | group | Enable the Loop Builder to repeat the module across a set of items. |
| [Order](https://help.elegantthemes.com/en/articles/11754241-understanding-divi-s-new-flexbox-layout) | option | Choose the order in which the Contact Form 7 Styler module appears inside a Flexbox and Grid layout. |
| [Meta](https://help.elegantthemes.com/en/articles/10066900-understanding-the-meta-option-group-in-divi-5) | group | Set the module's Label text and force its Visibility inside the Visual Builder. |

### Design Tab

All the design styles and options for the **Contact Form 7 Styler** module are in this tab. Styles you set here apply to the rendered Contact Form 7 form.

![Contact Form 7 Styler Module Design tab](../assets/screenshots/modules/contact-form-7-styler/settings-design.png){ loading=lazy }
*The Design tab with field styling options.*

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose the Layout Style: Block, [Flex](https://help.elegantthemes.com/en/articles/11754241-understanding-divi-s-new-flexbox-layout) (default), or [Grid](https://help.elegantthemes.com/en/articles/12350654-understanding-divi-s-css-grid-layout). |
| Input | group | Style the Input and Textarea fields with background, text, and spacing options. |
| Checkbox | group | Style the Checkbox field types. |
| Radio | group | Style the Radio buttons field types. |
| [Button](https://help.elegantthemes.com/en/articles/10259854-understanding-the-button-option-group-in-divi-5) | group | Choose the submit button styles. |
| Success Message | group | Style the form's submission success message. |
| Validation Message | group | Style the form's validation message. |
| Acceptance Message | group | Style the form's acceptance message. |
| Invalid Form Message | group | Style the form's invalid message. |
| Failure Message | group | Style the form's failure message. |
| Spam Message | group | Style the form's spam message. |
| [Sizing](../options-groups/sizing.md) | group | Choose the Contact Form 7 Styler module's sizing (width, height, alignment). |
| [Spacing](../options-groups/spacing.md) | group | Choose the Contact Form 7 Styler module's spacing (margin, padding). |
| [Border](../options-groups/border.md) | group | Choose the Contact Form 7 Styler module's border styles. |
| [Box Shadow](../options-groups/box-shadow.md) | group | Choose the Contact Form 7 Styler module's Box Shadow styles. |
| [Filters](../options-groups/filters.md) | group | Choose the module's filters, such as hue shifts, saturation changes, and blending modes. |
| [Transform](../options-groups/transform.md) | group | Choose the module's advanced design effects, such as scaling, rotating, skewing, and translating. |
| [Animation](../options-groups/animation.md) | group | Choose the module's animation styles. |

### Advanced Tab

The **Advanced tab** provides tools for experienced designers, including options for adding CSS IDs and Classes, controlling visibility, managing transitions, adjusting element positions, and creating scroll effects.

![Contact Form 7 Styler Module Advanced tab](../assets/screenshots/modules/contact-form-7-styler/settings-advanced.png){ loading=lazy }
*The Advanced tab with CSS and conditional logic options.*

| Setting | Type | Description |
|---------|------|-------------|
| [Attributes](https://help.elegantthemes.com/en/articles/10102722-understanding-the-custom-css-options-in-divi-5) | group | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. |
| [CSS](https://help.elegantthemes.com/en/articles/10102722) | text | Add custom CSS code to fine-tune your Contact Form 7 Styler module. |
| [HTML](https://help.elegantthemes.com/en/articles/13284097-semantic-elements-custom-html-wrappers-for-divi-5) | select | Choose the semantic HTML tag for the Contact Form 7 Styler module. |
| [Conditions](https://help.elegantthemes.com/en/articles/10102758) | group | Create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. |
| [Interactions](https://help.elegantthemes.com/en/articles/11666517-interactions-in-divi-5) | group | Create custom interactions, such as showing or hiding the module, and many more. |
| [Visibility](https://help.elegantthemes.com/en/articles/10102735) | group | Choose the module's visibility based on different devices. |
| [Transitions](https://help.elegantthemes.com/en/articles/10102770) | group | Choose how long the module's animation takes. |
| [Position](https://help.elegantthemes.com/en/articles/10102783) | group | Choose precise control of the module's placement and create dynamic, visually engaging designs. |
| [Scroll Effects](https://help.elegantthemes.com/en/articles/10102792) | group | Control how the module behaves and transforms during scrolling. |

## Code Examples

```css
/* TODO: Add CSS targeting .et_pb_cf7_styler for form field styling */
```

```php
// TODO: Add CF7 filter hooks for custom validation or submission handling
```

## Common Patterns

<!-- TODO: Add 2-3 real-world use cases -->

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

<!-- TODO: Add common issues and solutions -->

## Related

- [Contact Form Module](contact-form.md)
- [Login Form Module](login.md)
