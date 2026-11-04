---
title: "Part 7: Building a Custom Footer in Divi 5"
description: "Part 7 of the Divi 5 Mastery Course: build a global Theme Builder footer with three styled columns and an auto-updating copyright row, using Design Variables and Element Presets."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15530979-part-7-building-a-custom-footer-in-divi-5"
---

# Part 7: Building a Custom Footer in Divi 5

!!! abstract "Quick Reference"
    **Result:** A global footer with three styled columns (brand block, address and socials, contact call to action on an accent background) and a one-line copyright row whose year updates automatically.
    **Built with:** Theme Builder, the Design Variables from Part 3, and the Element Presets from Part 4.
    **Course position:** Part 7 of 16. Previous: Part 6 (header and navigation). Next: Part 8 (Theme Builder global templates).

A footer appears on every page, carries essential business details, reinforces the brand, and gives visitors a last clear path to contact you. Because it relies on existing variables and presets, this build is fast.

## Set up the global footer template

1. Go to **Divi > Theme Builder**.
2. In the **Default Website Template**, click **Add Global Footer > Build Global Footer**.
3. Save the template once so the assignment is committed.
4. Open the layout in the Visual Builder.

## Section settings

1. In the section settings, go to **Content tab > Background** and choose the **Background - Light Gray** option group preset.
2. Go to **Design tab > Layout > Vertical Gap** and set the **Spacing - Medium** variable.
3. Go to **Advanced tab > HTML > Element Type** and choose **Footer**. The look does not change, but browsers, screen readers, and search engines now know this area is the site footer.

## Row settings

1. Add a row and choose the 3-column layout under Equal Columns.
2. In the row's **Design tab > Layout > Layout Wrapping**, set the **Horizontal** and **Vertical** gap to the **Spacing - XSmall** variable.
3. Enable **Wrap**.

## Add the modules

| Column | Modules |
|---|---|
| Column 1 | Image, Text |
| Column 2 | Heading, Social Media Follow |
| Column 3 | Two Headings, Button |

Then add a second row using **Flex Single Column** with one Text module in it.

## Style the columns

1. In the first row, open **Content tab > Elements** and click the edit icon for Column 1.
2. Apply the **Contained - Dark** Element Preset from the Column preset menu.
3. Under **Design tab > Layout**, set **Justify Content** to **Space Between**.
4. Use Extend Design Attribute to copy these styles to Columns 2 and 3.
5. To turn Column 3 into the call-to-action block, open its settings and set **Content tab > Background > Background Color** to the **Primary Color**.

## Responsive column classes

Desktop is the base breakpoint, so its values cascade down unless overridden. Desktop is already handled by the Flex Three Equal Columns choice.

1. Switch to the **Tablet** breakpoint. In Column 1, set **Sizing > Column Class** to **Fullwidth**.
2. Still on Tablet, enable **Grow To Fill** (Design tab > Sizing) on Columns 2 and 3 so they share the remaining width.
3. Switch to **Phone**. Set **Column Class** to **Fullwidth** on Columns 2 and 3.

Together with the row's Wrap setting, this stacks the cards cleanly on mobile.

## Logo image

1. In Column 1's Image module, hover the **Image** field on the Content tab and click **Insert Dynamic Content**.
2. Bind it to the **Logo Light** Design Variable.
3. Set alt text to the brand name, or leave it empty if the brand name is already written beside a purely decorative logo, so screen readers do not announce it twice.
4. Under **Design > Sizing**, set **Max Height** to `64px`.

## Headings

1. Apply the **Heading 5** Element Preset to the Column 2 Heading.
2. Create a second Heading Element Preset named **Heading Light** with its text color set to the **White** Design Variable, and apply it too. If two presets define the same property, the last one applied wins.
3. In **Content tab > Text > Heading**, use Insert Dynamic Content and choose the **Address** Design Variable.
4. Use Extend to apply both presets to the other Headings in the row.
5. For the first Heading in Column 3, choose the **Phone Number** variable the same way.

### Link variables for phone and email

1. Open the Variable Manager and go to **Links**.
2. Create **Link to Phone** with a `tel:` value and **Link to Email** with a `mailto:` value.
3. On each Heading in Column 3, go to **Content tab > Link > Module Link**, use Dynamic Content, and assign the matching variable.

## Social Media Follow

1. Apply the **Isolated Icons - Light** Element Preset.
2. In **Content tab > Elements**, add three Social Network children for the brand's platforms.
3. In each, pick the platform, set the Account Link URL, and apply the **No Background** preset.

The result is a row of white icons with no plate behind each.

## Button

1. In Column 3's Button module, apply the **Field - White** Element Preset.
2. Set **Button Text** to "Send a message".
3. Link it to the contact page URL variable if you made one, or to the same `mailto:` variable used for the email.

## Text modules

1. In Column 1, apply the **Light Text** Element Preset and enter the tagline.
2. In the second row's Text module, stack two presets: **Dark Text** first, then **Small Text**. Order matters because stacked presets cascade: Small Text narrows the type from Body to Body Small, while Dark Text keeps color and link behavior unless a later preset overrides it.
3. In **Content tab > Text > Body**, click Insert Dynamic Content and choose **Current Date**.
4. Put the copyright wording in the **Before** field and the closing sentence in the **After** field.
5. Set **Date Format** to **Custom** and **Custom Date Format** to `Y`. The year then updates automatically each January.
6. Optionally, in the Design tab's Body Text group, apply the **Text - Dark Transparent** variable to Body Text Color for a quieter copyright line.

## Save and verify

- Preview Tablet and Phone: Column 1 full width on Tablet, Columns 2 and 3 sharing the next row, and all cards stacked on Phone.
- Test the social icons, the button link, and the `tel:` and `mailto:` links.

Save the Visual Builder, return to Theme Builder, click **Save Changes**, then check the footer at the bottom of any front-end page.

## Import the ready-made template

Elegant Themes provides a JSON footer layout. Ideally define a WordPress menu first in **Appearance > Menus**, though you can assign it later.

1. Download the JSON file from the official article.
2. Go to **Divi > Theme Builder** and edit or create the **Global Footer**.
3. Click the gear icon at top left and choose **Import**.
4. Select the "Master Course Footer Layout" JSON file.
5. Make sure **Import Presets** is checked.
6. Click **Import Layout**.

## Official documentation

[Part 7: Building a Custom Footer in Divi 5](https://help.elegantthemes.com/en/articles/15530979-part-7-building-a-custom-footer-in-divi-5)
