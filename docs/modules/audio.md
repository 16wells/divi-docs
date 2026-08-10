---
title: "Audio"
description: "Complete Divi 5 Audio module reference — settings for embedding audio players with album art, metadata, and playback controls."
category: modules
tags: ["modules", "media", "audio", "music", "podcast", "mp3", "player"]
related: ["video", "video-slider"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10125708-the-audio-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Audio

The Audio module embeds an audio player with optional album artwork, title, and artist metadata.

!!! abstract "Quick Reference"
    **What it does:** Embeds a styled HTML5 audio player with cover image, title, and artist metadata.
    **When to use it:** Podcast episodes, music portfolios, guided audio content, voice recordings
    **Key settings:** Audio file source, Image (cover art), Text (title/artist), Link, Background
    **Block identifier:** `divi/audio`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10125708-the-audio-module-in-divi-5)

!!! tip "When to Use This Module"
    - You need an inline audio player with playback controls on a page
    - Podcast or music pages where cover art and metadata should display alongside the player
    - Audio lessons, meditations, or recordings paired with written content

!!! warning "When NOT to Use This Module"
    - You need to embed video content → use [Video](video.md)
    - You need a playlist of multiple video files → use [Video Slider](video-slider.md)
    - You need background audio that plays automatically → use a [Code](code.md) module with custom JavaScript

## Overview

The Audio module provides a fully styled, browser-native audio player that you can drop into any page layout. It wraps the standard HTML5 `<audio>` element with Divi's design controls, letting you present music tracks, podcast episodes, voice recordings, or any other audio file with a polished, on-brand appearance.

Beyond basic playback, the module supports an accompanying cover image, making it well suited for album art, podcast artwork, or episode thumbnails. You can also display a title and artist/caption alongside the player, giving visitors the context they need without leaving the page.

Because the module relies on the browser's native audio capabilities, it supports common formats such as MP3, OGG, and WAV. Upload files to the WordPress Media Library and select them from within the module settings, or paste an external URL to a hosted audio file.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10125708-the-audio-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/audio/)

![Audio module](../assets/screenshots/modules/audio/element.png){ loading=lazy }
*The Audio module displaying a track with cover artwork and playback controls.*

## Use Cases

1. **Podcast Episode Player** — Embed individual episodes directly on a show notes page so visitors can listen without navigating to a third-party platform.
2. **Music Portfolio** — Showcase original compositions or production samples with album artwork, giving prospective clients or fans an inline listening experience.
3. **Guided Meditation or Course Audio** — Offer audio lessons, meditations, or training recordings alongside written content for a multimedia learning experience.

## How to Add the Audio Module

1. Open the Visual Builder on the page you want to edit.
2. Click the gray **+** icon to add a new module to a row.
3. Search for "Audio" in the module picker or locate it in the Media category, then click to insert it.


## Settings & Options

The Audio module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the audio source, accompanying text and image, link behavior, background, and metadata.

| Setting | Type | Description |
|---------|------|-------------|
| Text | text fields | Enter the track title and artist or description that display above the audio player. |
| Audio | file upload / URL | Select or upload an audio file (MP3, OGG, WAV) from the Media Library, or paste an external audio URL. This is the file the player will stream. |
| Image | image upload | Upload or select a cover image displayed alongside the player. Commonly used for album art, podcast artwork, or a branded thumbnail. |
| Link | URL | Optionally wrap the module in a link so clicking navigates to another page or resource. |
| Background | background controls | Apply a background color, gradient, image, or video behind the entire Audio module container. |
| Loop | toggle | When enabled, the module output can be repeated in loop-based layouts such as post type archives or custom queries. |
| Order | select | Control the display order when the module is used inside a loop or dynamic layout context. |
| Meta | admin label | Set an internal admin label to identify this module in the Visual Builder's layer panel and search. |

![Audio Content tab settings](../assets/screenshots/modules/audio/settings-content.png){ loading=lazy }

### Design Tab

The Design tab controls all visual styling for the audio player and its surrounding elements.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Image | image styling | Adjust the cover image dimensions, alignment, and how it is displayed relative to the player. |
| Caption Text | text styling | Style the artist or caption text below the title with its own font, size, color, and spacing values. |
| Text |  | Choose the overall Audio module's text styles for this module. <!-- AUTO-ADDED --> |
| Title Text |  | Choose the Audio module's title styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Audio module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Audio module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Audio module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Audio module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Audio module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Audio module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Audio module's animation styles, adding personality and interactivity while keeping a polished, professional feel. <!-- AUTO-ADDED --> |
| Layout - |  | Choose the Layout Style. It allows you to change how the child modules are being displayed.BlockFlex(default)Grid <!-- AUTO-ADDED --> |
| Block |  |  <!-- AUTO-ADDED --> |
| Flex |  | (default) <!-- AUTO-ADDED --> |
| Grid |  |  <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Title Text](../options-groups/text.md) | Font, size, color, letter spacing for the track title |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding (responsive) |
| [Border](../options-groups/border.md) | Width, color, style, radius |
| [Box Shadow](../options-groups/box-shadow.md) | Shadow effects |
| [Filters](../options-groups/filters.md) | CSS filters (brightness, contrast, etc.) |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew |
| [Animation](../options-groups/animation.md) | Entrance animation styles |

![Audio Design tab settings](../assets/screenshots/modules/audio/settings-design.png){ loading=lazy }

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
| CSS- |  | Allows you to add custom CSS code to fine-tune your Audio module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Audio module's visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Audio's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Audio module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Audio module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

![Audio Advanced tab settings](../assets/screenshots/modules/audio/settings-advanced.png){ loading=lazy }

## Code Examples

### Custom CSS

```css
/* Style the Audio module container */
.et_pb_audio_module {
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 30px;
}

/* Style the cover image area */
.et_pb_audio_module .et_pb_audio_cover_art {
    max-width: 200px;
    border-radius: 8px;
}

/* Style the track title */
.et_pb_audio_module h2 {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
}

/* Customize the playback controls bar */
.et_pb_audio_module .mejs-container {
    background: transparent;
}

.et_pb_audio_module .mejs-controls .mejs-time-rail .mejs-time-total {
    border-radius: 4px;
}

/* Responsive adjustments */
@media (max-width: 980px) {
    .et_pb_audio_module .et_pb_audio_cover_art {
        max-width: 150px;
    }
    .et_pb_audio_module h2 {
        font-size: 18px;
    }
}
```

### PHP Hooks

```php
/* Filter the Audio module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_audio' !== $render_slug) {
        return $output;
    }
    // Example: add a download link after the player
    $output .= '<a href="#" class="audio-download-link">Download Episode</a>';
    return $output;
}, 10, 2);
```

## Common Patterns

1. **Podcast Show Notes Layout** — Place the Audio module at the top of a blog post, followed by a text module with episode show notes and timestamps. Set a branded cover image and use the title field for the episode name.

2. **Music Portfolio Grid** — Arrange multiple Audio modules in a multi-column row to create a grid of playable tracks. Give each a unique cover image and keep titles short so the layout stays compact and scannable.

3. **Background Ambience Player** — Use a single Audio module in a sticky footer or sidebar section to provide ambient background audio. Style it with a minimal design, reduced spacing, and subtle colors so it does not compete with primary content.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/audio` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Audio URL | `attrs.audio` | Source URL of the audio file |
| Title | `attrs.title` | Track or episode title |
| Artist | `attrs.artist` | Artist or creator name |
| Image URL | `attrs.image_url` | Cover artwork image URL |

!!! tip "Module Selection Guidance"
    For audio playback use Audio; for video use Video; for background music consider custom code.

## Saving Your Work

After configuring the Audio module:

- **Save changes** — Click the purple **Save** button at the bottom of the Visual Builder, or press `Ctrl+S` (Windows) / `Cmd+S` (Mac).
- **Exit the builder** — Click the **X** button or use `Ctrl+Shift+E` to return to the WordPress dashboard.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Audio File Not Playing"
    If the player appears but no audio plays, verify that:

    - The audio file URL is accessible and not behind authentication
    - The file format is supported by browsers (MP3 is the most widely compatible)
    - Your hosting server allows direct file access and has not blocked the MIME type

!!! warning "Cover Image Not Displaying"
    If the uploaded image does not appear beside the player:

    - Confirm the image was uploaded to the Media Library and the URL is valid
    - Check that Design tab image sizing settings are not collapsing the image to zero dimensions
    - Verify no custom CSS is hiding the `.et_pb_audio_cover_art` element

!!! tip "Player Looks Unstyled or Broken"
    The Audio module relies on the MediaElement.js library bundled with WordPress. If the player appears as a plain HTML5 control, check that no optimization plugin is deferring or combining the mediaelement scripts incorrectly. Exclude `wp-mediaelement` from script optimization to restore styling.

## Related

- [Video](video.md) — Embed video content with a similar media-focused layout
- [Video Slider](video-slider.md) — Present multiple videos in a sliding carousel format
