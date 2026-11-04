---
title: "The Support Center in Divi 5"
description: "Overview of the Divi Support Center: system status, remote access, documentation, Safe Mode, and the debug log."
category: builder
tags: [builder, support-center, troubleshooting, safe-mode]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15501073-the-support-center-in-divi-5"
---

# The Support Center in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A single admin screen for system status reports, remote support access, documentation, Safe Mode, and the debug log.
    **Where to find it:** Log in to WordPress and go to **Divi → Support Center**.
    **Key behavior:** Only a WordPress Administrator can enable Remote Access, and it switches itself off after 4 days.

## System Status

System Status shows how your site is configured and flags problems since your last login. It monitors PHP, CSS, JavaScript, and WordPress core files, using a stoplight scheme:

- **Green:** no detectable issues.
- **Yellow:** a potential issue worth fixing soon.
- **Red:** fix immediately.

Two actions are available: **Show Full Report** displays the complete system report, and **Copy Full Report** copies it so you can hand it to Elegant Themes support if asked.

Typical triggers for yellow or red include a PHP memory limit set too low or an outdated PHP version, plus problems with CSS, JavaScript, or WordPress core files.

## Remote Access

Remote Access lets Elegant Themes support staff securely log in to your site. Turning it on sends a secure token with login credentials to the support team.

- Access lasts up to 4 days, then disables automatically. You can turn it off earlier.
- Only a WordPress Administrator can enable it.
- After enabling it, an extra toggle appears to grant **Admin Access** if support requests it.

To enable it:

1. Log in to your Divi website.
2. Go to **Divi → Support Center**.
3. Turn on **Remote Access**.

When you request support, include the exact URL of the affected page(s) and as much detail as possible.

### Copy Support Token

If Remote Access does not work, or you have enabled it on several Divi sites, support will need the Support Token. With Remote Access on, click the **Copy Access Token** link (called Copy Support Token in the text), then paste the token into the support chat.

## Documentation

The Support Center embeds Divi documentation with step-by-step guides, videos, and overviews of modules and features such as the Theme Builder and Visual Builder. Use **View Full Divi Documentation** to open the full library.

## Safe Mode

Safe Mode disables third-party plugins, child themes, and custom code **for you only**, so you can troubleshoot while visitors keep seeing the normal site. You or an Elegant Themes support agent can enable it with one toggle. If you find a problem you are not comfortable fixing, turn on Remote Access so support can take over.

Common reasons to use it:

1. **Third-party plugins:** a plugin may be out of date for the current WordPress version and break the site.
2. **Child themes:** errors in a child theme can cause problems such as the white screen of death; Safe Mode disables the child theme.
3. **Custom CSS or JavaScript:** even a missing semicolon can break a site; Safe Mode disables installed custom code.

## Debug Log

If WordPress debugging is enabled, you can read the debug log from the Support Center. If not, you will need to enable WordPress debug mode first.

## Official documentation

[The Support Center in Divi 5](https://help.elegantthemes.com/en/articles/15501073-the-support-center-in-divi-5){:target="_blank"}
