---
title: "How to Move the Filterable Portfolio Module From the Parent Theme to a Child Theme"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/3192155-how-to-move-the-filterable-portfolio-module-from-the-parent-theme-to-a-child-theme"
---

# How to Move the Filterable Portfolio Module From the Parent Theme to a Child Theme

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/3192155-how-to-move-the-filterable-portfolio-module-from-the-parent-theme-to-a-child-theme).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Advanced File Manager WordPress plugin |  | using theAdvanced File Manager WordPress plugin, browse thewp-content/themes/child theme folder, create a new folder, and name itincludes |
| FilterablePortfolio.php |  | terablePortfolio.phplocated inwp-content/themes/divi/includes/builder/module/into thewp-content/themes/child theme folder/includes/folder |
| custom-FilterablePortfolio.php |  | d theme folder) tocustom-FilterablePortfolio.php |
| custom-FilterablePortfolio.php |  | rtfolio.phpfile and replace this code (the first line):class ET_Builder_Module_Filterable_Portfolio extends ET_Builder_Module_Type_PostBased {With:class custom_ET_Builder_Module_Filterable_Portfolio extends ET_Builder_Module_Type_PostBased { |
| functions.php |  | ions.phpfile from your child theme folder and add the following code at the very bottom:/*================================================#Load custom Filterable Portfolio Module================================================*/function divi_custom_filterable_portfolio_module() {get_template_part( '/includes/custom-FilterablePortfolio' );$dcfm = new custom_ET_Builder_Module_Filterable_Portfolio();remove_shortcode( 'et_pb_filterable_portfolio' );add_shortcode( 'et_pb_filterable_portfolio', array( $dcfm, '_shortcode_callback' ) );}add_action( 'et_builder_ready', 'divi_custom_filterable_portfolio_module' );function divi_custom_filterable_portfolio_class( $classlist ) {// FiterablePortfolio Module 'classname' overwrite.$classlist['et_pb_filterable_portfolio'] = array( 'classname' => 'custom_ET_Builder_Module_Filterable_Portfolio',);return $classlist;}add_filter( 'et_module_classes', 'divi_custom_filterable_portfolio_class' ); |

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
