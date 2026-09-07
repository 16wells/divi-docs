---
title: "How to Add Icons to Divi Blog Posts Based on Their Categories"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8352847-how-to-add-icons-to-divi-blog-posts-based-on-their-categories"
---

# How to Add Icons to Divi Blog Posts Based on Their Categories

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8352847-how-to-add-icons-to-divi-blog-posts-based-on-their-categories).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Posts → Categories |  | ories |
| Add New Category |  | New Categorybutton |
| Gear icon |  | Page which contains the Blog Module and open the Blog module's settings by clicking on theGear icon |
| Advanced Tab → Custom CSS → Free Form CSS |  | m CSSand add this CSS code:selector .et_pb_post[class*="category-"] .entry-title {position: relative;padding-left: 34px;}selector .et_pb_post[class*="category-"] .entry-title::before {font-size: 24px;font-family: 'ETmodules';position: absolute;left: 0;top: 0px;color: #73c32e;}selector .et_pb_post[class*="news"] .entry-title::before {content: "\e059";}selector .et_pb_post[class*="landscape"] .entry-title::before {content: "\e04e";}selector .et_pb_post[class*="houses"] .entry-title::before {content: "\e05a";} |
| news |  | he CSS Code above, you will have to replace thenews,landscape,houseswith your own categories slug text. |
| Dynamic Icons |  | e above CSS code, theDynamic Iconsoption from theDivi → Theme Options → Performance tabshould bedisabled. |

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
