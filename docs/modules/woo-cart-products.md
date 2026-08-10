---
title: "Woo Cart Products"
description: "Divi 5 Woo Cart Products module — WooCommerce cart item table with product images, quantities, coupon codes, and removal controls for custom cart pages."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "cart", "checkout", "product"]
related: ["woo-cart-totals", "woo-cross-sells", "shop"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/12095351"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Woo Cart Products

The Woo Cart Products module displays the list of products added to the WooCommerce shopping cart with quantities, prices, and management controls.

!!! abstract "Quick Reference"
    **What it does:** Renders the cart product table showing items, images, quantities, coupon field, update button, and remove controls on the cart page.
    **When to use it:** Custom cart page templates in the Theme Builder
    **Key settings:** Show Product Image, Show Coupon Code, Show Update Cart Button, Show Remove Item Icon, Layout, Table styling
    **Block identifier:** `divi/woo-cart-products`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095351)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce cart page template in the Theme Builder
    - Displaying cart contents with product images, quantities, and individual prices
    - Pairing with Woo Cart Totals and Woo Cross Sells for a complete cart layout

!!! warning "When NOT to Use This Module"
    - On non-cart pages — this module requires the WooCommerce cart context
    - For displaying a product grid or catalog — use [Shop](shop.md)
    - For checkout order summary — use [Woo Checkout Details](woo-checkout-details.md)

## Overview

The Woo Cart Products module renders the main cart table that customers interact with when reviewing their shopping selections. It displays each product in the cart with its featured image, name, price, quantity selector, and subtotal. Customers can update quantities, apply coupon codes, and remove items directly from this table, making it the central management interface for the shopping cart.

The module provides several toggle controls that let you customize which elements appear. You can show or hide product images, the coupon code input field, the update cart button, and the remove item icon. The Design tab offers a Layout option to switch between a horizontal table format (the traditional WooCommerce cart layout) and a vertical card-based display, which can work better on mobile-first designs.

This module is intended for use within a Theme Builder template assigned to the WooCommerce cart page. It pairs naturally with the [Woo Cart Totals](woo-cart-totals.md) module, which handles the subtotal, shipping, and checkout button, and the [Woo Cross Sells](woo-cross-sells.md) module, which displays cross-sell product recommendations. Together, these three modules replace the default WooCommerce cart page with a fully customizable Divi layout. For the official Elegant Themes documentation, see the [Woo Cart Products help article](https://help.elegantthemes.com/en/articles/12095351).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Custom Branded Cart Page** — Replace the default WooCommerce cart page with a Divi-styled layout that matches your store's branding. Use the table styling options to apply custom fonts, colors, and spacing to the cart table, creating a premium shopping experience that feels consistent with the rest of your site.

2. **Minimal Cart Layout** — Hide the product image and coupon code field for a streamlined cart that focuses on product names, quantities, and prices. This works well for digital product stores or subscription-based businesses where visual product thumbnails add little value.

3. **Two-Column Cart Page** — Place the Woo Cart Products module in a two-thirds column alongside Woo Cart Totals in a one-third sidebar column. This side-by-side layout keeps the order summary visible as customers modify quantities, reducing the need to scroll on desktop screens.

## How to Add the Woo Cart Products Module

1. Ensure WooCommerce is installed and activated. Navigate to the Theme Builder and create or edit the template assigned to the WooCommerce cart page.
2. Open the Visual Builder on your cart page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Cart Products" in the module picker or find it in the WooCommerce category, then click to insert it. The module will display the current cart contents automatically.

## Settings & Options

The Woo Cart Products module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which cart elements are visible and the module's background styling.

| Setting | Type | Description |
|---------|------|-------------|
| Show Product Image | toggle | Display or hide the featured image thumbnail for each product in the cart table. Enabled by default. |
| Show Coupon Code | toggle | Display or hide the coupon code input field and "Apply Coupon" button below the cart table. |
| Show Update Cart Button | toggle | Display or hide the "Update Cart" button that recalculates totals after quantity changes. |
| Show Remove Item Icon | toggle | Display or hide the X icon that lets customers remove individual items from the cart. |
| Background | background controls | Set a background color, gradient, image, or video behind the module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |
| Elements |  | Choose to display or hide various elements:Show Product Image- Display or hide the feature image of each product that is in the cart.Show Coupon Code- Display or hide the Coupon form.Show Update Cart Button- Display or hide the Update cart button.Show Remove Item Icon- Display or hide the remove item icon. <!-- AUTO-ADDED --> |
| Loop- |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Woo Cart Products Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides extensive control over the cart table appearance, including layout orientation, typography, row/cell styling, and button design.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between Horizontal (default table layout) or Vertical (card-based layout) for the cart display. Vertical may be more suitable for mobile-first designs. |
| Table Header | text styling | Customize the font, size, weight, and color of the table header row text (Product, Price, Quantity, Subtotal). |
| Body Text | text styling | Style the product names, prices, and other text content within the table cells. |
| Table | styling controls | Configure overall table appearance including background, borders, and spacing. |
| Table Row | styling controls | Style individual rows including alternating row colors, padding, and borders. |
| Table Cell | styling controls | Control individual cell appearance including padding, alignment, and borders. |
| Remove Icon | styling controls | Customize the delete/remove button icon size, color, and hover effects. |
| Image | styling controls | Set border radius, sizing, and hover effects for product thumbnail images in the cart. |
| Fields | styling controls | Style the coupon code input field including border, background, text color, and focus states. |
| Button | styling controls | Customize the "Apply Coupon" and "Update Cart" buttons including font, colors, borders, and padding. |
| Disable Button | styling controls | Style the inactive/disabled state of the Update Cart button when no changes have been made. |
| Horizontal |  | (default) <!-- AUTO-ADDED --> |
| Vertical |  | each element is displayed on a separate table row. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall text styles for the Woo Cart Products module. <!-- AUTO-ADDED --> |
| Button- |  | Choose the button's design styles. Those will apply to the Apply Coupon button as well as the Update Cart button - when it becomes active. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Cart Products module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Cart Products module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Cart Products module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Cart Products module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Cart Products module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Cart Products module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Cart Products module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

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
| [CSS](../options-groups/css.md) | Custom CSS per element target (table, rows, cells, buttons, images) |
| HTML | Semantic HTML tag selection for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS to the Woo Cart Products module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Cart Products module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Woo Cart Products' module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Cart Products module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Cart Products module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Style the cart table with clean borders */
.et_pb_wc_cart_products .woocommerce-cart-form table.shop_table {
    border-collapse: separate;
    border-spacing: 0;
    border: 1px solid #e5e5e5;
    border-radius: 8px;
    overflow: hidden;
}

/* Style table header */
.et_pb_wc_cart_products table.shop_table thead th {
    background-color: #f8f9fa;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 12px;
    letter-spacing: 1px;
    padding: 16px 20px;
}

/* Style product rows */
.et_pb_wc_cart_products table.shop_table tbody td {
    padding: 20px;
    vertical-align: middle;
    border-bottom: 1px solid #f0f0f0;
}

/* Style the coupon input field */
.et_pb_wc_cart_products .coupon input[type="text"] {
    border: 2px solid #e5e5e5;
    border-radius: 4px;
    padding: 10px 14px;
    transition: border-color 0.3s ease;
}

.et_pb_wc_cart_products .coupon input[type="text"]:focus {
    border-color: #2ea3f2;
    outline: none;
}

/* Style the Apply Coupon button */
.et_pb_wc_cart_products .coupon button {
    background-color: #2ea3f2;
    color: #fff;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    cursor: pointer;
}

/* Responsive: stack cells on mobile */
@media (max-width: 767px) {
    .et_pb_wc_cart_products table.shop_table thead {
        display: none;
    }
    .et_pb_wc_cart_products table.shop_table tbody td {
        display: block;
        text-align: right;
        padding: 10px 15px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Cart Products module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_cart_products' !== $render_slug) {
        return $output;
    }
    // Add a "Continue Shopping" link below the cart table
    $shop_url = get_permalink(wc_get_page_id('shop'));
    $output .= '<div class="continue-shopping"><a href="' . esc_url($shop_url) . '">&larr; Continue Shopping</a></div>';
    return $output;
}, 10, 2);

/* Add a custom column to the cart table */
add_filter('woocommerce_cart_item_name', function($name, $cart_item, $cart_item_key) {
    if (isset($cart_item['data'])) {
        $sku = $cart_item['data']->get_sku();
        if ($sku) {
            $name .= '<br><small class="cart-item-sku">SKU: ' . esc_html($sku) . '</small>';
        }
    }
    return $name;
}, 10, 3);
```

## Common Patterns

1. **Side-by-Side Cart Layout** — Place the Woo Cart Products module in a two-thirds column and Woo Cart Totals in a one-third column within the same row. This desktop layout keeps the order summary visible while customers adjust quantities. Add Woo Cross Sells in a full-width row below to suggest additional products.

2. **Image-Free Digital Cart** — For digital product stores selling software, ebooks, or downloads, disable the Show Product Image toggle to create a compact, text-focused cart table. Enable the coupon code field prominently for promotional campaigns and use custom CSS to add generous padding for readability.

3. **Branded Cart with Custom Buttons** — Use the Button design options to style the Apply Coupon and Update Cart buttons with your brand colors, custom border radius, and hover effects. Match the table header background to your brand's secondary color and apply consistent typography through the Text styling options for a cohesive checkout flow.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-cart-products` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Cart Products module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple cart instances, or added to your Divi Library for reuse on other templates by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Cart Products module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "Cart Table Shows Empty"
    If the module renders but displays an empty table, verify that the template is assigned to the WooCommerce cart page in the Theme Builder. The module requires the cart page context to function. Also confirm that you have products added to the cart when previewing — use a separate browser tab to add products, then refresh the cart page preview.

!!! warning "Coupon Code Not Working"
    If the coupon input field appears but submitted codes are not applied, check WooCommerce > Settings > General and ensure coupons are enabled. Also verify the specific coupon exists and meets its usage conditions (minimum spend, allowed products, expiry date) in WooCommerce > Marketing > Coupons.

!!! tip "Update Cart Button Stays Disabled"
    The Update Cart button is intentionally disabled until a customer changes a quantity value. This is standard WooCommerce behavior. If you want the button always active, use custom JavaScript to remove the disabled attribute, though this is generally not recommended as it may cause unnecessary page reloads.

## Related

- [Woo Cart Totals](woo-cart-totals.md)
- [Woo Cross Sells](woo-cross-sells.md)
- [Shop](shop.md)
