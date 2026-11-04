---
title: "Why the Page Is Blank or Missing Content on the Live Site in Divi 5"
description: "Diagnose and fix a Divi 5 page that looks complete in the Visual Builder but is blank or partly rendered on the live site."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15393605-why-the-page-is-blank-or-missing-content-on-the-live-site-in-divi-5"
---

# Why the Page Is Blank or Missing Content on the Live Site in Divi 5

!!! abstract "Quick Reference"
    **Symptom:** The page looks right in the Visual Builder but is blank, shows only a title, or renders only part of the layout on the live site.
    **Most common cause:** A Theme Builder template's Custom Body is replacing the page content.
    **Fix order:** Clear cache, check Theme Builder templates, check Custom Body visibility, check the homepage setting, test in Safe Mode.

## Likely causes

- A Theme Builder template (the **Default Website Template** or a custom one) is assigned to the page and its **Custom Body** replaces your content.
- A custom template body lacks the **Post Content** module, so the page's own content has nowhere to display.
- The wrong page is set as the WordPress homepage.
- A stale cache is serving an old or empty version.

## Fix 1: Clear the Divi 5 CSS cache

1. Go to **Divi > Theme Options**.
2. Click **Clear CSS Cache** at the top right.
3. Reload the live page.

You can also append `?nocache=1` to the page URL. If the page is still blank with it, caching is not the cause.

## Fix 2: Check for a Theme Builder template overriding the page

1. Go to **Divi > Theme Builder**.
2. Review the **Default Website Template** and any custom template that could apply to the page.
3. Open the applicable template and inspect its **Custom Body**.

Look for two problems:

- **Empty or sparse body.** A Custom Body replaces the page content on the front end, which explains seeing only a background or logo. Add the missing design to the template, or remove the Custom Body so the page shows its own content.
- **No Post Content module.** Add the **Post Content** module to the template body wherever the page content should appear, then save.

!!! note
    Assigning a template to a page that already had a different template makes the newly saved one take precedence and removes the old assignment. Divi warns you before this happens.

## Fix 3: Confirm the Custom Body is not hidden

1. Go to **Divi > Theme Builder** and find the template assigned to the page.
2. Check the Custom Body's visibility (eye) icon. If it is crossed out, click it to make the body visible.
3. Do the same check for the Custom Body inside the Default Website Template.

## Fix 4: Confirm the homepage setting

If only the homepage is affected:

1. Go to **Settings > Reading**.
2. Under **Your homepage displays**, select **A static page**.
3. Set the **Homepage** dropdown to the page you built.
4. Save and reload.

## Fix 5: Test in Safe Mode

1. Go to **Divi > Support Center** and turn **Safe Mode** on. It disables plugins, your child theme, and custom code for your account only.
2. Reload the page.

If the content appears, turn Safe Mode off and reactivate plugins one at a time, clearing caches and rechecking after each. The last plugin you enabled before the page goes blank again is the conflict.

## Still having trouble

- If the page is not blank but looks different or out of date, see [Why the Live Page Looks Different From the Visual Builder](why-the-live-page-looks-different-from-the-visual-builder-in-divi-5.md).
- If the content shows but the header is wrong or the menu lists every page, see [Why the Site Shows the Wrong Header](why-the-site-shows-the-wrong-header-or-a-menu-listing-every-page-in-divi-5.md).

When contacting support, include a link to the affected page, a screenshot comparing the Builder and live site, and a note of which templates are assigned in the Theme Builder.

## Official documentation

[Why the Page Is Blank or Missing Content on the Live Site in Divi 5](https://help.elegantthemes.com/en/articles/15393605-why-the-page-is-blank-or-missing-content-on-the-live-site-in-divi-5)
