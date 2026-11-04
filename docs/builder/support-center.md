---
title: "Support Center"
description: "Divi 5 Support Center — system status reports, Safe Mode for conflict isolation, debug logging, remote access tokens, and built-in documentation search."
category: builder
tags: ["builder", "support", "debugging", "safe-mode"]
related: ["visual-builder"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/using-the-divi-support-center"
---

# Support Center

The Divi Support Center gives you and our support team the tools they need to fix problems more quickly and efficiently, without disrupting your website.

!!! abstract "Quick Reference"
    **What it does:** Provides diagnostic tools for troubleshooting Divi issues, including system health checks, Safe Mode, and debug logging.
    **Where to find it:** WordPress admin → Divi → Support.
    **Key features:**

    - Automated System Status panel checking PHP, WordPress, MySQL, and plugin/theme conflicts
    - Safe Mode to temporarily disable child theme, custom CSS, and plugins for conflict isolation
    - Debug Log for Divi-specific errors and warnings
    - Secure Remote Access tokens for Elegant Themes support agents

    **ET Docs:** [Support Center](https://www.elegantthemes.com/documentation/divi/using-the-divi-support-center){:target="_blank"}

The Divi Support Center is designed to bring all of the elements of great support into one interface. Fully automated system status reports, in-depth documentation, safe mode, a debug log, and even seamless remote access for support agents.

Accessing the Divi Support Center is a breeze. Simply log in to your Divi website, then navigate toDivi > Support.

<!-- ![Support Center overview](../assets/screenshots/builder/support-center/overview.png){ loading=lazy }
*The Support Center interface in Divi 5.* -->

## How to Access the Divi Help & Support Center

1. Log in to your WordPress site.
2. Navigate to **Divi > Support** in the left-hand admin menu.
3. The Support Center dashboard loads with tabs for each feature area.

You can also access Safe Mode and the Debug Log from within the Visual Builder's Help panel.

## Divi Support Center: System Status

The System Status panel runs a fully automated health check on your WordPress environment. It reports on:

| Check | What It Verifies |
|-------|-----------------|
| **PHP Version** | Whether your server's PHP version meets Divi's minimum requirements. |
| **WordPress Version** | Whether WordPress is up to date. |
| **Divi Version** | Whether the latest Divi release is installed. |
| **PHP Memory Limit** | Whether the memory limit is sufficient (256 MB or higher recommended). |
| **PHP Max Input Vars** | Whether the input variable limit is high enough for large pages. |
| **PHP Post Max Size** | Whether uploaded file size limits are adequate. |
| **MySQL Version** | Whether the database server version is compatible. |
| **WordPress Debug Mode** | Whether WP_DEBUG is enabled or disabled. |
| **Plugin Conflicts** | Flags known plugin conflicts that may affect Divi. |
| **Theme Conflicts** | Checks for child theme issues or incompatible parent themes. |

Each check displays a green (pass) or red (fail) status indicator with a recommendation if the check fails.

## Divi Support Center: Remote Access

The Remote Access feature lets you generate a secure, time-limited access token that allows Elegant Themes support agents to log in to your site without sharing your password.

- Tokens expire automatically after a set period.
- You can revoke access at any time.
- Support agents see a clearly labeled admin session so their actions are distinguishable in your activity logs.

## Divi Support Center: Documentation

The Documentation tab provides an embedded search interface for the Elegant Themes knowledge base. Search for any Divi feature, error message, or workflow directly from your WordPress admin without opening a separate browser tab.

## Safe Mode

Safe Mode is a diagnostic tool that temporarily disables elements that commonly cause conflicts, allowing you to isolate the source of a problem.

### What Safe Mode Disables

| Element | Effect |
|---------|--------|
| **Child Theme** | Switches to the parent Divi theme, bypassing child theme customizations. |
| **Custom CSS** | Disables all custom CSS added through Divi options, the Customizer, and element-level CSS. |
| **Third-Party Plugins** | Deactivates all plugins except Divi to test for plugin conflicts. |
| **Static CSS File Generation** | Falls back to inline styles instead of cached CSS files. |

### Using Safe Mode

1. Navigate to **Divi > Support > Safe Mode**.
2. Toggle Safe Mode **on**.
3. Test whether the issue persists.
4. If the issue disappears, re-enable items one by one to identify the conflict.
5. Toggle Safe Mode **off** when finished.

!!! tip "Safe Mode is Non-Destructive"
    Safe Mode does not delete or permanently change any settings. It only temporarily bypasses potential conflict sources. All settings are restored when you turn it off.

## Divi Debug Log

The Debug Log records Divi-specific errors, warnings, and notices. It is useful for diagnosing issues that do not produce visible error messages on the front end.

- Access the log from **Divi > Support > Debug Log**.
- The log captures PHP errors, JavaScript console messages, and Divi internal events.
- Copy the log contents when submitting a support ticket to give the support team detailed diagnostic information.

## More Resources

- [Visual Builder](visual-builder.md) -- General builder documentation
- [Troubleshooting](../troubleshooting/index.md) -- Problem-solution guides
- [Elegant Themes Support](https://www.elegantthemes.com/support/){:target="_blank"} -- Official support portal

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If this feature is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.


## Related

- [Visual Builder](visual-builder.md)
