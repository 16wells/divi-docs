---
title: "How to Create a Stripe Payment Link"
description: "Create a Stripe Payment Link, optionally redirect buyers after payment, and plug the link into the Divi 5 Payment Button module."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/16160284-how-to-create-a-stripe-payment-link"
---

# How to Create a Stripe Payment Link

!!! abstract "Quick Reference"
    **What it is:** A Stripe-hosted checkout URL that the [Payment Button module](the-payment-button-module-in-divi-5.md) sends buyers to.
    **Where to set it:** Stripe Dashboard (create the link), then Payment Button settings → Content tab → Payment → Provider → Stripe.
    **You need:** A Stripe account; optionally a product already created in Stripe.

## Create the payment link in Stripe

1. Log in to your Stripe account.
2. Click the **Plus icon** (top right) and choose **Payment Link**.
3. Pick the type. Products or Subscriptions is selected by default.
4. In the **Product** field, select an existing Stripe product or create a new one.
5. Click **Create Link** (top right).
6. Click the **clipboard icon** to copy the link.

## Redirect buyers after payment (optional)

By default Stripe shows its own thank-you message once payment completes. To send buyers to a page on your site instead:

1. In Stripe, choose **Payment Links** in the left sidebar.
2. Hover the link, click the **three dots**, and choose **Edit**.
3. Open the **After Payment** tab.
4. Select **Don't show confirmation page**.
5. Enter the URL of the page buyers should land on.

## Add the link to the Payment Button module

1. Add a **Payment Button** module to your page.
2. In **Content tab → Payment → Provider**, choose **Stripe** and click **Add**.
3. Enter a **Product name**. Any label works, but matching the Stripe product name keeps things clear.
4. Paste the copied link into **Checkout URL**.
5. Click **Submit**.

## Gotchas

- Each item you sell needs its own payment link in Stripe, so repeat the process per product.
- Edits to a link's redirect behavior are made in Stripe, not in Divi.

## Official documentation

[How to Create a Stripe Payment Link](https://help.elegantthemes.com/en/articles/16160284-how-to-create-a-stripe-payment-link) (Elegant Themes Help Center)
