---
title: "How to Create a Promo Bar in Divi"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8352478-how-to-create-a-promo-bar-in-divi"
---

# How to Create a Promo Bar in Divi

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8352478-how-to-create-a-promo-bar-in-divi).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### Design Tab

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Divi → Theme Builder |  | ilder |
| Gear icon |  | Section's setting by clicking on theGear icon |
| Content Tab → Background → Background |  | ackgroundcolor and set a background color for the entire Section |
| Design Tab → Spacing |  | → Spacingand set theTopandBottomPaddingto 5px - change this value to your liking |
| Advanced Tab → CSS ID & Classes → CSS ID |  | SS IDand typedivi-promo-bar |
| Text |  | theTextmodule and theIconmodule |
| Gear icon |  | Icon module's settings by clicking on theGear icon |
| Advanced Tab → CSS ID & Classes → CSS ID |  | SS IDand typedivi-close-bar |
| Gear icon |  | Row setting by clicking on theGear icon |
| Design Tab → Sizing |  | → Sizingand:Enable the optionUse Custom GutterWidthSet the Gutter's value to 0 |
| Use Custom Gutter |  | Use Custom GutterWidth |
| Design Tab → Spacing |  | → Spacingand set theTopandBottomPaddingto 0 |
| Content Tab |  | ntent Taband click on the Gear icon for the Column |
| Advanced Tab |  | d Tab→Custom CSS→Free Form CSSand add this CSS Code:selector {display: grid;grid-template-columns: auto 30px;align-items: center;} |
| Divi → Theme Option → Integration tab → Header |  | eaderand add this JS code:<script>(function ($) {$(document).ready(function () {var promoBar = $('#divi-promo-bar');var closeIcon = $('#divi-close-bar');closeIcon.on('click', function () {promoBar.hide();})});})(jQuery)</script> |
| Divi → Theme Options → General Tab → Custom CSS |  | m CSSand add this CSS code:#divi-close-bar:hover {cursor: pointer;} |

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
