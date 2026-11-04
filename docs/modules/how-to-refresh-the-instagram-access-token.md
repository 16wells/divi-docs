---
title: "How to Refresh the Instagram Access Token"
description: "Generate a new Instagram access token in Meta for Developers and swap it into the Divi 5 Instagram Feed module before the 60-day token expires."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/16197038-how-to-refresh-the-instagram-access-token"
---

# How to Refresh the Instagram Access Token

!!! abstract "Quick Reference"
    **What it is:** Replacing the expiring token that powers the [Instagram Feed module](the-instagram-feed-module-in-divi-5.md).
    **Why:** A token is valid for 60 days; once it lapses the module stops displaying your feed.
    **Where:** Facebook Developers (generate the token), then Instagram Feed settings → Content tab → Account.

## Generate a new token

1. Log in to your Facebook Developers account.
2. Click the app you created for the Instagram feed.
3. In the left sidebar, choose **Use Cases**.
4. Click **Customize** next to **Manage messaging & content on Instagram**.
5. Expand the **Generate access token** section.
6. Click the **Generate token** option.
7. Log in to Instagram if asked, then click **Allow**.
8. Tick the **I Understand** checkbox and copy the new token.
9. Click **Done**.

## Put the new token in the module

1. Open the page containing the Instagram Feed module and open its settings.
2. In **Content tab → Account**, click **Remove**.
3. Click **Add**.
4. Name the account (any label).
5. Paste the new token into **Instagram Access token**.
6. Click **Submit**.

## Gotchas

- Copy the token before clicking **Done**; you need it for the module.

## Official documentation

[How to Refresh the Instagram Access Token](https://help.elegantthemes.com/en/articles/16197038-how-to-refresh-the-instagram-access-token) (Elegant Themes Help Center)
