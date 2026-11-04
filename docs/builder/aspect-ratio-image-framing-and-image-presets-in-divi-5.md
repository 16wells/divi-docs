---
title: "Aspect Ratio, Image Framing, and Image Presets in Divi 5"
description: "How to set an aspect ratio, control image fit and position with Framing, and save image presets for any Divi 5 module that shows an image."
category: builder
tags: ["builder", "images", "aspect-ratio", "presets"]
related: ["image", "gallery", "the-instagram-feed-module-in-divi-5"]
divi_version: "5.5+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15066231-aspect-ratio-image-framing-and-image-presets-in-divi-5"
---

# Aspect Ratio, Image Framing, and Image Presets in Divi 5

!!! abstract "Quick Reference"
    **What it is:** Three related image tools: an Aspect Ratio field in Sizing, a Framing group (Object Fit and Object Position), and preset support for the Image option group.
    **Where to find it:** Aspect Ratio in **Design → Sizing**; Framing in **Design → Framing** (Image, Woo Product Images) or **Design → Image → Framing** (Person, Blurb); presets via the preset chip at the top of the Image option group.
    **Key behavior:** Object Fit only shows an effect when the image's rendered size differs from its natural size, so set an aspect ratio or a custom width and height first.

Image option groups are now consistent across Divi 5 modules, so the same controls sit in the same place wherever an image appears. The Image, Person, Blurb, and Woo Product Images modules are the main examples, but the changes apply to every module that displays an image.

## Aspect Ratio

Aspect Ratio ties an element's height to its width. Set it once and Divi keeps the proportion as the element scales across phone, tablet, and desktop.

1. Open the module settings and go to **Design → Sizing**.
2. Find the **Aspect Ratio** field.
3. Enter a ratio as W:H, for example `16:9`, `1:1`, or `4:5`.
4. Save.

The height is calculated from the element's rendered width, so when a parent container narrows on smaller screens the height adjusts automatically.

| Ratio | Typical use |
|---|---|
| 16:9 | Widescreen video, hero images, video-style thumbnails |
| 4:3 | Classic photo prints and slideshow images |
| 1:1 | Square gallery images, social cards, avatar-style cards |
| 3:4 or 4:5 | Portrait product photos and team headshots |
| 21:9 | Cinematic banners |

## Framing

If an image has an aspect ratio, or an explicit width and height, it stretches to fill that frame by default, which can distort it. The **Framing** group decides how the image fills the frame and where it sits inside it.

### Object Fit

| Value | Behavior |
|---|---|
| Fill (default) | Stretches the image to the frame; may distort it |
| Contain | Shows the whole image inside the frame; may leave empty space on two sides |
| Cover | Fills the frame completely and crops what does not fit, keeping proportions |
| None | Shows the image at its natural size with no scaling |
| Scale Down | Acts like None for images smaller than the frame and like Contain for larger ones |

### Object Position

Object Position picks which part of the image stays visible when Object Fit crops it. Use the position selector to anchor to a corner, edge, or the center, or enter custom X and Y percentage values. The nine presets are Top Left, Top Center, Top Right, Center Left, Center, Center Right, Bottom Left, Bottom Center, and Bottom Right.

### Where Framing lives

- **Image module:** Design → Framing
- **Person module:** Design → Image → Framing
- **Blurb module** (image instead of icon): Design → Image → Framing
- **Woo Product Images module:** Design → Framing

## Image presets

The Image option group supports presets, like Button, Text, and other option groups. Style an image once (corners, border, shadow, filters, framing) and reuse that preset on every image on the site.

**Create a preset**

1. Open a module that displays an image.
2. Go to **Design → Image** (or **Design → Image & Icon** in modules that use that group).
3. Style the image as you want it.
4. Click the preset chip at the top of the Image option group.
5. Choose **Save As Preset** and give it a descriptive name, such as "Brand Card Image".

**Apply a preset:** open a module with an image, go to **Design → Image**, click the preset chip, and pick the preset.

**Update or reset**

- **Update:** change the image styles in a module that uses the preset, click the chip, and choose **Update Preset**. Every image using it updates.
- **Reset:** choose **Reset** from the chip to detach the current module from the preset without altering the preset.

All image option groups also support composable settings, so any sub-element of a module, including its image, can use the full design option set without custom CSS.

## Tips

- Pair Aspect Ratio with Object Fit **Cover** when contributors upload images of different sizes; the images crop cleanly instead of stretching.
- Save a site-wide image preset early to keep brand styling consistent.
- Set framing inside a Loop Builder template so every loop item shares the same ratio and crop.
- Anchor headshots to **Top Center** with Object Position so heads are not trimmed.

## FAQ

**I set Object Fit but nothing changed.** Object Fit only has a visible effect when the rendered size differs from the natural size. Set an Aspect Ratio, or both a custom Width and Height in Sizing.

**Will an Aspect Ratio crop my image?** Not by itself. It sets the frame; Object Fit decides whether the image is cropped (Cover), letterboxed (Contain), or stretched (Fill).

**Does this apply to WooCommerce product images?** Yes. The Woo Product Images module uses the same harmonized Image group and the Framing group.

**Where do I edit a saved image preset?** Update it from any module that uses it, or manage it in the Preset Manager.

## Official documentation

[Aspect Ratio, Image Framing, and Image Presets in Divi 5](https://help.elegantthemes.com/en/articles/15066231-aspect-ratio-image-framing-and-image-presets-in-divi-5){:target="_blank"}
