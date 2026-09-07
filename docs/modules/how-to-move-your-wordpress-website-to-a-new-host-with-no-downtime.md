---
title: "How to Move Your WordPress Website to a New Host With No Downtime"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/5338125-how-to-move-your-wordpress-website-to-a-new-host-with-no-downtime"
---

# How to Move Your WordPress Website to a New Host With No Downtime

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/5338125-how-to-move-your-wordpress-website-to-a-new-host-with-no-downtime).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Downtime causes confusion |  | after all, every site should be up 24/7. |
| You could scare visitors away - |  | if your site is down, users may consider their alternatives.​ |
| It looks unprofessional - |  | there are plenty of legitimate reasons why a website might experience downtime; however, not being there when they need you can make you look unprofessional. |
| Export a Copy of Your Website |  |  |
| Upload Your Copied Site to Your New Web Host |  |  |
| Modify Your hosts' File |  |  |
| Run Your Installer and Complete the Migration |  |  |
| Update Your Domain’s Nameservers |  |  |
| WordPress Dashboard → Duplicator → Packages |  | kages |
| Setup tab |  | efault settings under theSetup tabto store it on your server |
| Next |  | k on theNextbutton |
| Use a File Transfer Protocol FTP) client |  | we recommendFileZilla. When you signed up for your new web host, you should have received a set of credentials to access yourFTP server. If you didn’t, check yourhost’s cPanelfor them (they’re normally prominently displayed), or contact the support team as a last resort. |
| public_html |  | gained access to your FTP server, navigate to thepublic_htmlfolder (it could also be calledrootorwww). |
| Installer |  | s folder and use FileZilla’s upload function to move both yourInstallerandArchivefiles to your server. |
| C:/Windows/System32/drivers/etc/ |  | rivers/etc/ |
| hosts |  | the system'shostsfile in question using yourpreferred text editor. |
| hosts |  | the changes to the system'shostsfile |
| Database |  | ourDatabaseand a corresponding user for your new website through your web host’s cPanel. You may need to check the hosting's support team. |
| www.yourwordpresssite.com/installer.php |  | staller.php, replacing the placeholder domain with yours. |
| Test validate |  | one, click theTest validatebutton to ensure everything is working as it should. If it isn’t, your database might not get imported correctly, so don’t skip this step! |
| Run Deployment |  | bottom of the page and click onRun Deployment. The plugin may take a couple of minutes to do its thing. Once it does so, it’ll ask you to confirm your new site’s path and title, and you’ll get the option to set up a new admin account as well |

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
