---
title: "The Payment Button Module in Divi 5"
description: "The Divi 5 module that adds a PayPal or Stripe checkout button, styled like the regular Button module."
category: modules
tags: [modules]
related: []
divi_version: "5.11+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15944794-the-payment-button-module-in-divi-5"
---

# The Payment Button Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A button that sends visitors straight to a PayPal or Stripe payment. It styles like the regular [Button module](https://help.elegantthemes.com/en/articles/10259665-the-button-module-divi-5), with an extra **Payment** group for the provider and amount.
    **Three concepts:** *Provider* (PayPal or Stripe, one per button), *Resource* (the account that receives the money), *Environment* (Sandbox for testing, Live for real payments).
    **Stripe prerequisite:** Each Stripe product needs its own Stripe Payment Link.

## Concepts

- **Provider:** PayPal or Stripe, chosen per button.
- **Resource:** the destination account: a **PayPal business email** or a **Stripe hosted checkout link**. Save it once and reuse it on any Payment Button.
- **Environment:** **Sandbox** tests the button without moving real money; switch to **Live** to accept payments.

## Add the module

1. In the Visual Builder, click the green plus icon to insert a Row into the Section.
2. Click the gray plus icon inside the Row to open the module list.
3. Find **Payment Button** (or search for it) and click it.

## Use cases

- **Selling a single product** with a Buy Now button at a fixed price.
- **Accepting donations** by setting the button to a user-defined amount.
- **Collecting a booking or deposit fee** to reserve a spot, table, or appointment.

## Content tab

### Payment group

| Setting | Description |
|---|---|
| Provider | PayPal or Stripe. Stripe requires a [Stripe Payment Link](https://intercom.help/elegantthemes/en/articles/16160284-how-to-create-a-stripe-payment-link) for each product linked to the button |
| Resource | The account the payment goes to. Click **Add**, name it, and enter the PayPal business email or Stripe hosted checkout link, then select it. Saved resources can be edited or removed |
| Environment | Sandbox (safe testing) or Live (real payments) |
| Amount Mode | **Fixed** charges a set price; **User Defined** lets the visitor enter an amount |
| Amount | The price to charge; used when Amount Mode is Fixed |
| Currency | Payment currency; type to search by currency or country. Default is USD |
| Return URL | PayPal only: the page visitors land on after a successful payment |
| Cancel URL | PayPal only: the page visitors land on if they cancel |
| Open In New Tab | Whether checkout opens in a new browser tab |

### Other Content settings

| Setting | Description |
|---|---|
| Text | The button label, such as "Buy Now" or "Donate" |
| Loop | Enables the Loop Builder |
| Order | Position in a Flexbox or Grid layout |
| Meta | Label text and forced visibility inside the Visual Builder |

## Design tab

The module shares the Button module's styling, so these controls behave the same way.

| Setting | Description |
|---|---|
| Layout | Text and logo alignment, full-width option, and Layout Style (Block, Flex by default, or Grid) |
| Alignment | Position of the module on the page |
| Text | Overall text styles |
| Button | Button design styles |
| Spacing | Module spacing |
| Box Shadow | Box shadow styles |
| Filters | Hue shifts, saturation changes, blend modes |
| Transform | Scale, rotate, skew, translate |
| Animation | Animation styles |

## Advanced tab

| Setting | Description |
|---|---|
| Attributes | CSS ID, reusable CSS classes, or custom HTML attributes |
| CSS | Custom CSS for the module |
| HTML | Semantic HTML tag |
| Conditions | Show content based on conditions |
| Interactions | Custom interactions such as showing or hiding the button |
| Visibility | Visibility per device |
| Transitions | Duration of animations |
| Position | Precise placement |
| Scroll Effects | Behavior during scrolling |

Save the page with `CMD + S` (Mac) or `CTRL + S` (PC), or use the **Save** and **Exit** buttons.

## Official documentation

- [The Payment Button Module in Divi 5](https://help.elegantthemes.com/en/articles/15944794-the-payment-button-module-in-divi-5)
