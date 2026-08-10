---
title: "Woo Cart Totals"
description: "Divi 5 Woo Cart Totals module — WooCommerce cart subtotal, shipping, tax, and total price summary with customizable table styling and proceed-to-checkout button."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "cart", "checkout", "pricing"]
related: ["woo-cart-products", "woo-checkout-billing"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/12095355"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Woo Cart Totals

The Woo Cart Totals module displays the cart price summary including subtotal, shipping, taxes, and total amount with a proceed-to-checkout button.

!!! abstract "Quick Reference"
    **What it does:** Shows the cart subtotal, shipping costs, taxes, and total amount with a proceed-to-checkout button.
    **When to use it:** Custom cart page templates in the Theme Builder
    **Key settings:** Title Text, Column Label, Body Text, Table styling, Button styling, Fields styling
    **Block identifier:** `divi/woo-cart-totals`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095355)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce cart page template alongside Woo Cart Products
    - Displaying order totals with shipping and tax calculations
    - Providing the proceed-to-checkout action in a custom cart layout

!!! warning "When NOT to Use This Module"
    - On non-cart pages — this module requires the WooCommerce cart context
    - For checkout order details — use [Woo Checkout Details](woo-checkout-details.md)
    - For product pricing display — use [Woo Product Price](woo-product-price.md)

## Overview

The Woo Cart Totals module renders the price summary section of the WooCommerce cart page. It calculates and displays the cart subtotal (sum of all product line totals), applicable shipping costs based on the customer's location, tax amounts when configured, and the final total. At the bottom, it provides a "Proceed to Checkout" button that directs customers to the next step of the purchase flow.

This module dynamically recalculates values when customers change quantities in the Woo Cart Products module or apply coupon codes. If shipping calculations are enabled in WooCommerce settings, the module may also display a shipping calculator that lets customers enter their location to estimate shipping costs before proceeding to checkout. The fields design options let you style this calculator input to match your layout.

The Woo Cart Totals module is designed to work within a Theme Builder template assigned to the WooCommerce cart page. It pairs directly with the [Woo Cart Products](woo-cart-products.md) module and is typically placed alongside it in a sidebar or adjacent column. For the official Elegant Themes documentation, see the [Woo Cart Totals help article](https://help.elegantthemes.com/en/articles/12095355).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Sidebar Cart Summary** — Place the Woo Cart Totals module in a one-third sidebar column next to the cart products table. Style it with a light background and subtle border to create a visually distinct summary card that stays visible as customers scroll through their cart items.

2. **Branded Checkout Button** — Use the Button design options to create a prominent, brand-colored "Proceed to Checkout" button with custom padding, border radius, and hover effects. Making this button stand out visually encourages customers to complete their purchase rather than abandoning the cart.

3. **Promotional Cart Page** — Combine the cart totals with styled coupon messaging above or below the module. Use Conditions to show promotional banners near the totals area when cart value exceeds a threshold, encouraging customers to reach a free shipping minimum.

## How to Add the Woo Cart Totals Module

1. Ensure WooCommerce is installed and activated. Navigate to the Theme Builder and create or edit the template assigned to the WooCommerce cart page.
2. Open the Visual Builder on your cart page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Cart Totals" in the module picker or find it in the WooCommerce category, then click to insert it. The module will display calculated totals based on the current cart contents.

## Settings & Options

The Woo Cart Totals module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the module's background and layout positioning. The cart totals data (subtotal, shipping, total) is pulled automatically from WooCommerce and does not require manual configuration.

| Setting | Type | Description |
|---------|------|-------------|
| Background | background controls | Set a background color, gradient, image, or video behind the cart totals module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |
| Loop- |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Woo Cart Totals Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides controls for styling the totals table, typography, the checkout button, and shipping calculator fields.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Title Text | text styling | Customize the font, size, weight, and color of the "Cart Totals" heading above the summary table. |
| Column Label | text styling | Style the label column text (Subtotal, Shipping, Total) including font, size, and color. |
| Body Text | text styling | Style the value column text (actual prices and amounts) including font, size, and color. |
| Table | styling controls | Configure the overall table appearance including background color, borders, and spacing. |
| Table Row | styling controls | Style individual rows including alternating backgrounds, padding, and border separators. |
| Table Cell | styling controls | Control individual cell appearance including padding, alignment, and borders. |
| Fields | styling controls | Style the shipping calculator input fields (country, state, postcode) including border, background, and text color. |
| Button | styling controls | Customize the "Proceed to Checkout" button including font, text color, background color, border, border radius, padding, and hover effects. |
| Text |  | Choose the overall text styles for the Woo Cart Totals module. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Cart Totals module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Cart Totals module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Cart Totals module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Cart Totals module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Cart Totals module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Cart Totals module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Cart Totals module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (table, rows, cells, button, fields) |
| HTML | Semantic HTML tag selection for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Choose the button's attributes. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS to the Woo Cart Totals module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Cart Totals module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Woo Cart Totals' module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Cart Totals module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Cart Totals module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Style the cart totals container as a card */
.et_pb_wc_cart_totals .cart_totals {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    padding: 24px;
}

/* Style the Cart Totals heading */
.et_pb_wc_cart_totals .cart_totals h2 {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 2px solid #f0f0f0;
}

/* Style the totals table rows */
.et_pb_wc_cart_totals .cart_totals table.shop_table tr td,
.et_pb_wc_cart_totals .cart_totals table.shop_table tr th {
    padding: 12px 0;
    border-bottom: 1px solid #f0f0f0;
}

/* Emphasize the total row */
.et_pb_wc_cart_totals .cart_totals .order-total td {
    font-size: 22px;
    font-weight: 700;
    color: #333;
}

/* Style the Proceed to Checkout button */
.et_pb_wc_cart_totals .wc-proceed-to-checkout .checkout-button {
    background-color: #27ae60;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 16px 24px;
    font-size: 16px;
    font-weight: 600;
    width: 100%;
    text-align: center;
    transition: background-color 0.3s ease;
}

.et_pb_wc_cart_totals .wc-proceed-to-checkout .checkout-button:hover {
    background-color: #219a52;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_cart_totals .cart_totals {
        margin-top: 30px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Cart Totals module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_cart_totals' !== $render_slug) {
        return $output;
    }
    return $output;
}, 10, 2);

/* Add free shipping progress bar above cart totals */
add_action('woocommerce_before_cart_totals', function() {
    $min_amount = 75; // Free shipping threshold
    $current_total = WC()->cart->get_subtotal();
    $remaining = $min_amount - $current_total;

    if ($remaining > 0) {
        $progress = ($current_total / $min_amount) * 100;
        echo '<div class="free-shipping-notice">';
        echo '<p>Add <strong>' . wc_price($remaining) . '</strong> more for free shipping!</p>';
        echo '<div class="progress-bar"><div class="progress" style="width:' . esc_attr($progress) . '%"></div></div>';
        echo '</div>';
    } else {
        echo '<div class="free-shipping-notice success"><p>You qualify for free shipping!</p></div>';
    }
});
```

## Common Patterns

1. **Sticky Cart Summary Sidebar** — Place the cart totals in a one-third column and use the Position advanced option to make it sticky. As customers scroll through a long cart product list, the totals and checkout button remain visible, reducing friction in the checkout flow.

2. **Minimal Totals Card** — Apply a white background with a subtle box shadow to create a floating card effect. Use the Title Text options to style the "Cart Totals" heading and make the checkout button full-width with a strong green background color. This clean, focused design draws attention to the total and the action button.

3. **Cart with Shipping Calculator** — When WooCommerce shipping calculations are enabled, the cart totals module displays a "Calculate Shipping" section with country, state, and postcode fields. Style these fields using the Fields design option to match your form styling throughout the site. This lets customers see accurate shipping costs before committing to checkout.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-cart-totals` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Cart Totals module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple cart templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Cart Totals module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "Totals Not Updating After Quantity Changes"
    If the cart totals do not recalculate when quantities are changed in the Woo Cart Products module, check for JavaScript errors in the browser console. This is typically caused by plugin conflicts that interfere with WooCommerce's AJAX cart update. Disable other plugins temporarily to identify the conflict.

!!! warning "Shipping Costs Not Displaying"
    If the shipping row is missing from the totals table, verify that shipping zones and methods are configured in WooCommerce > Settings > Shipping. The module only displays shipping costs when at least one shipping method is available for the customer's location. Also check that the "Enable the shipping calculator on the cart page" option is enabled under WooCommerce > Settings > Shipping > Shipping Options.

!!! tip "Checkout Button Text Customization"
    To change the "Proceed to Checkout" button text, use the `woocommerce_order_button_text` filter or the `gettext` filter in your theme's functions.php. The Divi module renders the standard WooCommerce button, so standard WooCommerce text filters apply.

## Related

- [Woo Cart Products](woo-cart-products.md)
- [Woo Checkout Billing](woo-checkout-billing.md)
