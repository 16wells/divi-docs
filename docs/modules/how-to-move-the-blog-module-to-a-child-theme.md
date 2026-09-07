---
title: "How to Move the Blog Module to a Child Theme"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/4532734-how-to-move-the-blog-module-to-a-child-theme"
---

# How to Move the Blog Module to a Child Theme

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/4532734-how-to-move-the-blog-module-to-a-child-theme).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Divi Child theme |  | e |
| Advanced File Manager |  | (hosting File Manager app or a WordPress plugin such asAdvanced File Manager) inside the Child Theme folder. Create a new folder and name itincludes |
| Blog.php |  | Blog.phpfile located in theDivi/includes/builder/modulefolder to thechild theme folder/includesfolder. |
| Blog.php |  | Blog.phpfile from your Child Theme and replace the following lines of code:The code on line 3:require_once 'helpers/Overlay.php';With:get_template_part( '/includes/builder/module/helpers/Overlay.php' );The code on line 5:class ET_Builder_Module_Blog extends ET_Builder_Module_Type_PostBased {With:class custom_ET_Builder_Module_Blog extends ET_Builder_Module_Type_PostBased {The code on line 17:$this->vb_support       = 'on';With:$this->vb_support       = 'off'; |
| Blog.php |  | own at the end of theBlog.phpfile and remove this PHP code:if ( et_builder_should_load_all_module_data() ) {new ET_Builder_Module_Blog();} |
| functions.php file |  | php fileinside the Child Theme's folder and add this PHP code:/*================================================#Load custom Blog Module================================================*/function divi_custom_blog_module() {get_template_part( '/includes/Blog' );$dcfm = new custom_ET_Builder_Module_Blog();remove_shortcode( 'et_pb_blog' );add_shortcode( 'et_pb_blog', array( $dcfm, '_shortcode_callback' ) );}add_action( 'et_builder_ready', 'divi_custom_blog_module' );function divi_custom_blog_class( $classlist ) {// Blog Module 'classname' overwrite.$classlist['et_pb_blog'] = array( 'classname' => 'custom_ET_Builder_Module_Blog',);return $classlist;}add_filter( 'et_module_classes', 'divi_custom_blog_class' ); |
| functions.php |  | ions.phpfile. |
| Marketplace |  | d prefer to avoid manual customization, you can browse yourMarketplaceand check all the third-party plugins available that can be used to customize the Blog Module. |

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
