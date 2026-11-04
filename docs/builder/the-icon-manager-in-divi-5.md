---
title: "The Icon Manager in Divi 5"
description: "The Divi 5 Icon Manager and compact icon picker: collections, SVG and icon font import, default collection, and import/export."
category: builder
tags: [builder, icons]
related: []
divi_version: "5.17+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/17693045-the-icon-manager-in-divi-5"
---

# The Icon Manager in Divi 5

!!! abstract "Quick Reference"
    **Introduced in:** Divi 5.17 (2026-10-22).
    **What it is:** A site-wide manager for icons, plus a compact icon picker used by every module with an icon setting.
    **Built-in collections:** Divi Icons and Font Awesome (cannot be deleted). Some plugins add read-only collections.
    **Import:** SVG files, or one icon font (WOFF2, WOFF, TTF, OTF). No ZIP files; no extra SVG-upload plugin needed.
    **Open it:** the **Icon Manager** button at the bottom of the icon picker menu.

## The icon picker

The picker is used by modules such as Icon, Blurb, Icon List, Accordion, Timeline, Image, Gallery, Portfolio, Blog, Menu, Group Carousel, Fullwidth Header, and Fullwidth Image, and by every Button's icon setting. The setting shows a small preview (hover for name and collection).

1. Click the preview (or the Plus icon if none is set).
2. Choose a collection from the dropdown (**All Collections**, **Theme Icons**, **Custom Icons**, or a **Styles** filter such as Solid or Line) or use **Search Icons...**.
3. Click an icon; the menu closes. Arrow keys move through the grid; Home and End jump to first and last.

The picker opens on the collection of the selected icon, or on your default collection.

## Managing collections

The Icon Manager window can be dragged, resized, and expanded.

| Control | Purpose |
|---|---|
| Search icons... | Searches all collections by icon name, search terms, or collection name |
| New Collection | Creates an empty collection (name it, then **Create**) |
| Import Icons | Adds SVGs or an icon font to a collection |
| Import & Export Icon Collections | Moves collections between sites |
| Per collection: Rename, Reset, Make Default, Delete | Delete only on collections you created; Reset restores removed icons without removing added ones |
| Toggle switch | Hides or shows the collection in pickers site-wide; a hidden collection cannot be the default |

**Importing:** click **Import Icons**, choose files (SVGs or one font, not both), optionally add a Name Mapping File for fonts, pick the target **Collection** (or create one), and click **Import**. Files are saved to the Media Library; SVGs are sanitized on upload and named after their file. SVG icons take the module's icon color, so multi-color SVGs render in one color.

**Selecting icons:** click to select; Shift, Cmd, or Ctrl-click for several in one collection. Actions (buttons or right-click): **Insert** (one icon, when opened from a picker), **Remove**, **Move**.

## Export and import

Use the Import & Export icon in the window header. Export lets you choose collections (all by default) and includes the icon files; Import adds collections alongside existing ones without removing anything.

## Safety and permissions

- Icons already used on pages keep displaying after you remove icons or hide or delete a collection. Original files stay in the Media Library. Divi asks for confirmation first.
- Anyone who can edit pages can browse and insert icons. Creating, importing, renaming, moving, removing, and deleting needs an Administrator (or a role that can manage theme options and upload files). Import/export also needs the Role Editor portability permission.
- Changes are site-wide. If two people edit at once, Divi may prompt **Reload Library**.
