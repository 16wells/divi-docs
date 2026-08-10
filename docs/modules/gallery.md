---
title: "Gallery"
description: "Complete Divi 5 Gallery module reference — image grid and slider layouts with titles, captions, pagination, and overlay effects."
category: modules
tags: ["modules", "media", "images", "gallery", "grid", "slider", "lightbox", "photos"]
related: ["image", "filterable-portfolio", "slider"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10315545-the-gallery-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Gallery

The Gallery module displays a collection of images in a configurable grid or slider layout with optional titles, captions, and pagination.

!!! abstract "Quick Reference"
    **What it does:** Arranges multiple images from the Media Library into a grid or horizontal slider with titles, captions, and pagination.
    **When to use it:** Product photo galleries, event photography, real estate listings, portfolio image showcases
    **Key settings:** Gallery Images, Images Per Page, Layout (Grid/Slider), Columns, Show Title, Show Caption, Show Pagination
    **Block identifier:** `divi/gallery`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10315545-the-gallery-module-in-divi-5)

!!! tip "When to Use This Module"
    - You need to display a curated set of images in a grid or slider format
    - Product photos, event galleries, or real estate listing images
    - You want built-in pagination for large image collections

!!! warning "When NOT to Use This Module"
    - You need to display project posts with category filtering → use [Filterable Portfolio](filterable-portfolio.md)
    - You need a single featured image → use [Image](image.md)
    - You need a full-screen content slider with text overlays → use [Slider](slider.md)

## Overview

The Gallery module lets you assemble and present multiple images as a unified visual collection anywhere on your page. Rather than placing individual image modules one by one, the Gallery module accepts a batch of images from your WordPress Media Library and arranges them automatically into either a multi-column grid or a horizontal slider. Each image can include a title and caption pulled from the media file's metadata.

The grid layout supports flexible column counts and spacing, making it adaptable to different content widths and design requirements. The slider layout presents images in a horizontal carousel that visitors can navigate through. Both layouts support overlay effects on hover and can be configured to link images to custom URLs, lightboxes, or other pages.

This module is particularly useful for showcasing product photos, real estate listings, event galleries, team headshots, or any situation where you need to display a curated set of images in an organized format. It works well alongside other media modules and can be combined with text and heading modules to build complete gallery sections.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10315545-the-gallery-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/gallery/)

![Gallery module](../assets/screenshots/modules/gallery/element.png){ loading=lazy }
*The Gallery module displaying images in a grid layout with hover overlay.*

## Use Cases

1. **Product Photo Gallery** — Display product images organized in a grid layout on an e-commerce or service page. Visitors can browse all product angles and variations in one place, with optional captions describing each image.

2. **Event or Portfolio Showcase** — Present event photography or creative work in a slider layout that visitors can browse through sequentially. Use titles and captions to provide context for each image.

3. **Real Estate or Property Listing** — Show property photos in a paginated grid, allowing potential buyers to browse through a large set of images without overwhelming page load. Link each image to a lightbox for full-size viewing.

## How to Add the Gallery Module

1. **Insert the module.** Open the Visual Builder, click the gray plus icon in any row, and search for "Gallery" in the module picker. Click it to add it to your layout.

2. **Add your images.** In the Content tab under Images, click the upload area to select images from your Media Library or upload new ones. Set the image order and the number of images displayed per page.

3. **Choose layout and style.** Switch to the Design tab to select grid or slider layout, configure column count and spacing, and customize overlay effects, typography, and other visual properties. Save when finished.

## Settings & Options

### Content Tab

The Content tab controls which images are displayed, their order, element visibility, linking behavior, and background styling.

| Setting | Type | Description |
|---------|------|-------------|
| **Images** | | |
| Gallery Images | media-library | Opens the WordPress Media Library to select and arrange the images included in the gallery. |
| Image Order | select | Sets whether images display in the order they were arranged (Default) or in a randomized sequence (Random). |
| Images Per Page | number | Controls how many images appear on each page of the gallery before pagination activates. |
| **Elements** | | |
| Show Title | toggle | Displays or hides the title text below each gallery image. Titles are pulled from the image's media library metadata. |
| Show Caption | toggle | Displays or hides the caption text below each gallery image. Captions are pulled from the image's media library metadata. |
| Show Pagination | toggle | Enables or disables numbered pagination below the gallery when the total image count exceeds the per-page limit. |
| **Link** | | |
| Module Link URL | url | Wraps the entire gallery module in a link to a specified URL, page, or section. |
| Module Link Target | select | Sets whether the module link opens in the same window or a new tab. |
| **Background** | | |
| Background Color | color | Applies a solid background color to the module container. |
| Background Gradient | gradient | Applies a gradient background with configurable direction, stops, and colors. |
| Background Image | image | Sets a background image behind the gallery module. |
| Background Video | video | Embeds a background video behind the gallery module. |
| Background Pattern | pattern | Adds a repeating pattern overlay to the module background. |
| Background Mask | mask | Applies a decorative mask shape to the module background. |
| **Meta** | | |
| Admin Label | text | Custom label displayed in the Visual Builder layers panel to help identify the module. |
| Disable On | toggle | Forces the module to remain visible in the Visual Builder even when front-end visibility is restricted. |
| **Order** | | |
| Flexbox Order | number | Sets the display order of the module when its parent row uses Flexbox layout. |
| Grid Order | number | Sets the display order of the module when its parent row uses CSS Grid layout. |
| Images |  | Choose the images to be displayed, their order, and the number of images per page. <!-- AUTO-ADDED --> |
| Elements |  | Choose to display or remove the Image's title, caption, and pagination text. <!-- AUTO-ADDED --> |
| Link |  | Make the entire Gallery module clickable, creating a seamless way to direct users to another page, section, or external site. <!-- AUTO-ADDED --> |
| Background |  | Choose the Gallery module's background styles. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Gallery Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |
| Order |  | Choose the order in which the Gallery module appears inside a Flexbox and Grid layout. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab controls the visual layout, image styling, typography for titles and captions, and all visual effects applied to the gallery.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Switches between Grid (multi-column thumbnails) and Slider (horizontal carousel) display modes. |
| Layout Style | select | When Grid is selected, chooses between Flexbox and Grid CSS layout methods for the thumbnail arrangement. |
| Columns | number | Sets the number of columns in the grid layout. Available values typically range from 1 to 6. |
| Column Spacing | range | Controls the gap between columns and rows in the grid layout. |
| Caption Text | text styling | Font, weight, style, color, size, letter spacing, line height, and text shadow for image captions. |
| Grid |  | Allows you to choose the Layout Style (Flexbox or Grid), choose the number of columns, the space in between columns, and more. <!-- AUTO-ADDED --> |
| Slider |  | Display all images in a slider layout. <!-- AUTO-ADDED --> |
| Overlay |  | Choose the Gallery module's Post Image overlay styles. <!-- AUTO-ADDED --> |
| Image |  | Choose the style for the Project's Featured Images. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall Gallery module's text styles for this module. <!-- AUTO-ADDED --> |
| Title Text |  | Choose the Gallery module's title styles. <!-- AUTO-ADDED --> |
| Pagination Text |  | Choose the Pagination text's styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Gallery module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Gallery module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Gallery module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Gallery module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Gallery module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Gallery module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Gallery module's animation styles, adding personality and interactivity while keeping a polished, professional feel. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Overlay](../options-groups/overlay.md) | Hover overlay icon, icon color, overlay background color |
| [Image](../options-groups/image.md) | Rounded corners, border, box shadow, CSS filters for gallery images |
| [Text](../options-groups/text.md) | Text alignment, color scheme |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, line height, text shadow for image titles |
| [Pagination Text](../options-groups/pagination-text.md) | Font, size, color for pagination links |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (main element, gallery item, image, title, caption, pagination) |
| HTML | Semantic HTML tag for the module wrapper (div, article, section) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Gallery module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Gallery's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Gallery's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Gallery's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Gallery module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Create a masonry-style gap between gallery items */
.et_pb_gallery .et_pb_gallery_items {
    gap: 16px;
}

/* Style individual gallery items with rounded corners and shadow */
.et_pb_gallery .et_pb_gallery_item {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.et_pb_gallery .et_pb_gallery_item:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

/* Customize the overlay appearance */
.et_pb_gallery .et_pb_gallery_item .et_overlay {
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 8px;
}

/* Responsive: 2 columns on tablet, 1 on mobile */
@media (max-width: 980px) {
    .et_pb_gallery .et_pb_gallery_item {
        width: 48% !important;
    }
}

@media (max-width: 767px) {
    .et_pb_gallery .et_pb_gallery_item {
        width: 100% !important;
    }
}
```

### PHP Hooks

```php
/* Modify the Gallery module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_gallery' !== $render_slug) {
        return $output;
    }

    // Example: Add a custom data attribute to the gallery wrapper
    $output = str_replace(
        'class="et_pb_gallery',
        'data-gallery="true" class="et_pb_gallery',
        $output
    );

    return $output;
}, 10, 2);
```

```php
/* Add a lightbox script for gallery images */
add_action('wp_enqueue_scripts', function() {
    if (is_singular()) {
        wp_enqueue_style('custom-gallery-lightbox', get_stylesheet_directory_uri() . '/css/gallery-lightbox.css');
        wp_enqueue_script('custom-gallery-lightbox', get_stylesheet_directory_uri() . '/js/gallery-lightbox.js', array('jquery'), '1.0', true);
    }
});
```

## Common Patterns

1. **Product Image Grid** — Set the layout to Grid with 3 or 4 columns and tight column spacing. Upload product photos with descriptive titles in the Media Library so they appear as labels beneath each thumbnail. Enable pagination if you have more than 12 images to keep the page lightweight.

2. **Fullwidth Slider Showcase** — Place the Gallery in a fullwidth row and select the Slider layout. This creates a prominent image carousel suitable for hero sections or featured work. Adjust the overlay color to match your branding and add entrance animations for visual impact on scroll.

3. **Captioned Photo Gallery** — Enable both titles and captions to create an informative gallery suitable for event documentation or educational content. Style the caption text with a smaller font size and lighter color to create visual hierarchy between the title and description. Use two columns for a magazine-style layout.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/gallery` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Gallery IDs | `attrs.gallery_ids` | Comma-separated media attachment IDs |
| Gallery Orderby | `attrs.gallery_orderby` | Image display order |
| Fullwidth | `attrs.fullwidth` | Toggle fullwidth display mode |

!!! tip "Module Selection Guidance"
    For image galleries use Gallery; for project portfolios use Portfolio; for single featured images use Image.

## Saving Your Work

After configuring the Gallery module, save your layout by clicking the green **Save** button at the bottom of the Visual Builder panel, or use the keyboard shortcut **Ctrl+S** (Windows) / **Cmd+S** (Mac). To reuse this configured gallery on other pages, right-click the module in the Visual Builder and select **Save to Library**. You can also copy and paste modules between pages using **Ctrl+C** / **Ctrl+V**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Gallery module in Divi 5 uses the updated Visual Builder interface with accordion-style settings panels. Settings organization, layout options, and naming may differ from Divi 4.

## Troubleshooting

!!! warning "Images Not Displaying"
    If the gallery appears empty or images fail to load, verify that images have been selected in the Content tab under Images. Check that the image files still exist in the WordPress Media Library and have not been deleted or moved. Also confirm that the **Images Per Page** value is greater than zero.

!!! warning "Slider Layout Not Advancing"
    If the slider layout displays only the first image and navigation arrows are unresponsive, check for JavaScript conflicts with other plugins or custom scripts. Open the browser console (F12) to look for errors. Ensure your Divi theme files are up to date, as older versions may have slider rendering issues.

!!! tip "Optimizing Gallery Performance"
    Large galleries with high-resolution images can significantly slow page load times. Before uploading, resize images to a maximum of 1200px on the longest side and compress them using a tool like TinyPNG or ShortPixel. Use the **Images Per Page** setting to paginate large collections rather than loading all images at once.

## Related

- [Image](image.md) — Display a single image with optional lightbox, link, and styling
- [Filterable Portfolio](filterable-portfolio.md) — Grid display with client-side category filtering for project posts
- [Slider](slider.md) — Sliding content panels with text overlays and navigation controls
- [Image Options](../options-groups/image.md) — Shared image styling options available across visual modules
- [CSS Grid](../builder/css-grid.md) — Advanced grid layouts for precise gallery-style arrangements
- [Overlay Options](../options-groups/overlay.md) — Configure hover overlay effects on gallery images
