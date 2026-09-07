---
title: "How to Translate the Divi Theme"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2434045-how-to-translate-the-divi-theme"
---

# How to Translate the Divi Theme

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2434045-how-to-translate-the-divi-theme).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Settings → General → Site language |  | guage |
| Divi Child Theme |  | aDivi Child Themefrom thisGitHub page |
| Appearance |  | rance→Themes→Add New→Upload Theme |
| Choose |  | the zip file you have downloaded from the link above |
| Install Now |  | eInstall Nowbutton. |
| Activate |  | e installation is completed, click on theActivatelink |
| Advanced File Manager plugin |  | osting File Manager app, or theAdvanced File Manager plugin |
| wp-content/theme/child-theme folder |  | ld-theme folder |
| lang |  | te a new folder and name itlang |
| lang |  | de thelangfolder, create two new folders and name them:themebuilder |
| theme |  |  |
| builder |  |  |
| functions.php |  | ions.phpfile and add this PHP code (after the existing code)/*================================================#Load the translations from the child theme folder================================================*/function dt_translation() {// Hook into textdomain loading to handle hyphenated filenamesadd_filter('load_textdomain_mofile', function($mofile, $domain) {if ($domain === 'Divi') {$child_mofile = get_stylesheet_directory() . '/lang/theme/Divi-' . determine_locale() . '.mo';if (file_exists($child_mofile)) {return $child_mofile;}}if ($domain === 'et_builder') {$child_mofile = get_stylesheet_directory() . '/lang/builder/et_builder-' . determine_locale() . '.mo';if (file_exists($child_mofile)) {return $child_mofile;}}return $mofile;}, 10, 2);// Load the textdomainsload_child_theme_textdomain('Divi', get_stylesheet_directory() . '/lang/theme/');load_child_theme_textdomain('et_builder', get_stylesheet_directory() . '/lang/builder/');}// Run after theme setupadd_action('after_setup_theme', 'dt_translation'); |
| PO Edit app |  | PO Edit app |
| this link |  | the Divi language files fromthis link |
| en_US.po |  | en_US.pofile from theDivi / lang folderfound in the zip file, using the PO Edit app |
| Divi-xx_XX.po |  | asDivi-xx_XX.po- where thexxis your country code. For example, for Romanian, the file name will beDivi-ro_RO.po. |
| Advanced File Manager plugin |  | osting File Manager app, or theAdvanced File Manager pluginto upload the.mofile that the PO edit created during the Save towp-content/themes/child theme folder/lang/theme |
| en_US.po |  | en_US.pofile from theDivi / includes / builder / languagesfolderfound in the zip file, using the PO Edit app |
| et_builder-xx_XX.po |  | builder-xx_XX.po- where thexxis your country code. For example, for Romanian, the file name will beet_builder-ro_RO.po. |
| Advanced File Manager plugin |  | osting File Manager app, or theAdvanced File Manager pluginto upload the.mofile that the PO edit created during the Save towp-content/themes/child theme folder/lang/builder |

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
