---
title: "How to Connect the Email Optin Module to ActiveCampaign"
description: "Connect the Divi 5 Email Optin module to ActiveCampaign using your account's API key and API URL."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14178447-how-to-connect-the-email-optin-module-to-activecampaign"
---

# How to Connect the Email Optin Module to ActiveCampaign

!!! abstract "Quick Reference"
    **What it is:** The steps for linking the Divi 5 [Email Optin module](the-divi-email-optin-module.md) to ActiveCampaign so form submissions land in your chosen list.
    **Where to set it:** Email Optin module settings → Content tab → Email Account.
    **You need:** An ActiveCampaign API key and API URL, plus at least one list in your ActiveCampaign account.

## Get your API credentials

1. Log in to your ActiveCampaign account.
2. Click the **Gear icon** at the top right (left of your profile icon).
3. In the left sidebar, choose **Developers**.
4. Copy the **URL** and the **Key** shown there.


## Connect the module

1. Open the Email Optin module's settings by clicking the module or its **Gear icon**.
2. Go to **Content tab → Email Account**.
3. Choose **ActiveCampaign** from the provider list and click **Add**.
4. Enter an **Account Name**. It is only a label for you (for example `my-activecampaign`).
5. Paste the key into **API Key** and the URL into **API URL**.
6. Click **Submit**.
7. Pick the ActiveCampaign list that should receive subscribers.

## Gotchas

- The Account Name is arbitrary; only the key and URL authenticate the connection.
- The source also lists an optional ActiveCampaign Form ID as a prerequisite but does not describe where it is used; the steps above work without it.
- Create the target list in ActiveCampaign first, or it will not be available to choose.

## Official documentation

[How to Connect the Email Optin Module to ActiveCampaign](https://help.elegantthemes.com/en/articles/14178447-how-to-connect-the-email-optin-module-to-activecampaign) (Elegant Themes Help Center)
