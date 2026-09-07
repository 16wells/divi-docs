---
title: "How to Disable the AJAX Pagination for the Blog Module using the WP PageNavi Plugin"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8570102-how-to-disable-the-ajax-pagination-for-the-blog-module-using-the-wp-pagenavi-plugin"
---

# How to Disable the AJAX Pagination for the Blog Module using the WP PageNavi Plugin

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8570102-how-to-disable-the-ajax-pagination-for-the-blog-module-using-the-wp-pagenavi-plugin).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard  → Plugins → Add new plugin |  | lugin. |
| WP-PageNavi |  | rch form(on the top right corner) and search forWP-PageNavi. |
| WP-PageNavi plugin. |  | e theWP-PageNavi plugin. |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand type indivi_blog_module_custom_nav |
| Divi → Theme Option → Integration tab > Header |  | eaderand add this jQuery code:<script id="divi-disable-ajax-pagination-blog-module">(function ($) {$(document).ready(function () {$(".divi_blog_module_custom_nav .wp-pagenavi a").click(function () {window.location.href = $(this).attr('href').replace('?et_blog', '');return false;});});})(jQuery);</script> |

## Code Examples

<!-- TODO: Add CSS/PHP code examples -->

## Common Patterns

<!-- TODO: Document 2-3 common usage patterns -->

## Troubleshooting

<!-- TODO: Document common issues and solutions -->

## AI Interaction Notes

| Task | Confidence | Notes |
|------|-----------|-------|
| Basic placement | 🔬 Needs Testing | Untested — stub page |
| Settings configuration | 🔬 Needs Testing | Untested — stub page |
| Custom styling | 🔬 Needs Testing | Untested — stub page |

## Related

<!-- TODO: Add links to related documentation pages -->
