---
title: "How to Stop Background Video at the Last Frame in Divi 5"
description: "Make a Divi 5 background video play once and freeze on its final frame using a custom class and a short head script."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15374106-how-to-stop-background-video-at-the-last-frame-in-divi-5"
---

# How to Stop Background Video at the Last Frame in Divi 5

!!! abstract "Quick Reference"
    **Goal:** The background video plays once and holds on its last frame instead of looping.
    **Two parts:** A `stop_bg_video` class on the element, plus a script added once in Theme Options.
    **Works on:** Any element with a background video (section, row, column, or module).

## Before you begin

The element must already have a background video, set in the **Background** option group on the **Content** tab using the **Video** background type.

## Step 1: Add a class to the element

Divi 5 attaches custom classes through the **Attributes** option group.

1. Open the settings of the element with the background video.
2. On the **Advanced** tab, open **Attributes**.
3. Click **+ Add Attribute** and choose **class**.
4. Set **Target Element** to the module (the usual choice).
5. Enter `stop_bg_video` as the **Attribute Value**.

The class alone does nothing; it is a hook for the script. You can reuse it on as many elements as you like.

## Step 2: Add the script

Add this once; it applies site-wide to every element carrying the class.

1. Go to **Divi > Theme Options > Integrations**.
2. Paste the script into the **Head** code field.
3. Save.

```html
<script>
(function ($) {
  $(document).ready(function () {
    $('.stop_bg_video video').each(function () {
      var video = this;
      video.removeAttribute('loop');
      video.addEventListener('loadedmetadata', function () {
        var pause_at = video.duration - 0.5;
        video.addEventListener('playing', function () {
          var interval = setInterval(function () {
            if (video.currentTime >= pause_at) {
              video.pause();
              clearInterval(interval);
            }
          }, 150);
        }, false);
      });
    });
    setTimeout(function () {
      $(window).trigger('resize');
    }, 500);
  });
})(jQuery);
</script>
```

## Result

Reload the front end. The video plays through once and holds on its final frame. To apply it elsewhere, add the same class to another element; no extra script is needed.

## Official documentation

[How to Stop Background Video at the Last Frame in Divi 5](https://help.elegantthemes.com/en/articles/15374106-how-to-stop-background-video-at-the-last-frame-in-divi-5)
