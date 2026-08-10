---
title: "Before After Image"
description: "Complete Divi 5 Before/After Image module reference — settings, design options, code examples, and troubleshooting for interactive image comparison sliders with horizontal and vertical orientation."
category: modules
tags: ["modules", "content-modules", "before-after", "image", "comparison", "slider", "interactive"]
related: ["image", "gallery", "slider"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/13714462"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Before After Image

The Before/After Image module creates an interactive image comparison slider that allows users to drag a handle to reveal the difference between two images, such as before-and-after transformations.

!!! abstract "Quick Reference"
    **What it does:** Renders two overlapping images with a draggable slider handle, allowing users to interactively compare "before" and "after" states.
    **When to use it:** Product transformations, design comparisons, photo editing showcases, renovation reveals
    **Key settings:** Before Image, After Image, Labels, Slider (orientation, handle color, position, arrows)
    **Block identifier:** `divi/before-after-image`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/13714462)

!!! tip "When to Use This Module"
    - Showcasing transformation results (beauty, fitness, home renovation, design work)
    - Comparing product versions, color options, or feature differences side by side
    - Demonstrating photo editing, retouching, or image processing results

!!! warning "When NOT to Use This Module"
    - For displaying a single image — use [Image](image.md)
    - For multiple images in a browsable format — use [Gallery](gallery.md)
    - For a content slideshow — use [Slider](slider.md)

## Overview

The Before/After Image module provides an interactive way to compare two images by overlaying them and allowing users to drag a divider handle across the image area. As the handle moves, it reveals more of one image and less of the other, creating an engaging comparison experience that is far more effective than placing two static images side by side.

The module requires two images: a "before" image and an "after" image. These should ideally be the same dimensions and show the same subject from the same angle, differing only in the aspect being compared (such as before and after a renovation, a color correction, or a design change). Customizable text labels can be placed on each side to identify which image is which.

The **Slider** settings in the Design tab provide detailed control over the comparison interaction. You can choose between horizontal (left-to-right) and vertical (top-to-bottom) slider orientation, customize the handle color and arrow appearance, and set the initial position of the handle. The handle position determines how much of each image is visible when the page first loads — setting it to 50% shows equal portions of both images, while a position closer to 0% or 100% reveals most of one image and invites the user to drag and discover the other.

The module also supports nested child elements through the Elements setting and integrates with the Loop Builder for dynamic content generation, making it possible to create automated comparison galleries from WordPress data.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13714462).

<!-- ![Before After Image module](../assets/screenshots/modules/before-after-image/element.png){ loading=lazy } -->
<!-- *The Before/After Image module showing a home renovation comparison with a horizontal slider at the 50% position.* -->

## Use Cases

1. **Home Renovation Portfolio** — Display before-and-after photos of completed renovation projects with labeled "Before" and "After" overlays, letting potential clients interactively explore the transformation quality of your work.
2. **Product Comparison** — Compare two versions of a product (standard vs. premium, old vs. new model) by showing them in the same framing, allowing customers to see the visual differences by sliding the handle.
3. **Photo Editing Showcase** — Demonstrate retouching, color grading, or restoration skills by letting users compare the original and edited versions of a photograph, providing a compelling portfolio piece for photographers and designers.

## How to Add the Before/After Image Module

1. Open the Visual Builder on the page where you want the comparison slider to appear.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Before After Image" in the module picker, then click to insert it.
4. Upload or select the "before" and "after" images in the Content tab.

For an animated walkthrough of adding and configuring this module, see the
[official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/13714462).

## Settings & Options

The Before/After Image module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the two comparison images, label text, nested elements, and the link and Loop Builder options.

| Setting | Type | Description |
|---------|------|-------------|
| Before Image | image upload | Select or upload the "before" image — the starting state shown on one side of the slider. |
| After Image | image upload | Select or upload the "after" image — the transformed state shown on the other side of the slider. |
| Before Label | text | Set the text label displayed on the "before" side of the comparison (e.g., "Before," "Original," "Standard"). |
| After Label | text | Set the text label displayed on the "after" side of the comparison (e.g., "After," "Edited," "Premium"). |
| Link | url | Optionally make the entire module clickable, directing users to a detail page or portfolio item. |
| Elements | nested modules | Insert nested child modules within the comparison container for additional content overlays. |
| Background | background controls | Set a background color, gradient, image, or video behind the module container. |
| Loop | toggle | Enable the Loop Builder to dynamically generate comparison instances from WordPress data. |
| Order | select | Set the flexbox order of the module relative to sibling elements in the same row. |
| Meta | admin label | Assign an admin label and control module visibility inside the Visual Builder. |
| Images |  | Choose the Before and After Images. <!-- AUTO-ADDED --> |
| Labels |  | Choose the text each label (before and after) displays. <!-- AUTO-ADDED --> |

<!-- ![Before After Image Content tab settings](../assets/screenshots/modules/before-after-image/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the comparison layout, slider handle appearance, label styling, and the module's visual container.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose how the module and any nested child elements are arranged: Block (stacked), Flex (flexible alignment, default), or Grid (CSS Grid layout). |
| Labels | composite styling | Style the before/after label text, including font styles, spacing, border, and background. Controls how the text labels appear on top of the comparison images. |
| Slider | composite styling | Configure the slider handle appearance: orientation (Horizontal or Vertical), handle color, initial handle position (percentage), and arrow color. |
| Layout - |  | Choose the Layout Style. It allows you to change how the child modules are being displayed.BlockFlex(default)Grid <!-- AUTO-ADDED --> |
| Block |  |  <!-- AUTO-ADDED --> |
| Flex |  | (default) <!-- AUTO-ADDED --> |
| Grid |  |  <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Before/After Image module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the spacing for the Before/After Image module. <!-- AUTO-ADDED --> |
| Border |  | Choose the border styles for the Before/After Image module. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Box Shadow styles for the Before/After Image module. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Before/After Image module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Before/After Image module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Before/After Image module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

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

<!-- ![Before After Image Design tab settings](../assets/screenshots/modules/before-after-image/settings-design.png){ loading=lazy } -->

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
| CSS- |  | Allows you to add custom CSS code to fine-tune your Before/After Image module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the visibility of the Before/After Image module for different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Before/After Image's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Before/After Image's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Before/After Image module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

<!-- ![Before After Image Advanced tab settings](../assets/screenshots/modules/before-after-image/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Style the comparison container */
.et_pb_before_after_image {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

/* Style the slider handle */
.et_pb_before_after_image .comparison-handle {
    width: 40px;
    height: 40px;
    background: #fff;
    border: 3px solid #2ea3f2;
    border-radius: 50%;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    cursor: ew-resize;
}

/* Style the divider line */
.et_pb_before_after_image .comparison-divider {
    width: 3px;
    background: #2ea3f2;
}

/* Style the labels */
.et_pb_before_after_image .before-label,
.et_pb_before_after_image .after-label {
    background: rgba(0, 0, 0, 0.6);
    color: #fff;
    padding: 6px 14px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Position labels in corners */
.et_pb_before_after_image .before-label {
    position: absolute;
    top: 15px;
    left: 15px;
}

.et_pb_before_after_image .after-label {
    position: absolute;
    top: 15px;
    right: 15px;
}

/* Change cursor for vertical slider */
.et_pb_before_after_image.vertical .comparison-handle {
    cursor: ns-resize;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_before_after_image .before-label,
    .et_pb_before_after_image .after-label {
        font-size: 11px;
        padding: 4px 10px;
    }
}
```

### PHP Hooks

```php
/* Filter the Before/After Image module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_before_after_image' !== $render_slug) {
        return $output;
    }
    // Modify $output as needed
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Renovation Portfolio Grid** — Place multiple Before/After Image modules in a 2-column row to create a portfolio section showcasing transformation projects. Use consistent image dimensions across all modules and add descriptive labels like "Day 1" and "Completed" for context.

2. **Full-Width Hero Comparison** — Place a single Before/After Image module in a full-width section as a hero element. Set the initial handle position to 30% to show mostly the "after" result, enticing users to drag and discover the "before" state.

3. **Vertical Comparison for Tall Content** — For images where the transformation is primarily top-to-bottom (such as web page redesigns or full-body transformations), use the Vertical slider orientation. This changes the drag direction and divider line to better suit vertically oriented comparison content.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/before-after-image` — *Needs Testing*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

!!! tip "Module Selection Guidance"
    For interactive image comparison use Before/After Image; for a single image display use Image; for a browsable image collection use Gallery; for a content slideshow use Slider.

## Saving Your Work

After configuring the before/after image module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Module Not Rendering"
    If the Before/After Image module does not appear on the front end, verify that:

    - The module is placed inside a valid section and row
    - Both a "before" and "after" image have been selected
    - Visibility settings are not hiding the module on the current device

!!! warning "Slider Handle Not Draggable"
    If the comparison images display but the handle cannot be dragged, check that:

    - JavaScript is not blocked or erroring on the page (check browser console)
    - No CSS `pointer-events: none` is applied to the module or its parent
    - The module is not inside an element with `overflow: hidden` that clips the handle

!!! tip "Images Not Aligning Properly"
    For the best comparison experience, both images should have identical dimensions and aspect ratios. If the images are different sizes, the comparison may look misaligned or one image may appear cropped. Resize both images to the same width and height before uploading.

## Related

- [Image](image.md) — Single image display module
- [Gallery](gallery.md) — Image gallery with grid and slider options
- [Slider](slider.md) — Content slideshow with custom slides
- [Blurb](blurb.md) — Image/icon with text module
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow in the Visual Builder
