---
title: "How to Create a Full-Screen Slider in Divi 5"
description: "Build a slider that fills the viewport by combining a full-width row, slide background images, and a Min Height of 100vh or a calc() expression."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15379916-how-to-create-a-full-screen-slider-in-divi-5"
---

# How to Create a Full-Screen Slider in Divi 5

!!! abstract "Quick Reference"
    **Goal:** A Slider module that fills the visitor's screen, with no custom code.
    **Key setting:** Slider > Design > Sizing > **Min Height** = `100vh` (or `calc(100vh - 80px)` below a fixed header).
    **Also needed:** Section vertical padding at 0, Row Width and Max Width at 100%, and a background image on every slide.

Divi 5's Sizing options accept viewport units and math functions, so the full-screen height can be set directly in the Visual Builder.

## Before you begin

- Divi 5 installed and activated.
- A few large background images ready. Roughly 1920px by 1500px keeps them sharp on big screens.

## Step 1: Add the Slider module

1. In the Visual Builder, click the **Green Plus** icon in the automatically created Section to add a one-column Row.
2. Click the **Gray Plus** icon in the Row to open the module list.
3. Click the **Slider** module (or search for it).

## Step 2: Remove the Section's vertical padding

1. Open the Section settings (click it or use the **Gear** icon).
2. Go to **Design > Spacing**.
3. Set **Top** and **Bottom** padding to `0`.

## Step 3: Make the Row full width

1. Open the settings of the Row that holds the Slider.
2. Go to **Design > Sizing**.
3. Set both **Width** and **Max Width** to `100%`.

## Step 4: Add a background image to each slide

1. Open the Slider settings with the **Gear** icon.
2. On the **Content** tab, open a slide or click **Add New Slide**.
3. In the slide's **Background** option group, add your image.
4. Repeat for each slide.

!!! tip
    Use images of similar size and orientation so the slider height stays steady as slides rotate.

## Step 5: Set the height with Sizing

1. Open the Slider settings and go to **Design > Sizing**.
2. In **Min Height**, enter `100vh`. One `vh` is one percent of the screen height, so `100vh` fills the viewport.

If a fixed header sits on top of the page, subtract its height with `calc()`:

```text
calc(100vh - 80px)
```

Replace `80px` with your header's real height. To enter a function, click the unit label beside the **Min Height** field, choose the function option, then type the expression. See [Advanced Units, CSS Functions, and Variables for Divi 5](https://help.elegantthemes.com/en/articles/10823890-advanced-units-css-functions-and-variables-for-divi-5).

Sizing fields accept `px`, `%`, `em`, `rem`, `vw`, `vh`, and more, plus the `calc`, `min`, and `max` functions. Prefer `vh` or `calc()` over fixed pixels so the slider stays full screen on every device.

## Finish up

Style slide titles, body text, and buttons on the **Design** tab, and preview phone, tablet, and desktop to check the height on each.

## Official documentation

[How to Create a Full-Screen Slider in Divi 5](https://help.elegantthemes.com/en/articles/15379916-how-to-create-a-full-screen-slider-in-divi-5)
