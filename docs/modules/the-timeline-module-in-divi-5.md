---
title: "The Timeline Module in Divi 5"
category: modules
tags: ["modules", "timeline", "animation", "loop"]
related: ["post-content", "blog"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/15162149-the-timeline-module-in-divi-5"
status: stub
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# The Timeline Module in Divi 5

The Divi 5 **Timeline Module** creates animated, vertically (or horizontally) flowing timelines of events. It is loop-aware, so each timeline entry can be generated from a post, custom post type, or other dynamic source.

## Overview

<!-- TODO: Expand from ET help article 15162149 once network access permits a full scrape. -->

This module was introduced as part of the **Five New Modules for Divi 5** release (Timeline, Breadcrumbs, Table of Contents, SVG, Instagram Feed). Per the announcement, the Timeline module is designed to work well inside loops, making it suitable for date-based content such as company history, release changelogs, or résumés generated from a CPT.

![Timeline module overview](../assets/screenshots/modules/timeline/overview.png){ loading=lazy }
*Caption: Placeholder — capture once a working install is available.*

## Settings & Options

<!-- TODO: Build complete Content / Design / Advanced settings tables from the ET help article and a live install. -->

### Content Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO --> | | | |
| Add, edit, and remove |  | add new Timeline Items, edit them, duplicate them, or delete them. Covered in detail below. <!-- AUTO-ADDED --> |
| Link |  | make the entire Timeline module clickable, directing users to another page, section, or external URL. <!-- AUTO-ADDED --> |
| Background |  | choose the Timeline module's background styles. <!-- AUTO-ADDED --> |
| Loop |  | enables the loop builder so the timeline can pull events from a dynamic data source. <!-- AUTO-ADDED --> |
| Order |  | choose where the Timeline module appears inside a Flexbox or Grid layout. <!-- AUTO-ADDED --> |
| Meta |  | choose the Timeline module's label text and force its visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <!-- TODO --> | | | |
| Timeline |  | choose the Timeline module's overall layout, including the alternating-sides toggle that drives the Even-variant styling. <!-- AUTO-ADDED --> |
| Track |  | choose the styling for the connecting line that runs through the timeline, including color, weight, and spacing. <!-- AUTO-ADDED --> |
| Item |  | choose the Timeline module's item wrapper styles. Includes Even-variant options to style every second item differently. <!-- AUTO-ADDED --> |
| Spacer |  | choose the gap between items along the track. Includes Even-variant options. <!-- AUTO-ADDED --> |
| Connector |  | choose the styling for the short line that joins each marker out to its card. <!-- AUTO-ADDED --> |
| Marker |  | choose the dot, icon, or shape that sits on the track at each event. <!-- AUTO-ADDED --> |
| Card |  | choose the Timeline module's card styles, the block that holds each event's date, title, and body text. Includes Even-variant options for alternating-side designs. <!-- AUTO-ADDED --> |
| Date Text |  | choose the typography for the date label on each event. Includes Even-variant options. <!-- AUTO-ADDED --> |
| Title Text |  | choose the Timeline module's title text styles. Includes Even-variant options. <!-- AUTO-ADDED --> |
| Body Text |  | choose the Timeline module's body text styles. Includes Even-variant options. <!-- AUTO-ADDED --> |
| Sizing |  | choose the Timeline module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | choose the Timeline module's spacing. <!-- AUTO-ADDED --> |
| Border |  | choose the Timeline module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | choose the Timeline module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | choose the Timeline module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | choose the Timeline module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | choose the Timeline module's animation styles, adding personality and interactivity while keeping a polished, professional feel. <!-- AUTO-ADDED --> |

### Advanced Tab

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| CSS ID | text | none | Custom HTML id attribute |
| CSS Class | text | none | Custom CSS class(es) |
| Custom CSS | code | none | Target specific elements within the module |
| Attributes |  | assign a CSS ID, reusable classes, or custom HTML attributes. <!-- AUTO-ADDED --> |
| CSS |  | add custom CSS for fine-grained styling. <!-- AUTO-ADDED --> |
| HTML |  | choose the semantic HTML tag for the module wrapper. <!-- AUTO-ADDED --> |
| Conditions |  | show or hide the module based on dynamic conditions. <!-- AUTO-ADDED --> |
| Interactions |  | trigger actions on the module from elsewhere on the page. <!-- AUTO-ADDED --> |
| Visibility |  | control which devices the module displays on. <!-- AUTO-ADDED --> |
| Transitions |  | set the duration and easing for hover and state changes. <!-- AUTO-ADDED --> |
| Position |  | pin the module relative to its parent. <!-- AUTO-ADDED --> |
| Scroll Effects |  | animate the module as the visitor scrolls past it. <!-- AUTO-ADDED --> |
| Add New Timeline Item |  | Add New Timeline Itemin the Content tab. Fill in the date, title, and body, then style it as needed. <!-- AUTO-ADDED --> |
| Card |  | he sameCardoption group, switch to the Even sub-options and set the card to align to the right of the track. [VERIFY: confirm the exact option label that controls the card side and how even sub-options are surfaced in the UI.] <!-- AUTO-ADDED --> |
| Item |  | at the same odd/even pairing inside theItemandSpacergroups to fine-tune the offset and gap on each side. <!-- AUTO-ADDED --> |
| Item Content |  | the date, title, and body fields for this specific event. <!-- AUTO-ADDED --> |
| Spacer |  | ,Connector,Marker,Card- per-item overrides of the structural design. <!-- AUTO-ADDED --> |
| Date Text |  | ,Title Text,Body Text- per-item typography overrides. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Elegant Themes tutorials

- [Five New Modules for Divi 5 (Timeline, Breadcrumbs, Table of Contents, SVG, Instagram Feed)](https://www.elegantthemes.com/blog/theme-releases/five-new-modules){:target="_blank"} — release announcement covering all five modules; the Timeline module is highlighted as loop-friendly.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Related

- [Blog Module](blog.md)
- [Post Content Module](post-content.md)
