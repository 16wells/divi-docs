---
title: "How to Control the Contact Form Module's Field Widths in Divi 5"
description: "Set Contact Form field widths in Divi 5 with the Column Class setting: full width, side by side, spacing, and per-device stacking."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15443972-how-to-control-the-contact-form-module-s-field-widths-in-divi-5"
---

# How to Control the Contact Form Module's Field Widths in Divi 5

!!! abstract "Quick Reference"
    **Where:** Each field's settings, Design tab, Sizing, **Column Class**.
    **Requires:** The Contact Form layout set to Flex (the default). Column Class has no effect in Block layout.
    **Divi 4 note:** The old "Make Fullwidth" toggle no longer exists; Column Class replaces it.

The Contact Form module lays out its fields with Flexbox, and every field has its own width setting. No custom CSS is needed.

## Where field widths are set

1. Click the gear icon on the Contact Form module.
2. On the **Content** tab, find the field and click the pencil icon next to it.
3. In the field's settings, go to the **Design** tab and open **Sizing**.
4. Set **Column Class**, which defines the field's width as a column in the flex layout (for example **Fullwidth**, **1/2**, or **1/3**).

## Make a field full width

1. Open the field's settings as above.
2. Go to **Design > Sizing > Column Class** and choose **Fullwidth**.

The field spans the whole form, and later fields move to the next line.

## Place fields side by side

1. Set the first field's **Column Class** to **1/2**.
2. Set the second field's **Column Class** to **1/2** as well.

They now share one line. The same approach works for three fields at **1/3**, four at **1/4**, and so on.

!!! note
    The two fields must sit directly next to each other in the field list. A Fullwidth field between them forces a line break.

## Adjust spacing between fields

Adjust spacing on the Contact Form module itself, not on an individual field:

1. Open the module's settings.
2. On the **Design** tab, open the **Layout** option group.
3. Adjust the horizontal and/or vertical gap values.

!!! tip
    Avoid using the Row's gap settings for field spacing, since they apply to the whole layout and can shift the entire form. Fields Margin targets only the form fields.

## Different widths per device

Field widths are responsive. To make side-by-side fields stack on smaller screens:

1. Edit each field whose Column Class is 1/2, 1/3, and so on.
2. Go to **Design > Sizing**.
3. Switch to the tablet and/or phone breakpoint.
4. Change **Column Class** to 100%.

## Official documentation

[How to Control the Contact Form Module's Field Widths in Divi 5](https://help.elegantthemes.com/en/articles/15443972-how-to-control-the-contact-form-module-s-field-widths-in-divi-5)
