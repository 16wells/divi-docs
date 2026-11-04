---
title: "Part 14: Mastering the Divi 5 Loop Builder"
description: "Part 14 of the Divi 5 Mastery Course: build a custom, responsive blog feed with the Loop Builder, dynamic content fields, and pagination, and reuse loops in Theme Builder templates."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15704205-part-14-mastering-the-divi-5-loop-builder"
---

# Part 14: Mastering the Divi 5 Loop Builder

!!! abstract "Quick Reference"
    **What it does:** You design one item and Divi repeats it for every matching post, product, term, user, menu, or custom post type.
    **Result of this guide:** A responsive blog page with featured images, titles, excerpts, metadata, Read More buttons, and pagination.
    **Where to enable:** A Row, Column, Group, or supported module, under Content tab > Loop.
    **Course position:** Part 14 of 16. Previous: Part 13 (off-canvas and popups). Next: Part 15 (power user workflow).

!!! tip "Divi AI Agent"
    With a Divi AI subscription, the Divi AI Agent can turn a designed row into a loop, set its source, order, and filters, and connect each module to the right dynamic field from one request. It stops for approval before anything destructive.

## What the Loop Builder does

The Loop is the WordPress mechanism that retrieves and shows content. The Blog module is quick but has a fixed structure. The Loop Builder gives you control of the repeated item's design:

- **Custom layout:** build the item from Divi elements.
- **Dynamic fields:** featured images, titles, terms, authors, dates, excerpts, links.
- **Flexible queries:** posts, products, terms, users, menus, custom post types, and supported custom field data.
- **Design system consistency:** reuse the course's Design Variables and Presets.
- **Theme Builder support:** archives, search results, product archives, and other dynamic views.

## Prepare your site

Create at least 6 to 8 published posts, each with a featured image, title, excerpt, and any categories or tags to show (6 posts lets you test pagination). A test-content plugin such as FakerPress can generate placeholders. Then create and publish a page named **Blog**, open it in the Visual Builder, and add a Heading and any intro content above the loop.

## Build the post card

1. Below the heading section, add a section with a **1 Column Row**. Label the column **Column Looped**.
2. Add an **Image** module (label it Featured Image).
3. Add a **Group** module (label it Right Column) containing:
    - A **Text** module for the category (Post Category)
    - A **Heading** module for the title (Post Title)
    - A nested **Group** (Post Meta Information) with two Text modules for author and publish date (Post Author, Post Publish Date)
    - A **Text** module for the excerpt (Post Excerpt)
    - A **Button** module (Read More Button)

Meaningful labels make the later steps easier to follow.

## Style the two-column layout

1. In the **Row**, go to **Design tab > Layout > Layout Wrapping** and enable **Wrap**.
2. In the **Column Looped** settings, go to **Design tab > Layout** and set **Horizontal** and **Vertical Gap** to `0px`, **Layout Direction** to **Row**, and **Layout Wrapping** to **Wrap**. Under **Border**, apply the **Rounded - Regular** option group preset.
3. **Featured Image:** **Design tab > Sizing > Column Class** to **2/5**.
4. **Right Column** group:
    - **Content tab > Background > Background color**: the **Background - Light Gray** variable.
    - **Design tab > Layout** gaps: the **Spacing - XSmall** variable.
    - **Sizing > Column Class**: **3/5**.
    - **Spacing > Padding**: the **Spacing - Medium** variable.
5. **Post Category** text: Background Color to the **White** variable; **Text Size** to the **Body Small** variable; padding on all four sides to **Spacing - XSmall**.
6. **Post Title** heading: apply the **Heading 3** Element Preset.
7. **Post Meta Information** group: Horizontal Gap **Spacing - XSmall**, Vertical Gap `0px`, Layout Direction **Row**, Align Items **Center**, Sizing Alignment **Start**.
8. Each meta Text module: stack the **Dark Text** and **Small** Element Presets, and set both the paragraph **Text Color** and the link **Link Text Color** to the **Text - Dark Transparent** variable.
9. **Post Excerpt** text: apply the **Dark Text** Element Preset.
10. **Button:** apply the **Text - Primary** Element Preset.

## Enable the loop

1. Open the column's settings and go to **Content tab > Loop**.
2. Enable **Loop Element**.
3. Configure the query: **Order** Ascending, **Posts per Page** 6.

## Connect dynamic content

For each field, hover over it and click **Insert Dynamic Content**.

| Module | Dynamic field |
|---|---|
| Image | Loop Featured Image |
| Post Category text (Body) | Loop Post Terms |
| Post Title heading | Loop Post Title |
| Author text | Loop Author, with "by" in the **Before** field for a byline |
| Publish date text | Loop Publish Date, with `M, Y` in **Custom Date Format** (abbreviated month and year) |
| Excerpt text (Body) | Loop Excerpt |
| Button | Button Text "Read More"; **Loop Link** in the Button Link URL field |

## Add pagination

1. Select the Row containing the looped column and open **Content tab > Elements**.
2. Click **+ Add Element** to insert a new column and label it **Column - Loop Pagination**.
3. Add the **Pagination** module.
4. In its **Content tab > Target**, select **Column - Looped**.

## Make it responsive

On the **Tablet** breakpoint the two-column card fits poorly, so:

1. **Column Looped:** Design tab > Layout > **Layout Direction** to **Column**.
2. **Featured Image:** Sizing > **Column Class** to **100% (Fullwidth)**.
3. **Right Column:** Sizing > **Column Class** to **100% (Fullwidth)**.

Then check typography, spacing, image size, button placement, and column stacking. The ellipsis menu opens the Breakpoints modal to enable or disable breakpoints, and the Responsive Editor handles targeted changes.

## Loops in Theme Builder

You can enable a loop on a Row, Column, Group, or supported module inside a template, to build category, tag, and author archives, search results, product archives, and custom post type archives once.

!!! warning
    For archive templates, set **Query Type** to **Posts for Current Page** so the loop shows the right content for the archive being viewed.

Use Flexbox or CSS Grid for layout, for example Grid for card archives and Flexbox for stacked or horizontal lists.

## Best practices

- Start with Design Variables and Presets, and save the layout to the Divi Library if you will reuse it.
- Test with real titles, excerpts, categories, and images on Tablet and Phone, since dynamic content varies.
- Keep a clear heading hierarchy, give featured images meaningful alt text in WordPress, and confirm links and buttons are keyboard-accessible.
- The same techniques power portfolios, product grids, team directories, event listings, menus, and custom post type archives.

## Official documentation

[Part 14: Mastering the Divi 5 Loop Builder](https://help.elegantthemes.com/en/articles/15704205-part-14-mastering-the-divi-5-loop-builder)
