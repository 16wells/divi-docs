---
title: "How to Open or Close All Toggle Modules Using the Button Module"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8352354-how-to-open-or-close-all-toggle-modules-using-the-button-module"
---

# How to Open or Close All Toggle Modules Using the Button Module

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8352354-how-to-open-or-close-all-toggle-modules-using-the-button-module).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Gear Icon |  | Button's module settings by clicking on theGear Icon |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand type indivi-open-toggle-button |
| Advanced Tab → CSS ID & Classes → CSS Class |  | controlled, click on the button, open the settings, and go toAdvanced Tab → CSS ID & Classes → CSS Classand type indivi-open-toggle-module |
| WordPress Dashboard → Divi → Theme Options → Integrations Tab |  | s Taband copy/paste this jQuery code:<script>$(document).ready(function () {$('.divi-open-toggle-button').click(function (e) {e.preventDefault();$('.divi-open-toggle-module').each(function () {if ($(this).hasClass('et_pb_toggle_close')) {$(this).removeClass('et_pb_toggle_close').addClass('et_pb_toggle_open');$(this).find('.et_pb_toggle_content').show();} else {$(this).removeClass('et_pb_toggle_open').addClass('et_pb_toggle_close');$(this).find('.et_pb_toggle_content').hide();}});});});</script> |

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
