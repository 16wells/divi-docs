---
title: "How to Change the Image's Aspect Ratio Displays on the Portfolio Module"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8352400-how-to-change-the-image-s-aspect-ratio-displays-on-the-portfolio-module"
---

# How to Change the Image's Aspect Ratio Displays on the Portfolio Module

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8352400-how-to-change-the-image-s-aspect-ratio-displays-on-the-portfolio-module).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Gear icon |  | Portfolio module's setting by clicking on theGear icon |
| Design tab → Layout |  | → Layoutand choose theGridoption |
| Advanced Tab → Custom CSS → Free Form CSS |  | m CSSand add this CSS  codeselector {--aspect-ratio-width: 16;--aspect-ratio-height: 9;--aspect-ratio: calc(var(--aspect-ratio-height) / var(--aspect-ratio-width));--padding-top: calc(var(--aspect-ratio) * 100%);}selector .et_portfolio_image {padding-top: var(--padding-top);display: block;position: relative;}selector .et_portfolio_image img {position: absolute;aspect-ratio: var(--aspect-ratio-width) / var(--aspect-ratio-height);top: 0;left: 0;right: 0;bottom: 0;object-fit: cover;width: 100%;height: 100%;} |
| Aspect Ratio of 1/1 (square) |  |  |
| Aspect Ratio of 16/9 |  |  |
| Aspect Ratio of 4/3 |  |  |
| Aspect Ratio of 3/2 |  |  |
| Aspect Ratio of 9/16 |  |  |
| Aspect Ratio of 3/4 |  |  |
| Aspect Ratio of 2/3 |  |  |

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
