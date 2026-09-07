---
title: "How to Create a Fixed Navigation that Sticks to the Top When the Page is Scrolled Down"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/3659948-how-to-create-a-fixed-navigation-that-sticks-to-the-top-when-the-page-is-scrolled-down"
---

# How to Create a Fixed Navigation that Sticks to the Top When the Page is Scrolled Down

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/3659948-how-to-create-a-fixed-navigation-that-sticks-to-the-top-when-the-page-is-scrolled-down).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Divi → Theme Builder |  | ilder |
| Add Global Header |  | lobal Headeroption |
| Build Global Header |  | bal Headeroption |
| Section's setting |  | settingby clicking on theGear Icon |
| Content Tab |  | t Tab→Background→Background colorand set a transparent color |
| Design Tab → Sizing |  | → Sizingand set the following options:Width: 100%Max Width: 100%Min Height: 100vh |
| Design Tab → Spacing → Padding |  | → Paddingand set the following values:Padding Top: 0Padding Bottom: 0 |
| Advanced Tab → CSS ID |  | → CSS IDand set it todt-site-header |
| Advanced Tab → Position |  | sition, set the following options:Position: AbsoluteLocation: Top Center |
| Green Plus Icon |  | en Plus Iconto add a1 Column Row |
| Row's setting |  | settingby clicking on theGear Icon |
| Content Tab → Background → Background Color |  | und Colorand set it toWhite |
| Desing Tab |  | esing Tab→Sizingand set the following valuesWidth: 100%Max Width: 100% |
| Advanced Tab → CSS ID |  | → CSS IDand set it todt-menu-wrapper |
| Advanced Tab → Position |  | itionand set the following values:Position: AbsoluteLocation: Bottom Center |
| Wireframe Icon |  | frame mode by clicking on theWireframe Icon |
| Plus Dark Grey Icon |  | rk Grey Iconand add theMenu module. Configure it to your liking. |
| Green Plus Icon |  | en Plus Iconto insert a new Row into the existing Section |
| Plus Dark Grey Icon |  | ick on thePlus Dark Grey Iconand insert twoCode Modules |
| Row's settings |  | dRow's settingsby clicking on theGear Icon |
| Content Tab → Admin |  | b → AdminLabel and type inUtils Row |
| Design Tab → Sizing |  | → Sizingand enable theUse Custom Gutteroption |
| first Code Module |  | e Moduleand paste the following JS code:<script>jQuery(function ($) {var headerHeight = $('#dt-site-header #dt-menu-wrapper').outerHeight();$(window).bind('scroll', function () {var windowHeight = $(window).height();if ($(window).scrollTop() < windowHeight - headerHeight) {$('#dt-site-header').removeClass('dt-fixed');} else {$('#dt-site-header').addClass('dt-fixed');}});});</script> |
| second Code Module |  | e Moduleand paste the following CSS code:#dt-site-header.dt-fixed {position: fixed !important;}.dt-fixed #dt-menu-wrapper {position: fixed !important;bottom: auto;top: 0;} |
| Save Changes |  | ire Theme Builder by clicking on theSave Changesbutton |

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
