---
title: "How to Create and Use the "Ken Burns Effect" in Divi"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/2717227-how-to-create-and-use-the-ken-burns-effect-in-divi"
---

# How to Create and Use the "Ken Burns Effect" in Divi

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/2717227-how-to-create-and-use-the-ken-burns-effect-in-divi).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Fullwidth Section |  | ction |
| Fullwidth Header |  | Headermodule |
| Background option → Background Image |  | und Imageand set the desired image |
| Use Parallax Effect |  | lax Effectoption |
| Design Tab → Layout |  | ayoutand enable theMake Fullscreenoption |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand use one of the following CSS classes:kb-zoomin– zooms in on the image​kb-zoomout– zooms out from the imagekb-zoomin-right– zooms in and pans right on the imagekb-zoomout-right– zooms out and pans right on the image |
| kb-zoomin |  | zooms in on the image |
| kb-zoomout |  | t– zooms out from the image |
| kb-zoomin-right |  | zooms in and pans right on the image |
| kb-zoomout-right |  | zooms out and pans right on the image |
| Divi → Theme Options → General Tab → Custom CSS |  | m CSSand add this CSS code:.kb-zoomout .et_pb_slide .et_parallax_bg {animation: zoomout 7s forwards;-ms-animation: zoomout 7s forwards;-webkit-animation: zoomout 7s forwards;-0-animation: zoomout 7s forwards;-moz-animation: zoomout 7s forwards;}.kb-zoomin .et_pb_slide .et_parallax_bg {animation: zoomin 7s forwards;-ms-animation: zoomin 7s forwards;-webkit-animation: zoomin 7s forwards;-0-animation: zoomin 7s forwards;-moz-animation: zoomin 7s forwards;}.kb-zoomin-right .et_pb_slide .et_parallax_bg {animation: zoomin-right 7s forwards;-ms-animation: zoomin-right 7s forwards;-webkit-animation: zoomin-right 7s forwards;-0-animation: zoomin-right 7s forwards;-moz-animation: zoomin-right 7s forwards;}.kb-zoomout-right .et_pb_slide .et_parallax_bg {animation: zoomout-right 7s forwards;-ms-animation: zoomout-right 7s forwards;-webkit-animation: zoomout-right 7s forwards;-0-animation: zoomout-right 7s forwards;-moz-animation: zoomout-right 7s forwards;}.kb-zoomout .et_parallax_bg {animation: zoomout 17s forwards;-ms-animation: zoomout 17s forwards;-webkit-animation: zoomout 17s forwards;-0-animation: zoomout 17s forwards;-moz-animation: zoomout 17s forwards;}.kb-zoomin .et_parallax_bg {animation: zoomin 17s forwards;-ms-animation: zoomin 17s forwards;-webkit-animation: zoomin 17s forwards;-0-animation: zoomin 17s forwards;-moz-animation: zoomin 17s forwards;}.kb-zoomin-right .et_parallax_bg {animation: zoomin-right 7s forwards;-ms-animation: zoomin-right 17s forwards;-webkit-animation: zoomin-right 17s forwards;-0-animation: zoomin-right 17s forwards;-moz-animation: zoomin-right 17s forwards;}.kb-zoomout-right .et_parallax_bg {animation: zoomout-right 7s forwards;-ms-animation: zoomout-right 17s forwards;-webkit-animation: zoomout-right 17s forwards;-0-animation: zoomout-right 17s forwards;-moz-animation: zoomout-right 17s forwards;}@keyframes zoomout {0% {-ms-transform: scale3d(1.5, 1.5, 1.5) translate3d(-0px, 0px, 0px);-webkit-transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);-o-transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);-moz-transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);animation-timing-function: linear;}100% {-ms-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-webkit-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-o-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-moz-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);}}@keyframes zoomin {0% {-ms-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-webkit-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-o-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-moz-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);animation-timing-function: linear;}100% {-ms-transform: scale3d(1.5, 1.5, 1.5) translate3d(-0px, 0px, 0px);-webkit-transform: scale3d(3.5, 3.5, 3.5) translate3d(0px, 0px, 0px);-o-transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);-moz-transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);transform: scale3d(1.5, 1.5, 1.5) translate3d(0px, 0px, 0px);}}@keyframes zoomout-right {0% {-ms-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);-webkit-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);-o-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);-moz-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);animation-timing-function: linear;}100% {-ms-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-webkit-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-o-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-moz-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);}}@keyframes zoomin-right {0% {-ms-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-webkit-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-o-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);-moz-transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);transform: scale3d(1.1, 1.1, 1.1) translate3d(0px, 0px, 0px);animation-timing-function: linear;}100% {-ms-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);-webkit-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);-o-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);-moz-transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);transform: scale3d(1.5, 1.5, 1.5) translate3d(-150px, -20px, 0px);}} |

## Code Examples

<!-- TODO: Add CSS/PHP code examples -->

## Common Patterns

<!-- TODO: Document 2-3 common usage patterns -->

## Troubleshooting

<!-- TODO: Document common issues and solutions -->

## AI Interaction Notes

| Task | Confidence | Notes |
|------|-----------|-------|
| Basic placement | 🔬 Needs Testing | Untested — stub page |
| Settings configuration | 🔬 Needs Testing | Untested — stub page |
| Custom styling | 🔬 Needs Testing | Untested — stub page |

## Related

<!-- TODO: Add links to related documentation pages -->
