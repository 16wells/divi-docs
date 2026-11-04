---
title: "How to Connect the Email Optin Module to Brevo"
description: "Generate a Brevo API key, authorize your server IP, and connect it to the Divi 5 Email Optin module."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14087864-how-to-connect-the-email-optin-module-to-brevo"
---

# How to Connect the Email Optin Module to Brevo

Brevo (formerly SendinBlue) connects to the [Email Optin module](email-optin.md) with an API key. Brevo also blocks API calls from unapproved IP addresses, so the IP step below matters.

!!! abstract "Quick Reference"
    **You need:** A Brevo API key, an existing Brevo list, and your server's IP authorized in Brevo.
    **Where in Divi:** Email Optin settings → Content tab → Email Account (listed as Brevo (SendinBlue)).
    **Gotcha:** With an unauthorized IP, no lists load even if the key is right.

## Create the Brevo API key

1. Log in to Brevo.
2. Open your profile (top right) and choose **My Profile**.
3. In the left sidebar, choose **SMTP & API**.
4. Open the **API Keys & MCP** tab.
5. Click **Generate a new API key**.
6. Name it, click **Generate**, then **Copy to Clipboard** and confirm.

## Connect it in Divi

1. Open the Email Optin module's settings (click the module or its gear icon).
2. Go to **Content tab → Email Account**.
3. Select **Brevo(SendinBlue)** and click **Add**.
4. Enter an **Account Name** (such as `my-brevo`) and paste the key into **API Key**.
5. Click **Submit**.
6. Choose the Brevo list.

## Authorize your IP address

1. In Brevo, open the Authorized IPs (Authorization) page.
2. Open the **Unauthorized IP addresses** tab and copy your IP from there.
3. Click **Authorize IP addresses** (top right).
4. Paste the copied IP and save.

If the list dropdown stays empty after connecting, check this step first.

## Official documentation

[How to Connect the Email Optin Module to Brevo](https://help.elegantthemes.com/en/articles/14087864-how-to-connect-the-email-optin-module-to-brevo)
