---
title: "The Chart Module in Divi 5"
description: "How to add the Divi 5 Chart module, enter data in its table editor, pick one of nine chart types, and style the title, legend, and tooltip."
category: modules
tags: [modules]
related: []
divi_version: "5.11+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/16196630-the-chart-module-in-divi-5"
---

# The Chart Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A module that turns a spreadsheet-style table of labels and values into a chart, with no code or plugin.
    **Chart types:** Line (default), Area, Bar, Radar, Pie, Doughnut, Polar Area, Scatter, Bubble. Switching types keeps your data.
    **Colors:** Set in the data table, not the Design tab.
    **Starts with sample data**, so a chart shows as soon as you add it.

## Add the module

1. In the Visual Builder, click the green plus to add a Row inside a Section.
2. Click the gray plus inside the Row.
3. Find **Chart** in the module list (or search for it).

## Use cases

- **Reporting results:** revenue, traffic, or sign-ups over time as a line or bar chart.
- **Breaking down a total:** a pie or doughnut for budget, market share, or survey splits.
- **Comparing several things:** a radar chart scoring products, plans, or skills across the same categories.

## How the data table is read

All data lives in one table. A small label above each column header shows how that column is currently used: Category (labels), Series, Value, X axis, Y axis, Size, or Not Used.

| Chart type | Reading of the table |
|---|---|
| Line, Area, Bar, Radar | First column is category labels; every later column is a separate series. |
| Pie, Doughnut, Polar Area | First column is slice labels, second column is values. |
| Scatter | Second column is the X axis, third is the Y axis. |
| Bubble | Second is X, third is Y, fourth is bubble Size. |

Click a color swatch on a column (Line, Area, Bar, Radar) or on a row (Pie, Doughnut, Polar Area, Scatter, Bubble) to set colors. Unset colors are filled in automatically, and chosen colors carry over when you switch to a type that colors the other way.

In the table you can add and remove rows and columns, drag rows to reorder, move a column left or right, and hide a column. A hidden column stays in the table but is left off the chart.

## Content tab

| Group | Settings |
|---|---|
| Chart | **Chart Type**; **Data** (table editor, or import from a CSV file with the import button); Title; Subtitle; Legend Title. |
| Elements | Show Title (on), Show Subtitle (on), Show Legend (on), Show Legend Title (off), Show Tooltip (on). Nested modules can also be added. |
| Link | Makes the whole module clickable. |
| Background | Module background styles. |
| Loop | Enables the loop builder. |
| Order | Position inside Flexbox and Grid layouts. |
| Meta | Label text and forced visibility in the Visual Builder. |

!!! note
    The source article refers to the import as "CVS"; it means CSV. WordPress blocks some data-file uploads by default, and Elegant Themes has a separate article on allowing them.

## Design tab

The Title Text, Subtitle Text, Legend, and Tooltip groups appear only while the matching element is on in Elements.

| Group | Settings |
|---|---|
| Layout | Flex, Grid, or Block. |
| Title Text / Subtitle Text | Text styles for each. |
| Legend | Title text and label text (font, weight, italic, color, size, line height); **Legend Position** (Top default, Left, Bottom, Right, Chart Area) and **Legend Align** (Start, Center default, End); Markers: Legend Label Padding, **Use Point Style** (Circle, Cross, Star, Triangle) or, when off, Label Box Width and Height. |
| Tooltip | Title and body text styles; Box: background color, border color and width, corner radius, padding; Color Boxes: Display Color Boxes toggle with width and height. Opening this group shows a live tooltip while you style. |
| General | Sizing, Spacing, Border, Box Shadow, Filters, Transform, Animation. |

## Advanced tab

Attributes (CSS ID, classes, custom attributes), CSS (including a **Chart Canvas** field that targets the chart area), HTML (semantic tag), Conditions, Interactions, Visibility, Transitions, Position, and Scroll Effects.

## Save

Press `CMD + S` (Mac) or `CTRL + S` (PC), or use the Save and Exit buttons.

## Official documentation

[The Chart Module in Divi 5](https://help.elegantthemes.com/en/articles/16196630-the-chart-module-in-divi-5) on the Elegant Themes Help Center.
