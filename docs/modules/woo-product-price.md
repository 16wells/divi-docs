---
title: "Woo Product Price"
description: "Complete Divi 5 Woo Product Price module reference — settings, design options, code examples, and troubleshooting for WooCommerce product price display."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "pricing"]
related: ["woo-product-title", "woo-product-stock", "shop"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12034706"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Woo Product Price

The Woo Product Price module displays the WooCommerce product price with support for regular pricing, sale pricing with strikethrough formatting, and custom typography.

!!! abstract "Quick Reference"
    **What it does:** Renders the WooCommerce product price, automatically displaying sale prices with the original price struck through and the discounted price highlighted.
    **When to use it:** Product page templates, custom product layouts in the Theme Builder
    **Key settings:** Product selector, Price Text, Sale Old Price Text, Sale New Price Text
    **Block identifier:** `divi/wc-product-price`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12034706)

!!! tip "When to Use This Module"
    - Building custom WooCommerce product page templates with prominent pricing
    - Displaying sale prices with visual emphasis on the discount
    - Positioning the price independently from other product elements in custom layouts

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce pages — this module requires a product context
    - For product grids with prices — use [Shop](shop.md) (prices are built in)
    - For cart or checkout totals — use [Woo Cart Totals](woo-cart-totals.md) or [Woo Checkout Details](woo-checkout-details.md)

## Overview

The Woo Product Price module pulls the price directly from the WooCommerce product data fields and renders it with full typographic control. When a product has a sale price configured, the module automatically displays both the original price (with strikethrough formatting) and the sale price, making the discount immediately visible to customers.

The module provides independent styling controls for the regular price, the original sale price (crossed out), and the new sale price, allowing you to create strong visual hierarchy that draws attention to discounts and promotions.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12034706).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Prices are pulled from the WooCommerce product editor's pricing fields.

<!-- ![Woo Product Price module](../assets/screenshots/modules/woo-product-price/element.png){ loading=lazy } -->
<!-- *The Woo Product Price module displaying regular and sale pricing in the Visual Builder.* -->

## Use Cases

1. **Prominent Price Display** — Place the price module in large, bold typography directly below the product title and above the add-to-cart button, making pricing the focal point of the product page.
2. **Sale Price Emphasis** — Style the old price in a muted color with strikethrough and the new sale price in a bold, attention-grabbing color to highlight the discount.
3. **Price in Product Header** — Position the price module alongside the product title in a horizontal layout using flexbox ordering, creating a compact product header with title and price side by side.

## How to Add the Woo Product Price Module

1. Navigate to **Divi > Theme Builder** and create or edit a product page template.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Product Price" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12034706).

## Settings & Options

The Woo Product Price module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product is referenced and the module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Content (Product) | select | Choose which product supplies the price data. On a dynamic product template, this defaults to the current product. |
| Link | url | Optionally make the entire module clickable, directing users to a specific page or URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the price module. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |
| Content |  | Choose the product details displayed by the Woo Product Price module. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |

<!-- ![Woo Product Price Content tab settings](../assets/screenshots/modules/woo-product-price/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the visual styling of the price text, including separate controls for regular and sale pricing.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Price Text | text styling | Customize the font family, size, color, weight, letter spacing, and line height of the regular product price display. |
| Sale Old Price Text | text styling | Style the original price when a product is on sale. This text is typically displayed with strikethrough formatting. Customize font, color, and size independently from the sale price. |
| Sale New Price Text | text styling | Style the discounted sale price. Customize font, color, size, and weight to make the sale price visually prominent. |
| Sizing |  | Choose the Woo Product Price module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Product Price module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Product Price module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Product Price module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Product Price module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Product Price module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Product Price module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, hue, saturation, blending) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Woo Product Price Design tab settings](../assets/screenshots/modules/woo-product-price/settings-design.png){ loading=lazy } -->

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
| CSS |  | Allows you to add custom CSS to the Woo Product Price module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Product Price module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Woo Product Price's module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Product Price module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Product Price module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

<!-- ![Woo Product Price Advanced tab settings](../assets/screenshots/modules/woo-product-price/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the price container */
.et_pb_wc_price {
    margin-bottom: 15px;
}

/* Style the regular price */
.et_pb_wc_price .price {
    font-size: 28px;
    font-weight: 700;
    color: #222;
}

/* Style the original price on sale items (strikethrough) */
.et_pb_wc_price .price del {
    font-size: 20px;
    color: #999;
    font-weight: 400;
    text-decoration: line-through;
    margin-right: 8px;
}

/* Style the sale price */
.et_pb_wc_price .price ins {
    font-size: 28px;
    color: #e74c3c;
    font-weight: 700;
    text-decoration: none;
}

/* Style variable product price range */
.et_pb_wc_price .price .woocommerce-Price-amount {
    font-weight: 700;
}

/* Add a "From" label for variable products */
.et_pb_wc_price .price .woocommerce-Price-currencySymbol {
    font-size: 0.75em;
    vertical-align: top;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_price .price {
        font-size: 24px;
    }
    .et_pb_wc_price .price del {
        font-size: 18px;
    }
    .et_pb_wc_price .price ins {
        font-size: 24px;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Price module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_price' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Add a "Save X%" badge after the price */
add_filter('woocommerce_get_price_html', function($price, $product) {
    if ($product->is_on_sale() && $product->get_regular_price()) {
        $percentage = round((($product->get_regular_price() - $product->get_sale_price()) / $product->get_regular_price()) * 100);
        $price .= '<span class="save-badge"> Save ' . $percentage . '%</span>';
    }
    return $price;
}, 10, 2);
```

## Common Patterns

1. **Title-Price Stack** — Place the Woo Product Price module directly below the Woo Product Title module in a single column. Use a large font size and bold weight for the price to create a clear visual hierarchy from title to price to add-to-cart.

2. **Sale Highlight** — Style the old price in a light gray with strikethrough and the sale price in red or another accent color with a larger font size. This creates a strong visual contrast that emphasizes the discount.

3. **Compact Price Row** — Use flexbox ordering to place the price module in the same row as the product title, creating a horizontal layout where the title and price appear side by side. This works well for minimalist product page designs.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-product-price` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Product | `attrs.product` | Product ID reference |

!!! tip "Module Selection Guidance"
    For standalone product price display use Woo Product Price; for product grids with built-in pricing use Shop; for cart/checkout totals use Woo Cart Totals.

## Saving Your Work

After configuring the product price module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Prices are pulled from the WooCommerce product editor's pricing fields (Regular price and Sale price).

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Price module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template or a page with a valid product context
    - The module is not inside a disabled section or row
    - Visibility settings are not hiding it on the current device

!!! warning "Price Shows as Empty or Zero"
    If the module renders but displays no price or shows $0.00, check that:

    - The product has a regular price set in **Product Data > General** in the WooCommerce product editor
    - For variable products, at least one variation has a price defined
    - The product is published and not in draft status

!!! warning "Sale Price Not Showing Strikethrough"
    If a product is on sale but the original price does not show the strikethrough formatting, verify that:

    - Both a regular price and a sale price are configured in the WooCommerce product editor
    - The sale schedule has not expired (check the sale date range if set)
    - Custom CSS is not overriding the `text-decoration` property on the `del` element

!!! tip "Price Format Looks Wrong"
    If the currency symbol, decimal places, or thousands separator appear incorrect, check your WooCommerce currency settings under **WooCommerce > Settings > General**. The module inherits the global WooCommerce price format.

## Related

- [Woo Product Title](woo-product-title.md) — Displays the product title with customizable typography
- [Woo Product Stock](woo-product-stock.md) — Shows product stock status and availability
- [Shop](shop.md) — Product grid module with built-in pricing display
- [Woo Cart Totals](woo-cart-totals.md) — Displays cart subtotal and total on the cart page
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
