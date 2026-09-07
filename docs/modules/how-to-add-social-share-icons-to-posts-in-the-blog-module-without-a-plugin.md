---
title: "How to Add Social Share Icons to Posts in the Blog Module Without a Plugin"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8575022-how-to-add-social-share-icons-to-posts-in-the-blog-module-without-a-plugin"
---

# How to Add Social Share Icons to Posts in the Blog Module Without a Plugin

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8575022-how-to-add-social-share-icons-to-posts-in-the-blog-module-without-a-plugin).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Rank Math |  | nd activate theRank Mathplugin. |
| Blog Module |  | g Module's settings, go toAdvanced Tab → CSS ID & Classes → CSS Class,and type indivi_blog_with_sharing_icons. |
| Advanced Tab → Custom CSS → Free-Form CSS, |  | Custom CSS → Free-Form CSS,and paste in this CSS code:selector .divi-social-share-icons-wrapper {position: absolute;bottom: 10px;padding-left: 10px;}selector .et_pb_no_thumb .divi-social-share-icons-wrapper {position: relative;bottom: auto;padding-left: 0;padding-top: 10px;}selector .divi-social-share-icons-wrapper .divi-social-icon-link span::before {font-family: ETModules;font-size: 16px;color: white;padding: 4px 8px;border-radius: 5px;display: inline-block;margin-right: 10px;}selector .divi-social-share-icons-wrapper .divi-social-icon-link .divi-icon-facebook::before {content: "";background-color: #3b5998;}selector .divi-social-share-icons-wrapper .divi-social-icon-link .divi-icon-twitter::before {content: "";background-color: #000000;}selector .divi-social-share-icons-wrapper .divi-social-icon-link .divi-icon-linkedin::before {content: "";background-color: #007bb6;} |

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
