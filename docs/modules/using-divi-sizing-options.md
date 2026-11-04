---
title: "Using Divi Sizing Options"
description: "How to control width, height, flex behavior, aspect ratio, and alignment of Divi 5 elements from the Design tab Sizing option group."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/10102469"
---

# Using Divi Sizing Options

!!! abstract "Quick Reference"
    **Where:** Module settings > Design tab > Sizing.
    **Controls:** Flex size behavior, width, max width, alignment, heights, column class, and aspect ratio.
    **Gotcha:** Alignment only appears once Width or Max Width has a value.

Sizing controls the dimensions and alignment of any layout element. See also the [Sizing option group reference](../options-groups/sizing.md).

## Open the options

1. Click the module or its Gear icon to open its settings.
2. Go to the **Design** tab and open **Sizing**.

## Settings

| Setting | Description |
|---|---|
| Size | How the element behaves as a flex item. **Shrink to Fit** lets it shrink when space is tight. **Grow to Fill** makes it expand into free space (flex-grow of 1). **Custom** lets you type your own flex-grow and flex-shrink values, which are output as entered. |
| Width | Set in units such as px, %, or vw. |
| Max Width | Caps how wide the element can get. |
| Alignment | Start (left), center, end (right), or stretch. Available only when Width or Max Width is set. |
| Min Height | Keeps a minimum vertical size. |
| Height | A fixed height that overrides automatic sizing. |
| Max Height | Prevents the element from growing too tall. |
| Column Class | Picks a predefined column width, such as 1/2 or 1/3, when the element sits inside a flex layout. It has no effect if the parent is not a flex layout. |
| Aspect Ratio | Locks the relationship between width and height so the proportion holds on phones, tablets, and desktops. |

Accepted units include px, %, em, rem, vw, vh, in, mm, cm, pt, and pc, plus CSS functions such as calc, min, and max. See [Advanced units](../builder/advanced-units.md) for details.

## Tips

- Percentage and viewport units help keep layouts responsive.
- Keep sizing consistent with neighboring elements.
- Use alignment to center or position a module that has a custom width.


## Official documentation

- [Using Divi Sizing Options (Elegant Themes Help Center)](https://help.elegantthemes.com/en/articles/10102469)
