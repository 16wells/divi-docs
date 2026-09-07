---
title: "How to Increase the Height of Divi's Custom CSS Box"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8352706-how-to-increase-the-height-of-divi-s-custom-css-box"
---

# How to Increase the Height of Divi's Custom CSS Box

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8352706-how-to-increase-the-height-of-divi-s-custom-css-box).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Divi Child theme |  | vate aDivi Child theme |
| WordPress Dashboard → Appearance → Theme Files Editor |  | ditor |
| functions.php |  | ions.phpfile and add this PHP code after the existing codefunction divi_admin_custom_css() {echo '<style id="divi-increase-css-box-height">#divi_custom_css + .CodeMirror-wrap{height: 800px !important;resize: both;overflow: auto;}</style>';}add_action( 'admin_head', 'divi_admin_custom_css' ); |
| Code Snippets |  | ctivate theCode Snippetsplugin |
| Only run in the administration area |  | the administration area |

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
