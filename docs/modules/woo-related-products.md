---
title: "Woo Related Products"
description: "Divi 5 Woo Related Products module — WooCommerce related product suggestions on product pages to increase sales and engagement."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "related-products", "upsell"]
related: ["woo-products", "woo-cross-sells", "shop"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12041865"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Woo Related Products

The Woo Related Products module displays related WooCommerce products on product pages to encourage additional browsing and purchases.

!!! abstract "Quick Reference"
    **What it does:** Shows products related to the current product based on shared categories and tags, displayed in a configurable grid.
    **When to use it:** Product page templates in the Theme Builder
    **Key settings:** Product Count, Column Layout, Order, Included Categories, Show elements (Name, Image, Price, Rating, Sale Badge), Product Offset
    **Block identifier:** `divi/woo-related-products`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12041865)

!!! tip "When to Use This Module"
    - Building custom product page templates with a "You may also like" section
    - Increasing product page engagement and average order value through related product suggestions
    - Displaying category-filtered related products for more targeted recommendations

!!! warning "When NOT to Use This Module"
    - On non-product pages — related products require a product context to determine relationships
    - For cross-sell suggestions on the cart page — use [Woo Cross Sells](woo-cross-sells.md)
    - For manually curated product grids — use [Shop](shop.md) or [Woo Products](woo-products.md)

## Overview

The Woo Related Products module displays products that share categories or tags with the product currently being viewed. WooCommerce determines the relationship automatically based on the product's assigned categories and tags, then the module renders those related products in a styled grid. This encourages customers to continue browsing after viewing a product, increasing time on site and the likelihood of additional purchases.

The module provides control over how many related products appear, how they are arranged in columns, and how they are sorted. You can also filter related products by specific categories using the Included Categories setting, which narrows the suggestions to products from particular categories rather than showing all category-matched results. The Product Offset setting allows you to skip a number of products from the results, useful for preventing the same related products from appearing across similar product pages.

Each product card in the related products grid can display the featured image, product name, price, star rating, and sale badge. These elements are individually toggleable, giving you control over the density of information displayed. The grid includes image overlay controls for hover effects, adding a polished interactive feel to the product suggestions.

This module is one of the key building blocks for custom product page templates in the Theme Builder. It pairs well with the main product content modules (title, price, images, description) and creates a complete product page experience that encourages continued shopping.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated. It will not appear in the module picker if WooCommerce is absent.

[View the official Elegant Themes documentation for this module.](https://help.elegantthemes.com/en/articles/12041865)

<!-- ![Woo Related Products module overview](../assets/screenshots/modules/woo-related-products/overview.png){ loading=lazy } -->
<!-- *The Woo Related Products module as it appears in the Divi 5 Visual Builder.* -->

## Use Cases

1. **"You May Also Like" Section** — Place the module at the bottom of the product page template in a full-width row with a heading above it. Set the Product Count to 4 with a 4-column layout. This is the most common pattern and mirrors what customers expect from major e-commerce sites, keeping them browsing after they finish reading about a product.

2. **Category-Specific Recommendations** — Use the Included Categories filter to show related products only from the same category as the current product. This creates more targeted recommendations — for example, on a running shoe product page, only other running shoes appear rather than all footwear. This increases the relevance of suggestions and improves click-through rates.

3. **Sidebar Product Suggestions** — Place the module in a narrow sidebar column with a 1-column layout and a Product Count of 3-4. Disable the sale badge and rating to keep the display compact. This provides persistent product suggestions alongside the main product content without taking up full-width space.

## How to Add the Woo Related Products Module

1. Ensure WooCommerce is installed and activated, and that products have categories or tags assigned so WooCommerce can determine relationships.
2. Open the Visual Builder on a product page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Related Products" in the module picker or find it in the WooCommerce category, then click to insert it.

## Settings & Options

The Woo Related Products module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which related products display, how they are filtered and sorted, and what elements are visible on each product card.

| Setting | Type | Description |
|---------|------|-------------|
| Product | select | Choose the product for which you want to display related products. On Theme Builder templates, this defaults to the current product dynamically. |
| Product Count | number input | Set the maximum number of related products to display in the grid. |
| Column Layout | select | Set the number of columns in the related products grid. Affects how many products appear per row on desktop. |
| Order | select | Control the sort order of related products. Options include date, title, price, popularity, rating, and random. |
| Included Categories | multi-select | Filter related products by specific WooCommerce product categories. Narrows the suggestions beyond the default category/tag matching. |
| Product Offset Number | number input | Skip a specified number of products from the beginning of the related products query results. Useful for preventing repetitive product suggestions across similar product pages. |
| Show Name | toggle | Display or hide the product title on each related product card. |
| Show Image | toggle | Display or hide the product featured image. |
| Show Price | toggle | Display or hide the product price, including sale pricing when applicable. |
| Show Rating | toggle | Display or hide the star rating on each product card. |
| Show Sale Badge | toggle | Display or hide the "Sale" badge overlay on related products that are currently on sale. |
| Link | url | Optionally make the entire module clickable, directing visitors to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the module. |
| Order (Flexbox) | select | Control the module's placement order within Flexbox and Grid parent layouts. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |
| Content |  | Choose the product for which you want to display the related products.Product Count- Choose how many linked upsell products the module displays.Column Layout- Choose the number of columns in which the linked upsell products are displayed.Order- Choose how the linked upsell products are ordered.Included Categories- Choose based on which WooCommerce categories the related products should be generated.Product Offset Number- Choose the number of products that are offset. <!-- AUTO-ADDED --> |
| Elements |  | Choose to display or hide different elements, such as:Show Name- Display or hide the product's titles.Show Image- Display or hide the product's featured image.Show Price- Display or hide the product's price.Show Rating -Display or hide the product's ratings.Show Sale Badge- Display or hide the product's sale badge. <!-- AUTO-ADDED --> |
| Show Rating - |  | Display or hide the product's ratings. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Woo Related Products Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides controls for the visual presentation of the related products grid, including image overlays, typography, sale badges, and star ratings.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Overlay | styling controls | Configure the featured image overlay including overlay color, overlay icon, and hover behavior. Controls the visual effect when hovering over related product images. |
| Image | styling controls | Customize the product featured image appearance including border radius, box shadow, spacing, and object fit. |
| Star Rating | color/size controls | Adjust the star rating display including alignment, filled color, empty color, star size, and spacing between stars. |
| Sale Badge | styling controls | Customize the sale badge appearance including background color, text color, font, size, border radius, and positioning. |
| Title Text | text styling | Control the font, size, color, weight, line height, and letter spacing for the module heading ("Related Products"). |
| Product Title Text | text styling | Style the individual product name text on each card separately from the module heading. |
| Price Text | text styling | Customize the regular price text including font family, size, weight, and color. |
| Sale Price Text | text styling | Style the sale price independently from the regular price, including strikethrough styling for the original price. |
| Text |  | Choose the design style for the number of reviews text. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Related Products module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Related Products module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Related Products module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Related Products module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Related Products module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Related Products module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Related Products module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

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
| [CSS](../options-groups/css.md) | Custom CSS per element target (product card, image, title, price, sale badge, rating, overlay) |
| HTML | Semantic HTML tag selection for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS to the Woo Related Products module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Related Products module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Woo Related Products' module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Related Products module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Related Products module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Style the related products section heading */
.et_pb_wc_related_products h2 {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #2ea3f2;
}

/* Style related product cards */
.et_pb_wc_related_products ul.products li.product {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.et_pb_wc_related_products ul.products li.product:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

/* Style the product image */
.et_pb_wc_related_products ul.products li.product a img {
    width: 100%;
    transition: transform 0.3s ease;
}

.et_pb_wc_related_products ul.products li.product:hover a img {
    transform: scale(1.05);
}

/* Style the product title */
.et_pb_wc_related_products ul.products li.product h3 {
    font-size: 15px;
    font-weight: 600;
    padding: 10px 15px 5px;
}

/* Style the price */
.et_pb_wc_related_products ul.products li.product .price {
    color: #2ea3f2;
    font-weight: 700;
    padding: 0 15px 15px;
}

/* Sale badge */
.et_pb_wc_related_products span.onsale {
    background-color: #e74c3c;
    color: #fff;
    border-radius: 4px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_wc_related_products ul.products li.product {
        width: 48% !important;
    }
}

@media (max-width: 767px) {
    .et_pb_wc_related_products ul.products li.product {
        width: 100% !important;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Related Products module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_related_products' !== $render_slug) {
        return $output;
    }
    // Example: Change the related products heading
    $output = str_replace('Related products', 'You May Also Like', $output);
    return $output;
}, 10, 2);

/* Change the number of related products WooCommerce returns */
add_filter('woocommerce_output_related_products_args', function($args) {
    $args['posts_per_page'] = 8;
    $args['columns'] = 4;
    return $args;
});

/* Exclude specific categories from related products */
add_filter('woocommerce_related_products', function($related_posts, $product_id, $args) {
    $exclude_cat_ids = array(15, 23); // Category IDs to exclude
    foreach ($related_posts as $key => $related_id) {
        $terms = get_the_terms($related_id, 'product_cat');
        if ($terms) {
            foreach ($terms as $term) {
                if (in_array($term->term_id, $exclude_cat_ids)) {
                    unset($related_posts[$key]);
                    break;
                }
            }
        }
    }
    return array_values($related_posts);
}, 10, 3);
```

## Common Patterns

1. **Full-Width Related Products Row** — Place the module in a full-width row at the bottom of the product page template with 4 columns and 4 products. Add a section background color that differs from the main content area to visually separate the related products. This is the standard e-commerce pattern that customers expect.

2. **Compact Sidebar Suggestions** — In a two-column product layout, place the module in the narrower sidebar column with 1 column and 3 products. Disable the sale badge and rating to keep the display compact. This provides persistent "browse more" options alongside the main product details.

3. **Styled Card Grid with Overlay** — Enable the image overlay design settings and configure a semi-transparent overlay color with an icon. Apply card-style box shadows and hover lift effects to the product cards. This creates a polished, interactive product suggestion section that invites clicking and exploration.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content
    that renders on the front end but may not appear in the Visual Builder layer
    view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-related-products` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Product | `attrs.product` | Target product for related products lookup |
| Product Count | `attrs.posts_number` | Maximum related products to display |
| Column Layout | `attrs.columns_number` | Number of grid columns |
| Order | `attrs.orderby` | Sort order field |
| Included Categories | `attrs.include_categories` | Category filter for related products |
| Product Offset | `attrs.offset_number` | Number of products to skip |

!!! tip "Module Selection Guidance"
    For related products on product pages use Woo Related Products; for cross-sells on the cart page use Woo Cross Sells; for manually curated product grids use Shop or Woo Products.

## Saving Your Work

After configuring the Woo Related Products module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple product templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Related Products module in Divi 5 benefits from the updated rendering engine and supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated. Related products are determined by WooCommerce based on shared categories and tags. Products must have categories or tags assigned for relationships to be established. WooCommerce 7.0 or later is recommended for full Divi 5 compatibility.

## Troubleshooting

!!! warning "No Related Products Displaying"
    If the module appears but shows no products, verify that the current product has categories or tags assigned in WooCommerce. Related products are determined by shared categories and tags — if a product has no categories or tags, WooCommerce cannot find related products. Also check that other published products share at least one category or tag with the current product.

!!! warning "Same Related Products on Every Page"
    WooCommerce's related products algorithm includes a degree of randomness. However, if you consistently see the same products, it may be because only a few products share categories/tags with the current product. Add more products to shared categories, or use the Included Categories filter to broaden the pool of potential related products.

!!! tip "Related Products Not Updating After Category Changes"
    If you recently changed product categories but related products have not updated, clear your site cache. WooCommerce and caching plugins may cache the related products query. Also verify that the category changes have been saved and the products are still published.

## Related

- [Woo Products](woo-products.md)
- [Woo Cross Sells](woo-cross-sells.md)
- [Shop](shop.md)
