---
title: "Portfolio Module"
description: "Complete Divi 5 Portfolio module reference — project grids, fullwidth layouts, category filtering, pagination, and query controls."
category: modules
tags: ["modules", "content-modules", "portfolio", "projects", "grid", "fullwidth", "pagination", "dynamic-content"]
related: ["filterable-portfolio", "gallery", "blog"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10358290-the-portfolio-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Portfolio Module

The Portfolio module displays WordPress project posts in configurable grid or fullwidth layouts with optional pagination and category filtering.

!!! abstract "Quick Reference"
    **What it does:** Queries WordPress project posts and displays them in grid or fullwidth layouts with pagination.
    **When to use it:** Creative portfolio pages, homepage work showcases, service category project listings
    **Key settings:** Projects Number, Project Categories, Show Title/Categories/Pagination, Layout (Grid/Fullwidth)
    **Block identifier:** `divi/portfolio`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10358290-the-portfolio-module-in-divi-5)

!!! tip "When to Use This Module"
    - Displaying project posts from the WordPress Projects custom post type
    - Building paginated portfolio archives filtered by category
    - Creating grid or fullwidth project showcases with featured images

!!! warning "When NOT to Use This Module"
    - Needing client-side category filter buttons → use [Filterable Portfolio](filterable-portfolio.md)
    - Displaying standard blog posts in a grid → use [Blog](blog.md)
    - Creating an image-only gallery without post type dependency → use [Gallery](gallery.md)

## Overview

The Portfolio module provides a streamlined way to showcase project-based content on your Divi 5 site. It connects directly to the WordPress Projects custom post type, pulling in project titles, featured images, and category labels to create polished portfolio displays. Whether you are building a creative agency site, a freelancer portfolio, or a corporate case studies page, this module gives you the layout and styling controls needed to present your work professionally.

Two primary layout modes are available: a fullwidth list view that stacks projects vertically with large images, and a multi-column grid view that arranges projects in rows. The grid mode supports both Flexbox and CSS Grid parent configurations, and you can control the number of columns and spacing between items. Pagination is built in, allowing visitors to browse through large project collections without overwhelming a single page.

The Portfolio module pairs well with the [Filterable Portfolio](filterable-portfolio.md) module when you need client-side category filtering, and with the [Gallery](gallery.md) module when your content is image-focused rather than project-focused. For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10358290-the-portfolio-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/portfolio/)

![Portfolio module](../assets/screenshots/modules/portfolio/element.png){ loading=lazy }
*The Portfolio module displaying projects in a grid layout with featured images and category labels.*

## Use Cases

1. **Creative Portfolio Page** — Display all published projects in a multi-column grid with featured images, titles, and category labels. Enable pagination so visitors can browse the full collection without excessive page length.
2. **Homepage Work Showcase** — Feature a limited number of recent projects (3-4) in a grid layout without pagination, giving visitors a quick visual summary of your best work and encouraging them to explore the full portfolio.
3. **Service Category Highlights** — Filter the module to a specific project category to build dedicated landing pages for each service area, such as "Web Design," "Branding," or "Photography."

## How to Add the Portfolio Module

1. Open the Visual Builder on the page where you want to display your portfolio.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Portfolio" in the module picker or find it in the Content Elements category, then click to insert it.

## Settings & Options

The Portfolio module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls which projects appear, what metadata is visible, and how the module connects to other pages or elements.

| Setting | Type | Description |
|---------|------|-------------|
| Projects Number | number | The maximum number of projects to display per page. Works with pagination to determine how many items a visitor sees before navigating to the next page. |
| Project Categories | multi-select | Filter the portfolio to show projects from specific categories only. When no categories are selected, all published projects are included in the query. |
| Show Title | toggle | Display or hide the project title beneath each featured image. Disabling this creates an image-only portfolio layout. |
| Show Categories | toggle | Display or hide the category labels associated with each project. Categories typically appear below the title as clickable links. |
| Show Pagination | toggle | Enable or disable page navigation at the bottom of the portfolio grid. When disabled, only the first set of results is displayed. |
| Link | url | Make the entire Portfolio module wrapper clickable, directing users to a specified page, section, or external URL. Configure whether the link opens in the same window or a new tab. |
| Background | background controls | Set a background color, gradient, image, or video behind the entire Portfolio module container. Supports multi-layered backgrounds with blend modes. |
| Order | order controls | Define the display order of the Portfolio module within Flexbox and CSS Grid parent layouts. Useful when the visual order should differ from the DOM order. |
| Meta | admin label | Assign a custom admin label to the module for easier identification in the Visual Builder layer panel. Force visibility in the builder interface. |
| Content |  | Choose how many Projects the module will display and from which Project Categories. <!-- AUTO-ADDED --> |
| Elements |  | Enable or Disable the visibility of the Project's title, Categories, and Pagination. <!-- AUTO-ADDED --> |

#### Portfolio Content Settings Detail

The Content group within the Content tab contains the core query settings:

| Setting | Type | Description |
|---------|------|-------------|
| Projects Number | number | Sets the maximum number of project posts to load per page. Combined with the pagination toggle, this determines how your project library is divided across pages. |
| Project Categories | multi-select | Limits the displayed projects to one or more specific project categories. This is useful when creating section-specific portfolio displays on different pages. |

### Design Tab

The Design tab provides full visual control over the portfolio layout, image presentation, typography for titles and meta elements, and standard module styling.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | layout controls | Choose between Fullwidth (list) and Grid layout modes. In Grid mode, configure the underlying grid method (Flexbox or CSS Grid), number of columns, and column spacing to control the visual density of the portfolio. |
| Fullwidth |  | (Default) <!-- AUTO-ADDED --> |
| Grid layout |  | Choose betweenFlexboxandGridlayout, the number of columns, the space between columns, and much more. <!-- AUTO-ADDED --> |
| Overlay |  | Choose the hover overlay's styles. <!-- AUTO-ADDED --> |
| Image |  | Choose the styles applied to each project's Featured Image. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall Portfolio module's text styles for this module. <!-- AUTO-ADDED --> |
| Title Text |  | Choose the Portfolio module's title styles. <!-- AUTO-ADDED --> |
| Meta Text |  | Choose the module's body text styles. <!-- AUTO-ADDED --> |
| Pagination Text |  | Choose the module's pagination text styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Portfolio module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Portfolio module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Portfolio module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Portfolio module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Portfolio module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Portfolio module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Portfolio module's animation styles. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Image](../options-groups/image.md) | Border radius, alignment, sizing for project featured images |
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, line height, text shadow for project titles |
| [Meta Text](../options-groups/meta-text.md) | Font, size, color for category labels and metadata |
| [Pagination Text](../options-groups/pagination-text.md) | Font, size, color, hover states for pagination links |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides developer-oriented controls for custom attributes, conditional display logic, and scroll-driven effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (container, project item, title, category label, image, pagination) |
| HTML | Semantic HTML tag for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Portfolio module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Portfolio's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Portfolio's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Portfolio's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Portfolio module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Card-style portfolio grid with hover lift */
.et_pb_portfolio_grid .et_pb_portfolio_item {
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.et_pb_portfolio_grid .et_pb_portfolio_item:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

/* Add padding below each project image */
.et_pb_portfolio_grid .et_pb_portfolio_item .et_pb_portfolio_item_content {
    padding: 1.25rem;
}

/* Style the category label */
.et_pb_portfolio_grid .et_pb_portfolio_item .post-meta {
    font-size: 0.8rem;
    color: #999999;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_portfolio_grid .et_pb_portfolio_item .et_pb_portfolio_item_content {
        padding: 1rem;
    }
}
```

### PHP Hooks

```php
/**
 * Filter the Portfolio module output to add a custom wrapper class.
 */
add_filter( 'et_module_shortcode_output', function( $output, $render_slug ) {
    if ( 'et_pb_portfolio' !== $render_slug ) {
        return $output;
    }
    $output = str_replace(
        'class="et_pb_portfolio',
        'class="et_pb_portfolio my-custom-portfolio',
        $output
    );
    return $output;
}, 10, 2 );

/**
 * Modify portfolio query arguments to change post ordering.
 */
function my_portfolio_custom_order( $args ) {
    $args['orderby'] = 'menu_order';
    $args['order']   = 'ASC';
    return $args;
}
add_filter( 'et_pb_portfolio_query_args', 'my_portfolio_custom_order', 10, 1 );
```

## Common Patterns

1. **Fullwidth Project Showcase** — Set the layout to Grid with 3 or 4 columns and enable both titles and categories. Use the Spacing settings to add generous padding around each item, and apply a subtle box shadow from the Design tab for a card-style appearance. This is ideal for agencies and designers who want their work to be the focal point of the page.

2. **Minimal Image Grid** — Disable both the title and category toggles to create a clean, image-only portfolio grid. Set equal column spacing and apply a consistent border radius to the images. On hover, the overlay will reveal project details, keeping the default view visually minimal.

3. **Paginated Project Archive** — Enable pagination and set the projects number to 9 or 12 for a balanced grid. Use the Pagination Text settings in the Design tab to style the page navigation to match your site's design system. This pattern works well for studios with large project libraries that need organized browsing.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/portfolio` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Posts Number | `attrs.posts_number` | Maximum projects to display |
| Include Categories | `attrs.include_categories` | Filter by project category |
| Fullwidth | `attrs.fullwidth` | Toggle fullwidth layout mode |

!!! tip "Module Selection Guidance"
    For project grids use Portfolio; for filterable grids use Filterable Portfolio; for edge-to-edge display use Fullwidth Portfolio.

## Saving Your Work

After configuring the Portfolio module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Portfolio module in Divi 5 uses updated markup and supports CSS Grid parent layouts in addition to the traditional Flexbox approach found in earlier versions.

## Troubleshooting

!!! warning "Projects Not Displaying"
    If the Portfolio module appears empty, verify that: (1) you have published projects using the Projects custom post type (not regular posts), (2) the Project Categories filter is not excluding all available projects, and (3) no plugin or custom code is interfering with the project query. Check that the Projects Number is greater than zero.

!!! warning "Grid Columns Not Matching Expected Layout"
    If the grid columns do not align as expected, check whether the parent row is using Flexbox or CSS Grid. The Portfolio module's column count works within the constraints of the parent container. Also verify that the column spacing values are not pushing items to the next row.

!!! tip "Portfolio Images Are Different Sizes"
    For the most polished grid appearance, crop all project featured images to a consistent aspect ratio before uploading. The Portfolio module does not enforce aspect ratio uniformity, so differently sized images will produce uneven tile heights unless you set fixed image dimensions in the Design tab.

## Related

- [Filterable Portfolio Module](filterable-portfolio.md) — Portfolio with built-in client-side category filtering
- [Gallery Module](gallery.md) — Display images in grid layouts without post type dependency
- [Blog Module](blog.md) — Display standard WordPress posts in grid or list layouts
- [Fullwidth Portfolio](fullwidth-portfolio.md) — Full-browser-width portfolio variant for fullwidth sections
- [Loop Builder](../builder/loop-builder.md) — Create custom post loops with full layout control
- [Overlay Options](../options-groups/overlay.md) — Configure hover overlay effects on portfolio items
