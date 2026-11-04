---
title: "Part 5: Building A Divi 5 Homepage From Scratch"
description: "Divi 5 Mastery Course part 5: assembling a seven-section coworking homepage from existing Design Variables and presets using Flexbox and CSS Grid."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15530587-part-5-building-a-divi-5-homepage-from-scratch"
---

# Part 5: Building A Divi 5 Homepage From Scratch

!!! abstract "Quick Reference"
    **What it is:** Part 5 of the Elegant Themes Divi 5 Mastery Course. A tutorial that builds a coworking-space homepage in seven sections.
    **Prerequisite:** The Design Variables (Part 3) and presets (Part 4) are already set up, so the build is mostly assembly.
    **Layout tools used:** Flexbox for most sections, CSS Grid for the features grid, testimonials, and pricing.
    **Result:** Hero, Features Grid, Split Features, Testimonials, Pricing, Countdown, and FAQ, all styled through presets and variables.

## The build approach

Every section follows the same four steps:

1. **Add the Section** and set up its rows and columns. Both Flexbox and CSS Grid controls are available.
2. **Place the modules** in the right columns. Do structure before styling.
3. **Apply presets.** Element Presets (for example on a Heading or Button) set font, size, color, padding, and radius in one click.
4. **Fill in static content:** text, images, video sources, countdown dates, accordion items, and icons.

To create the page, go to **Pages > Add Page** in the WordPress dashboard, title it (for example "Home"), and click **Use Divi Builder**. The global header and footer come later via the Theme Builder (Parts 6 and 7).

!!! tip
    The tutorial points out the Divi AI Agent as a shortcut: opened from the Visual Builder sidebar, it can draft a page from a written brief, a screenshot, or a URL as normal editable Divi elements. It is part of every Divi AI subscription.

## 1. Hero section

Three rows: headline with calls to action, a full-width image, and a three-column statement row.

1. Add a Section using a **Flex Equal Columns** one-column structure.
2. In the column, add a Heading module and a Group module. Put two Button modules inside the Group.
3. On the Group, go to **Design > Layout** and set **Flex Direction** to **Row** and **Horizontal Gap** to **10px**, so the buttons sit side by side.
4. Add a second one-column Flex Equal Columns Row with an Image module for the hero visual.
5. Add a third Row with a three-column Flex Equal Columns structure, each column holding a Heading and a Text module.
6. Apply presets:
    - First Heading: **Heading 1 Big**.
    - Buttons: **Filled - Primary Color** and **Filled - Black**.
    - Image: **Rounded**.
    - Third row: the **Top Border** Option Group Preset on each column's Border group, **30px** top padding, **Heading 4** on the headings, **Dark Text** on the text.
7. Add the copy: heading "Coworking in San Francisco", buttons "Book Tour" and "View Plans", and column headings "Flexible Spaces", "Exceptional Amenities", and "Vibrant Community", each with a short paragraph.

## 2. Features Grid section

Six amenities in an evenly spaced CSS Grid that holds its shape across breakpoints.

1. Add a one-column Flex Equal Columns Section. Under **Design > Background**, set the background color with the **Background - Light Gray** variable. Put a Video module in the first Row.
2. Add a second Row with one column containing an Icon, a Heading, and a Text module, in that order.
3. In the new Row's **Content > Elements**, click **Apply Structure Template** and set:
    - Desktop: three-column grid.
    - Tablet: two-column grid.
    - Mobile: one-column grid.
4. Back on Desktop, duplicate the first column five times for six items.
5. Presets: Video **Rounded**; Icons **Dark - Small - Contained**; titles **Heading 5**; descriptions **Dark Text**. Give each grid column a **Vertical Gap** of **12px**.
6. Add the video source and overlay image, plus six features (Gigabit Wi-Fi, 24/7 Access, Meeting Rooms, Private Phone Booths, Bottomless Coffee, Mailing Address) each with its own icon from the Icon Library and a one- or two-sentence description.

## 3. Split Features section

A tall image on the left, three content blocks on the right.

1. Add a Flex Equal Columns Section with two columns.
2. Left column: an Image module. Right column: a Group containing a Heading and a Text module.
3. Duplicate the Group, add a Button to the bottom of the duplicate, then duplicate that Group again.
4. On each Group, go to **Design > Layout** and set **Flex Direction** to **Column** with a **10px** row gap. Style one Group and use **Extend Attributes** to copy the layout to the others.
5. Presets: Image **Rounded**; first Group Heading **Heading 2** with **Dark Text**; the other two Headings **Heading 5** with **Dark Text**; both Buttons **Text - Primary Color** so they read as inline links.
6. Copy: lead heading "Thrive in a better work environment", and two blocks, "Ergonomic Comfort" and "Inspiring Atmosphere", each with a "Learn More" button.

## 4. Testimonials section

Three quote cards under a heading.

1. Add a one-column Flex Equal Columns Section with a Heading in the first Row.
2. Add a second Row using a **Grid Multi-Column** structure with three equal columns. Each column gets an Icon, a Text module, and a Blurb module.
3. Presets: section Heading **Heading 2**; Row **Horizontal Gap** of **30px**; each column **Outlined - Dark**; Icon **Dark - Small**; Text **Dark Text**; Blurb stacks **Dark Text** and **Dense**, with an **8px** Border Radius on its image (or your rounded image preset).
4. Style the first column, then use **Extend Attributes** to push those styles to matching elements in the parent Row.
5. Copy: heading "Testimonials"; each card has a quotation-mark icon, a quote, and an author photo, name, and role (Lisa Robinson, CEO of Brightwave Media; Albert Flores, Marketing Agency Owner; Cody Fisher, Founder of Sprout Lab).

## 5. Pricing section

The most complex section, built from nested Groups, an Icon List, and a footer Group.

1. Add a one-column Section with a Heading in its first Row.
2. Add a second Row with a **Grid Multi-Column** structure and three columns. Build only the first column at first:
    - A Group containing another Group, which holds a Heading and a Text module.
    - An **Icon List** module as a sibling of the inner Group.
    - A second Group as a sibling, containing a Heading and a Button.
3. Delete the two extra columns for now. Apply the **Outlined - Dark** Border Option Group Preset to the remaining column.
4. Name the three Groups for clarity: Header Group, Inner Group, Footer Group (check the Layers View to confirm which one you are editing). Apply:
    - Header Group: **Contained - Light** on outer cards, **Contained - Dark** on the middle card.
    - Inner Group: **Vertical Gap** of **10px**.
    - Footer Group: **Padding - Medium** Option Group Preset.
    - Tier Headings **Heading 3**, price Headings **Heading 5**.
    - Descriptions **Dark Text** on light cards, **Light Text** on the dark card.
    - Buttons **Filled - Primary Color** on outer cards, **Filled - Black** on the middle card.
    - Icon List **Dark** on light cards, **Light Text** on the dark card.
5. Duplicate the first column twice. On the middle card, switch to the light-text presets and set the card background to **Black**.
6. On the Tablet breakpoint, set the Row's **Content > Elements** Layout Structure to **1 column** with a **30px** Horizontal Gap.
7. Content: Hot Desk at $299/month, Dedicated Desk at $449/month, Private Office at $999+/month, each with a short description, benefits in the Icon List (swapped to right-pointing arrow icons), and a Button.

## 6. Countdown section

A promotional call to action on a bright background.

1. Add a one-column Section and apply the **Contained - Dark** Row Element Preset to its Row.
2. In the column, add a Heading, a **Countdown Timer** module, and a Button.
3. Presets: Heading **Heading 2** and **Center Aligned** with white text; Countdown Timer **Light Text**; Button **Filled - White**.
4. Clear the Countdown Timer's own heading text so the CTA headline stays the main title.
5. Content: heading "Founder's Rates Ending Soon!", a target date matching your promotion, and button text "Lock In Low Rates".

## 7. FAQ section

A short intro on the left and a collapsible question list on the right.

1. Add a Section with a **Flex Offset Columns** structure and two columns. A 2/5 + 3/5 split works well.
2. Left column: a Heading and a Text module. Right column: an **Accordion** module.
3. Presets: Heading **Heading 2**; Text and Accordion **Dark Text**.
4. Content: heading "Frequently asked questions", a short intro, and five Accordion items (for example opening hours, guests, parking, business address use, meeting room bookings).

## Reviewing the result

Every module in the finished page references Design Variables and presets instead of hardcoded hex values, one-off font sizes, or ad hoc padding. That is what makes the page easy to revise and keep consistent. The article also offers a downloadable layout JSON of this homepage and links to the longer version on the Elegant Themes blog.

## Official documentation

[Part 5: Building A Divi 5 Homepage From Scratch](https://help.elegantthemes.com/en/articles/15530587-part-5-building-a-divi-5-homepage-from-scratch)
