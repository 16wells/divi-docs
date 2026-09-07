---
title: "How to Move the Contact Form Module to a Child Theme"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2865589-how-to-move-the-contact-form-module-to-a-child-theme"
---

# How to Move the Contact Form Module to a Child Theme

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2865589-how-to-move-the-contact-form-module-to-a-child-theme).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Child theme for Divi |  | aChild theme for Divi |
| Advanced File Manager |  | on, your hosting File Manager app, or theAdvanced File Managerplugin, copy the fileContactForm.phplocated in theDivi Parent theme folder/includes/builder/module/to theChild theme/includes/folder. |
| ContactForm.php |  | Form.phpfile from theChild theme/includes/folder and find and replace this line of code:class ET_Builder_Module_Contact_Form extends ET_Builder_Module_Type_WithSpamProtectionWith:class Custom_ET_Builder_Module_Contact_Form extends ET_Builder_Module_Type_WithSpamProtection |
| functions.php |  | ions.phplocated in the Child theme folder and add this code after the existing PHP code:/*================================================#Load custom Contact Form Module================================================*/function divi_custom_contact_form() {get_template_part( '/includes/ContactForm' );$dcfm = new Custom_ET_Builder_Module_Contact_Form();remove_shortcode( 'et_pb_contact_form' );add_shortcode( 'et_pb_contact_form', array( $dcfm, '_render' ) );}add_action( 'et_builder_ready', 'divi_custom_contact_form' );function divi_custom_contact_form_class( $classlist ) {// Contact Form Module 'classname' overwrite.$classlist['et_pb_contact_form'] = array( 'classname' => 'Custom_ET_Builder_Module_Contact_Form',);return $classlist;}add_filter( 'et_module_classes', 'divi_custom_contact_form_class' ); |
| ContactForm.php |  | g the process, you can add/customize theContactForm.phpto your needs. |

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
