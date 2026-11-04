---
title: "The Grid Editor in Divi 5"
description: "How to open and use the Divi 5 Grid Editor, a floating visual tool for shaping CSS Grid layouts and item placement."
category: builder
tags: [builder, grid, layout, grid-editor]
related: []
divi_version: "5.9+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15847488-the-grid-editor-in-divi-5"
---

# The Grid Editor in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A floating visual editor for CSS Grid layouts: drag lines to resize tracks, drag gaps, and move or resize items.
    **Where to find it:** **Design tab → Layout → Layout Style → Grid**, then **Open Grid Editor**. Works on Sections, Rows, Columns, and Groups.
    **Key behavior:** It only exists for elements using Grid layout; switching the Layout Style away from Grid closes it.

## Availability

1. Open the element's settings.
2. Go to **Design tab → Layout → Layout Style**.
3. Choose **Grid** (Flex and Block expose different controls).

## Opening it

- **Layout option group:** with Grid chosen, click **Open Grid Editor** (it becomes Close Grid Editor while open).
- **Content tab:** go to **Content tab → Elements** and click **Open Grid Editor**.
- **New row:** click the blue + icon to insert a section, scroll down in the Insert Section modal, and click **Build Custom Grid**. The new row's Layout Style is set to Grid automatically.

The editor is a floating, draggable panel you can move, resize, and expand. It stays open while you work, like a tool palette.

## Quick fields

| Field | Description |
|---|---|
| Columns | Number of columns |
| Rows | Number of rows |
| Horz. Gap | Horizontal spacing between items (applies in Flex and Grid) |
| Vert. Gap | Vertical spacing between items |
| Grid Items | How many placeholder items the preview shows; adds no real content |

Three toggles control the display: **Show/Hide Grid Editor**, **Show/Hide Grid Lines**, and **Show/Hide Track IDs** (labels each grid line for precise placement).

## Editing on the canvas

- **Resize a column or row:** drag a grid line.
- **Adjust a gap:** drag the space between tracks; a tooltip shows the size.
- **Add or remove columns:** use the floating + and - buttons.
- **Exact track size:** type or scrub a value in the track's input.
- **Move an item:** drag a numbered preview item to another cell.
- **Resize an item:** drag a corner handle to span more columns or rows.

Moving or resizing an item records a rule for that item. Items with a rule show a chip with its name and edit and delete icons.

## Fine-tuning in the Layout group

| Setting | Description |
|---|---|
| Column Widths | Equal Width, Equal Minimum Width, Equal Fixed Width, Auto Width, or Manual Width Columns |
| Grid Column Template | For manual widths, a raw pattern such as `1fr 2fr 1fr` |
| Row Heights | Auto, Equal, Minimum, Fixed, or Manual Height Rows |
| Grid Direction | Whether auto-placed items flow by Row or Column |
| Grid Density | Auto places in order; Dense back-fills gaps left by larger items |
| Justify Items | Start, Center, End, Stretch, or Baseline within each cell |

Justify Content, Align Items, and Align Content are shared with Flexbox; in Grid they align the whole grid in its container and items within their cells.

## Grid Offset Rules

Grid Offset Rules target specific items, for example one item spanning two columns. In the Layout group, open **Grid Offset Rules** and click **Add Grid Offset Rule**. In the editor you set:

1. **Admin Label:** optional name.
2. **Target Offset:** First Item, Last Item, Even Items, Odd Items, Every Third through Tenth Item, or a Custom nth-child Rule such as `3n+1`.
3. **Placement values:** Column Span, Column Start, Column End, Row Span, Row Start, Row End, and Grid Template Columns. Leave unused ones empty to keep them out of the generated CSS.

Dragging an item on the canvas creates its rule automatically: moving sets Column Start and Row Start, and resizing sets the spans. The canvas and rule list are two views of the same data. Older layouts using the earlier grid-offset format are upgraded automatically.

## Official documentation

[The Grid Editor in Divi 5](https://help.elegantthemes.com/en/articles/15847488-the-grid-editor-in-divi-5){:target="_blank"}
