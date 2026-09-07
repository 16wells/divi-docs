---
title: "How to Include the Post/Page's Title in the Contact Form's Email Body"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/7190539-how-to-include-the-post-page-s-title-in-the-contact-form-s-email-body"
---

# How to Include the Post/Page's Title in the Contact Form's Email Body

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/7190539-how-to-include-the-post-page-s-title-in-the-contact-form-s-email-body).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Gear icon |  | Contact Form module that you want to include the Post/Page's title in the Email's body, open its setting by clicking on theGear icon |
| dt-custom-title |  | eld and set the following options:Field ID:dt-custom-titleTitle:Post TitleType:Input FieldRequired Field:No |
| dt-custom-title |  | tom-title |
| Post Title |  | Title |
| Input Field |  | Field |
| No |  | quired Field:No |
| Advanced Tab |  | d Tab→Custom CSS→Free Form CSS |
| %%dt-custom-title%% |  | ttern and make sure the field is included by using%%dt-custom-title%% |
| Child theme |  | using aChild theme, edit thefunctions.phpfile and place this PHP code after the existing code:// Add current post title to a contact form hidden fieldfunction add_post_title_to_cf_field(){// Get post titleglobal $post;$title = get_the_title($post->ID); ?><!-- Script for adding the retrieved title into the hidden field --><script>(function($){$(document).ready(function(){if ($('p[data-id="dt-custom-title"] input').length) {$('p[data-id="dt-custom-title"] input').attr('value','<?php echo $title; ?>');}});})(jQuery);</script><?php }add_action('wp_footer', 'add_post_title_to_cf_field'); |

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
