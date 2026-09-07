---
title: "How to Fix the "Error Establishing a Database Connection" in WordPress"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2239768-how-to-fix-the-error-establishing-a-database-connection-in-wordpress"
---

# How to Fix the "Error Establishing a Database Connection" in WordPress

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2239768-how-to-fix-the-error-establishing-a-database-connection-in-wordpress).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Access Your Site’s Files |  | To locate your site's files, use an FTP client or your hosting provider’s file manager. |
| Open wp-config.php |  | Find and open thewp-config.phpfile in the root directory. |
| Verify Credentials |  | Ensure theDB_NAME,DB_USER,DB_PASSWORD, andDB_HOSTvalues are correct. |
| Contact Your Hosting Provider |  | Ask if there are any ongoing server issues. |
| Test Connection |  | Use a simple PHP script to test the connection to your database server. |
| Add Code to wp-config.php |  | Add the following line to yourwp-config.phpfile to enable automatic database repair:define('WP_ALLOW_REPAIR', true); |
| Run the Repair Script |  | Navigate tohttp://yoursite.com/wp-admin/maint/repair.phpand follow the instructions. |
| Remove the Repair Code |  | Remove the repair line from yourwp-config.phpfile. |
| Access phpMyAdmin |  | Log into your hosting account and access phpMyAdmin. |
| Select Your Database |  | Choose your WordPress database. |
| Check wp_options Table |  | Look for thesiteurlandhomerows in thewp_optionstable. Ensure both are correct. |
| Download WordPress |  | Get the latest version of WordPress fromwordpress.org. |
| Re-upload Files |  | Upload thewp-adminandwp-includesfolders to your site using an FTP client. |
| Access Backup Files |  | Locate your backup files. |
| Restore Database and Files |  | Follow your backup tool’s instructions to restore both the database and site files. |

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
