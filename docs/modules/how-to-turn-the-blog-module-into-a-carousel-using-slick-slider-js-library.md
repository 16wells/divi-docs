---
title: "How to Turn the Blog Module Into a Carousel Using Slick Slider JS Library"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8564516-how-to-turn-the-blog-module-into-a-carousel-using-slick-slider-js-library"
---

# How to Turn the Blog Module Into a Carousel Using Slick Slider JS Library

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8564516-how-to-turn-the-blog-module-into-a-carousel-using-slick-slider-js-library).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Blog module's |  | module'ssettings, go toContent Tab → Elements,and deactivate the Pagination. |
| Design Tab → Layout |  | ayoutand chooseFullwidth. |
| Advanced Tab → CSS ID & Classes → CSS Class |  | Classand type in:divi_blog_slick_slider. |
| Advanced Tab |  | d Tab→Custom CSS→Free Form CSSand paste in this CSS snippet:selector .et_pb_post {border: 1px solid #dddddd;margin: 10px;padding: 20px;}selector .et_pb_post .entry-featured-image-url {margin: -20px -20px 20px -20px;}selector .slick-prev:before,selector .slick-next:before {color: #6c2fb9;}selector .slick-dots li button:before {color: #6c2fb9;} |
| Divi → Theme Option → Integration tab > Header |  | n → Integration tab > Header:<script type="text/javascript" src="//cdn.jsdelivr.net/npm/[email protected]/slick/slick.min.js"></script><link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/[email protected]/slick/slick.css"/><link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/[email protected]/slick/slick-theme.css"/><script id="divi-blog-module-slick-slider-carousel">(function ($) {$(document).ready(function () {if ($('.divi_blog_slick_slider').length) {$('.divi_blog_slick_slider .et_pb_ajax_pagination_container').slick({dots: true,arrows: true,infinite: false,speed: 300,slidesToShow: 4,slidesToScroll: 4,responsive: [{breakpoint: 1024,settings: {slidesToShow: 3,slidesToScroll: 3,infinite: true,dots: true,},},{breakpoint: 600,settings: {slidesToShow: 2,slidesToScroll: 2,},},{breakpoint: 480,settings: {slidesToShow: 1,slidesToScroll: 1,},},],});}});})(jQuery);</script> |
| starting guide for the Slick Slider JS Library |  | er JS Libraryto learn how it can be customized further. |
| Post Count |  | all the published posts, set thePost Countoption to-1inBlog Module settings → Content Tab → Post Count |

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
