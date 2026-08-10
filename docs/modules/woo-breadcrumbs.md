---
title: "Woo Breadcrumbs"
description: "Divi 5 Woo Breadcrumbs module — WooCommerce breadcrumb navigation for product pages with customizable styling, separator options, and dynamic home links."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "navigation", "breadcrumbs", "product"]
related: ["woo-products", "woo-product-title"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12032985"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Woo Breadcrumbs

The Woo Breadcrumbs module displays WooCommerce breadcrumb navigation to help customers orient themselves within your store.

!!! abstract "Quick Reference"
    **What it does:** Displays WooCommerce breadcrumb navigation showing the path from shop to current product or category.
    **When to use it:** Product page templates, category archive templates, custom shop layouts
    **Key settings:** Product, Home Text, Home Link, Separator, Text styling
    **Block identifier:** `divi/woo-breadcrumbs`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12032985)

!!! tip "When to Use This Module"
    - Adding breadcrumb navigation to WooCommerce product page templates in the Theme Builder
    - Helping customers navigate back to parent categories or the shop page
    - Improving SEO with structured breadcrumb markup on product pages

!!! warning "When NOT to Use This Module"
    - On non-WooCommerce pages — breadcrumbs require WooCommerce context
    - For general site breadcrumbs outside of WooCommerce — use a dedicated breadcrumb plugin
    - For page-level navigation — use [Post Navigation](post-navigation.md)

## Overview

The Woo Breadcrumbs module renders a navigational trail that shows customers exactly where they are within your WooCommerce store hierarchy. When placed on a product page, the breadcrumbs might display something like "Home > Clothing > Men > T-Shirts > Product Name," giving visitors a clear path to retrace their steps. This navigational aid is particularly valuable for stores with deep category structures where customers may have arrived via search or a direct link.

Unlike static breadcrumb implementations, this module pulls its data dynamically from WooCommerce's category taxonomy. The path updates automatically based on the product's assigned categories, and you can customize the home link text and URL to match your site's structure. The separator between breadcrumb items is also configurable, letting you use arrows, slashes, or other visual indicators.

This module is designed specifically for use within Theme Builder templates assigned to WooCommerce product pages, category archives, or other shop-related templates. It requires WooCommerce to be installed and activated. For the official Elegant Themes documentation, see the [Woo Breadcrumbs help article](https://help.elegantthemes.com/en/articles/12032985).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Product Page Header Navigation** — Place the breadcrumbs at the top of your product page template, above the product title, so customers can quickly return to the parent category or shop page. This mirrors the standard WooCommerce layout convention that shoppers expect.

2. **Multi-Level Category Store** — For stores with hierarchical category structures (e.g., Electronics > Computers > Laptops > Gaming Laptops), breadcrumbs help customers understand their location and navigate up any number of levels without relying on the main menu.

3. **SEO-Enhanced Product Templates** — Breadcrumbs generate structured navigation markup that search engines can use for rich snippets. Adding this module to every product template ensures consistent breadcrumb data across your entire catalog, improving how your products appear in search results.

## How to Add the Woo Breadcrumbs Module

1. Ensure WooCommerce is installed, activated, and that you have at least one published product. Navigate to the Theme Builder to create or edit a product page template.
2. Open the Visual Builder on your product page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Breadcrumbs" in the module picker or find it in the WooCommerce category, then click to insert it. The module will automatically display breadcrumb navigation based on the current product's category path.

## Settings & Options

The Woo Breadcrumbs module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the breadcrumb data source, home link configuration, separator style, and background.

| Setting | Type | Description |
|---------|------|-------------|
| Product | select | Choose which product's breadcrumb path to display. In Theme Builder templates, this defaults to the current product dynamically. |
| Home Text | text | Set the text for the first breadcrumb item (the "home" link). Supports Dynamic Content for localized or context-aware labels. |
| Home Link | url | Set the URL destination for the home breadcrumb item. Useful for pointing to your shop page instead of the site homepage. Supports Dynamic Content. |
| Separator | select | Choose the visual separator character displayed between breadcrumb items (e.g., >, /, or custom characters). |
| Link | url | Optionally make the entire module a clickable link to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the breadcrumb module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |
| Content |  | Choose the product details displayed by the Woo Breadcrumbs module.Product- Choose the product for which the Breadcrumbs module will be used.Home Text- Choose the text of the Breadcrumb's first item. You can also use Dynamic Content.Home Link- Choose the link for the first Breadcrumb's item. You can also use Dynamic Content.Separator: Choose how the Breadcrumbs items are separated. <!-- AUTO-ADDED --> |
| Loop- |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Woo Breadcrumbs Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab controls the visual appearance of the breadcrumb text, including typography and layout styling.

**Module-specific settings:**

This module does not have module-specific design settings beyond the shared options below. All breadcrumb text styling is handled through the Text options group.

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow for breadcrumb text |
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |
| Text |  | Choose the overall text styles for the Woo Breadcrumbs module. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Breadcrumbs module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Breadcrumbs module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Breadcrumbs module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Breadcrumbs module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Breadcrumbs module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Breadcrumbs module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Breadcrumbs module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Semantic HTML tag selection for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS to the Woo Breadcrumbs module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Breadcrumbs module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Woo Breadcrumbs's module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Breadcrumbs module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Breadcrumbs module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Style breadcrumb container with subtle background */
.et_pb_wc_breadcrumb {
    background-color: #f8f9fa;
    padding: 12px 20px;
    border-radius: 4px;
    margin-bottom: 20px;
}

/* Style breadcrumb links */
.et_pb_wc_breadcrumb .woocommerce-breadcrumb a {
    color: #2ea3f2;
    text-decoration: none;
    font-weight: 500;
}

.et_pb_wc_breadcrumb .woocommerce-breadcrumb a:hover {
    color: #1a7abf;
    text-decoration: underline;
}

/* Style the separator */
.et_pb_wc_breadcrumb .woocommerce-breadcrumb {
    font-size: 14px;
    color: #666;
}

/* Responsive: smaller text on mobile */
@media (max-width: 767px) {
    .et_pb_wc_breadcrumb .woocommerce-breadcrumb {
        font-size: 12px;
        padding: 8px 12px;
    }
}
```

### PHP Hooks

```php
/* Customize the WooCommerce breadcrumb separator */
add_filter('woocommerce_breadcrumb_defaults', function($defaults) {
    $defaults['delimiter'] = ' <span class="breadcrumb-sep">&raquo;</span> ';
    $defaults['wrap_before'] = '<nav class="woocommerce-breadcrumb" aria-label="Breadcrumb">';
    $defaults['wrap_after'] = '</nav>';
    return $defaults;
});

/* Filter the Woo Breadcrumbs module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_breadcrumb' !== $render_slug) {
        return $output;
    }
    // Add schema markup wrapper for enhanced SEO
    $output = '<div itemscope itemtype="https://schema.org/BreadcrumbList">' . $output . '</div>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Standard Product Page Header** — Place the breadcrumbs module in the first row of your product page template, spanning the full width. Set the Home Text to "Shop" and the Home Link to your main shop page URL. This provides a consistent navigation pattern at the top of every product page, matching what customers expect from standard ecommerce layouts.

2. **Styled Breadcrumb Bar** — Apply a light background color through the Content tab's Background setting, add subtle padding via Spacing, and use a slim bottom border to create a breadcrumb navigation bar that visually separates the header from the product content. This works especially well with full-width row layouts.

3. **Breadcrumbs with Custom Separator** — Use the PHP hook to change the default separator from a simple slash to a chevron or right arrow character. Combine with custom CSS to add spacing around the separator and apply a muted color so the separator is visually distinct but not distracting.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-breadcrumbs` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Breadcrumbs module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple breadcrumb instances, or added to your Divi Library for reuse on other templates by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Breadcrumbs module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "Breadcrumbs Not Displaying"
    If the module renders but shows no breadcrumb trail, verify that the product has at least one category assigned in WooCommerce. Products without categories produce minimal or empty breadcrumbs. Also confirm you are viewing the module on a page or template with WooCommerce product context — the module will not display useful data on a regular page or post.

!!! warning "Home Link Points to Wrong Page"
    If the first breadcrumb item links to the WordPress homepage instead of your shop page, use the Home Link setting to explicitly set the URL to your WooCommerce shop page. You can find this URL at WooCommerce > Settings > Products > Shop Page.

!!! tip "Breadcrumbs Missing in Visual Builder Preview"
    When editing a product page template in the Theme Builder, the breadcrumbs may show placeholder text since no specific product is loaded. Switch to previewing a specific product to see the actual breadcrumb trail, or save and preview the template on the front end.

## Related

- [Woo Products](woo-products.md)
- [Woo Product Title](woo-product-title.md)
