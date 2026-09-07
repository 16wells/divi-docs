---
title: "How to Make a Masonry Blog Layout Using the Isotope JS Library"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8560603-how-to-make-a-masonry-blog-layout-using-the-isotope-js-library"
---

# How to Make a Masonry Blog Layout Using the Isotope JS Library

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8560603-how-to-make-a-masonry-blog-layout-using-the-isotope-js-library).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Blog module |  | moduleto the Page |
| Design Tab → Layout |  | e's settings and go toDesign Tab → Layout |
| Fullwidth |  | lwidth |
| Advanced Tab → CSS ID & Classes → CSS Class |  | ss, type indivi_isotope_blog |
| Blog module's |  | dule's→Advanced Tab→Custom CSS→Free Form CSS, add this CSS code:selector {--space-between-each-post: 20px;}selector .et_pb_post {width: calc((100% / 3) - 20px);margin-bottom: 20px;border: 1px solid #d8d8d8;padding: 20px;}selector .et_pb_post .entry-featured-image-url {margin: -20px -20px 30px -20px;}@media (max-width: 980px) and (min-width: 768px) {selector .et_pb_post {width: calc((100% / 2) - 20px);}}@media (max-width: 767px) {selector .et_pb_post {width: calc(100% - 20px);}} |
| Divi → Theme Option → Integration tab > Header |  | er, add this Js Code:<script src="https://unpkg.com/isotope-layout@3/dist/isotope.pkgd.min.js"></script><script id="masonry-blog-layout">(function ($) {$(document).ready(function () {var gutter = Number($('.divi_isotope_blog').css('--space-between-each-post').replace('px', ''));function initIsotope() {var $container = $('.divi_isotope_blog .et_pb_ajax_pagination_container');// Check if Isotope has already been initializedif (!$container.data('isotope-initialized')) {$container.isotope({itemSelector: '.divi_isotope_blog .et_pb_post',percentPosition: true,masonry: {gutter: gutter,columnWidth: '.divi_isotope_blog .et_pb_post'},});// Set a flag to indicate that Isotope has been initialized$container.data('isotope-initialized', true);} else {// If already initialized, just reload Isotope$container.isotope('layout');}var wrapperHeight = $container.css('height');$('.et_pb_ajax_pagination_container > div').css({ 'top': wrapperHeight, 'position': 'relative' });}initIsotope();$(document).ajaxComplete(function () {setTimeout(initIsotope, 250);});});})(jQuery);</script> |

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
