---
title: "How to Fix Changes Not Saving in Divi Builder"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2194019-how-to-fix-changes-not-saving-in-divi-builder"
---

# How to Fix Changes Not Saving in Divi Builder

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2194019-how-to-fix-changes-not-saving-in-divi-builder).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Security Plugins |  | Reason: Third-party plugins, such asWordFence, might block valid actions, including saving or Publishing.Solution:Check the plugin's settings, usually found under the Firewall section, and ensure that the protection mode is set toLearning mode(this applies to WordFence); similar plugins may have a similar setting. |
| Reason |  | Third-party plugins, such asWordFence, might block valid actions, including saving or Publishing. |
| Solution |  | Check the plugin's settings, usually found under the Firewall section, and ensure that the protection mode is set toLearning mode(this applies to WordFence); similar plugins may have a similar setting. |
| Server-side Security |  | Reason: Some hosting providers implement server-level firewalls (like ModSecurity or custom WAFs) that automatically block requests they interpret as suspicious. These firewalls may block legitimate WordPress actions, such as publishing or updating posts or pages, especially if the request contains specific patterns (e.g., HTML, JavaScript, or long strings).Solution:Contact your hosting provider and request that they review the firewall logs for any false positives. Ask them to whitelist the specific rule being triggered or disable it temporarily while you complete your updates. If you're using cPanel, you might also be able to toggle ModSecurity settings per domain. |
| Reason |  | Some hosting providers implement server-level firewalls (like ModSecurity or custom WAFs) that automatically block requests they interpret as suspicious. These firewalls may block legitimate WordPress actions, such as publishing or updating posts or pages, especially if the request contains specific patterns (e.g., HTML, JavaScript, or long strings). |
| Solution |  | Contact your hosting provider and request that they review the firewall logs for any false positives. Ask them to whitelist the specific rule being triggered or disable it temporarily while you complete your updates. If you're using cPanel, you might also be able to toggle ModSecurity settings per domain. |
| Caching Issues |  | Reason:Both browser and server caching can prevent you from seeing the most recent changes.Solution:Clear your browser cache and cookies. Also, if you're using a caching plugin like WP Super Cache or W3 Total Cache, please clear the plugin cache. Additionally, verify if your hosting provider offers server-side caching and clear it as well. |
| Reason |  | Both browser and server caching can prevent you from seeing the most recent changes. |
| Solution |  | Clear your browser cache and cookies. Also, if you're using a caching plugin like WP Super Cache or W3 Total Cache, please clear the plugin cache. Additionally, verify if your hosting provider offers server-side caching and clear it as well. |
| Static CSS File Generation |  | Reason:Divi generates static CSS files to improve performance, which might not get updated immediately.Solution:Go toDivi → Theme Options → Builder → Advanced, and disable theStatic CSS File Generationoption. This will force Divi to use dynamic CSS instead of static files. |
| Reason |  | Divi generates static CSS files to improve performance, which might not get updated immediately. |
| Solution |  | Go toDivi → Theme Options → Builder → Advanced, and disable theStatic CSS File Generationoption. This will force Divi to use dynamic CSS instead of static files. |
| Minification and Combining CSS/JS |  | Reason:Minification and combining of CSS/JS files by performance optimization plugins can cause issues with seeing updates.Solution:Temporarily disable these settings in your optimization plugins, such as Autoptimize or WP Rocket, and see if the changes appear. After confirming the changes, you can re-enable them. |
| Reason |  | Minification and combining of CSS/JS files by performance optimization plugins can cause issues with seeing updates. |
| Solution |  | Temporarily disable these settings in your optimization plugins, such as Autoptimize or WP Rocket, and see if the changes appear. After confirming the changes, you can re-enable them. |
| Content Delivery Network (CDN) |  | Reason:CDNs can cache your content globally, which might cause delays in reflecting changes.Solution:Purge the CDN cache through your CDN provider's dashboard (e.g., Cloudflare). |
| Reason |  | CDNs can cache your content globally, which might cause delays in reflecting changes. |
| Solution |  | Purge the CDN cache through your CDN provider's dashboard (e.g., Cloudflare). |
| Database Connection Issues |  | Reason:Issues with your database can sometimes prevent changes from being saved properly.Solution:Check your database for errors. A plugin like WP-DBManager can repair and optimize your database. |
| Reason |  | Issues with your database can sometimes prevent changes from being saved properly. |
| Solution |  | Check your database for errors. A plugin like WP-DBManager can repair and optimize your database. |
| Plugin Conflicts |  | Reason:Conflicts with other plugins can cause issues with saving or displaying changes.Solution:Deactivate all plugins except Divi and see if the changes are visible. If they are, reactivate your plugins individually to identify the conflicting plugins. |
| Reason |  | Conflicts with other plugins can cause issues with saving or displaying changes. |
| Solution |  | Deactivate all plugins except Divi and see if the changes are visible. If they are, reactivate your plugins individually to identify the conflicting plugins. |
| Incorrect Theme or Child Theme Settings |  | Reason:Customizations in a child theme might override changes made in the Divi Builder.Solution:Check your child theme’s functions.php file or any custom CSS/JS for overrides that might be causing the issue. Temporarily switch to the parent Divi theme to see if the changes are reflected. |
| Reason |  | Customizations in a child theme might override changes made in the Divi Builder. |
| Solution |  | Check your child theme’s functions.php file or any custom CSS/JS for overrides that might be causing the issue. Temporarily switch to the parent Divi theme to see if the changes are reflected. |
| Syntax errors in your custom CSS code |  | Reason:Since all the CSS code is being minified, if any of your custom CSS codes have syntax issues, this will prevent the browser from parsing the rest of the CSS code, which can lead to differences on the front end.Solution:Use theCSS Syntax checkerfor any custom CSS code that could have been added toDivi → Theme Options → General Tab → Custom CSS, Module's Advanced Tab→Custom CSS→Free Form CSSor in thestyle.cssfile of your Child theme. |
| Reason |  | Since all the CSS code is being minified, if any of your custom CSS codes have syntax issues, this will prevent the browser from parsing the rest of the CSS code, which can lead to differences on the front end. |
| Solution |  | Use theCSS Syntax checkerfor any custom CSS code that could have been added toDivi → Theme Options → General Tab → Custom CSS, Module's Advanced Tab→Custom CSS→Free Form CSSor in thestyle.cssfile of your Child theme. |
| Syntax errors in your custom HTML code |  | Reason:Invalid custom HTML code can also break a page's entire HTML structure, resulting in a broken layout and/or broken styles.Solution:Use theHTML Syntax checkerfor any custom HTML code that could have been added to Code Modules, in theDivi → Theme Option → Integration tabor as a WordPress Widget. |
| Reason |  | Invalid custom HTML code can also break a page's entire HTML structure, resulting in a broken layout and/or broken styles. |
| Solution |  | Use theHTML Syntax checkerfor any custom HTML code that could have been added to Code Modules, in theDivi → Theme Option → Integration tabor as a WordPress Widget. |
| Browser-Specific Issues |  | Reason:Sometimes, browser-specific settings or extensions can cause issues.Solution:To rule out browser-specific issues, test your site in a different browser or incognito mode. |
| Reason |  | Sometimes, browser-specific settings or extensions can cause issues. |
| Solution |  | To rule out browser-specific issues, test your site in a different browser or incognito mode. |

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
