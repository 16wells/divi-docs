---
title: "How to Connect the Instagram Feed Module with an Instagram Account in Divi 5"
description: "How to create a Facebook app, generate an Instagram access token, and paste it into the Divi 5 Instagram Feed module."
category: troubleshooting
tags: [troubleshooting]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15175737-how-to-connect-the-instagram-feed-module-with-an-instagram-account-in-divi-5"
---

# How to Connect the Instagram Feed Module with an Instagram Account in Divi 5

!!! abstract "Quick Reference"
    **What you need:** An Instagram access token, generated from a Facebook app you create.
    **Prerequisite:** A Business Facebook account is required to create a Facebook app.
    **Token lifetime:** The token is valid for 60 days, then must be refreshed.
    **Where it goes:** Instagram Feed module, Content tab, Account.

## Create a Facebook app

1. Log in to Facebook and open the Facebook Developers page.
2. Click **Create App**.
3. Enter an app name and an **App Contact Email**, then click **Next**.
4. In the **Filter by** sidebar choose **Content Management**, select **Manage messaging & content on Instagram**, and click **Next**.
5. Select your profile name and click **Next**.
6. On the Requirements page, click **Next**, then click **Create app**.
7. Enter your Facebook password and click **Submit**.
8. Open the **Customize the Manage messaging & content on Instagram use case** option, then go to **Permissions and Features**.
9. Scroll to **instagram_basic** and click **Add**.

## Add yourself as an Instagram tester

1. In the left sidebar choose **App Roles**, then **Roles**.
2. Open the **Instagram Testers** tab and click **Add People**.
3. Choose **Instagram Tester**, enter your Instagram username, and click **Add**.
4. Click the **Apps and Websites** link. A new window asks you to log in to Instagram (or goes straight to the Instagram Apps and websites page if you are already logged in).
5. Open the **Tester Invites** tab and click **Accept**.
6. Return to the Facebook app's **App roles** page and refresh it. The tester should no longer show as Pending.

## Generate the access token

1. In the left sidebar choose **Use Cases**, then click **Customize** next to **Manage messaging & content on Instagram**.
2. Expand **Generate access token** and click **Generate token**.
3. Accept the cookies prompt, then log in to Instagram with the same account you added as a tester.
4. Click **Allow**.
5. Back on the Facebook app page, tick **I understand** and click **Copy** to copy the token.
6. Click **Done**.

!!! warning "Token expiry"
    The access token is only valid for 60 days. Refresh or regenerate it before it expires; Elegant Themes has a separate article on refreshing the Instagram access token.

## Add the token to the Instagram Feed module

1. Add or open the **Instagram Feed** module.
2. In the **Content** tab, under **Account**, click **Add**.
3. Enter an **Account name** (any label you like).
4. Paste the access token into the **Instagram Access token** field.
5. Click **Submit**.

## Official documentation

[How to Connect the Instagram Feed Module with an Instagram Account in Divi 5](https://help.elegantthemes.com/en/articles/15175737-how-to-connect-the-instagram-feed-module-with-an-instagram-account-in-divi-5)
