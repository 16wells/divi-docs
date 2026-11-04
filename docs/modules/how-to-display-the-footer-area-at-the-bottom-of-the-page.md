---
title: "How to Display the Footer Area at the Bottom of the Page"
description: "Two ways to keep a Divi 5 footer pinned to the bottom of short pages: a Theme Builder fixed-position setting, or a small script in Theme Options."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/9909636-how-to-display-the-footer-area-at-the-bottom-of-the-page"
---

# How to Display the Footer Area at the Bottom of the Page

On pages with little content, the footer can float up and leave empty space beneath it. Divi gives you two ways to keep it anchored to the bottom of the screen.

!!! abstract "Quick Reference"
    **What it solves:** A footer that sits mid-screen on short pages.
    **Option A:** Theme Builder, with the footer section's Position set to Fixed and aligned bottom center.
    **Option B:** A script pasted into Divi → Theme Options → Integration, which fixes the footer only when the page is shorter than the window.

## Option A: Use the Theme Builder

1. Go to **Divi → Theme Builder**.
2. Edit your Global Footer layout, or create one.
3. Open the settings of the Section that holds your footer content.
4. Go to **Advanced tab → Position** and set the position to **Fixed**. See [Position Options](../options-groups/position.md).
5. Set the **Alignment** to **bottom center**.

## Option B: Use a script (no Theme Builder)

1. In the WordPress dashboard, go to **Divi → Theme Options → Integration** (see [Integration Settings](../theme-options/integration.md)).
2. Paste the following into the head/body code area:

```html
<script id="change-footer-position">
document.addEventListener('DOMContentLoaded', function () {
  if (document.body.offsetHeight < window.innerHeight) {
    var footer = document.querySelector('footer');
    footer.style.position = 'fixed';
    footer.style.bottom = '0px';
    footer.style.left = '0';
    footer.style.right = '0';
  }
});
</script>
```

3. Save the changes and check a short page on the front end.

## Notes

- The script only acts when the page content is shorter than the browser window, so long pages keep their normal footer.
- It targets the first `<footer>` element on the page. If your footer is built differently, adjust the selector.
- A fixed element leaves the normal page flow, so check that it does not cover content on your own layouts. The Theme Builder option applies the fixed position on every page that uses that footer template.

## Official documentation

[How to Display the Footer Area at the Bottom of the Page](https://help.elegantthemes.com/en/articles/9909636-how-to-display-the-footer-area-at-the-bottom-of-the-page)
