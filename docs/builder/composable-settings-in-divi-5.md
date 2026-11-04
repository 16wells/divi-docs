---
title: "Composable Settings in Divi 5"
category: builder
tags: ["builder", "design-system", "option-groups", "composable-settings", "styling"]
related: ["advanced-styling-using-option-group-presets-in-divi-5.md", "element-presets.md", "understanding-divi-5-design-options.md"]
divi_version: "5.1+"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/14332889-composable-settings-in-divi-5"
---

# Composable Settings in Divi 5

Composable settings allow you to enable and disable design option groups on individual element sub-components. This modular approach gives you fine-grained control over styling while keeping your design system organized and flexible.

## Overview

In Divi 5, many elements contain multiple sub-elements (like Title Text, Button, Image, Body Text, etc.). Rather than forcing all design options onto every sub-element, composable settings let you decide which design groups to expose for each one.

For example, a Button element might have sub-elements for:

- Button text
- Button background
- Button border
- Button icon

With composable settings, you can:

- Enable **Sizing** only for the button background
- Enable **Border** for the button text
- Enable **Animation** for the button icon
- Disable options you don't need, keeping the interface clean

This approach supports design system consistency by letting you create presets that enforce specific styling rules per sub-element.

## What Are Option Groups?

Option groups are collections of related design settings:

| Group | Includes | Example Use |
|-------|----------|------------|
| **Sizing** | Width, height, aspect ratio | Set a button to a fixed width |
| **Border** | Border style, width, radius, shadow | Add rounded corners to a container |
| **Background** | Colors, gradients, images, overlays | Set a background image on a section |
| **Transform** | Rotate, skew, scale effects | Tilt an icon 45 degrees |
| **Animation** | Entrance, scroll, interaction effects | Fade in text on page load |
| **Spacing** | Padding, margin, gap | Adjust internal and external spacing |
| **Typography** | Font, size, weight, color, line-height | Control text appearance |
| **Shadow** | Box shadow properties | Add depth with shadow effects |

## Enabling and Disabling Option Groups

### In the Visual Builder

1. Open an element's settings (e.g., a module like Text, Button, or Card)
2. Navigate to the **Design** tab
3. Look for sub-element option groups listed below the main design controls (e.g., Title Text, Button, Image)
4. Hover over a sub-element name to reveal the **Toggle Options** icon (three dots or gear icon)
5. Click **Toggle Options** to open the list of available design groups for that sub-element
6. Check or uncheck the groups you want to expose:
   - **Enable**: checkbox is checked (design options appear for editors)
   - **Disable**: checkbox is unchecked (design options are hidden, default values apply)
7. Changes apply immediately as you toggle

### Common Patterns

**Button Sub-Element with Sizing & Transform**

```
Button
├── ☑ Sizing (Width, height)
├── ☑ Transform (Rotate, scale)
├── ☐ Background (disabled)
└── ☐ Animation (disabled)
```

This limits editors to size and rotate the button without accidentally changing its background color.

**Title Text with Typography & Animation**

```
Title Text
├── ☑ Typography (Font, size, weight, color)
├── ☑ Animation (Entrance effects)
├── ☐ Sizing (disabled)
└── ☐ Transform (disabled)
```

This lets editors style the title appearance and add motion, but prevents accidental resizing.

**Image Sub-Element with Full Design Control**

```
Image
├── ☑ Sizing
├── ☑ Border
├── ☑ Background
├── ☑ Transform
├── ☑ Animation
└── ☑ Shadow
```

For images, you might expose all groups to give maximum flexibility.

## Creating Presets with Composable Settings

Once you've configured option groups on a sub-element, you can save that configuration as a preset:

1. Style the element and its sub-elements as desired
2. In the **Design** tab, locate the **Presets** dropdown (usually at the top)
3. Click **Create Preset** or select from existing presets
4. Name your preset (e.g., "Styled Button with Animation")
5. Save

Other team members can now apply the same preset, and it will:

- Apply all saved styling values
- Enforce the same option group configuration (enabled/disabled)
- Maintain design system consistency across your site

## Why Composable Settings Matter

### Design System Consistency

Composable settings help enforce design patterns. By enabling only relevant options, you guide editors toward consistent decisions and prevent style sprawl.

### Cleaner Interface

Fewer visible options = less cognitive load. Editors see only the controls they need, not an overwhelming list of unused settings.

### Flexible Modularity

You can reuse elements across your site with different option group configurations. For example:

- **Blog post header**: Title + Image with Animation enabled
- **Sidebar component**: Title + Image with Animation disabled (performance)
- **Modal dialog**: Title + Image with full Transform options

### Learning Curve

New team members benefit from a curated set of options rather than having to learn every possible setting.

## Common Use Cases

### Hero Section with Text Overlay

```
Hero Image
├── ☑ Sizing (full width/height)
├── ☑ Background (optional overlay)
└── ☐ Transform (disabled to prevent skew)

Overlay Text
├── ☑ Typography
├── ☑ Sizing (constrain width)
└── ☑ Animation (fade in on load)
```

### Product Card Grid

```
Product Card
├── Title
│   ├── ☑ Typography
│   ├── ☑ Animation
│   └── ☐ Sizing (locked)
│
├── Image
│   ├── ☑ Sizing
│   ├── ☑ Transform (hover effects)
│   └── ☐ Animation (use card-level animation instead)
│
└── Price
    ├── ☑ Typography
    ├── ☑ Border
    └── ☐ Transform
```

### Form Input with Label

```
Input Field
├── Label
│   ├── ☑ Typography
│   └── ☐ Sizing
│
└── Input Box
    ├── ☑ Sizing (width)
    ├── ☑ Border (focus state)
    └── ☑ Background
```

## Troubleshooting

!!! warning "Toggle Options Not Visible"
    **Cause:** The element or sub-element doesn't support composable settings.
    
    **Solution:** Not all elements in Divi 5 support option groups. This is primarily available on modules with multiple styled sub-components. Try a different element type.

!!! warning "Changes Not Saving to Preset"
    **Cause:** Option group configuration is not persisted when overwriting a preset.
    
    **Solution:** Create a new preset with a different name rather than overwriting. Option group state is stored with the preset when first created.

!!! warning "Option Groups Not Appearing in Design Tab"
    **Cause:** The element may not have configurable sub-elements, or the theme hasn't loaded composable settings support.
    
    **Solution:** Check that you're on Divi 5.0 or later. Refresh the builder and try a different module.

## Version Notes

!!! note "Divi 5 Only"
    Composable settings are a Divi 5 feature. Divi 4 does not support per-sub-element option group configuration. This page documents Divi 5 behavior exclusively.

## Elegant Themes Tutorials

Long-form **Divi Resources** posts complement the Help Center documentation for this feature:

- [Everything You Need To Know About Composable Settings In Divi 5](https://www.elegantthemes.com/blog/divi-resources/everything-you-need-to-know-about-composable-settings-in-divi-5){:target="_blank"} — Deep dive into enabling design groups on sub-elements and building design systems (April 2026).

*Maintainers:* also list new posts in [`planning/et-blog-tutorials-map.md`](https://github.com/16wells/divi-docs/blob/main/planning/et-blog-tutorials-map.md){:target="_blank"}.

## Related

- [Advanced Styling Using Option Group Presets in Divi 5](../builder/advanced-styling-using-option-group-presets-in-divi-5.md)
- [Element Presets](../builder/element-presets.md)
- [Understanding Divi 5 Design Options](../builder/composable-settings-in-divi-5.md)
- [Getting Started with Divi 5 Theme Builder](../builder/getting-started-with-divi-5-theme-builder.md)
