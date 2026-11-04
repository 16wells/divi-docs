---
title: "Why the Site Shows the Wrong Header or a Menu Listing Every Page in Divi 5"
description: "Why Divi 5 pages fall back to the WordPress default header with an all-pages menu, and how to fix it in Theme Builder."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15443412-why-the-site-shows-the-wrong-header-or-a-menu-listing-every-page-in-divi-5"
---

# Why the Site Shows the Wrong Header or a Menu Listing Every Page in Divi 5

!!! abstract "Quick Reference"
    **Symptom:** Some or all pages show a plain header with the site title and a menu listing every page, often only on newly created pages.
    **Cause:** WordPress is falling back to its default header because no Divi template applies to the page.
    **Fixes:** Enable the Default Website Template, assign a Primary Menu, check which template applies, clear caches.

## What is going on

- The **Default Website Template** in Theme Builder is disabled, so pages without a custom template get the default WordPress header.
- The fallback header shows the menu assigned to the **Primary Menu** location. With none assigned, WordPress auto-generates a menu of every published page.
- The page uses a custom template that has no header of its own.
- A stale cache is serving an old header.

!!! tip "Divi AI Agent"
    If you have a Divi AI subscription, the Divi AI Agent in Ask mode can list your Theme Builder templates, tell you which one applies to a page, and then assign a menu to the Primary Menu location or fix display conditions. Example prompt: ask why your custom header is not showing on a page, and have it list templates without changing anything yet.

## Fix 1: Enable the Default Website Template

This template controls the header, body, and footer for every page not assigned to a custom template.

1. Go to **Divi > Theme Builder**.
2. Find the **Default Website Template** (the first card). If it is grayed out or crossed out, click its eye icon to enable it.
3. Click **Save Changes** and reload the affected page.

Once enabled, new pages without a custom Header template use your Global Header and Global Footer automatically.

## Fix 2: Assign a Primary Menu

Do this even when your Divi header works, since it is the fallback whenever no Divi template applies.

1. Go to **Appearance > Menus** and select (or create) the menu.
2. Under **Menu Settings**, check the **Primary Menu** display location.
3. Click **Save Menu**.

## Fix 3: Check which template applies

If only some pages are affected, a custom template may be taking over.

1. Go to **Divi > Theme Builder** and review each custom template's assignment.
2. Make sure a template meant to show your site-wide header has a header area. The Global Header is not used automatically on a custom template whose header was removed, so re-add it or remove the template assignment.
3. Save and reload.

## Fix 4: Clear caches

1. Go to **Divi > Theme Options** and click **Clear CSS Cache**.
2. Clear any caching plugin and server cache, then reload in a private window.

Re-saving Theme Builder (open it and click **Save Changes**) forces Divi to regenerate the header sitewide.

## Still having trouble

- Test with **Safe Mode** (**Divi > Support Center**). If the header looks right, a plugin or custom code is interfering.
- If the page body is blank rather than the header, see [Why the Page Is Blank or Missing Content](why-the-page-is-blank-or-missing-content-on-the-live-site-in-divi-5.md).
- For cache steps, see [Why the Live Page Looks Different From the Visual Builder](why-the-live-page-looks-different-from-the-visual-builder-in-divi-5.md).
- If it persists, send support a link to an affected page and a screenshot of your Theme Builder templates.

## Official documentation

[Why the Site Shows the Wrong Header or a Menu Listing Every Page in Divi 5](https://help.elegantthemes.com/en/articles/15443412-why-the-site-shows-the-wrong-header-or-a-menu-listing-every-page-in-divi-5)
