---
title: "Testimonial Module"
description: "Complete Divi 5 Testimonial module reference — customer quotes, author photo, job title, company attribution, and quote icon styling."
category: modules
tags: [testimonial, social-proof, reviews, quotes, content-modules, customer-feedback]
related: [person, slider, blurb]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10365121-the-testimonial-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Testimonial Module

The Testimonial module displays customer quotes, reviews, and endorsements with an author photo, name, job title, and company attribution.

!!! abstract "Quick Reference"
    **What it does:** Displays a structured customer quote with author photo, name, job title, company, and decorative quote icon.
    **When to use it:** Customer review sections, featured endorsements, case study quote highlights
    **Key settings:** Author, Job Title, Company, Body (quote text), Image, Quote Icon toggle
    **Block identifier:** `divi/testimonial`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10365121-the-testimonial-module-in-divi-5)

!!! tip "When to Use This Module"
    - Displaying customer quotes with structured attribution (name, title, company)
    - Building social proof sections near pricing or call-to-action areas
    - Creating multi-column testimonial grids with author photos

!!! warning "When NOT to Use This Module"
    - Displaying team member profiles with social links → use [Person](person.md)
    - Creating a rotating quote slideshow → use [Slider](slider.md)
    - Building general icon-and-text feature cards → use [Blurb](blurb.md)

## Overview

The Testimonial module provides a structured way to present social proof on your website. Each testimonial includes a quote body, author image, author name, job position, and company name, all arranged in a clean, professional layout. A decorative quote icon reinforces the visual identity of the module, making it immediately recognizable as a customer endorsement.

Social proof is one of the most effective conversion tools available to website owners. By placing testimonials near calls to action, pricing sections, or service descriptions, you provide visitors with third-party validation that builds trust and reduces hesitation. The Testimonial module makes this easy by combining all the necessary elements into a single, cohesive block.

The module supports both portrait and landscape orientations, allows you to toggle individual elements on or off, and provides granular typography controls for every text element. You can style the quote icon, adjust image dimensions, apply background overlays, and animate the module on scroll. When combined with Divi's row column structures, you can build multi-column testimonial grids, alternating layouts, or single featured endorsements.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10365121-the-testimonial-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/testimonial/)

![Testimonial module](../assets/screenshots/modules/testimonial/element.png){ loading=lazy }
*The Testimonial module displaying a customer quote with author photo, name, and company.*

## Use Cases

1. **Customer Reviews Section** — Place multiple Testimonial modules in a multi-column row to build a reviews grid on a landing page. Each column can hold a different customer quote, creating a mosaic of social proof that visitors can scan quickly.

2. **Featured Endorsement** — Use a single Testimonial module in a full-width row as a featured quote between content sections. Increase the font size of the body text and apply a background color to the section to make it stand out as a visual break in the page flow.

3. **Case Study Highlights** — Pair the Testimonial module with a Blurb or Text module to attribute a quote to a specific project or result. Position the testimonial alongside metrics or outcomes to reinforce credibility with concrete data.

## How to Add the Testimonial Module

1. **Open the Visual Builder** on the page where you want the testimonial to appear. Click the gray plus icon inside any row to open the module picker.

2. **Search for "Testimonial"** in the module picker search bar, then click the Testimonial module to insert it into the row.

3. **Configure the module** by entering the author name, job title, company name, and testimonial body text in the Content tab. Upload an author portrait image and adjust the design settings to match your site's style.

## Settings & Options

### Content Tab

The Content tab holds all the primary data fields for the testimonial, including the quote text, author details, image, and structural elements.

| Setting | Type | Description |
|---------|------|-------------|
| **Text** | | |
| Author | text | The name of the person giving the testimonial |
| Job Title | text | The author's professional title or role |
| Company | text | The organization the author represents |
| Body | rich text | The testimonial quote content, supports visual editing and HTML |
| URL | url | A link destination applied to the author name or company |
| **Image** | | |
| Image | upload | Portrait or headshot image of the testimonial author |
| Image Alt Text | text | Accessible alt text describing the author image |
| **Elements** | | |
| Quote Icon | toggle | Show or hide the decorative quotation mark icon |
| **Link** | | |
| Module Link URL | url | Makes the entire module a clickable link |
| Module Link Target | select | Opens the link in the same window or a new tab |
| **Background** | | |
| Background Color | color | Solid background color behind the module |
| Background Gradient | gradient | Gradient background with direction and color stop controls |
| Background Image | upload | An image displayed behind the module content |
| Background Video | url | A video URL (MP4 or WebM) used as a motion background |
| Background Pattern | select | A decorative pattern overlay applied to the background |
| Background Mask | select | A shaped mask overlay applied to the background |
| **Loop** | | |
| Dynamic Content | toggle | Enable dynamic content connections for supported fields |
| **Order** | | |
| Module Order | select | Position of this module relative to siblings in the row |
| **Meta** | | |
| Admin Label | text | A custom label shown in the builder layers panel for easy identification |
| Disable On | toggle | Disable the module on specific device sizes (phone, tablet, desktop) |
| Text |  | Set the Testimonial's Author Name, Job Title, Company, and body text. <!-- AUTO-ADDED --> |
| Elements |  | Choose to display or hide the quote icon. <!-- AUTO-ADDED --> |
| Link |  | Make the entire Testimonial module clickable, creating a seamless way to direct users to another page, section, or external site. <!-- AUTO-ADDED --> |
| Background |  | Choose the Testimonial module's background styles. <!-- AUTO-ADDED --> |
| Loop |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order |  | Choose the order in which the Testimonial module appears inside a Flexbox and Grid layout. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Testimonial Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides comprehensive visual controls for every element of the testimonial, from the quote icon to the individual text elements.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Icon Color | color | The color of the decorative quotation mark icon |
| Icon Size | range | The size of the quote icon in pixels |
| Image Width | range | The width of the author portrait image |
| Image Height | range | The height of the author portrait image |
| Image Rounded Corners | range | Border radius applied to the author image |
| Image Border | composite | Border width, style, and color around the author image |
| Image Box Shadow | composite | Shadow effect applied to the author image |
| Author Text | typography group | Font family, weight, style, color, size, letter spacing, line height, text shadow for the author name |
| Position Text | typography group | Font family, weight, style, color, size, letter spacing, line height, text shadow for the job title |
| Company Text | typography group | Font family, weight, style, color, size, letter spacing, line height, text shadow for the company name |
| Quote Icon |  | Choose the quote icon and icon styles. <!-- AUTO-ADDED --> |
| Image |  | Choose the Testimonial module's image styles. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall Testimonial module's text styles for this module. <!-- AUTO-ADDED --> |
| Body Text |  | Choose the module's body text styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Testimonial module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Testimonial module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Testimonial module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Testimonial module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Testimonial module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Testimonial module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Testimonial module's animation styles. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Body Text](../options-groups/body-text.md) | Font, size, color, spacing for the quote body |
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides technical controls for custom attributes, CSS overrides, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (main element, portrait image, description, author, position, company, quote icon, before, after) |
| HTML | Custom HTML attributes for module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Testimonial module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Testimonial's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Testimonial module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Testimonial's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Testimonial module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Style the testimonial quote body */
.et_pb_testimonial_description {
    font-style: italic;
    line-height: 1.8;
}

/* Make the author image circular */
.et_pb_testimonial_portrait {
    border-radius: 50%;
    border: 3px solid #2ea3f2;
}

/* Change the quote icon color and size */
.et_pb_testimonial::before {
    color: #2ea3f2;
    font-size: 28px;
}

/* Card-style testimonial with shadow */
.et_pb_testimonial {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    padding: 40px;
    border: none;
}

/* Responsive padding adjustments */
@media (max-width: 980px) {
    .et_pb_testimonial {
        padding: 24px;
    }
}
```

### PHP Hooks

```php
/**
 * Add a star rating above each testimonial body.
 */
function add_testimonial_stars( $output, $render_slug ) {
    if ( 'et_pb_testimonial' !== $render_slug ) {
        return $output;
    }

    $stars = '<div class="testimonial-stars" style="color: #f5a623; margin-bottom: 12px;">';
    $stars .= str_repeat( '&#9733;', 5 );
    $stars .= '</div>';

    // Insert stars before the testimonial description
    $output = str_replace(
        '<div class="et_pb_testimonial_description">',
        '<div class="et_pb_testimonial_description">' . $stars,
        $output
    );

    return $output;
}
add_filter( 'et_module_shortcode_output', 'add_testimonial_stars', 10, 2 );
```

## Common Patterns

1. **Testimonial Grid** — Place three Testimonial modules inside a three-column row. Give each a white background, rounded corners, and a subtle box shadow to create a card-based grid. Set consistent padding across all three and use the same image size for visual uniformity.

2. **Featured Quote with Background** — Use a single Testimonial module in a full-width row. Apply a dark background color or image to the section, switch the text color scheme to light, increase the body font size, and center-align all text. This creates a bold visual break that draws attention to a key endorsement.

3. **Rotating Testimonials** — Combine the Testimonial module with Divi's Slider module by placing individual testimonials on each slide. Alternatively, stack multiple toggles in a single column and use conditional display logic or JavaScript to cycle through them automatically.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/testimonial` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Author | `attrs.author` | Person giving the testimonial |
| Job Title | `attrs.job_title` | Author's professional title |
| Company | `attrs.company_name` | Author's organization |
| Body | `attrs.content` | Testimonial quote text |
| Portrait URL | `attrs.portrait_url` | Author headshot image |

!!! tip "Module Selection Guidance"
    For customer quotes with attribution use Testimonial; for team bios use Person; for general icon+text use Blurb.

## Saving Your Work

After configuring your Testimonial module, click the green checkmark at the bottom of the settings panel to save the module settings. Then save the page using the purple save button in the bottom dock of the Visual Builder. You can also use keyboard shortcut `Ctrl + S` (Windows) or `Cmd + S` (Mac) to save quickly. Consider saving to the Divi Library if you plan to reuse the same testimonial configuration across multiple pages.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Testimonial module in Divi 5 uses updated CSS class structures and the new options framework. Custom CSS selectors from Divi 4 may need adjustment.

## Troubleshooting

!!! warning "Author Image Not Displaying"
    If the author portrait image does not appear on the front end, check the following:

    - Confirm the image has been uploaded and saved in the Image field under the Content tab
    - Verify the image file still exists in the WordPress Media Library
    - Check that image dimensions are reasonable (recommended: 90x90px minimum)
    - Inspect the Image settings in the Design tab to ensure the width and height are not set to zero

!!! warning "Quote Icon Missing or Misaligned"
    If the decorative quote icon disappears or overlaps other content:

    - Verify that the Quote Icon toggle is enabled in the Elements section of the Content tab
    - Check the Icon Size and Icon Color settings in the Design tab to ensure the icon is visible against the background
    - If using custom CSS, inspect for `display: none` or `overflow: hidden` rules that may affect the pseudo-element

!!! warning "Text Styles Not Applying Consistently"
    If typography changes in the Design tab do not reflect on the front end:

    - Each text element (body, author, position, company) has its own typography group; confirm you are editing the correct one
    - Clear any site caching plugins and browser cache after making changes
    - Check for conflicting styles from your child theme or third-party plugins using the browser inspector

## Related

- [Person Module](person.md) — displays a team member profile with photo, name, and bio
- [Slider Module](slider.md) — creates sliding content panels, useful for rotating testimonials
- [Blurb Module](blurb.md) — pairs text content with an icon or image for feature highlights
- [Image Options](../options-groups/image.md) — Style the testimonial author portrait photo
- [Flexbox Layout](../builder/flexbox.md) — Arrange multiple testimonials in responsive grid layouts
