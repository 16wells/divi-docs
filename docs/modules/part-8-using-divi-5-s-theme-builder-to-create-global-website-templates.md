---
title: "Part 8: Using Divi 5’s Theme Builder To Create Global Website Templates"
description: "Divi 5 Mastery Course part 8: planning global Theme Builder templates and building a full All Posts template with Dynamic Content, Variables, and presets."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15531015-part-8-using-divi-5-s-theme-builder-to-create-global-website-templates"
---

# Part 8: Using Divi 5’s Theme Builder To Create Global Website Templates

!!! abstract "Quick Reference"
    **What it is:** Part 8 of the Elegant Themes Divi 5 Mastery Course. It covers Theme Builder templates for posts, categories, authors, search, and 404, then builds the All Posts template step by step.
    **Where:** WordPress dashboard > **Divi > Theme Builder**.
    **Key ideas:** Design Variables and presets keep templates consistent; Dynamic Content fills each template with live WordPress data.

## Why global templates matter

The Theme Builder lets you design a layout once and assign it to part of the site. One template can drive every blog post, another every category archive, and so on. Design Variables hold shared values (colors, spacing, typography, radii) and presets package them into reusable styles, so templates stay consistent without restyling each module.

**Dynamic Content** is the other half: it pulls post titles, featured images, author details, dates, categories, and post content from WordPress, so one layout shows different content for each post or archive.

## Create a template

1. Go to **Divi > Theme Builder**. If you followed the course, the **Default Website Template** already holds the global header and footer.
2. Click **+ Add New Template** and choose **Build New Template**.
3. Assign it to the area it should control (here, **All Posts**).
4. Click **Create Template**.
5. Click **Add Custom Body**, then **Build Custom Body** to open the Visual Builder.

Repeat for each template, choosing its assignment in the **Template Settings** modal.

## Use Dynamic Content

1. Open the settings of the module you want to fill.
2. Click the **Insert Dynamic Content** icon in a supported text, image, heading, or other field.
3. Pick the data you want; Divi connects the field to it.
4. Some fields also offer **Before** and **After** text, for example "Posted on" before a date or "By" before an author name.

## Templates for the coworking site

| Template | Purpose | Typical contents |
|---|---|---|
| **All Posts** | Individual blog posts | Post title, featured image, Post Content module, date, author name and bio, comment count, previous/next navigation, comments, optional related posts |
| **All Category Pages** | Posts in one category (for example Events, Office Tours, Member Stories) | Dynamic archive title plus a Blog module or Loop Builder layout for the current category |
| **All Author Pages** | Posts by one author | Dynamic author name, picture, and bio, plus a post list or loop for that author |
| **Search Results** | What visitors see after searching | A Search module for repeat searches, plus a Blog module or Loop Builder layout for results; module settings can exclude content types, pages, posts, or categories |
| **404 Page** | Missing pages | Search module, recent posts, popular links, or a call to action back to the homepage, styled with Variables and presets |

The **Post Content** module outputs the body of whichever post is being viewed, so styling it once applies your design system to every post.

## Build the All Posts template

These steps assume the All Posts template exists and its custom body is open in the Visual Builder.

### Step 1: Post Title and Content section

1. Open **Layers View**, double-click the Section name, rename it **Post Title and Content**, and press Return.
2. With the Section selected, go to **Design > Layout** and apply the **Spacing - Medium** variable to **Vertical Gap** (this uses Flexbox layout).

**Post Title module**

1. Add a single-column Row, then a **Post Title** module.
2. On the **Content** tab, turn off **Show Featured Image**. A separate Image module will handle it.
3. On the **Design** tab, open **Title Text**, click the **Preset** icon, and choose **Heading 1**.
4. Open **Meta Text**, set **Meta Font Style** to **Italics**, and apply the **Body** number variable to **Meta Text Size**.

**Featured image**

1. Add an **Image** module with the **Rounded** element preset.
2. On the **Content** tab, in the **Image** option group, click the **Insert Dynamic Content** icon on the Image field and choose **Featured Image**.

**Post Content module**

1. Add the **Post Content** module to the Row.
2. On the **Design** tab, open **Heading Text**. For **Heading Text Size**, apply the matching **H1** through **H6** number variables to each heading level.
3. For **Heading Line Height**, apply the **Line Height - Headings** variable at every level.
4. Open **Body Text** and apply your **Dark Text** option group preset.

**Row and column settings**

1. Select the Row, go to **Design > Layout**, and set **Align Items** to **Center**.
2. On the Row's **Content** tab, click the edit icon for the Column.
3. In the Column's **Design > Layout**, apply **Spacing - XSmall** to **Vertical Gap**.

**Post navigation**

1. Add another single-column Row and place a **Pagination** module in it.
2. Under **Content > Text > Previous/Next Link**, enter the labels you want.

### Step 2: Post Author section

1. Add a Section named **Post Author** (in Layers) with a **1/4 + 3/4** Row.
2. On the first Column, go to **Design > Sizing** and set **Column Class** to **1/8**. Set the second Column's class to **21/24**.
3. On the Row, open **Layout** and apply **Spacing - Medium** to both **Horizontal Gap** and **Vertical Gap**.

First column:

- Add an **Image** module, use **Insert Dynamic Content** on the Image field to choose **Author Profile Picture**, and apply the **Rounded** element preset.

Second column:

- A **Heading** module with the **Heading 4** preset; in its **Text** option group, insert dynamic **Post Author**.
- A **Text** module with the **Dark Text** preset; insert dynamic **Author Bio** in its **Text** option group.
- A **Button** module with **Filled - Primary Color**; in its **Text** option group use dynamic **Post Author** with "More Posts by" in the **Before** field, and set the Link option group's **Button Link URL** to dynamic **Author Page Link**.

### Step 3: Related Posts section

1. Add a Section named **Related Posts** with a single-column Row.
2. Add a **Heading** module (**Heading 2** preset) reading "Related Posts".
3. Add a **Blog** module:
    - Content tab: in the **Content** group set **Post Count** to **3**; in **Elements** turn off **Show Pagination**.
    - Design tab: **Heading 4** on **Title Text**, **Dark Text** on **Body Text**, **Small Text** on **Meta Text**.

### Step 4: Post Comments section

1. Add a Section named **Post Comments** with a single-column Row and a **Comments** module.
2. On the **Design** tab:
    - **Form Title Text**: **Heading 2** preset.
    - **Button**: **Filled - Primary Color** preset.
    - **Meta Text**: **Body Small** variable on **Meta Text Size**, **Line Height - Body** on **Meta Line Height**.
    - **Comment Text**: **Body** variable on **Comment Text Size**, **Line Height - Body** on **Comment Line Height**.

### Step 5: Test responsiveness

Divi 5 supports up to seven customizable breakpoints in the Visual Builder's Top Bar.

- Click the ellipsis menu beside the responsive icons to enable or disable breakpoints.
- Enter a width in the responsive width field, or click the responsive icons to cycle through active breakpoints.
- For module values, hover a responsive-capable field, click **Edit Responsive Values**, and set each breakpoint in one place with the Responsive Editor.

## Tips and best practices

- **Name everything** in the Layers panel so large templates stay navigable.
- **Reference Variables and presets** wherever possible; changing a shared variable then updates every template using it.
- **Use the Loop Builder** instead of the standard Blog module for Category and Author pages when you need more control over each repeated post item.
- **Export templates** as JSON from the Theme Builder for backups and reuse on other sites.
- **Test with real content:** publish test posts with featured images, varied lengths, several authors, categories, and comments before launch.

## Download and import the finished templates

The article links a JSON file (`coworking-website-global-website-templates.json`) containing the global header, global footer, All Posts, All Category Pages, Author Pages, Search Results, and 404 templates. Have at least one blog post with a featured image before importing.

1. Go to **Divi > Theme Builder**.
2. Click the **Import & Export** icon.
3. Open the **Import** tab.
4. Select the JSON file.
5. Click **Import Divi Theme Builder Templates**.

## Official documentation

[Part 8: Using Divi 5’s Theme Builder To Create Global Website Templates](https://help.elegantthemes.com/en/articles/15531015-part-8-using-divi-5-s-theme-builder-to-create-global-website-templates)
