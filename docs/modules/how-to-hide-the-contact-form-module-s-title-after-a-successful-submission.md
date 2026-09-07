---
title: "How to Hide the Contact Form Module's Title After a Successful Submission"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8203453-how-to-hide-the-contact-form-module-s-title-after-a-successful-submission"
---

# How to Hide the Contact Form Module's Title After a Successful Submission

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8203453-how-to-hide-the-contact-form-module-s-title-after-a-successful-submission).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classassign thedt-cfCSS class |
| WordPress Dashboard → |  | ard →Divi → Theme Option → Integration tab → Headerand copy/paste the following JS code<script>(function ($) {$(document).ready(function () {function remove_title() {var contactForm = $('.dt-cf.et_pb_contact_form_container');console.log(contactForm);if (!contactForm.find('.et-pb-contact-message').is(':empty')) {contactForm.find('.et_pb_contact_main_title').hide();}}$(document).ajaxComplete(remove_title);});})(jQuery)</script> |

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
