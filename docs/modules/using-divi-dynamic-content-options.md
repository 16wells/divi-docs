---
title: "Using Divi Dynamic Content Options"
description: "How to pull live WordPress data into Divi 5 content fields and apply design variables to Design tab options."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/11622973"
---

# Using Divi Dynamic Content Options

!!! abstract "Quick Reference"
    **Content tab:** Hover over a text-based field and click the Dynamic Content icon to insert live data (title, excerpt, author, custom fields, and more).
    **Design tab:** Click the Dynamic Content icon on an option to apply a [global variable](../builder/design-variables.md) (number, font, color).
    **Best for:** Templates that adapt to each post, and design systems you can update in one place.

Dynamic content lets a layout reflect your site's data and shared design values instead of fixed text and numbers. See also [Dynamic content](../builder/dynamic-content.md).

## Dynamic content in the Content tab

Dynamic content can supply values such as:

- Page or archive title
- Post or page excerpt
- Publish date
- Comment count
- Post or page link
- Author and author bio
- Site title and tagline
- Current date

It can also display native custom fields, ACF fields, and Toolset fields.

### Use it in a field

This works mainly in text-based modules such as Text, Blurb, Call to Action, and Button.

1. Open the module settings with the Gear icon or by clicking the module.
2. In the Content tab, hover over a text-based option such as Body, Title, or Module Link URL.
3. Click the **Dynamic Content** icon.
4. Choose one of the options.

The **Manage Global Strings** entry at the top opens the variable manager, where you define global strings available to dynamic content (see [Design variables](../builder/design-variables.md)).

### Example: author bio in a post template

1. Open the [Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md) and create or edit the template assigned to All Posts, adding a custom body layout.
2. Add a [Post Title module](the-divi-post-title-module.md) to pull in the current post's title.
3. Add a Text module for the meta info and use the dynamic icon to insert the author and publish date.
4. Add another Text module for the bio and choose Author Bio from the dynamic options.
5. Style the area with spacing, fonts, or a divider.

Every post then shows its own title, author, date, and bio without manual edits.

## Dynamic content in the Design tab

In the Design tab, the Dynamic Content icon applies [design variables](../builder/design-variables.md), which are shared values for colors, fonts, numbers, and text strings. Change the variable once and every place using it updates.

### Use it in an option

Create at least one global variable first, for example a number for spacing, a font, or a color.

1. Open the module settings.
2. In the Design tab, open the option group, such as Spacing.
3. Hover over the option, such as Padding Top.
4. Click the **Dynamic Content** icon.
5. Choose the variable.

Only variable types the option supports are listed, so a number option shows number variables only. The manage button follows suit (numbers, fonts, or colors) and opens the variable manager on that type. See [Global variables](../builder/global-variables.md).

### Example: consistent branded buttons

1. In the variable manager, create a color variable (for example Primary Brand Color), a number variable for button radius, a font variable, and a text variable for the button label.
2. Add a Button module. In Design > Button, turn on **Use Custom Styles for Button**.
3. Set the background to the color variable, the button font to the font variable, and the border radius to the number variable using the Dynamic Content icon.
4. Optionally save the result as a preset with **New Preset From Current Styles** (see [Option group presets](../builder/option-group-presets.md)).
5. Later, update the color variable and every button using it changes across the site.

## Divi AI Agent

The [Divi AI Agent](the-divi-ai-agent-in-divi-5.md) can list the dynamic content options for the current post type and connect a field to one from a plain-language request. It is part of the Divi AI subscription.


## Official documentation

- [Using Divi Dynamic Content Options (Elegant Themes Help Center)](https://help.elegantthemes.com/en/articles/11622973)
