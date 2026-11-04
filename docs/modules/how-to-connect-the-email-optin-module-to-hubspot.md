---
title: "How to Connect the Email Optin Module to HubSpot"
description: "Create a HubSpot private app token and connect it to the Divi 5 Email Optin module so form submissions land in a HubSpot static list."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/14086136-how-to-connect-the-email-optin-module-to-hubspot"
---

# How to Connect the Email Optin Module to HubSpot

Once the [Email Optin module](email-optin.md) is linked to HubSpot, each submission is sent to the HubSpot list you choose.

!!! abstract "Quick Reference"
    **You need:** A HubSpot private app access token and a HubSpot **static** list.
    **Where in Divi:** Email Optin settings → Content tab → Email Account.
    **Gotcha:** The token you copy from HubSpot goes into the module's "API Key" field.

## Get the HubSpot access token

1. Log in to HubSpot.
2. Click your profile at the top right and choose **Profile & Preferences**.
3. In the left sidebar, choose **Integration → Legacy Apps**.
4. Click **Create**, then choose **Private**.
5. Optionally fill in the app details.
6. Open the **Scopes** tab and click **+ Add new scope**.
7. Under **CRM**, select every available scope, then click **Update**.
8. Click **Create app**, then **Continue creating**.
9. Open the **Auth** tab and copy the **Access token**.

## Connect it in Divi

1. Open the Email Optin module's settings (click the module or its gear icon).
2. Go to **Content tab → Email Account**.
3. Select **HubSpot** from the provider list and click **Add**.
4. Enter a **Name** (anything, such as `my-hubspot`) and paste the token into **API Key**.
5. Click **Submit**.
6. Choose the HubSpot list to receive subscribers.

## Gotchas

- The list must be a static list; create it in HubSpot beforehand.
- If no lists appear, recheck the token and that the CRM scopes were saved.

## Official documentation

[How to Connect the Email Optin Module to HubSpot](https://help.elegantthemes.com/en/articles/14086136-how-to-connect-the-email-optin-module-to-hubspot)
