---
title: "Person"
description: "Complete Divi 5 Person module reference — team profiles with photo, name, job title, biography, social links, and card styling."
category: modules
tags: ["modules", "team", "profile", "social-media", "image", "bio", "staff", "about"]
related: ["blurb", "testimonial", "social-media-follow"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10353818-the-person-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Person

The Person module creates a structured profile card combining a photo, name, job title, biography, and social media links in a single cohesive element.

!!! abstract "Quick Reference"
    **What it does:** Displays a profile card with photo, name, position, bio text, and social media icon links.
    **When to use it:** Team member pages, speaker lineups, author bios, client/partner showcases
    **Key settings:** Name, Position, Body (bio), Image, Social Media URLs, Icon styling
    **Block identifier:** `divi/person`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10353818-the-person-module-in-divi-5)

!!! tip "When to Use This Module"
    - Building team or staff directory pages with photos and social links
    - Displaying speaker or author profiles with structured data fields
    - Creating profile cards that include multiple social media links per person

!!! warning "When NOT to Use This Module"
    - Displaying a customer quote with attribution → use [Testimonial](testimonial.md)
    - Creating a general icon-and-text feature card → use [Blurb](blurb.md)
    - Showing standalone social media follow links → use [Social Media Follow](social-media-follow.md)

## Overview

The Person module is purpose-built for showcasing individuals on your Divi 5 website. Whether you are building a team page, an about section, a speaker lineup for an event, or a staff directory, this module brings together all the essential profile components — a portrait image, the person's name, their role or title, a short biography, and links to their social media profiles — into one unified block.

Each profile card is self-contained and highly customizable. The image can be styled with rounded corners, borders, and filters to match your site's visual identity. Typography controls let you style the name, position, and body text independently, so you can create clear visual hierarchy between each element. Social media icons appear beneath the bio text and link directly to the person's individual profiles.

The module works best when placed in multi-column rows to create grid-style team layouts. Three or four Person modules in a row produce a professional team section with minimal configuration. For larger organizations, you can combine the module with Divi 5's Loop Builder to dynamically generate person cards from custom post types, eliminating the need to manually create each profile.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10353818-the-person-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/person/)

![Person module](../assets/screenshots/modules/person/element.png){ loading=lazy }
*The Person module as it appears on the live demo.*

## Use Cases

1. **Team Members Page** — Arrange Person modules in a three- or four-column grid to display company staff with their headshots, titles, and short bios. Link each person's social icons to their LinkedIn or Twitter profiles so visitors can connect directly.

2. **Conference Speaker Lineup** — Use the module on an event landing page to introduce keynote speakers and session leaders. The position field works well for displaying a speaker's company affiliation or talk title alongside their name and headshot.

3. **Client or Partner Showcase** — Repurpose the Person module to highlight key clients, advisors, or business partners. Replace the typical bio with a brief description of the partnership, and use the image field for a professional headshot or company logo.

## How to Add the Person Module

1. **Open the Visual Builder** on the page where you want to add the profile. Click the gray plus icon inside a row to open the module picker, then search for "Person" and click to insert it.

2. **Fill in the profile details** in the Content tab. Enter the person's name, position or job title, and a short biography in the Text group. Upload a headshot in the Image group. Add social media profile URLs for any platforms the person is active on.

3. **Customize the appearance** using the Design tab to adjust image styling, typography for the name, position, and body text, icon colors and sizes, and overall spacing. Save your page when the profile looks the way you want it.

## Settings & Options

### Content Tab

The Content tab holds all the informational fields for the profile, including the person's name, title, biography, image, and social media links.

| Setting | Type | Description |
|---------|------|-------------|
| **Text — Name** | text | Enter the person's full name, displayed as the primary heading on the profile card |
| **Text — Position** | text | Enter the person's job title, role, or other descriptor shown beneath the name |
| **Text — Body** | rich text | Write a short biography or description that appears below the position text |
| **Text — Social Media URLs** | URL fields | Enter profile URLs for social media platforms such as Facebook, Twitter/X, LinkedIn, Instagram, and others; each populated URL generates a clickable icon |
| **Image** | image upload | Upload or select a portrait photo or headshot that appears at the top of the profile card |
| **Link** | URL / toggle | Make the entire module a clickable link and configure the destination URL, target, and rel attributes |
| **Background** | composite | Set background color, gradient, image, or video behind the module |
| **Loop** | toggle | Enable the Loop Builder to render this module dynamically within loop templates |
| **Order** | number | Set the display order of the module inside a Flexbox or CSS Grid layout |
| **Meta — Label** | text | Assign a label for identification in the Visual Builder layer panel |
| **Meta — Force Visibility** | toggle | Keep the module visible in the Visual Builder even when conditions would normally hide it |
| Text |  | Choose the Name, Position, Social Media Profile URLs, and Body Text. <!-- AUTO-ADDED --> |
| Image |  | Choose the Profile Image. <!-- AUTO-ADDED --> |
| Link |  | Make the entire Person module clickable, creating a seamless way to direct users to another page, section, or external site. <!-- AUTO-ADDED --> |
| Background |  | Choose the Person module's background styles. <!-- AUTO-ADDED --> |
| Loop |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order |  | Choose the order in which the Person module appears inside a Flexbox and Grid layout. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Person Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides independent styling controls for every visual component of the profile card, from the image treatment to individual text elements, icons, and an optional button.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Icon — Font Size | range | Set the size of the social media icons displayed on the profile card |
| Icon — Color | color | Choose the color for social media icons, with optional hover state color |
| Position Text | text styling | Font, weight, style, color, size, letter spacing, line height, and text shadow for the position or job title text |
| Layout - |  | Choose the Layout Style. It allows you to change how the child modules are being displayed.BlockFlex(default)Grid <!-- AUTO-ADDED --> |
| Block |  |  <!-- AUTO-ADDED --> |
| Flex |  | (default) <!-- AUTO-ADDED --> |
| Grid |  |  <!-- AUTO-ADDED --> |
| Icon |  | Choose the Social Media Icon's font size and color. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall Person module's text styles for this module. <!-- AUTO-ADDED --> |
| Image |  | Choose the Profile Image's styles, such as:Border RadiusBorder StylesBox ShadowImage Filters <!-- AUTO-ADDED --> |
| Title Text |  | Choose the Person module's title styles. <!-- AUTO-ADDED --> |
| Body Text |  | Choose the module's body text styles. <!-- AUTO-ADDED --> |
| Button |  | Choose the Person module's button styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Person module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Person module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Person module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Person module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Person module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Person module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Person module's animation styles. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Image](../options-groups/image.md) | Border radius, border styles, box shadow, image filters for the profile photo |
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, line height, text shadow for the person's name |
| [Body Text](../options-groups/body-text.md) | Font, size, color, line height for the biography text |
| [Button](../options-groups/button.md) | Text color, background, border, padding, font, hover states for optional button |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, scroll-driven effects, and positioning.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target |
| HTML | Semantic HTML tag for the module wrapper (div, article, section) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Person module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Person's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Person's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Person module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Center-align the entire profile card */
.et_pb_team_member {
    text-align: center;
}

/* Make the profile image circular */
.et_pb_team_member .et_pb_team_member_image img {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin: 0 auto 20px;
}

/* Style the name with brand color */
.et_pb_team_member h4 {
    color: #1e40af;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
}

/* Subtle styling for the position text */
.et_pb_team_member .et_pb_member_position {
    color: #6b7280;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

/* Add hover effect to social media icons */
.et_pb_team_member .et_pb_member_social_links a {
    color: #9ca3af;
    transition: color 0.3s ease, transform 0.3s ease;
}

.et_pb_team_member .et_pb_member_social_links a:hover {
    color: #1e40af;
    transform: scale(1.2);
}

/* Card-style layout with background and shadow */
.et_pb_team_member {
    background: #ffffff;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    transition: box-shadow 0.3s ease;
}

.et_pb_team_member:hover {
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_team_member .et_pb_team_member_image img {
        width: 120px;
        height: 120px;
    }
}
```

### PHP Hooks

```php
/* Filter the Person module output to add a schema.org markup wrapper */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_team_member' !== $render_slug) {
        return $output;
    }
    // Wrap the person card in schema.org Person markup
    $output = '<div itemscope itemtype="https://schema.org/Person">' . $output . '</div>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Card-Style Team Grid** — Place three Person modules in a row with equal column widths. Add a white background, rounded corners, and a subtle box shadow to each module using the Design tab's Border and Box Shadow settings. Center-align the text and use the Image border radius to create circular headshots, producing a clean card-based team layout.

2. **Executive Leadership Section** — Use a two-column row with a larger left column for the CEO or founder and a smaller right column containing a stacked pair of Person modules for other executives. Give the primary profile a larger image and more detailed biography, while the secondary profiles use abbreviated bios and smaller images.

3. **Social-Forward Author Profiles** — On a blog or publication site, place a Person module at the bottom of article templates using the Theme Builder. Populate the name, position (such as "Senior Writer"), a short author bio, and link all relevant social profiles. Style the social icons with a bold accent color so they stand out, encouraging readers to follow the author.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/person` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Name | `attrs.name` | Person's display name |
| Position | `attrs.position` | Job title or role |
| Body | `attrs.content` | Biography or description text |
| Image URL | `attrs.image_url` | Portrait or headshot image |
| Facebook | `attrs.facebook_url` | Facebook profile link |
| Twitter | `attrs.twitter_url` | Twitter/X profile link |
| LinkedIn | `attrs.linkedin_url` | LinkedIn profile link |

!!! tip "Module Selection Guidance"
    For team member profiles with social links use Person; for general icon+text cards use Blurb; for customer quotes use Testimonial.

## Saving Your Work

After configuring the Person module, click the green **Save** button at the bottom of the Visual Builder page settings bar. For team page layouts you plan to reuse, right-click the row containing your Person modules and choose **Save to Library** to store the entire team section as a reusable element. Individual person cards can also be saved independently if different pages need different team compositions.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Person module in Divi 5 uses the updated options framework with Flexbox and Grid support, independent typography controls for each text element, conditions, interactions, and scroll effects that are not available in Divi 4. If you are still using Divi 4, consult the legacy Elegant Themes documentation.

## Troubleshooting

!!! warning "Social Media Icons Not Showing"
    If the social media icons do not appear beneath the biography text, verify that you have entered valid URLs in the Social Media URL fields under the Content tab's Text group. Icons only render for platforms that have a URL provided. If the URLs are present but icons are still missing, check the Design tab's Icon settings to ensure the font size is not set to zero and the color is not the same as the background.

!!! warning "Profile Image Not Displaying"
    If the headshot area appears blank, confirm that an image has been uploaded or selected in the Content tab's Image group. Check that the image file exists in your WordPress media library and has not been deleted. If the image is there but invisible, inspect the Design tab's Image Filters to make sure opacity has not been reduced to zero and that no extreme filter values are hiding the image.

!!! warning "Uneven Card Heights in Grid Layouts"
    When placing multiple Person modules side by side, cards may appear at different heights if biographies vary in length. To create uniform heights, set a fixed Min Height in the Design tab's Sizing group, or use CSS to apply `display: flex` and `align-items: stretch` on the parent row. Alternatively, keep biography text to a consistent length across all team members.

## Related

- [Blurb](blurb.md) — Icon or image with text for feature cards and team highlights
- [Testimonial](testimonial.md) — Display customer quotes with author photo and attribution
- [Social Media Follow](social-media-follow.md) — Add social profile links alongside team member bios
- [Image Options](../options-groups/image.md) — Style the person photo with borders, filters, and sizing
- [Flexbox Layout](../builder/flexbox.md) — Arrange multiple person modules in responsive team grids
