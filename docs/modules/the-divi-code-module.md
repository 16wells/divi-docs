---
title: "The Divi Code Module"
description: "Reference for the Divi 5 Code module, which inserts HTML, CSS, JavaScript, or shortcodes anywhere in a layout."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/10260309"
---

# The Divi Code Module

!!! abstract "Quick Reference"
    **What it is:** A module for dropping raw HTML, CSS, JavaScript, shortcodes, or third-party embed code into a page.
    **Where it lives:** Add it from the module library (Gray Plus icon inside a Row) or search for it by name.
    **Key settings:** Text (the code field), Link, Background, Loop, Order, Meta.

## Add the module

1. In the Visual Builder, click the **Green Plus** icon to add a Row to the Section.
2. Click the **Gray Plus** icon inside the Row to open the module library.
3. Find the **Code** module and click it, or use the search box.

## Use cases

- **Third-party plugins:** Paste a plugin's shortcode to place its output exactly where you want it.
- **Custom JavaScript:** Add scripts for interactivity such as custom animations or form validation.
- **Custom CSS:** Add CSS snippets directly on the page for styling the standard options can't reach.

## Settings

### Content tab

Add your code, set a module link, and style the background.

| Setting | Description |
|---|---|
| Text | The code field. Accepts HTML, CSS, and JavaScript. |
| Link | Turns the whole Code module into a link to a page, section, or external URL. |
| Background | Background color, gradient, image, video, pattern, or mask for the Code module. |
| Loop | Switches on the [Loop](../builder/loop-builder.md) so the module repeats for each item in a query. |
| Order | Sets where the module sits in a [Flexbox](../builder/understanding-divi-s-new-flexbox-layout.md) or Grid layout. |
| Meta | A custom label for the module and an option to force its visibility inside the Visual Builder. |

!!! note
    Wrap CSS in `<style></style>` tags and JavaScript in `<script></script>` tags so the browser treats them as code.

### Design tab

Design options for the Code module.

| Setting | Description |
|---|---|
| Text | Overall text styles for the module. |
| Sizing | Width, height, and related sizing for the Code module. |
| Spacing | Margin and padding around and inside the module. |
| Border | Border and corner styling. |
| Box Shadow | Drop shadow styling. |
| Filters | Hue, saturation, brightness, and blend-mode adjustments. |
| Transform | Scale, rotate, skew, and translate effects. |
| Animation | Entrance animation styles. |

### Advanced tab

Options for fine control over markup, visibility, and behavior.

| Setting | Description |
|---|---|
| Attributes | A CSS ID, reusable CSS classes, or custom HTML attributes, handy for hooking into your child theme's stylesheet or custom CSS. |
| CSS | Custom CSS for fine-tuning the Code module. |
| HTML | Picks the [semantic HTML tag](../builder/semantic-elements.md) the module outputs. |
| Conditions | Shows or hides the module based on rules, so different visitors see different content. |
| Interactions | Custom [Interactions](../builder/interactions.md), such as showing or hiding the module on a trigger. |
| Visibility | Hides the module on selected device sizes. |
| Transitions | Duration and timing of hover and state transitions. |
| Position | Precise placement of the module on the page. |
| Scroll Effects | How the module moves or changes as the visitor scrolls. |

## Save your work

Press `Cmd + S` (Mac) or `Ctrl + S` (Windows), or use the **Save** and **Exit** buttons in the Visual Builder.

## Official documentation

- [The Divi Code Module - Elegant Themes Help Center](https://help.elegantthemes.com/en/articles/10260309)
