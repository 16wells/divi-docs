---
title: "Woo Cross Sells"
description: "Complete Divi 5 Woo Cross Sells module reference — settings, design options, code examples, and troubleshooting for WooCommerce cross-sell product suggestions."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "cart", "cross-sells"]
related: ["woo-cart-products", "woo-related-products"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/12095391"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Woo Cross Sells

The Woo Cross Sells module displays cross-sell product suggestions on the WooCommerce cart page to encourage additional purchases.

!!! abstract "Quick Reference"
    **What it does:** Shows cross-sell products linked to items currently in the cart, prompting customers to add complementary items before checkout.
    **When to use it:** Custom cart page templates built in the Divi Theme Builder
    **Key settings:** Title Text, Price Text, Link, Background
    **Block identifier:** `divi/wc-cross-sells`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095391)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce cart page template in the Theme Builder
    - Increasing average order value by surfacing complementary product suggestions
    - Pairing with Woo Cart Products and Woo Cart Totals for a complete cart layout

!!! warning "When NOT to Use This Module"
    - On non-cart pages — cross-sells depend on cart contents and require the cart context
    - For related products on single product pages — use [Woo Related Products](woo-related-products.md)
    - For general product grids — use [Shop](shop.md)

## Overview

The Woo Cross Sells module dynamically displays products that have been linked as cross-sells to items in the customer's cart. Cross-selling is a merchandising strategy where complementary products are suggested alongside the items a customer is already purchasing — similar to impulse-buy displays near a physical store's register.

The products shown by this module are configured in each product's **Linked Products** section within the WooCommerce product editor. When a customer adds a product to their cart, any cross-sell products linked to that item appear in this module on the cart page.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12095391).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. It will only display content when products in the cart have cross-sell products configured.

<!-- ![Woo Cross Sells module](../assets/screenshots/modules/woo-cross-sells/element.png){ loading=lazy } -->
<!-- *The Woo Cross Sells module displaying complementary product suggestions on the cart page.* -->

## Use Cases

1. **Cart Page Upselling** — Display complementary accessories, add-ons, or related products beneath the cart table to encourage impulse purchases before checkout.
2. **Bundled Product Suggestions** — Suggest products that pair well with items already in the cart, such as a phone case when a phone is in the cart.
3. **Complete Cart Layout** — Combine with the Woo Cart Products and Woo Cart Totals modules to build a fully custom cart page that matches your store's branding.

## How to Add the Woo Cross Sells Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to the WooCommerce cart page.
2. Open the Visual Builder on the cart template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Cross Sells" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12095391).

## Settings & Options

The Woo Cross Sells module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the module's link behavior, background, ordering, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Link | url | Optionally make the entire cross-sells module clickable, directing users to a specific page or URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the cross-sells module. |
| Loop | toggle | Enable the Loop Builder feature for dynamic template contexts. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |
| Loop- |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |

<!-- ![Woo Cross Sells Content tab settings](../assets/screenshots/modules/woo-cross-sells/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual styling of the cross-sell product cards and their text.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Title Text | text styling | Customize the font, size, color, weight, and letter spacing of cross-sell product titles. |
| Price Text | text styling | Style the price display on each cross-sell product card, including font, color, and size. |
| Text |  | Choose the overall text styles for the Woo Cross Sells module. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Cross Sells module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Cross Sells module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Cross Sells module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Cross Sells module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Cross Sells module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Cross Sells module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Cross Sells module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Woo Cross Sells Design tab settings](../assets/screenshots/modules/woo-cross-sells/settings-design.png){ loading=lazy } -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Choose the semantic HTML tag for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS to the Woo Cross Sells module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Cross Sells module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Woo Cross Sells' module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Cross Sells module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Cross-Sells module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

<!-- ![Woo Cross Sells Advanced tab settings](../assets/screenshots/modules/woo-cross-sells/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the cross-sells container */
.et_pb_wc_cross_sells {
    background: #f9f9f9;
    padding: 30px;
    border-radius: 8px;
}

/* Style the cross-sells heading */
.et_pb_wc_cross_sells h2 {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 20px;
}

/* Style individual cross-sell product cards */
.et_pb_wc_cross_sells .cross-sells .products li {
    background: #fff;
    border-radius: 6px;
    padding: 15px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
    transition: box-shadow 0.3s ease;
}

/* Hover effect on product cards */
.et_pb_wc_cross_sells .cross-sells .products li:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

/* Style cross-sell product titles */
.et_pb_wc_cross_sells .cross-sells .products li .woocommerce-loop-product__title {
    font-size: 16px;
    font-weight: 500;
    color: #333;
}

/* Style cross-sell product prices */
.et_pb_wc_cross_sells .cross-sells .products li .price {
    font-size: 15px;
    color: #2ea3f2;
    font-weight: 600;
}

/* Style the Add to Cart button */
.et_pb_wc_cross_sells .cross-sells .products li .button {
    background: #2ea3f2;
    color: #fff;
    border-radius: 4px;
    padding: 8px 16px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_cross_sells {
        padding: 20px 15px;
    }
    .et_pb_wc_cross_sells .cross-sells .products li {
        margin-bottom: 15px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Cross Sells module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_cross_sells' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Limit the number of cross-sell products displayed */
add_filter('woocommerce_cross_sells_total', function($total) {
    return 4; // Show maximum of 4 cross-sell products
});

/* Change the number of columns for cross-sell products */
add_filter('woocommerce_cross_sells_columns', function($columns) {
    return 3; // Display in 3 columns
});
```

## Common Patterns

1. **Cart Page Footer** — Place the cross-sells module in a full-width row below the cart table and cart totals. This positions the suggestions where customers see them before scrolling to checkout, maximizing visibility without disrupting the checkout flow.

2. **Sidebar Suggestions** — In a two-column cart layout, use one column for the cart table and totals, and place the cross-sells module in the narrower sidebar column for a persistent product suggestion area.

3. **Styled Product Cards** — Apply custom border-radius, box shadows, and hover effects to cross-sell product cards to make them visually distinct from the cart table, drawing attention to the additional purchasing opportunity.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-cross-sells` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For cross-sell suggestions on the cart page use Woo Cross Sells; for related products on single product pages use Woo Related Products; for general product grids use Shop.

## Saving Your Work

After configuring the cross-sells module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Cross-sell products must be configured in the **Linked Products** section of each WooCommerce product for this module to display content.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Cross Sells module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a cart page template (not a regular page)
    - The module is not inside a disabled section or row
    - Visibility settings are not hiding it on the current device

!!! warning "No Cross-Sell Products Showing"
    If the module renders but displays no products, check that:

    - Products in the cart have cross-sell products configured under **Product Data > Linked Products**
    - The linked cross-sell products are published and in stock
    - Cross-sell products are not the same as items already in the cart

!!! tip "Cross-Sells Not Updating After Cart Changes"
    Cross-sell products are determined by the items currently in the cart. When a customer adds or removes items, the cross-sells should update on page reload. If they appear stale, check for page caching that may be serving an outdated cart page.

## Related

- [Woo Cart Products](woo-cart-products.md) — Displays the cart contents table on the cart page
- [Woo Related Products](woo-related-products.md) — Shows related products on single product pages
- [Woo Cart Totals](woo-cart-totals.md) — Displays cart subtotal, taxes, and total on the cart page
- [Shop](shop.md) — General product grid display module
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
