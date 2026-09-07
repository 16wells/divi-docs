---
title: "How to Send a Copy to the Sender Using the Contact Form Module"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2315928-how-to-send-a-copy-to-the-sender-using-the-contact-form-module"
---

# How to Send a Copy to the Sender Using the Contact Form Module

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2315928-how-to-send-a-copy-to-the-sender-using-the-contact-form-module).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| install and activate one |  | theme,install and activate one |
| Advanced File Manager |  | on, hosting File Manager app, or theAdvanced File Managerplugin, navigate to your child theme folder and create a new folder namemodule |
| module |  | modulefolder, create a new PHP file calledContactForm.php |
| this page |  | e the code fromthis page |
| functions.php |  | ions.phpfile inside your child theme, and after the existing code, add this PHP code:/*================================================#Load custom Contact Form Module================================================*/function divi_custom_contact_form() {get_template_part( '/module/ContactForm' );$dcfm = new Custom_ET_Builder_Module_Contact_Form();remove_shortcode( 'et_pb_contact_form' );add_shortcode( 'et_pb_contact_form', array( $dcfm, '_render' ) );}add_action( 'et_builder_ready', 'divi_custom_contact_form' );function divi_custom_contact_form_class( $classlist ) {// Contact Form Module 'classname' overwrite.$classlist['et_pb_contact_form'] = array( 'classname' => 'custom_ET_Builder_Module_Contact_Form',);return $classlist;}add_filter( 'et_module_classes', 'divi_custom_contact_form_class' ); |

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
