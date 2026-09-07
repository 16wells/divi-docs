---
title: "How to Display the Product's Gallery Images as a Carousel"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/4629929-how-to-display-the-product-s-gallery-images-as-a-carousel"
---

# How to Display the Product's Gallery Images as a Carousel

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/4629929-how-to-display-the-product-s-gallery-images-as-a-carousel).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Gear icon |  | Woo Product Images module's settings by clicking on theGear icon |
| Advanced Tab → Custom CSS → Free Form CSS |  | m CSSand add this CSS code.woocommerce #page-container div.product selector div.images .flex-control-thumbs .slick-slide,.woocommerce #page-container div.product selector div.images .flex-control-thumbs .slick-dots li {clear: none !important;margin: 0;}selector .flex-control-thumbs .slick-slide img {width: auto !important;margin: 0 auto !important;}selector .flex-control-thumbs {position: relative;}selector .flex-control-thumbs span.slick-prev,selector .flex-control-thumbs span.slick-next {position: absolute;top: 25%;left: 0;transform: translateY(-50%);background: #000;width: 40px;height: 40px;line-height: 40px;text-align: center;color: #fff;z-index: 99;cursor: pointer;}selector .flex-control-thumbs span.slick-next {left: auto;right: 0;}selector .flex-control-thumbs .slick-list.draggable {max-width: 90%;margin: 0 auto;}.woocommerce div.product selector div.images .flex-control-thumbs .slick-dots {text-align: center;clear: both;margin-top: 15px;}.woocommerce #page-container div.product selector div.images .flex-control-thumbs .slick-dots li {position: relative;display: inline-block;width: 20px;height: 20px;margin: 0 5px;padding: 0;cursor: pointer;float: none;}selector .flex-control-thumbs .slick-dots li button {font-size: 0;line-height: 0;display: block;width: 20px;height: 20px;padding: 5px;cursor: pointer;color: transparent;border: 0;outline: none;background: transparent;}selector .flex-control-thumbs .slick-dots li button:before {content: '•';font-size: 22px;line-height: 20px;position: absolute;top: 0;left: 0;width: 20px;height: 20px;text-align: center;opacity: .25;color: black;}@media only screen and (max-width: 767px) {selector .flex-control-thumbs span.slick-prev,selector .flex-control-thumbs span.slick-next {display: none !important;}selector .flex-control-thumbs .slick-list.draggable {max-width: 100%;}} |
| Advanced Tab → CSS ID & Classes → CSS Class, |  | Class,type indt_woo_gallery |
| WordPress Dashboard → Divi → Theme Options → Integrations Tab, |  | s Tab,add this code:<link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/[email protected]/slick/slick.css" /><script async src="//cdn.jsdelivr.net/npm/[email protected]/slick/slick.min.js"></script><script>jQuery(document).ready(function ($) {setTimeout(function () {jQuery('.dt_woo_gallery .flex-control-thumbs').slick({slidesToShow: 3,slidesToScroll: 3,arrows: true,prevArrow: '<span style="font-size:35px;" class="slick-prev et-pb-icon">&#x34;</span>',nextArrow: '<span style="font-size:35px;" class="slick-next et-pb-icon">&#x35;</span>',dots: true});}, 500);});</script> |
| Product Gallery Slider, Additional Variation Images for WooCommerce |  | n Images for WooCommerceplugin |
| WordPress Dashboard → Codeixer → Product Gallery |  | llery |
| Advanced Options |  | nced OptionsTab |
| Divi Page Builder |  | ge Builderoption |
| Save |  | k on theSavebutton |

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
