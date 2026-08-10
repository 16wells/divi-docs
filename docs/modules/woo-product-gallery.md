---
title: "Woo Product Gallery"
description: "Complete Divi 5 Woo Product Gallery module reference — settings, design options, code examples, and troubleshooting for WooCommerce product image galleries in slider or grid layout."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "product", "gallery", "images", "slider", "grid"]
related: ["woo-product-images", "gallery", "image"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/12033711"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Woo Product Gallery

The Woo Product Gallery module displays a WooCommerce product's gallery images in either a slider carousel or a four-column grid layout on custom single product page templates.

!!! abstract "Quick Reference"
    **What it does:** Renders the product gallery images in a slider or grid format, with optional pagination, titles, and captions.
    **When to use it:** Custom single product page templates built in the Divi Theme Builder
    **Key settings:** Product, Layout (Slider/Grid), Show Pagination, Show Title and Caption
    **Block identifier:** `divi/wc-gallery`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12033711)

!!! tip "When to Use This Module"
    - Building a custom product page that needs a gallery separate from the main product image
    - Displaying product photos in a browsable slider format for detailed product exploration
    - Showing product images in a grid layout with titles and captions for editorial-style product pages

!!! warning "When NOT to Use This Module"
    - For the primary product featured image — use [Woo Product Images](woo-product-images.md)
    - For non-WooCommerce image galleries — use [Gallery](gallery.md)
    - For a single standalone image — use [Image](image.md)

## Overview

The Woo Product Gallery module provides a dedicated way to showcase all gallery images assigned to a WooCommerce product. Unlike the Woo Product Images module, which focuses on the featured image with thumbnail navigation, this module presents the gallery images as a standalone visual element that can be styled and positioned independently within your product page layout.

The module offers two layout modes: **Slider** and **Grid**. In Slider mode, gallery images display in a horizontal carousel that customers can swipe or click through. In Grid mode, images are arranged in a four-column grid layout with optional pagination for products that have many gallery images. The Grid layout also supports displaying each image's title and caption text, which is useful for products where individual images need descriptive labels — such as product detail shots, different angles, or lifestyle imagery.

Each layout mode has its own set of conditional settings. Pagination controls and title/caption toggles only appear when Grid layout is selected, while the Slider mode provides a streamlined browsing experience without additional text overlays.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12033711).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and activated on your WordPress site. Gallery images must be added to the product in the WooCommerce product editor for this module to display content.

<!-- ![Woo Product Gallery module](../assets/screenshots/modules/woo-product-gallery/element.png){ loading=lazy } -->
<!-- *The Woo Product Gallery module displaying product images in a grid layout with titles and captions.* -->

## Use Cases

1. **Product Detail Showcase** — Place the gallery module below the main product information in a full-width row to give customers a dedicated image browsing area. Use the Slider layout for a focused, one-image-at-a-time viewing experience ideal for high-detail product photography.
2. **Grid Gallery with Descriptions** — Use the Grid layout with titles and captions enabled for products where each image tells part of the story — such as furniture with detail shots of materials, craftsmanship, and scale reference images.
3. **Supplementary Image Section** — Position the gallery module in a secondary section below the product description to provide additional visual context without cluttering the primary purchase area above the fold.

## How to Add the Woo Product Gallery Module

1. Navigate to **Divi > Theme Builder** and create or edit a template assigned to WooCommerce product pages.
2. Open the Visual Builder on the product template.
3. Click the gray **+** icon to add a new module to a row.
4. Search for "Woo Product Gallery" in the module picker, then click to insert it.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/12033711).

## Settings & Options

The Woo Product Gallery module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which product's gallery images are displayed and which elements are visible in the gallery.

| Setting | Type | Description |
|---------|------|-------------|
| Product | product selector | Choose which published WooCommerce product's gallery images to display. In Theme Builder templates, this defaults to the current product dynamically. |
| Show Pagination | toggle | Display or hide pagination controls below the grid. Only available when the Layout is set to Grid. Useful for products with many gallery images. |
| Show Title and Caption | toggle | Display or hide the image title and caption text below each gallery image. Only available when the Layout is set to Grid. |
| Background | background controls | Set a background color, gradient, image, or video behind the gallery module container. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |
| Content |  | Choose which product the module should display the Gallery Images.Show Pagination(applies to theGrid Layoutonly) - Display or Hide the Pagination.Show Title and Caption(applies to theGrid Layoutonly) - Display or Hide the image's title and caption text. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |

<!-- ![Woo Product Gallery Content tab settings](../assets/screenshots/modules/woo-product-gallery/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the gallery layout mode, image styling, and all text elements within the gallery.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between Slider (carousel browsing) or Grid (four-column layout) display format for gallery images. |
| Image | image styling | Apply design effects to individual gallery images, including border, shadow, and spacing. |
| Title Text | text styling | Customize the font, size, color, weight, and letter spacing of image titles. Only active when Grid layout and Show Title and Caption are enabled. |
| Caption Text | text styling | Style the caption text displayed below each gallery image. Only active when Grid layout and Show Title and Caption are enabled. |
| Pagination Text | text styling | Customize the appearance of pagination controls. Only active when Grid layout and Show Pagination are enabled. |
| Slider |  | Displays the product gallery in a slider format/layout. <!-- AUTO-ADDED --> |
| Grid |  | Displays the product gallery images in a 4-column grid layout. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall text styles for the Woo Product Gallery module. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Product Gallery module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Product Gallery module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Product Gallery module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Product Gallery module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Product Gallery module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Product Gallery module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Product Gallery module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

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

<!-- ![Woo Product Gallery Design tab settings](../assets/screenshots/modules/woo-product-gallery/settings-design.png){ loading=lazy } -->

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
| CSS |  | Allows you to add custom CSS to the Woo Product Gallery module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Product Gallery module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Woo Product Gallery's module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Product Gallery module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Product Gallery module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

<!-- ![Woo Product Gallery Advanced tab settings](../assets/screenshots/modules/woo-product-gallery/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the gallery container */
.et_pb_wc_gallery {
    padding: 20px 0;
}

/* Style gallery images in grid layout */
.et_pb_wc_gallery .woocommerce-product-gallery__image img {
    border-radius: 8px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.et_pb_wc_gallery .woocommerce-product-gallery__image img:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

/* Style image titles */
.et_pb_wc_gallery .wp-caption-text {
    font-size: 14px;
    color: #555;
    text-align: center;
    margin-top: 8px;
}

/* Style pagination controls */
.et_pb_wc_gallery .woocommerce-pagination {
    margin-top: 20px;
    text-align: center;
}

.et_pb_wc_gallery .woocommerce-pagination a {
    padding: 8px 14px;
    border: 1px solid #ddd;
    border-radius: 4px;
    color: #333;
    margin: 0 4px;
}

.et_pb_wc_gallery .woocommerce-pagination a:hover {
    background: #2ea3f2;
    color: #fff;
    border-color: #2ea3f2;
}

/* Responsive: stack grid to 2 columns on tablet */
@media (max-width: 980px) {
    .et_pb_wc_gallery .products {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Responsive: single column on mobile */
@media (max-width: 480px) {
    .et_pb_wc_gallery .products {
        grid-template-columns: 1fr;
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Product Gallery module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_gallery' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);

/* Filter the number of gallery columns */
add_filter('woocommerce_product_thumbnails_columns', function($columns) {
    return 3; // Change grid to 3 columns
});
```

## Common Patterns

1. **Two-Column Product Layout** — Place the Woo Product Gallery in the left column of a two-column row using Slider layout, and stack the product title, price, description, and add-to-cart modules in the right column. This creates a classic e-commerce product page with a prominent image carousel.

2. **Below-the-Fold Image Gallery** — Use the Grid layout with titles and captions enabled in a full-width section below the main product information. This works well for products that benefit from detailed visual documentation, such as handmade goods or technical products.

3. **Minimal Slider Gallery** — Use the Slider layout without any additional text elements for a clean, image-focused browsing experience. Apply subtle border-radius and box-shadow to the images for a modern card-like presentation.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/wc-gallery` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For a product image gallery use Woo Product Gallery; for the main product featured image with thumbnail strip use Woo Product Images; for non-WooCommerce image galleries use Gallery.

## Saving Your Work

After configuring the product gallery module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

!!! info "WooCommerce Required"
    This module requires the WooCommerce plugin to be installed and active. Products must have gallery images added through the WooCommerce product editor (Product Gallery section) for this module to display content.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Woo Product Gallery module does not appear on the front end, verify that:

    - WooCommerce is installed and activated
    - The module is placed on a product page template (not a regular page)
    - A valid, published product is assigned to the module
    - The product has gallery images uploaded in the Product Gallery section of the product editor

!!! warning "No Images Displaying"
    If the module renders but shows no images, check that:

    - The assigned product has images added to its **Product Gallery** (not just a featured image)
    - Gallery images are properly uploaded to the WordPress media library
    - Image files have not been deleted or moved from the server

!!! tip "Grid Pagination Not Appearing"
    Pagination controls only display when the Layout is set to Grid and the Show Pagination toggle is enabled. Additionally, pagination only renders when the number of gallery images exceeds what fits in the initial grid view.

## Related

- [Woo Product Images](woo-product-images.md) — Displays the main product featured image with thumbnail navigation
- [Gallery](gallery.md) — Non-WooCommerce image gallery module
- [Image](image.md) — Single image display module
- [Woo Product Description](woo-product-description.md) — Displays the product description text
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
