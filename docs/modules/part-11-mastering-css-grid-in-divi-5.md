---
title: "Part 11: Mastering CSS Grid in Divi 5"
description: "Tutorial that reshapes one six-column Row into three grid layouts using Structure Templates, Grid Offset Rules, and responsive overrides."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15702426-part-11-mastering-css-grid-in-divi-5"
---

# Part 11: Mastering CSS Grid in Divi 5

!!! abstract "Quick Reference"
    **What it is:** Part 11 of the Divi 5 Mastery course. It turns a single Row of six Columns into three different grid layouts using only the Row's **Layout** settings.
    **Where to set it:** Row settings > **Design** > **Layout** (set **Layout Style** to **Grid**). Per-item controls live in a child's **Design** > **Sizing**.
    **Key idea:** The parent (Section, Row, Column, or Group) defines the grid; each child can override its own span and alignment.

## How CSS Grid works in Divi 5

CSS Grid controls layout in two directions at once, rows and columns, instead of a single line of items. It works on two levels:

1. The **parent** container sets the structure: how many grid columns and rows exist, the gaps between them, and default alignment.
2. Each **child** can break from that default by spanning several cells or aligning itself differently.

In Divi 5 the parent's **Layout** option group holds the structure controls, and the child's **Sizing** option group holds the placement controls.

!!! note
    A grid column (a track in the CSS Grid) is not the same thing as a Divi Column module. The Divi Column is an element inside a Row; the grid column is part of the grid structure the Row defines. They work together.

## Before you start

- Have a Section containing a Row with six Columns, each with some content.
- Background reading: Elegant Themes' articles on Divi's CSS Grid layout and on Grid Offset Rules.

## Switch a Row to Grid

1. Open the Row settings.
2. Go to **Design** > **Layout**.
3. Set **Layout Style** to **Grid**.
4. Enter **6** in **Number of Columns**.
5. Go to the Row's **Content** tab > **Elements** and add (or duplicate) Columns until the Row holds six.

Changing **Number of Columns** to 3 afterward reflows the same six Columns into three per row.

## Row-level Layout settings

With **Layout Style** set to Grid, the Row's **Layout** group offers:

| Setting | Description |
|---|---|
| Horizontal Gap / Vertical Gap | Space between grid columns and rows |
| Column Widths / Number of Columns | Size and count of grid columns |
| Row Heights / Number of Rows | Size and count of grid rows |
| Grid Auto Columns / Grid Auto Rows | Size of tracks Divi creates automatically when items fall outside the defined grid |
| Grid Direction / Grid Density | How items are auto-placed, and whether empty cells get backfilled |
| Justify Content, Align Content, Align Items, Justify Items | Position of the whole grid and default alignment of items inside their cells |
| Collapse Empty Columns | Helps dynamic layouts where some cells may be empty |
| Offset Rules | Position-based rules the parent applies to its children, useful for repeating, asymmetric patterns |

## Child-level grid settings

To control one child (here, a Column):

1. Open the child's settings.
2. Go to **Design** > **Sizing**.

Below the usual Width, Height, and Module Alignment options you will find:

| Setting | Description |
|---|---|
| Column Span / Row Span | How many grid tracks the item occupies (a Column Span of 2 covers two grid columns) |
| Column Start, Column End, Row Start, Row End | Pin the item to specific grid lines when a span is not precise enough, such as starting at column 2 and ending at column 5 |
| Align Self / Justify Self | Override the parent's default alignment for this item only |

## Variation 1: simple grid from a Structure Template

1. Open the Row settings.
2. Go to **Content** > **Elements**.
3. Click **Apply Structure Template**.
4. Under **Grid Multi-Row**, pick the third template.

The template fills in the grid settings in one step.

## Variation 2: alternating grid with Grid Offset Rules

1. Import the tutorial's starting layout (download link is in the official article).
2. In the Row, open **Content** > **Elements** > **Apply Structure Template**.
3. Under **Grid Multi-Row**, choose the 11th structure.
4. Go to **Design** > **Layout** > **Grid Offset Rules**. Two rules are already there; click the pen icon to open a rule's editor.

Both rules use the same settings except for the targeted pattern:

| Rule | Target Offset (custom nth-child) | Matches items | Offset Rule | Offset Value |
|---|---|---|---|---|
| 1 | 4n+2 | 2, 6, 10, ... | Column Span | 2 |
| 2 | 4n+3 | 3, 7, 11, ... | Column Span | 2 |

The admin label is generated automatically from the rule (for example "4n+2 Spans 2 Columns"). The result is a rhythm in which the 2nd and 3rd items of each group of four span two columns while the 1st and 4th stay single width. To make the large items come first instead, switch the patterns to 4n+1 and 4n+4.

## Variation 3: masonry-style grid

1. Import the Variation 2 layout from the article.
2. In the Row, open **Content** > **Elements** > **Apply Structure Template**.
3. Under **Grid Masonry**, choose the second structure.
4. Open **Design** > **Layout** > **Grid Offset Rules**.

| Rule | Target Offset (custom nth-child) | Matches items | Offset Rule | Offset Value | Effect |
|---|---|---|---|---|---|
| 1 | 6n+1 | 1, 7, 13, ... | Row Span | 2 | Tall anchor item at the start of each group of six |
| 2 | 6n+6 | 6, 12, 18, ... | Column Span | 2 | Wide item at the end of each group of six |

!!! note
    Offset Rules repeat automatically. Adding more Columns continues the same six-item pattern, which suits dynamic content such as Loop Builder results where the item count varies.

### Make the masonry layout responsive

Grid settings can be overridden per breakpoint, which keeps a four-column masonry from feeling cramped on small screens.

1. Switch the Visual Builder to **Tablet**, open the Row's **Design** > **Layout**, and set **Number of Columns** to **2**.
2. Switch to **Phone** and set **Number of Columns** to **1**.
3. Still on Phone, add a new Grid Offset Rule with these values:
    - **Target Offset:** Custom nth-child Rule
    - **Custom Nth-Child Rule:** 3
    - **Offset Rules:** Column Span
    - **Offset Value:** 1

## Official documentation

- [Part 11: Mastering CSS Grid in Divi 5](https://help.elegantthemes.com/en/articles/15702426-part-11-mastering-css-grid-in-divi-5) (includes the downloadable starting layouts for each variation)
