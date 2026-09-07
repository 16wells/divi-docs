---
title: "How to Customize the Blog Module to Include Infinite Scrolling"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8564379-how-to-customize-the-blog-module-to-include-infinite-scrolling"
---

# How to Customize the Blog Module to Include Infinite Scrolling

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8564379-how-to-customize-the-blog-module-to-include-infinite-scrolling).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| YITH Infinite Scrolling |  | eYITH Infinite Scrollingplugin. |
| Row's |  | theRow'ssettings (that contains the Blog module), go toAdvanced Tab → CSS ID & Classes → CSS Class,and type indivi_infinite_blog_wrapper |
| Blog module |  | g modulesettings, and in theContent Tab → Post Count,set it to 9 or any other multiplier of 3. The value should not be less than9for the Infinite Scrolling to work correctly. |
| Design Tab → Layout |  | ayoutand chooseFullwidth. |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand type in:divi_blog_infinite_scroll |
| Advanced Tab → Custom CSS → Free Form CSS |  | m CSSand paste in this CSS snippet:selector .et_pb_ajax_pagination_container {display: grid;grid-template-columns: repeat(3, 1fr);gap: 30px;}selector .et_pb_ajax_pagination_container .et_pb_post {margin-bottom: 0;border: 1px solid #ddd;padding: 30px;}selector .et_pb_ajax_pagination_container .et_pb_post .entry-featured-image-url {margin: -30px -30px 30px -30px;}@media (min-width: 768px) and (max-width: 980px) {selector .et_pb_ajax_pagination_container {grid-template-columns: repeat(2, 1fr);gap: 20px;}selector .et_pb_ajax_pagination_container .et_pb_post {padding: 20px;}selector .et_pb_ajax_pagination_container .et_pb_post .entry-featured-image-url {margin: -20px -20px 20px -20px;}}@media (max-width: 767px) {selector .et_pb_ajax_pagination_container {grid-template-columns: repeat(1, 1fr);gap: 30px;}} |
| WordPress Dashboard → YITH → Infinite Scrolling |  | lling. |
| .divi_blog_infinite_scroll .pagination |  | tion Selector:.divi_blog_infinite_scroll .paginationNext Selector:.divi_blog_infinite_scroll .pagination .alignleft aItem Selector:.divi_blog_infinite_scroll .et_pb_postContent Selector:.divi_infinite_blog_wrapper |
| .divi_blog_infinite_scroll .pagination |  | e_scroll .pagination |
| .divi_blog_infinite_scroll .pagination .alignleft a |  | n .alignleft a |
| .divi_blog_infinite_scroll .et_pb_post |  | ll .et_pb_post |
| .divi_infinite_blog_wrapper |  | nite_blog_wrapper |

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
