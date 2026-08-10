---
title: "Tabs"
description: "Complete Divi 5 Tabs module reference — tabbed content panels, header styling, rich text bodies, responsive stacking, and code examples."
category: modules
tags: ["modules", "tabs", "tabbed-content", "content-organizer", "navigation", "panels"]
related: ["accordion", "toggle"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10365057-the-tabs-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Tabs

The Tabs module organizes content into switchable panels controlled by clickable tab headers.

!!! abstract "Quick Reference"
    **What it does:** Groups content into tabbed panels that visitors switch between by clicking horizontal tab headers.
    **When to use it:** Product specifications, service tier comparisons, categorized content sections
    **Key settings:** Tabs (repeater), Tab Title, Tab Content (rich text), Tab Text styling
    **Block identifier:** `divi/tabs`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10365057-the-tabs-module-in-divi-5)

!!! tip "When to Use This Module"
    - Organizing related content into switchable panels for quick comparison
    - Displaying product details across categories (specs, reviews, shipping)
    - Presenting location or branch information in a compact tabbed layout

!!! warning "When NOT to Use This Module"
    - Displaying FAQ-style content with vertical expand/collapse → use [Accordion](accordion.md)
    - Creating independently collapsible items that can all be open at once → use [Toggle](toggle.md)

## Overview

The Tabs module provides a tabbed interface for grouping related content into distinct panels that visitors switch between by clicking tab headers. Only one panel is visible at a time, which keeps the layout compact and allows you to present a significant amount of information without requiring visitors to scroll through long pages.

Each tab functions as an independent content block with its own title and rich text body. The body supports full HTML formatting, so you can include images, lists, embedded media, and styled text within any tab. At wider column widths, tab headers display in a horizontal row across the top. In narrow columns (quarter-width and below), the headers automatically stack vertically to remain accessible on constrained layouts.

The Tabs module differs from the [Accordion](accordion.md) module in its navigation pattern. While both organize content into collapsible sections, tabs present all headers simultaneously in a row, allowing instant access to any panel. The accordion stacks headers vertically with expand/collapse behavior. Choose tabs when visitors need to compare or switch between sections frequently, and accordions when content is sequential or FAQ-style.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10365057-the-tabs-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/tabs/)

![Tabs module](../assets/screenshots/modules/tabs/element.png){ loading=lazy }
*The Tabs module as it appears on the live demo.*

## Use Cases

1. **Product Specifications** — Present different categories of product information (description, specifications, reviews, shipping) in separate tabs so shoppers can quickly find the details they care about.
2. **Service Tiers or Pricing Plans** — Display different pricing plans or service levels in their own tabs, letting visitors compare options by switching between panels without scrolling.
3. **Categorized Content Blocks** — Organize a resource section where each tab contains a different content category such as tutorials, documentation, and FAQs, keeping everything accessible from a single location on the page.

## How to Add the Tabs Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Tabs" in the module picker or find it in the Content Elements category, then click to insert it.

## Settings & Options

The Tabs module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab manages the individual tab items and module-level configuration for links, backgrounds, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Tabs (Repeater) | item list | Manage individual tab items. Click **+** to add a new tab, the pencil icon to edit, the trash icon to delete, and drag to reorder. Each tab item has its own settings detailed below. |
| Link | url | Optionally link the entire tabs module to a specified URL. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire tabs module container. |
| Loop | toggle | Control repeating behavior for the tab items within the module. |
| Order | select | Control the display order of tab items within the module. |
| Meta | admin label | Set an internal label for the module visible only in the Visual Builder's layer panel, helpful for identifying the module when a page contains multiple tab instances. |

#### Individual Tab Item Settings

Each tab within the module has its own configuration panel:

| Setting | Type | Description |
|---------|------|-------------|
| Title | text | The label displayed in the clickable tab header. Keep titles short and descriptive for best usability. |
| Content | rich text editor | The body content displayed in the panel when the tab is active. Supports text formatting, images, lists, embedded media, and HTML. |

### Design Tab

The Design tab controls the visual styling of the tab headers, body content, and overall module layout.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Tab Text | text styling | Style the tab header labels with independent font family, size, weight, style, color, alignment, letter spacing, and line height settings. Separate styling can be configured for active and inactive tab states. |
| Body Text |  | Choose the module's body text styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Tabs module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Tabs module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Tabs module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Tabs module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Tabs module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Tabs module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Tabs module's animation styles. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Body Text](../options-groups/body-text.md) | Font, size, color, spacing for tab panel content |
| [Sizing](../options-groups/sizing.md) | Width, max-width, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level controls for custom attributes, CSS targeting, conditional display logic, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (tab headers, active tab header, tab content area, individual tab panels) |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Tabs module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Tabs module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Tabs's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Tabs' module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Tabs module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Open the Tab Module |  | Click on the Tab module on your page or click the Gear icon to open its settings. <!-- AUTO-ADDED --> |
| Edit an Item |  | Click thePencil iconnext to the Tab item you want to update(1). Modify the title, body content, or design settings as needed. <!-- AUTO-ADDED --> |
| Add a New Item |  | In theContenttab, clickAdd New Tab Item (2). Enter the title and body content, then customize design options like background color or text style. Click the arrow icon at the top left to return to the main module settings. <!-- AUTO-ADDED --> |
| Duplicate |  | Click on theDuplicateiconto duplicate the selected Tab item. <!-- AUTO-ADDED --> |
| Delete Item |  | Click theTrash icon (3)next to the Tab item to delete it. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS: Styled Tab Headers

```css
/* Custom tab header styling with bottom border indicator */
.et_pb_tabs .et_pb_tab_common a {
    background: transparent;
    color: #666666;
    font-weight: 600;
    padding: 12px 24px;
    border-bottom: 3px solid transparent;
    transition: all 0.3s ease;
}

.et_pb_tabs .et_pb_tab_common a:hover {
    color: #333333;
    border-bottom-color: #cccccc;
}

.et_pb_tabs .et_pb_tab_active a {
    color: #0073aa;
    border-bottom-color: #0073aa;
    background: transparent;
}
```

### Custom CSS: Full-Width Equal Tab Headers

```css
/* Make tab headers stretch to fill the full module width equally */
.et_pb_tabs .et_pb_tabs_controls {
    display: flex;
}

.et_pb_tabs .et_pb_tabs_controls li {
    flex: 1;
    text-align: center;
}

.et_pb_tabs .et_pb_tabs_controls li a {
    display: block;
    width: 100%;
}
```

### Custom CSS: Stacked Tabs on Mobile

```css
/* Vertical tab layout on smaller screens */
@media (max-width: 767px) {
    .et_pb_tabs .et_pb_tabs_controls {
        flex-direction: column;
    }

    .et_pb_tabs .et_pb_tabs_controls li {
        width: 100%;
        border-bottom: 1px solid #e0e0e0;
    }

    .et_pb_tabs .et_pb_tabs_controls li a {
        padding: 14px 16px;
    }
}
```

### PHP: Filter Tabs Module Output

```php
/* Add ARIA attributes to the tabs module for improved accessibility */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_tabs' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_tabs_controls"',
        'class="et_pb_tabs_controls" role="tablist"',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

### 1. Product Information Tabs

Create three to four tabs labeled "Overview," "Specifications," "Reviews," and "Shipping." Place detailed content in each panel so visitors can quickly locate the information they need. Style the active tab header with a distinct color that matches your brand, and keep the inactive headers in a neutral tone.

### 2. Location or Branch Selector

Use tabs to display information about different office locations, store branches, or regional services. Each tab header carries the location name, and the panel contains the address, hours, contact details, and an embedded map. This keeps all location data in one compact section.

### 3. Before/After or Comparison View

Create two tabs labeled "Before" and "After" or "Plan A" and "Plan B" to let visitors toggle between two states or options. This works well for case studies, renovation portfolios, or plan comparisons where seeing one view at a time is clearer than a side-by-side layout.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/tabs` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child tab items | Nested blocks | Each tab has title and content attributes |

!!! tip "Module Selection Guidance"
    For horizontal tabbed content use Tabs; for vertical collapsible content use Accordion; for independent collapsible items use Toggle.

## Saving Your Work

After configuring your tabs, save your changes by clicking the **Save** button (checkmark icon) in the Visual Builder's bottom toolbar. For reusable tab configurations, right-click the module and select **Save to Library** to store it as a preset that can be inserted on other pages.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Tabs settings and class names may differ from Divi 4.

## Troubleshooting

!!! warning "Tab Content Not Displaying"
    If clicking a tab header does not reveal the panel content:

    - Ensure the tab item has content entered in its **Content** field. Empty tabs will render a blank panel.
    - JavaScript errors from other plugins or custom scripts can break the tab switching behavior. Open the browser console (F12) and look for errors.
    - If the module was recently duplicated or imported from the library, re-save the page to ensure all tab data is properly stored.

!!! warning "Tab Headers Overlapping or Wrapping Unexpectedly"
    If tab labels are crowding together or breaking to a new line:

    - Shorten the tab titles. Long titles consume more horizontal space and can overflow, especially with many tabs.
    - Reduce the tab header font size in the Design tab's **Tab Text** settings.
    - If you have more than four or five tabs, consider using the Accordion module instead, which handles many items more gracefully in a vertical layout.
    - On smaller screens, the module automatically stacks tab headers. Use the responsive controls to adjust font size and padding for tablet and phone breakpoints.

!!! warning "Styling Not Applying to Active Tab"
    If custom CSS or Design tab styles are not affecting the currently active tab:

    - The active tab uses a distinct CSS class (`.et_pb_tab_active`). Ensure your selectors target this class specifically rather than the general tab class.
    - Inline styles from the Visual Builder may override your custom CSS. Use more specific selectors or add `!important` as a last resort.
    - Clear your browser cache and any site-level caching plugins to ensure you are seeing the latest styles.

## Related

- [Accordion](accordion.md) — Collapsible content panels where one item is open at a time
- [Toggle](toggle.md) — Individual collapsible content blocks that can be open simultaneously
- [Pricing Table](pricing-table.md) — Use tabs to switch between pricing tiers or billing periods
- [Text Options](../options-groups/text.md) — Shared typography settings for tab labels and content
- [Playbook: Build a Page](../playbooks/build-a-page.md) — Step-by-step page building workflow
