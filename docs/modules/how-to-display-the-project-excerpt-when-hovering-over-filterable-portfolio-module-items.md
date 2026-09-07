---
title: "How to Display the Project Excerpt When Hovering Over Filterable Portfolio Module Items"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/3192295-how-to-display-the-project-excerpt-when-hovering-over-filterable-portfolio-module-items"
---

# How to Display the Project Excerpt When Hovering Over Filterable Portfolio Module Items

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/3192295-how-to-display-the-project-excerpt-when-hovering-over-filterable-portfolio-module-items).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Child theme for Divi |  | equires having aChild theme for Diviinstalled and activated. |
| Move the Filterable Portfolio module |  | from the parent theme to your child theme folder. |
| WordPress Dashboard → Appearance → Theme Files Editor |  | ditor |
| custom-FilterablePortfolio.php |  | olio.phpfrom your child theme folder |
| WordPress Dashboard → Projects |  | the Excerpt text is added by editing each of the Projects inWordPress Dashboard → Projectsand filling in the Excerpt field for each project |
| Gear icon |  | Portfolio module's settings by clicking on theGear icon |
| Advanced Tab → Custom CSS → Free Form CSS |  | m CSSand add this CSS code:selector .dt-excerpt {z-index: -1;position: absolute;top: 0;left: 0;display: block;width: 100%;height: auto;opacity: 0;pointer-events: none;-webkit-transition: all 0.3s;transition: all 0.3s;-webkit-box-sizing: border-box;box-sizing: border-box;-webkit-backface-visibility: hidden;backface-visibility: hidden;-webkit-font-smoothing: antialiased;text-align: center;padding: 10px;}selector .et_portfolio_image:hover .dt-excerpt {z-index: 3;opacity: 1;}selector .et_overlay::before {top: calc(50% + 20px);} |
| (optional) |  | Add styling for the new Excerpt text by opening the Filterable Portfolio module's settings and adding this CSS  code toAdvanced Tab→Custom CSS→Free Form CSSselector p.project-excerpt {color: black;padding: 10%;text-align: center;position: absolute;bottom: 25px;} |

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
