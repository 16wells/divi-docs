---
title: "Part 9: Building the Core Inner Pages of Your Divi 5 Website"
description: "Part 9 of the Divi 5 Mastery Course: building a Contact page and an Events page for a coworking site by reusing presets, design variables, and Flex layouts."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15533059-part-9-building-the-core-inner-pages-of-your-divi-5-website"
---

# Part 9: Building the Core Inner Pages of Your Divi 5 Website

!!! abstract "Quick Reference"
    **What it is:** Part 9 of the Divi 5 Mastery Course. You build a Contact page and an Events page for the coworking-space site.
    **Prerequisites:** Homepage, global header and footer, and Theme Builder templates done, plus presets and Design Variables from earlier parts.
    **Tools used:** Page Manager, Command Center, Extend Attributes, element and option group presets, spacing variables.
    **Previous / next:** Part 8 (Theme Builder templates) and Part 10 (Flexbox).

Because the header and footer load globally and presets and variables already control color, typography, spacing, and borders, this stage is mostly structural assembly with a few new presets.

## Contact page

**Create it:** WordPress Dashboard > **Pages > Add Page**, name it Contact, **Publish**, click the Divi builder button, and choose **Build From Scratch**.

**Structure** (two sections):

1. Section one, three rows:
    1. A one-column row with a Heading module (page heading).
    2. A two-column row using the fifth Offset Columns structure. Left column: Contact Form module. Right column: a Group module containing a Heading and a Text module, duplicated twice for three contact blocks. In each Group, set **Design > Layout > Vertical Gap** to the **Spacing - XSmall** variable.
    3. A one-column row with a Map module. The Map module needs a valid Google Maps API key.
2. Section two: a single-column Flex row with a Heading and an Accordion module (FAQ).

**Presets:**

| Module | Preset |
|---|---|
| First Heading | Heading 1 |
| Group headings (right column) | Subheading |
| Group text modules | Small Text |
| Contact Form | Dark |
| Map | Black and White (sets Filters Saturate to 0%, turns Mouse Wheel Zoom off, adds rounded corners) |
| FAQ heading | Heading 2 |
| Accordion | Stack **Dark Text** (text color, divider style, toggle icon) and **Contained** (rounded corners, light gray item background) |

**Content:** a heading such as "Get in touch" or "Book a Tour & Say Hello"; phone, email, and address in the three groups; an FAQ heading; and accordion items with a question as the title and the answer as body text.

## Events page

Create it the same way, naming it Events. If the Visual Builder is already open, the Page Manager can create the page from inside the builder. The page has three sections: a featured event with countdown, an upcoming events list, and a subscribe section.

### Featured event section

**Structure:**

1. A one-column row with a Heading (page title).
2. A two-column row.
    - Left column: three Heading modules, one Text module, one Countdown Timer module, in that order. (The Command Center can add these faster by keyboard.)
    - Right column: a Group module (Heading and Text), then a Text module, then a Button module.

**Presets:**

| Element | Presets and settings |
|---|---|
| First row Heading | Heading 1 |
| Second row | Contained - Dark |
| Left: first Heading | Subheading + Light, heading level H2 |
| Left: second Heading | Heading 2 + Light, level H3 |
| Left: third Heading | Heading 5 + Light, level H3 |
| Left: Text | Light Text + Small Text |
| Left: Countdown Timer | Light Text - Dense |
| Right: Group Heading / Text | Heading 3 + Light / Light Text |
| Right: Text | Light Text + Small Text |
| Right: Button | Filled - Primary Color |

**Content:** "Community Events"; "Featured Event"; "Startup Pitch Night & Mixer"; "August 24 - 25"; a description; the Countdown Timer pointed at the event start date with its heading text removed; "$25", "/person", and a "Reserve your spot" button.

**Layout refinements:** left Column Class 3/5 with Vertical Gap set to the **Spacing - Small** variable (and an internal 20px gap for the stacked details); right Column Class 2/5; in the right Group set Flex Direction to Row, Align Items to Flex End, and Horizontal Gap to **Spacing - XSmall** so the price and qualifier share a baseline.

### Upcoming events list section

**Structure:** a new Section. Row one: Equal Columns Flex with a Heading. Row two: three equal columns.

- Left: a Heading and a Text module (date block).
- Middle: a Heading, a Blurb module, and a Text module.
- Right: a Group (Heading and Text) with a Button below.

**Presets:** first-row Heading uses Heading 2; the left column uses Contained - Light plus the Background - Light Gray option group preset; middle Heading uses Heading 3, Blurb uses Dense, Text uses Dark Text; right Group Heading uses Heading 3 and Text uses Dark Text; the Button uses Filled - Primary Color.

**Content:** "Events"; date "17." over "Sep."; a title such as "Dominate local search: SEO strategies for small businesses"; a Blurb with a location icon and a venue as its title (default body deleted); a description; "$59.", "/person", and an "RSVP" button.

**Refinements:**

- Second row: Padding Bottom set to **Spacing - Medium**; the Bottom Border options group preset.
- Left column: Vertical Gap 0px; Column Class set to No Column Class.
- Middle column: Vertical Gap **Spacing - Small**; Grow to Fill on; Column Class 3/5. In the Blurb, Image/Icon Placement set to Left.
- Right column: Layout Direction Row; Justify Content End; Align Items End; Layout Wrapping Wrap; No Column Class.

### Subscribe section

1. Add a Section with a one-column Row, and an Email Optin module.
2. Apply the **Contained - Dark** element preset to the Row and the **Background - Light Gray** option group preset to its Background. Apply the **Dark** element preset to the Email Optin (the source also names a Signup - Dark preset for the module).
3. Set the title to "Subscribe to Events Newsletter", remove the body text, connect your email provider under Email Account, and turn off Show First Name Field and Show Last Name Field.

## Layout downloads

The source article links downloadable JSON layouts for both pages. See the official article to get them.

## Official documentation

[Part 9: Building the Core Inner Pages of Your Divi 5 Website](https://help.elegantthemes.com/en/articles/15533059-part-9-building-the-core-inner-pages-of-your-divi-5-website) on the Elegant Themes Help Center. Back to [Part 1](part-1-what-to-prepare-before-building-your-divi-5-website.md).
