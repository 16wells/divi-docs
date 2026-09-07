---
title: "How to Change the Site's Logo When the Page is Scrolled"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2346897-how-to-change-the-site-s-logo-when-the-page-is-scrolled"
---

# How to Change the Site's Logo When the Page is Scrolled

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2346897-how-to-change-the-site-s-logo-when-the-page-is-scrolled).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Divi → Theme Options → General Tab |  | l Tab |
| Fixed Navigation Bar |  | Navigation Baroption is enabled |
| Divi → Theme Options → General Tab → Custom CSS |  | m CSSand add this CSS Code:.et-fixed-header #logo {content: url(https://demo.divi.tech/wp-content/uploads/divi-logo-white.svg)} |
| Content Tab → Logo |  | go image is added to the Menu module'sContent Tab → Logo |
| Stick at Top |  | module is set to beStick at TopinAdvanced Tab → Scroll Effects, add this CSS code toAdvanced Tab→Custom CSS→Free Form CSS:selector.et_pb_sticky--top .et_pb_menu__logo img {content: url(https://demo.divi.tech/wp-content/uploads/divi-logo-white.svg)} |
| Section's settings → Advanced Tab → Scroll Effects |  | t to Sticky at Top in theSection's settings → Advanced Tab → Scroll Effects, add this CSS code to theSection'sAdvanced Tab→Custom CSS→Free Form CSS:selector.et_pb_sticky--top .et_pb_menu__logo img {content: url(https://demo.divi.tech/wp-content/uploads/divi-logo-white.svg)} |

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
