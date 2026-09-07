---
title: "How to Change the Number of Columns in the Blog Module"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2310880-how-to-change-the-number-of-columns-in-the-blog-module"
---

# How to Change the Number of Columns in the Blog Module

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2310880-how-to-change-the-number-of-columns-in-the-blog-module).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Design Tab → Layout |  | ayoutand chooseGrid |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Class |
| dt-4-columns-blog |  | dt-4-columns-blog |
| Divi → Theme Options → General Tab → Custom CSS, |  | S,add the following CSS code:@media (min-width: 981px) {.dt-4-columns-blog .et_pb_salvattore_content[data-columns]::before {content: '4 .column.size-1of4' !important;}.dt-4-columns-blog .column.size-1of4 {width: 24% !important;margin-right: 1%;}.dt-4-columns-blog .et_pb_post {margin-bottom: 11px;}} |
| Design Tab → Layout |  | ayoutand chooseFullwidth |
| Advanced Tab → |  | Tab →Custom CSS →Free Form CSS |
| Advanced Tab |  | S code uses CSS Grid and CSS variables. When the code is added toAdvanced Tab→Custom CSS→Free Form CSS, the syntax checker will flag many of the rules as invalid.Please ignore that. |
| --no-of-columns |  | change the number of columns, change the value of the--no-of-columnsproperty inside each of the media query |
| 4 Columns layout |  | ill change the Blog module's Fullwidth layout to:4 Columns layouton desktop3 Columns layouton tablet1 Column layouton phone |
| 4 Columns layout |  | on desktop |
| 3 Columns layout |  | on tablet |
| 1 Column layout |  | on phone |

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
