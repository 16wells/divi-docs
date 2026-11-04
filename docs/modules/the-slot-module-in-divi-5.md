---
title: "The Slot Module in Divi 5"
description: "The Divi 5 Slot module: per-page content areas inside a component, behavior rules, use cases, and settings."
category: modules
tags: [modules, components, slots]
related: []
divi_version: "5.15+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/17438196-the-slot-module-in-divi-5"
---

# The Slot Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A module placed inside a [component](../builder/components.md) that marks an area each page fills with its own content.
    **Where it lives:** Add it from the module list (next to the Group module) via the Gray Plus icon inside a component's column or Group.
    **Key behavior:** Slot content is saved with the page, not the component, so editing the component never overwrites it.

## How it works

1. Add the Slot to the component once; it becomes part of the shared component in the same position everywhere.
2. On each page using the component, click the Gray Plus icon inside the Slot and add modules.
3. Keep editing the component as usual; each page's Slot content is left alone.

## Behavior rules

- **Empty Slots render nothing** on the front end.
- Content can be dragged from the page into a Slot or out to the page, but not into the shared part of the component.
- **Duplicating a Slot** while editing the component gives an empty Slot.
- **Components inside a Slot** stay linked to their own originals.
- **Deleting a Slot** from the component removes its content everywhere it was used.

## Use cases

- **Shared card, different content:** a styled card component with a Slot; each page supplies its image, text, and buttons.
- **Hero with a page-specific message:** shared background and layout, Slot for headline and buttons.
- **Call-to-action band:** shared heading, Slot below for a signup form on one page and a contact button on another.

## Settings

| Tab | Settings |
|---|---|
| Content | Component Settings (component title), Elements, Link, Background, Loop, Order (in Flexbox and Grid), Meta (label and Visual Builder visibility) |
| Design | Layout (Block, Flex default, Grid), Sizing, Spacing, Border, Box Shadow, Filters, Transform, Animation |
| Advanced | Attributes (CSS ID, classes, custom attributes), CSS, HTML (semantic tag), Conditions |
