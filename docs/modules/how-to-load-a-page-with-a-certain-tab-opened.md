---
title: "How to Load a Page with a Certain Tab Opened"
description: "Link visitors to a page with a specific Tabs module tab already open, using a dt-tabs ID attribute and a URL hash."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/16958621"
---

# How to Load a Page with a Certain Tab Opened

!!! abstract "Quick Reference"
    **What it is:** A link such as `https://your-domain-name.com/page-slug/#dt-tabs|1` that opens a chosen tab of the [Tabs module](the-divi-tabs-module.md).
    **Setup:** Give the module the ID `dt-tabs` via an ID attribute, then link to the page with `#dt-tabs|N`.
    **Numbering:** Zero-based. `|0` is the first tab, `|1` the second, `|2` the third.

## Steps

1. Open the page containing the Tabs module in the Visual Builder.
2. Open the module's settings by clicking it or its **Gear icon**.
3. Go to **Advanced tab → Attributes** and click **+ Add Attributes**.
4. Choose **id** and set the **Attribute Value** to `dt-tabs`.
5. Go to **WordPress Dashboard → Appearance → Menus**.
6. Add a **Custom Link** with the URL `https://your-domain-name.com/page-slug/#dt-tabs|1` and any label.

The same URL works as the Link on a Button module or anywhere else you can place a link.

## Scroll to the Tabs module too

If the module sits far down the page, add this script so the browser scrolls to it after opening the tab.

1. Go to **WordPress Dashboard → Divi → Theme Options → Integrations tab**.
2. Paste the script below on that tab.

```html
<script>
  (function ($) {
    $(document).ready(function () {
      var hash = document.location.hash;
      if (hash) {
        var hashLenght = hash.match(/#(.*?)(.*?)(?=\|)/);
        if (hashLenght && hashLenght[0]) {
          var loggedIn = ($('#wpadminbar').length) ? $('#wpadminbar').outerHeight() : 0;
          var diviHeader = ($('#main-header').length) ? $('#main-header').outerHeight() : 0;
          var tbHeader = ($('.et-l.et-l--header .et_pb_sticky_module').length) ? $('.et-l.et-l--header .et_pb_sticky_module').outerHeight() : 0;
          var headerHeight = loggedIn + diviHeader + tbHeader;
          $('html, body').animate({
            scrollTop: ($(hashLenght[0]).offset().top - headerHeight)
          }, 500);
        }
      }
    });
  })(jQuery);
</script>
```

## Gotchas

- Tab numbering starts at 0, so `|1` opens the second tab.
- The script accounts for the admin bar, Divi's main header, and sticky Theme Builder headers when scrolling.

## Official documentation

[How to Load a Page with a Certain Tab Opened](https://help.elegantthemes.com/en/articles/16958621) (Elegant Themes Help Center)
