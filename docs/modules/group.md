---
title: "Group"
description: "Complete Divi 5 Group module reference — nestable container for wrapping child modules with Flex, Grid, and Block layout modes."
category: modules
tags: ["modules", "group", "container", "layout", "flexbox", "grid", "wrapper"]
related: ["group-carousel", "tabs"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/11170855"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Group

The Group module is a lightweight container that wraps child modules within a column and lets you style, move, or save them as a single unit.

!!! abstract "Quick Reference"
    **What it does:** Wraps multiple child modules in a nestable container with shared styling and Block, Flex, or Grid layout modes.
    **When to use it:** Reusable component blocks, inline button rows, card layouts, dynamic loop templates
    **Key settings:** Layout (Block/Flex/Grid), Background, Link, Loop toggle
    **Block identifier:** `divi/group`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/11170855)

!!! tip "When to Use This Module"
    - You need to treat multiple modules as a single styled unit with shared background and borders
    - Building reusable card layouts or CTA blocks that can be saved as global presets
    - Arranging child modules side by side using Flex or in structured grids using CSS Grid

!!! warning "When NOT to Use This Module"
    - You need a horizontal scrollable carousel of grouped content → use [Group Carousel](group-carousel.md)
    - You need tab-based content organization → use [Tabs](tabs.md)
    - You only need a single module with no grouping requirement → place the module directly in the column

## Overview

The Group module acts as a nestable wrapper inside columns. It can hold any number of child modules and nested rows, giving you the ability to treat a collection of elements as one block. You can apply shared styling such as backgrounds, borders, and spacing to the entire group rather than styling each child individually. It also lets you drag, duplicate, or convert the group into a global preset without affecting the content inside.

Three layout modes are available: Block, Flex (the default), and Grid. Flex layout distributes child modules in a row-based flow with wrapping and alignment controls, while Grid mode enables CSS Grid placement for more structured arrangements. Block mode stacks children vertically in standard document flow.

Because the Group module sits at the column level within the Divi hierarchy (Section > Row > Column > Group > Modules), it fills a role that previously required extra rows or columns. It is especially useful for building reusable component blocks like card layouts, inline button groups, or call-to-action clusters that need to move together.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/11170855).

![Group module](../assets/screenshots/modules/group/element.png){ loading=lazy }
*The Group module wrapping child elements in the Visual Builder.*

## Use Cases

1. **Reusable Call-to-Action Block** — Combine a heading, body text, and button inside a Group, apply shared background styling, and save the Group as a global preset to reuse across the site without configuring each child individually.
2. **Inline Button Row** — Place multiple Button modules inside a Group set to Flex layout to arrange them side by side with consistent gap spacing, wrapping automatically on smaller screens.
3. **Dynamic Card Template** — Build a card structure with an image, title, excerpt, and price inside a Group, then use the loop builder to repeat the card for posts, products, or custom query results.

## How to Add the Group Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Group" in the module picker or locate it in the Layout Elements category, then click to insert it.


## Settings & Options

The Group module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the Group's link behavior, background, loop settings, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Link | url/link settings | Makes the entire Group clickable, directing users to an internal page or external URL. Includes target window and link relationship options. |
| Background | background controls | Apply a background color, gradient, image, or video behind the Group container. Multiple layers can be combined. |
| Loop | toggle | Enables the loop builder so the Group repeats dynamically based on a query data source such as posts or custom post types. |
| Order | number | Sets the CSS order value when the Group's parent uses Flexbox or Grid layout, controlling where the Group appears in the visual sequence. |
| Meta | admin label | Assign an admin label to identify the Group in the Visual Builder layer panel. Also controls whether the module is always visible in the builder. |

<!-- ![Group Content tab settings](../assets/screenshots/modules/group/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the Group's layout mode, dimensions, spacing, and visual effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | dropdown | Choose between Block, Flex, or Grid layout modes for arranging child modules within the Group. Flex is the default and supports horizontal alignment, wrapping, and gap controls. Grid enables CSS Grid placement. |
| Block |  |  <!-- AUTO-ADDED --> |
| Flex |  | (default) <!-- AUTO-ADDED --> |
| Grid |  |  <!-- AUTO-ADDED --> |
| Sizing |  | Choose the desired sizing for the Group module. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the spacing for the Group module. <!-- AUTO-ADDED --> |
| Border |  | Choose the border styles for the Group module. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Group module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Group module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Group module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Group module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (hue, saturation, brightness, blend mode) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Group Design tab settings](../assets/screenshots/modules/group/settings-design.png){ loading=lazy } -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display, interactions, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Group module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Group's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Group's module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Group's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Group module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

<!-- ![Group Advanced tab settings](../assets/screenshots/modules/group/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

```css
/* Card-style Group with shadow and rounded corners */
.et_pb_module_group.card-group {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    padding: 30px;
}

/* Flex Group with even spacing between children */
.et_pb_module_group.spaced-group {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    align-items: center;
}

/* Full-width Group with constrained inner content */
.et_pb_module_group.contained-group {
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
    padding: 40px 20px;
}

/* Stack children vertically on mobile */
@media (max-width: 767px) {
    .et_pb_module_group.spaced-group {
        flex-direction: column;
        align-items: stretch;
    }
}
```

### PHP Hooks

```php
/* Add a custom wrapper class to all Group modules */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_group' !== $render_slug) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_module_group',
        'class="et_pb_module_group custom-group-wrapper',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Feature Card Grid** — Place multiple Group modules inside a row using Grid layout on the row. Each Group contains an icon, heading, and text module styled as a card with background, padding, and border radius. This creates a uniform card grid without needing separate rows for each card.

2. **Sticky CTA Bar** — Set the Group's position to sticky in the Advanced tab and place it near the top of a section. Fill it with a text module and button arranged via Flex layout. The bar sticks to the viewport as the user scrolls, keeping the call to action visible.

3. **Tabbed Content Container** — Nest Groups inside a Tabs module to organize complex content blocks. Each tab panel's Group can contain its own layout of mixed modules, giving you full design control within each tab.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/group` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Child modules | Nested blocks | Group contains child modules as nested block elements |

!!! tip "Module Selection Guidance"
    For grouping multiple modules as a single styled unit use Group; for rotating grouped content use Group Carousel; for tab-based organization use Tabs.

## Saving Your Work

After configuring the Group module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Child Modules Not Aligning Properly"
    If child modules inside the Group are stacking when you expect them side by side:

    - Verify the Group's Layout is set to **Flex** in the Design tab. Block layout stacks children vertically by default.
    - Check whether child modules have explicit width values that exceed the Group's available space, forcing wrapping.
    - Inspect whether the parent column has a narrow width that constrains the Group's flex container.

!!! warning "Group Background Not Visible"
    If the background color or image does not appear:

    - Confirm that a background is applied in the Group's Content tab, not just the parent row or section.
    - If using a background image, ensure the Group has enough height (via content or min-height) for the image to render visibly.
    - Check whether child modules have their own opaque backgrounds that cover the Group's background.

!!! tip "Saving a Group as a Global Preset"
    Right-click the Group module in the Visual Builder and select "Save as Global." Changes to the global Group will propagate everywhere it is used. To make a local copy that does not sync, right-click and choose "Unlink from Global."

## Related

- [Group Carousel](group-carousel.md) — Arranges grouped modules in a horizontal scrollable carousel
- [Tabs](tabs.md) — Organizes content into switchable tabbed panels
