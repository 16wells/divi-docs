---
title: "How to Optimize Divi Layouts for Mobile Devices"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2254621-how-to-optimize-divi-layouts-for-mobile-devices"
---

# How to Optimize Divi Layouts for Mobile Devices

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2254621-how-to-optimize-divi-layouts-for-mobile-devices).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Design Tab |  | esign Taband find the option that you want to change |
| Phone icon |  | hePhone iconto enable the Responsive settings |

### Advanced Tab

| Setting | Type | Description |
|---------|------|-------------|
| Gear icon |  | Section settings by clicking on theGear icon |
| Advanced Tab → CSS ID & Classes → CSS |  | → CSSClass and set a custom CSS class for it. For example, let's useipad-landscape-display |
| Divi → Theme Options → General Tab → Custom CSS |  | SSadd this CSS code:.ipad-landscape-display {display: none;}@media (min-width : 981px) and (max-width : 1024px) {.ipad-landscape-display {display: block;}} |
| ipad-landscape-display |  | is larger than 1024px or smaller than 980px, the element with the CSS classipad-landscape-displaywillnot display. |
| ipad-landscape-display |  | is between 981px and 1024px, the element with the CSS classipad-landscape-displaywill display. |

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
