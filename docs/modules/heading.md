---
title: "Heading"
description: "Complete Divi 5 Heading module reference — H1-H6 heading text with full typography control, dynamic content, and semantic markup."
category: modules
tags: ["modules", "heading", "title", "typography", "text", "h1", "h2", "h3", "seo"]
related: ["text", "post-title"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10315593-the-heading-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Heading

The Heading module displays customizable heading text that works across headers, footers, templates, posts, and pages.

!!! abstract "Quick Reference"
    **What it does:** Displays a single heading element (H1-H6, p, or span) with independent typography controls and dynamic content support.
    **When to use it:** Section headers, dynamic post titles in templates, linked navigation labels
    **Key settings:** Text (heading content), Heading Text typography, HTML tag level (H1-H6), Link
    **Block identifier:** `divi/heading`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10315593-the-heading-module-in-divi-5)

!!! tip "When to Use This Module"
    - You need a standalone heading with precise typographic control and semantic HTML tag selection
    - Dynamic post titles in Theme Builder templates
    - Section headers that need consistent styling independent of body text settings

!!! warning "When NOT to Use This Module"
    - You need a heading combined with body text → use [Text](text.md)
    - You need a heading with a description and button → use [Call to Action](call-to-action.md)
    - You need the post title to render automatically in a template → use [Post Title](post-title.md)

## Overview

The Heading module provides a dedicated element for displaying title-level text with full typographic control. It is designed to serve as a section header, page title, or any prominent text label that needs to stand apart from body content. The module supports all standard HTML heading levels (H1 through H6) as well as paragraph and span tags, giving you control over both visual presentation and semantic markup.

Unlike the Text module, which is built for longer-form rich content, the Heading module is focused on single-line or short-phrase titles. It ships with its own typography controls that are independent of body text settings, making it straightforward to maintain consistent heading styles across a site. [Dynamic content](../builder/dynamic-content.md) is supported, so the heading text can pull from post titles, custom fields, or other data sources in template contexts.

The module integrates with the [Loop Builder](../builder/loop-builder.md) and supports [Flexbox](../builder/flexbox.md) ordering, making it useful in dynamic layouts where headings need to accompany repeated content blocks. It can also be linked to make the entire heading clickable, which is helpful for navigation elements and linked section titles.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10315593-the-heading-module-in-divi-5).

![Heading module](../assets/screenshots/modules/heading/element.png){ loading=lazy }
*The Heading module displaying styled title text.*

## Use Cases

1. **Section Headers** — Place a Heading module at the top of each content section to clearly label and visually separate different areas of a page, improving both readability and accessibility.
2. **Dynamic Post Titles** — Use in post or page templates with dynamic content enabled so the heading automatically displays the current post's title without manual entry.
3. **Linked Navigation Labels** — Configure a heading with a link to create prominent, styled anchor text that directs users to key pages, sections, or external resources.

## How to Add the Heading Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Heading" in the module picker or find it in the Content Elements category, then click to insert it.


## Settings & Options

The Heading module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the heading text, link behavior, background, and module metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text input | The heading text content displayed on the page. Supports dynamic content for use in templates and loop contexts. |
| Link | url/link settings | Makes the entire heading clickable, directing users to a page, section anchor, or external URL. Includes target and relationship options. |
| Background | background controls | Apply a background color, gradient, image, or video behind the heading module. |
| Loop | toggle | Enables the loop builder for repeating the heading dynamically within query-driven layouts. |
| Order | number | Controls the display order of this module when its parent uses Flexbox or Grid layout. |
| Meta | admin label | Set an admin label for identification in the Visual Builder layer panel. Controls builder-only visibility. |

<!-- ![Heading Content tab settings](../assets/screenshots/modules/heading/settings-content.png){ loading=lazy } -->

### Design Tab

The Design tab controls the heading's typography, dimensions, spacing, and visual effects.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Heading Text | typography controls | Font family, weight, style, size, color, letter spacing, line height, and text shadow settings specifically for the heading element. Independent from general text settings. |
| Text |  | Choose the overall Heading module's text styles for this module. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Heading module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Heading module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Heading module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Heading module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Heading module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Heading module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Heading module's animation styles. <!-- AUTO-ADDED --> |
| Layout - |  | Choose the Layout Style. It allows you to change how the child modules are being displayed.BlockFlex(default)Grid <!-- AUTO-ADDED --> |
| Block |  |  <!-- AUTO-ADDED --> |
| Flex |  | (default) <!-- AUTO-ADDED --> |
| Grid |  |  <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | General text styling — font, alignment, color |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (hue, saturation, brightness, blend mode) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

<!-- ![Heading Design tab settings](../assets/screenshots/modules/heading/settings-design.png){ loading=lazy } -->

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, semantic HTML, conditional display, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Semantic HTML tag selection (H1-H6, p, span) for the heading element |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Heading module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Heading's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Heading's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Heading's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Heading module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

<!-- ![Heading Advanced tab settings](../assets/screenshots/modules/heading/settings-advanced.png){ loading=lazy } -->

## Code Examples

### Custom CSS

!!! tip "Native gradient text (Divi 5.7+)"
    Before writing custom CSS, check **Design → Heading Text** for **gradient fill**, **image fill**, and **text stroke** settings. These use the [Gradient Picker](../builder/gradient-builder.md) and support gradient variables. The CSS below remains useful for fine-tuning or targeting child themes.

```css
/* Gradient text effect on headings */
.et_pb_heading .et_pb_heading_title {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Underline accent below heading */
.et_pb_heading.underline-accent .et_pb_heading_title::after {
    content: '';
    display: block;
    width: 60px;
    height: 3px;
    background: #2ea3f2;
    margin-top: 12px;
}

/* Center the underline accent */
.et_pb_heading.underline-accent.centered .et_pb_heading_title::after {
    margin-left: auto;
    margin-right: auto;
}

/* Responsive heading sizes */
@media (max-width: 980px) {
    .et_pb_heading .et_pb_heading_title {
        font-size: 28px !important;
    }
}

@media (max-width: 767px) {
    .et_pb_heading .et_pb_heading_title {
        font-size: 22px !important;
    }
}
```

### PHP Hooks

```php
/* Add structured data markup to H1 headings */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_heading' !== $render_slug) {
        return $output;
    }
    // Add an itemprop attribute for SEO
    $output = str_replace(
        '<h1 class=',
        '<h1 itemprop="headline" class=',
        $output
    );
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Section Title with Subtitle** — Pair a Heading module (H2) with a Text module containing a short subtitle beneath it. Place both inside a Group module and center-align the Group for a clean section opener. Apply a decorative underline using the CSS example above.

2. **Dynamic Archive Header** — In a category or tag template, use the Heading module with dynamic content to display the archive name. Set the HTML tag to H1 for proper document structure and apply conditional logic to show different headings based on the archive type.

3. **Sticky Page Title** — Set the Heading module's position to sticky in the Advanced tab with a top offset of 0. Add a solid background color and padding so the heading remains readable as it overlays scrolling content below it. This works well for long-form content pages that benefit from persistent section labels.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/heading` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Title | `attrs.title` | The heading text content |
| Tag Level | `attrs.header_level` | HTML heading level (h1-h6) |

!!! tip "Module Selection Guidance"
    For standalone headings with full typography control use Heading; for heading+body text use Text; for heading+button use Call to Action.

## Saving Your Work

After configuring the Heading module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Heading Not Displaying Dynamic Content"
    If the heading shows placeholder text instead of dynamic post data:

    - Confirm that the dynamic content icon is activated in the Text field and the correct data source (e.g., Post Title) is selected.
    - Dynamic content only resolves on the front end or in template preview mode. The Visual Builder may show placeholder text during editing.
    - Ensure the module is used within a template that has an associated post type, not a static page without query context.

!!! warning "Wrong Heading Level Rendering"
    If the heading renders as the wrong HTML tag (e.g., H2 when you need H1):

    - Check the **HTML** settings in the Advanced tab where the semantic tag is selected. The default may not match your intended heading level.
    - The Design tab's visual size settings are independent of the HTML tag, so a heading can look like an H1 visually while being an H3 semantically. Always verify the HTML tag matches your document outline.

!!! tip "Multiple H1 Tags on a Page"
    For SEO best practices, use only one H1 per page. If you have multiple Heading modules, set all but the primary page title to H2 or lower in the Advanced tab's HTML settings. Use the Design tab's Heading Text controls to make them visually prominent without affecting the heading hierarchy.

## Related

- [Text](text.md) — Rich text content module for body copy, paragraphs, and formatted content
- [Post Title](post-title.md) — Displays the post or page title dynamically within templates
- [Heading Text Options](../options-groups/heading-text.md) — Shared heading typography settings across modules
- [Dynamic Content](../builder/dynamic-content.md) — Pull page or post titles dynamically into heading fields
- [Semantic Elements](../builder/semantic-elements.md) — Choose the correct HTML heading level for accessibility
