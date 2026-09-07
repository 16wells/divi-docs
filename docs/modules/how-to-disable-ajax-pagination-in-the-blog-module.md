---
title: "How to Disable AJAX Pagination in the Blog Module"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2912512-how-to-disable-ajax-pagination-in-the-blog-module"
---

# How to Disable AJAX Pagination in the Blog Module

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2912512-how-to-disable-ajax-pagination-in-the-blog-module).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Divi → Theme Option → Integration tab → Header |  | eader |
| insert the Code module |  | in the page layout,insert the Code module |
| Gear icon |  | Blog module's settings by clicking on theGear icon |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand set a custom CSS class such asdt-blog-no-ajax |
| Divi → Theme Option → Integration tab → Header |  | eaderand add this JS code:<script>(function ($) {$(document).ready(function () {$(".dt-blog-no-ajax .pagination a").click(function () {window.location.href = $(this).attr('href');return false;});});})(jQuery);</script> |

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
