---
title: "How to Change Server's Maximum Upload File Size"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2267999-how-to-change-server-s-maximum-upload-file-size"
---

# How to Change Server's Maximum Upload File Size

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2267999-how-to-change-server-s-maximum-upload-file-size).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| WordPress Dashboard → Tools → Site Health |  | te Health |
| Info |  | k on theInfotab |
| Server |  | theServeroption |
| Upload max filesize |  | Upload max filesize |
| php.ini |  | thephp.inifile (usually in the root directory or a directory like/etc/) |
| php.ini |  | ephp.inifile and add or modify the following lines:upload_max_filesize = 64Mpost_max_size = 64M |
| .htaccess |  | e.htaccessfile in the root directory of your WordPress installation |
| .htaccess |  | ollowing lines to the.htaccessfile:php_value upload_max_filesize 64Mphp_value post_max_size 64M |
| wp-config.php |  | config.phpfile in the root directory of your WordPress installation |
| wp-config.php |  | wing lines to thewp-config.phpfile:@ini_set( 'upload_max_size' , '64M' );@ini_set( 'post_max_size', '64M'); |
| .user.ini |  | edit a.user.inifile in the root directory of your WordPress installation |
| .user.ini |  | ollowing lines to the.user.inifile:upload_max_filesize = 64Mpost_max_size = 64M |
| upload_max_filesize |  | max_filesizeandpost_max_sizevalues |
| MaxUploader – Increase Media Upload File Size | Increase Execution Time |  | crease Execution Time |
| WordPress Dashboard → Tools → Site Health |  | ashboard → Tools → Site Health→Info → Server |
| upload_max_filesize |  | rease theupload_max_filesizeandpost_max_sizelimits. |
| Is The WordPress Upload Limit Giving You Trouble? Here’s How To Change It |  | es on your server, please check ourIs The WordPress Upload Limit Giving You Trouble? Here’s How To Change Itarticle. |
| Divi Hosting |  | ooking for better hosting, we recommendDivi Hosting, which is optimized and configured specifically for the Divi Theme and comes with Divi preinstalled |

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
