---
title: "Icon"
description: "Complete Divi 5 Icon module reference — scalable vector icons from the Divi and Font Awesome libraries with color, size, and link controls."
category: modules
tags: ["modules", "icon", "graphics", "font-awesome", "visual-elements", "decorative"]
related: ["blurb", "image"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10315683-the-icon-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Icon

The Icon module displays a single scalable icon from the Divi icon library or Font Awesome icon set with full color, size, and link controls.

!!! abstract "Quick Reference"
    **What it does:** Places a single vector icon from the Divi or Font Awesome icon library with customizable color, size, alignment, and optional link.
    **When to use it:** Feature highlight grids, social media link bars, decorative section accents
    **Key settings:** Icon (icon picker), Icon Color, Icon Size, Module Alignment, Module Link URL
    **Block identifier:** `divi/icon`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10315683-the-icon-module-in-divi-5)

!!! tip "When to Use This Module"
    - You need a standalone decorative or functional icon without accompanying text
    - Building custom social media link bars with individually linked icons
    - Visual accents or divider elements between content sections

!!! warning "When NOT to Use This Module"
    - You need an icon paired with a heading and text → use [Blurb](blurb.md)
    - You need a list of items each with its own icon → use [Icon List](icon-list.md)
    - You need a raster image (photo/illustration) → use [Image](image.md)

## Overview

The Icon module provides a simple way to place individual icons anywhere in your Divi layout. Icons are vector-based, meaning they scale cleanly to any size without losing quality, making them suitable for everything from small inline accents to large decorative focal points. The module supports both the built-in Divi icon set and the extended Font Awesome icon library, giving you access to hundreds of icon options.

Each icon can be fully customized with color, size, alignment, and background settings. You can also link icons to any URL, page, or section, turning them into functional navigation elements or call-to-action triggers. The module's lightweight footprint makes it efficient to use multiple instances on a single page without impacting performance.

Icons work well as visual indicators that draw attention to specific content areas, represent features or services, or add decorative flair to headings and sections. They pair naturally with text, blurb, and button modules to build feature grids, service listings, and other structured content blocks.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10315683-the-icon-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/icon/)

![Icon module](../assets/screenshots/modules/icon/element.png){ loading=lazy }
*The Icon module displaying a customized icon with color and sizing applied.*

## Use Cases

1. **Feature Highlight Grid** — Place Icon modules in a multi-column row alongside text modules to create a feature grid. Each icon visually represents a different service or product benefit, making the section scannable and engaging.

2. **Social Media Links** — Use Icon modules with Font Awesome social media icons to build a custom social link bar. Link each icon to the corresponding social profile and style them with brand-appropriate colors.

3. **Section Divider Accent** — Position a large, lightly-colored icon between content sections as a decorative divider element. This adds visual rhythm to long-form pages without introducing heavy imagery.

## How to Add the Icon Module

1. **Insert the module.** Open the Visual Builder, click the gray plus icon inside any row, and search for "Icon" in the module picker. Click it to add it to your layout.

2. **Select your icon.** In the Content tab under Icon, click the icon picker to browse and select from the Divi icon library or Font Awesome icons. Use the search field to quickly find specific icons by name.

3. **Customize appearance.** Switch to the Design tab to set the icon color, size, and alignment. Optionally add a link in the Content tab and adjust spacing, borders, and effects in the Design tab. Save when finished.

## Settings & Options

### Content Tab

The Content tab controls which icon is displayed, its link destination, background styling, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| **Icon** | | |
| Icon | icon-picker | Opens the icon selection interface where you can browse or search the Divi icon library and Font Awesome icon set. Click any icon to apply it. |
| **Link** | | |
| Module Link URL | url | Sets a URL, page, or section that the icon links to when clicked. |
| Module Link Target | select | Controls whether the link opens in the same window or a new tab. |
| **Background** | | |
| Background Color | color | Applies a solid background color behind the icon. |
| Background Gradient | gradient | Applies a gradient background with configurable direction, stops, and colors. |
| Background Image | image | Sets a background image behind the icon. |
| Background Video | video | Embeds a background video behind the icon. |
| Background Pattern | pattern | Adds a repeating pattern overlay to the module background. |
| Background Mask | mask | Applies a decorative mask shape to the module background. |
| **Order** | | |
| Flexbox Order | number | Sets the display order of the module when its parent row uses Flexbox layout. |
| Grid Order | number | Sets the display order of the module when its parent row uses CSS Grid layout. |
| **Meta** | | |
| Admin Label | text | Custom label displayed in the Visual Builder layers panel to help identify the module. |
| Disable On | toggle | Forces the module to remain visible in the Visual Builder even when front-end visibility is restricted. |
| Link |  | Make the entire Icon module clickable, creating a seamless way to direct users to another page, section, or external site. <!-- AUTO-ADDED --> |
| Background |  | Choose the Icon module's background styles. <!-- AUTO-ADDED --> |
| Order |  | Choose the order in which the Icon module appears inside a Flexbox and Grid layout. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Icon Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab controls the icon's visual properties including color, size, alignment, and all decorative effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Icon Color | color | Sets the color of the icon. Supports solid colors and can be set independently for default and hover states. |
| Icon Size | range | Controls the display size of the icon in pixels, em, rem, or other CSS units. |
| Module Alignment | alignment | Sets the horizontal alignment of the icon within its column (left, center, right). |
| Icon |  | Choose the Icon module's color and size. <!-- AUTO-ADDED --> |
| Alignment |  | Choose the Icon module's alignement. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Icon module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Icon module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Icon module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Icon module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Icon module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Icon module's animation styles. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Spacing](../options-groups/spacing.md) | Margin and padding per side |
| [Border](../options-groups/border.md) | Width, color, style, border radius (set to 50% for circular) |
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
| [CSS](../options-groups/css.md) | Custom CSS per element target (main element, icon) |
| HTML | Semantic HTML tag for the module wrapper (div, article, section) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Icon module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Icon's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Icon's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Icon's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Icon module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Create a circular icon with background */
.et_pb_icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 80px;
    height: 80px;
    background-color: #2ea3f2;
    border-radius: 50%;
    color: #fff;
    font-size: 32px;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.et_pb_icon:hover {
    background-color: #1a8cd8;
    transform: scale(1.1);
}

/* Outlined icon style */
.outlined-icon .et_pb_icon {
    background-color: transparent;
    border: 2px solid #2ea3f2;
    color: #2ea3f2;
}

.outlined-icon .et_pb_icon:hover {
    background-color: #2ea3f2;
    color: #fff;
}

/* Responsive icon sizing */
@media (max-width: 980px) {
    .et_pb_icon {
        width: 64px;
        height: 64px;
        font-size: 26px;
    }
}

@media (max-width: 767px) {
    .et_pb_icon {
        width: 48px;
        height: 48px;
        font-size: 20px;
    }
}
```

### PHP Hooks

```php
/* Modify the Icon module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_icon' !== $render_slug) {
        return $output;
    }

    // Example: Wrap the icon in an accessible span with aria-label
    $output = str_replace(
        'class="et_pb_icon',
        'role="img" aria-label="decorative icon" class="et_pb_icon',
        $output
    );

    return $output;
}, 10, 2);
```

```php
/* Add custom icon fonts alongside Divi's built-in set */
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'custom-icon-font',
        get_stylesheet_directory_uri() . '/fonts/custom-icons.css',
        array(),
        '1.0'
    );
});
```

## Common Patterns

1. **Circular Icon Badges** — Add padding and a background color to the Icon module, then set the border radius to 50% in the Design tab to create a circular badge. Use a contrasting icon color for visibility. This pattern works well for feature grids and service listings where each column has an icon, heading, and description.

2. **Animated Hover Icons** — Set different icon colors for default and hover states, and configure a smooth transition duration (300-400ms) in the Advanced tab. Add a subtle scale transform on hover for an interactive feel. This is effective for navigation elements, social links, and call-to-action icons.

3. **Linked Icon Navigation** — Use multiple Icon modules in a single row to create an icon-based navigation bar. Link each icon to a different page or section and set consistent sizing and spacing across all instances. Apply the same color scheme and hover effects for a cohesive look.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/icon` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Icon | `attrs.font_icon` | Icon character or identifier from icon library |
| Icon Color | `attrs.icon_color` | CSS color value for the icon |

!!! tip "Module Selection Guidance"
    For decorative standalone icons use Icon; for icons with text use Blurb; for icon lists use Icon List.

## Saving Your Work

After configuring the Icon module, save your layout by clicking the green **Save** button at the bottom of the Visual Builder panel, or use the keyboard shortcut **Ctrl+S** (Windows) / **Cmd+S** (Mac). To reuse this configured icon on other pages, right-click the module in the Visual Builder and select **Save to Library**. You can also copy and paste modules between pages using **Ctrl+C** / **Ctrl+V**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Icon module in Divi 5 uses the updated Visual Builder interface with accordion-style settings panels. Settings organization and available icon libraries may differ from Divi 4.

## Troubleshooting

!!! warning "Icon Not Displaying"
    If the Icon module appears as an empty box or shows a broken character, verify that an icon has been selected in the Content tab. If you selected a Font Awesome icon, ensure the Font Awesome library is loading correctly by checking for CSS conflicts in the browser developer tools. Clear any site caching plugins after making changes.

!!! warning "Icon Color Not Changing"
    If the icon color does not respond to the Design tab color setting, check for custom CSS overrides that may be applying a more specific color rule. Inspect the icon element in the browser developer tools to identify conflicting styles. Also verify that you are not accidentally setting the hover-state color instead of the default color.

!!! tip "Accessibility Considerations"
    Icons that convey meaning (such as navigation or action indicators) should include accessible text for screen readers. Use the CSS ID or Class field to target the icon with custom CSS that adds an `aria-label` attribute, or pair the Icon module with a visually hidden text element. Purely decorative icons should be marked with `aria-hidden="true"` to prevent confusion for assistive technology users.

## Related

- [Blurb](blurb.md)
- [Image](image.md)
