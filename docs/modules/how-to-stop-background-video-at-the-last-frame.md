---
title: "How to Stop Background Video at the Last Frame"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2834586-how-to-stop-background-video-at-the-last-frame"
---

# How to Stop Background Video at the Last Frame

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2834586-how-to-stop-background-video-at-the-last-frame).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand type instop_bg_video |
| WordPress Dashboard → Divi → Theme Options → Integrations Tab |  | s Taband paste in this JS code<script>(function ($) {$(document).ready(function () {$('.stop_bg_video video').each(function () {$(this).removeAttr('loop');$(this).mediaelementplayer({autoRewind: false});});setTimeout(function () {$(window).trigger('resize');}, 500);});})(jQuery);</script> |

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
