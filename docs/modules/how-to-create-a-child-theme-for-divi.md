---
title: "How to Create a Child Theme for Divi"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2188070-how-to-create-a-child-theme-for-divi"
---

# How to Create a Child Theme for Divi

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2188070-how-to-create-a-child-theme-for-divi).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Divi |  | ng a Child theme is not required if you only use CSS customizations. You can place your custom CSS code inDivi→Theme Options→General Tab→Custom CSS. |
| header.php |  | n to modify Divi's theme files, such asheader.phporfooter.php, you will need to create a Child theme to retain those changes when updating. |
| Ultimate Guide to Creating a Divi Child Theme |  | ltimate Guide to Creating a Divi Child Themeguide. |
| Using a 3rd party plugin (easy) |  |  |
| Creating it from scratch (advanced) |  |  |
| Plugins → Add new |  | d new |
| Child Theme Configurator |  | nfigurator |
| Tools →  Child Themes |  | hemes |
| Create a new Child Theme |  | hild Themeoption is selected |
| Divi |  | re thatDiviis selected as the Parent Theme |
| Analyze |  | n theAnalyzebutton |
| Primary Stylesheet (style.css) |  | style.css)option |
| Use the WordPress style queue |  | queueoption |
| Create New Child Theme |  | Child Themebutton |
| Appearance →  Themes |  | hemesand activate the new Child Theme |

### Advanced Tab

| Setting | Type | Description |
|---------|------|-------------|
| divi-child |  | ew folder on your local computer and name itdivi-child |
| divi-child |  | divi-childfolder, create a new file calledstyle.cssand place the following CSS code:/*Theme Name: Divi Child ThemeTheme URI: http://yourwebsite.comDescription: Child Theme For DiviAuthor: Your NameAuthor URI: http://yourwebsite.comVersion: 1.0.0Template: Divi*/Theme Name:It's the child's theme name. It can be anything you want. Usually, I useDivi's Child ThemeTheme URI:Represents the child theme author's website URL.Description:a short description of your child's theme. You can include things like color scheme used, features added, etcAuthor:The person's name who has created the Child themeAuthor URI: This could be your business website, or it can be the actual URL of the website where the child theme is usedTemplate: It is the parent theme name folder. In this case, that would always beDivi- case sensitive. |
| Theme Name |  | It's the child's theme name. It can be anything you want. Usually, I useDivi's Child Theme |
| Theme URI |  | Represents the child theme author's website URL. |
| Description |  | a short description of your child's theme. You can include things like color scheme used, features added, etc |
| Author |  | The person's name who has created the Child theme |
| Author URI |  | This could be your business website, or it can be the actual URL of the website where the child theme is used |
| Template |  | It is the parent theme name folder. In this case, that would always beDivi- case sensitive. |
| divi-child |  | childfolder, create a second file and name itfunctions.php |
| functions.php |  | lowing PHP code inside thefunctions.phpfile:<?php/*================================================#Load the Parent theme style.css file================================================*/function dt_enqueue_styles() {$parenthandle = 'divi-style';$theme = wp_get_theme();wp_enqueue_style( $parenthandle, get_template_directory_uri() . '/style.css',array(),  // if the parent theme code has a dependency, copy it to here$theme->parent()->get('Version'));wp_enqueue_style( 'child-style', get_stylesheet_uri(),array( $parenthandle ),$theme->get('Version'));}add_action( 'wp_enqueue_scripts', 'dt_enqueue_styles' ); |
| style.css |  | ntire folder, which should contain the two files:style.cssandfunctions.php |
| WordPress Dashboard → Appearance → Themes |  | arance → Themes |
| Add New Theme |  | dd New Themebutton |
| Upload Theme |  | Upload Themebutton |
| Install Now |  | eInstall Nowbutton |

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
