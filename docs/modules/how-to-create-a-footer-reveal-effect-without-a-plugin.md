---
title: "How to Create a Footer Reveal Effect Without a Plugin"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8374589-how-to-create-a-footer-reveal-effect-without-a-plugin"
---

# How to Create a Footer Reveal Effect Without a Plugin

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8374589-how-to-create-a-footer-reveal-effect-without-a-plugin).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Divi |  | oDivi→Theme Builderand create a Footer layout. This could be a Global Footer or a Footer layout assigned to a specific page. |
| Advanced Tab |  | tion that contains all the footer information and go toAdvanced Tab→CSS ID & Classes→CSS Classand inputdivi-site-footer-section. |
| Advanced Tab |  | d Tab→Positionand set its position toFixed |
| Location |  | ocationoption and set the position to beBottom Centered |
| Divi |  | oDivi→Theme Options→General Tab→Custom CSSand add this CSS code:#page-container:has(.divi-site-footer-section) #main-content{z-index: 2;position: relative;} |
| Divi |  | oDivi→Theme Option→Integration tab→Headerand add this JS code:<script id="divi-reveal-footer-effect">(function ($) {function diviCalcFooterHeight() {var footerHeight = $('.divi-site-footer-section').outerHeight();$('#main-content').css('margin-bottom', footerHeight);}$(document).ready(function () {diviCalcFooterHeight();});$(window).on('resize', diviCalcFooterHeight)})(jQuery);</script> |

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
