---
title: "How to Connect the Email Optin Module to ConstantContact"
description: "Register a ConstantContact developer app with the right redirect URI and connect its keys to the Divi 5 Email Optin module."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14087425-how-to-connect-the-email-optin-module-to-constantcontact"
---

# How to Connect the Email Optin Module to ConstantContact

This setup needs a developer application in ConstantContact, because the connection authorizes through a redirect back to your site.

!!! abstract "Quick Reference"
    **You need:** HTTPS on your domain, a ConstantContact API key (Client ID) and client secret, and an existing list.
    **Key detail:** The redirect URI is your site URL plus `?et-core-api-email-auth=1`, with no slash before the `?`.
    **Where in Divi:** [Email Optin](email-optin.md) settings → Content tab → Email Account.

## Create the ConstantContact app

1. Log in to the ConstantContact Developer portal.
2. On **My Application**, click **New Application**.
3. Name the application, leave the defaults, and click **Create**.
4. Click **Edit** on the new application.
5. Click the pencil icon under Redirect URI.
6. Enter your site URL followed by `?et-core-api-email-auth=1`, for example `https://example.com?et-core-api-email-auth=1`. Remove any trailing `/` from the site address before the `?`.
7. Click **Confirm**.
8. Copy the **API Key (Client ID)**.
9. Click **Generate Client Secret** and copy it.

## Connect it in Divi

1. Open the Email Optin module's settings (click the module or its gear icon).
2. Go to **Content tab → Email Account**.
3. Select **ConstantContact** and click **Add**.
4. Fill in:
    - **Account Name**: anything, such as `my-constantcontact`.
    - **API Key**: the Client ID from step 8.
    - **Access Token**: the client secret from step 9.
5. Click **Submit**.
6. Choose the ConstantContact list to use.

## Gotchas

- A redirect URI with a stray slash or a non-HTTPS site will fail to authorize.
- The client secret goes into the module's "Access Token" field, which is easy to mix up.

## Official documentation

[How to Connect the Email Optin Module to ConstantContact](https://help.elegantthemes.com/en/articles/14087425-how-to-connect-the-email-optin-module-to-constantcontact)
