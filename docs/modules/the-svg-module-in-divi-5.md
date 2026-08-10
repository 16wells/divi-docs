---
title: "The SVG Module in Divi 5"
category: modules
tags: ["modules", "svg", "icons", "graphics"]
related: ["icon", "image"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/15081438-the-svg-module-in-divi-5"
status: stub
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# The SVG Module in Divi 5

The Divi 5 **SVG Module** lets you place SVG graphics directly on a page and control their appearance with **native stroke and width settings** — keeping vector artwork lightweight and pixel-perfect at any size.

## Overview

<!-- TODO: Expand from ET help article 15081438 once network access permits a full scrape. -->

This module was introduced as part of the **Five New Modules for Divi 5** release (Timeline, Breadcrumbs, Table of Contents, SVG, Instagram Feed). Unlike inserting an SVG as an image, the SVG module exposes the source vector's strokes and fills as Divi settings, so you can restyle the artwork in the builder without editing the file.

![SVG module overview](../assets/screenshots/modules/svg/overview.png){ loading=lazy }
*Caption: Placeholder — capture once a working install is available.*

## Settings & Options

<!-- TODO: Build complete Content / Design / Advanced settings tables from the ET help article and a live install. -->

### Content Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO --> | | | |
| SVG Source |  | Choose how the SVG is supplied to the module:SVG Code: Paste in valid SVG markup. The code you paste must be well-formed<svg>element. Broken or partial markup will not render.Uploaded SVG: Upload any SVG file from the WordPress Media Library.Important note:By default, WordPress blocks the upload of SVG files for security reasons. You'll need to enable SVG uploads before this option will work. For instructions, refer to theHow to Upload SVG and JSON Filesarticle.Title: Set the SVG's title text. The title is used for accessibility and appears as a tooltip when a visitor hovers over the graphic. <!-- AUTO-ADDED --> |
| SVG Code |  | Paste in valid SVG markup. The code you paste must be well-formed<svg>element. Broken or partial markup will not render. <!-- AUTO-ADDED --> |
| Uploaded SVG |  | Upload any SVG file from the WordPress Media Library.Important note:By default, WordPress blocks the upload of SVG files for security reasons. You'll need to enable SVG uploads before this option will work. For instructions, refer to theHow to Upload SVG and JSON Filesarticle. <!-- AUTO-ADDED --> |
| Title |  | Set the SVG's title text. The title is used for accessibility and appears as a tooltip when a visitor hovers over the graphic. <!-- AUTO-ADDED --> |
| Link |  | Make the entire SVG module clickable. Set theLink URL, choose theLink Target(same tab or new tab), and add aLink Relvalue such asnofollowornoopenerwhen needed. <!-- AUTO-ADDED --> |
| Elements |  | Toggle which sub-elements of the SVG module are shown. <!-- AUTO-ADDED --> |
| Background |  | Choose the SVG module's background styles. <!-- AUTO-ADDED --> |
| Loop |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order |  | Choose the order in which the SVG module appears inside a Flexbox or Grid layout. <!-- AUTO-ADDED --> |
| Meta |  | Choose the SVG Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Stroke | <!-- TODO --> | | Native stroke styling exposed by the module |
| Stroke Width | <!-- TODO --> | | Native stroke width styling exposed by the module |
| <!-- TODO --> | | | |
| Layout |  | Choose how the SVG module lays out its content using Divi'sFlexboxorCSS Gridsystem. <!-- AUTO-ADDED --> |
| Fill |  | Choose the SVG's fill color, which is the paint applied to the inside of closed shapes. Setting Fill here overrides anyfillvalues defined inside the SVG markup itself. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the SVG module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the SVG module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the SVG module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the SVG module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the SVG module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the SVG module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the SVG module's animation styles. <!-- AUTO-ADDED --> |

### Advanced Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | none | Custom HTML id attribute |
| CSS Class | text | none | Custom CSS class(es) |
| Custom CSS | code | none | Target specific elements within the module |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS code to fine-tune your SVG module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| HTML |  | Choose the semantic HTML tag for the SVG module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Interactions |  | Create custom interactions, such as showing or hiding the SVG, and many more. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the SVG module's visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the SVG module's animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the SVG module's placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the SVG module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Elegant Themes tutorials

- [Five New Modules for Divi 5 (Timeline, Breadcrumbs, Table of Contents, SVG, Instagram Feed)](https://www.elegantthemes.com/blog/theme-releases/five-new-modules){:target="_blank"} — release announcement; SVG module is highlighted for native stroke and width styling.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! tip "Uploading SVGs"
    See [Uploading SVG and JSON files](../troubleshooting/upload-svg-json.md) for WordPress upload-permission setup.

## Related

- [Icon Module](icon.md)
- [Image Module](image.md)
- [Uploading SVG and JSON files](../troubleshooting/upload-svg-json.md)
