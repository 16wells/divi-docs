---
title: "Part 10: Mastering Flexbox in Divi 5"
description: "Part 10 of the Divi 5 Mastery Course: what each Flexbox layout setting does and how to build a responsive three-column layout with variables and presets."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15691996-part-10-mastering-flexbox-in-divi-5"
---

# Part 10: Mastering Flexbox in Divi 5

!!! abstract "Quick Reference"
    **What it is:** Part 10 of the Divi 5 Mastery Course. It explains Divi 5's Flexbox controls and builds a three-column layout with them.
    **Where it lives:** Design tab → Layout option group, on sections, rows, columns, groups, and modules.
    **Prerequisite:** Set **Layout Style** to **Flex** (the default) so the Flexbox settings appear.
    **Builds on:** Earlier parts of the course (the coworking site, Design Variables, and Presets).

## Why Flexbox

Flexbox suits one-dimensional layouts: items arranged mainly in a row or a column, with control over alignment, spacing, distribution, wrapping, and order. In the course site it drives navigation bars, feature rows, testimonial cards, pricing tables, hero content, and event rows. The controls work with [Design Variables](https://help.elegantthemes.com/en/articles/11027601-design-variables-in-divi-5) and [Presets](https://help.elegantthemes.com/en/articles/12817235-stacked-and-nested-presets-in-divi-5) so spacing stays consistent.

## Flexbox settings

To reach them, select an element, open the **Design** tab, and expand **Layout**.

| Setting | Options and behavior |
|---|---|
| Layout Style | **Block** (traditional stacked layouts), **Flex** (default; row or column alignment), **CSS Grid** (two-dimensional layouts). |
| Horizontal Gap | Space between items side by side. Supports unit selection and Design Variables. |
| Vertical Gap | Space between items stacked top to bottom. Same unit and variable support. |
| Layout Direction | **Row** (default, left to right), **Row Reverse**, **Column** (top to bottom), **Column Reverse**. |
| Justify Content | Distribution along the main axis: Start, Center, End, Space Between, Space Around, Space Evenly. Horizontal in Row, vertical in Column. |
| Align Items | Alignment on the cross axis: Start, Center, End, Stretch. Vertical in Row, horizontal in Column. |
| Layout Wrapping | **No Wrap** (one line), **Wrap**, **Wrap Reverse**. |
| Align Content | Aligns wrapped lines on the cross axis when there is extra space. Only relevant when wrapping is on and there are multiple lines. Options: Stretch, Start, Center, End, Space Between, Space Around, Space Evenly. |

Related tips from the source: Space Between suits headers (logo on one side, links or buttons on the other); Stretch makes cards match height; switching Layout Direction from Row to Column at a breakpoint lets side-by-side items stack on small screens.

## Build a three-column layout

### Set the row gap

1. Add a three-column Row. In **Design → Layout**, confirm **Flex** is selected.
2. Hover **Horizontal Gap**, click the Insert Dynamic Content icon, and apply the **Spacing – Medium** variable.
3. Repeat for **Vertical Gap**.

### Style the columns

1. With the Row selected, go to **Content → Elements** and click Edit on the first column.
2. In **Design → Spacing**, link the Padding sides and apply the **Spacing – Small** variable.
3. Hover the **Border** group, click Assign Presets, and choose **Outlined – Dark**.

### Copy styles to the other columns

1. Right-click the first column and choose **Copy Attributes**.
2. Right-click the second column, choose **Paste Attributes**, then **Paste Column Design Attributes**.
3. Repeat for the third column.

### Add content

1. In the first column, add a **Group** module containing two Heading modules, a Text module, and a Divider module.
2. Outside the Group but still in the column, add an Icon List module and a Button module.
3. Create an element preset named **Pricing Divider** for the Divider: Line color uses the **Border - Dark** variable and Line Position is **Vertically Centered**.
4. Apply earlier presets: **Heading 5** to the first Heading, **Heading 2** to the second, **Dark Text** to the Text module. Create a **Dark List Item** preset for Icon List Items with the icon set to the **Black** color variable.
5. Fill the other columns the same way.

### Adjust gaps

1. In each Group's **Design → Layout**, set **Vertical Gap** to the **Spacing – XSmall** variable.
2. In each column's **Design → Layout**, set **Vertical Gap** to **Spacing – Small**.

### Align the buttons

Differing text lengths can leave buttons at different heights. In each column's **Design → Layout**, set **Justify Content** to **Space Between** so the Group stays at the top and the Button sits at the bottom.

## Responsive adjustments

Use the [Responsive Editor](https://help.elegantthemes.com/en/articles/12105366-responsive-editor-in-divi-5) and [customizable breakpoints](https://help.elegantthemes.com/en/articles/13001900-customize-the-divi-5-s-default-breakpoints); Divi 5 supports up to seven breakpoints, enabled from the Top Bar.

- **Change row structure per breakpoint:** Use **Apply Structure Template** in the Row's Elements group.
- **Center stacked columns:** In each column's **Design → Layout**, hover **Align Items**, click Edit Responsive Values, and set **Center** at the breakpoint.
- **Column width (for example Tablet Wide):** Select the breakpoint, then **Design → Sizing → Column Class** and choose **1/2**.
- **Reorder:** At the breakpoint, open the third column's **Content → Order → Display Order** and set it to `-1` to move it earlier in the row's visual order.

## Tips

- Use the gap controls before adding custom margins to individual modules.
- Use Space Between so card content stays at the top and buttons near the bottom.
- Use Stretch on the parent container for equal-height cards.
- Reference Design Variables for gaps, padding, and widths so updates are easier to manage.

## Resources

- [Download the Flexbox example page layout](https://www.dropbox.com/scl/fi/m5r58912gairtccvc328e/Mastering-Flexbox-in-Divi-5.json?rlkey=xoja82j0rryaxgnoviyz5q8k6&st=v17t0vme&dl=1)
- [Full tutorial on the Elegant Themes blog](https://www.elegantthemes.com/blog/divi-resources/part-10-mastering-flexbox-in-divi-5)
- Previous: [Building the Core Inner Pages of Your Divi 5 Website](https://help.elegantthemes.com/en/articles/15533059-building-the-core-inner-pages-of-your-divi-5-website). Next: [Mastering CSS Grid in Divi 5](https://help.elegantthemes.com/en/articles/15702426-mastering-css-grid-in-divi-5)

## Official documentation

[Part 10: Mastering Flexbox in Divi 5](https://help.elegantthemes.com/en/articles/15691996-part-10-mastering-flexbox-in-divi-5)
