---
title: "Variable Fonts and New Text Styling Options"
description: "Divi 5 variable font support (font axes) and the text styling options added in 2026: columns, drop caps, text direction, stroke position, spacing, hyphenation, line wrap."
category: builder
tags: [builder, typography, variable-fonts, text]
related: [understanding-the-body-text-option-group-in-divi-5.md, gradient-builder.md, advanced-units.md]
divi_version: "5.8+"
last_updated: 2026-11-04
source_url: "https://www.elegantthemes.com/blog/theme-releases/variable-fonts"
---

# Variable Fonts and New Text Styling Options

!!! abstract "Quick Reference"
    **Announced:** June 26, 2026 (Elegant Themes release post). The new body text options are listed in the changelog under Divi 5.8.1 (2026-06-25); gradient and image text fills arrived in 5.7.0.
    **Variable fonts:** Divi 5 supports the current Google Fonts collection, including variable fonts. Choosing one adds controls for each *axis* the font defines.
    **Text styling:** new base-level settings were added to all title and body font option groups.
    **Where:** the Text option groups on any module, e.g. [Body Text](understanding-the-body-text-option-group-in-divi-5.md).

## Variable fonts

A traditional font offers a few fixed variations (regular, bold, italic). A variable font exposes continuous axes such as weight, slant, width, and roundness, so you adjust the style within a range instead of picking a preset. For example, weight can be any value in the font's range (the announcement cites 200 to 900) rather than only thin, regular, medium, or bold.

The controls shown depend on the font you choose: Divi lists only the axes that font supports. Typical entries in the option group are Variable Font Weight, Width, and Slant, plus font-specific axes (for example element shape, element expansion, roundness, or grade). Axis settings are per option group, so a heading and body text can use different values.

## New text styling options

These live in the title and body text option groups.

| Option | What it does |
|---|---|
| Text Columns | Flows text through CSS columns for magazine-style layouts without splitting content across containers; works responsively |
| Drop Caps | New tab in the body text option group for creating and styling drop caps in any module |
| Text Direction | Lays text out along a vertical axis |
| Stroke Position | Places a text stroke at the center or outside the glyph; outside avoids clipping the text. Follows the earlier gradient-text and text-stroke options |
| Capitalization | Capitalization is now separate from text styling and offers the full range of options |
| Paragraph & List Spacing | Controls space between paragraphs and between list items (body text group) |
| Hyphenation | Lets long words that exceed the container hyphenate and wrap rather than overflow |
| Line Wrap Style | Chooses how text breaks onto new lines |

## Notes for implementers and AI assistants

- Exact setting labels vary by option group. Check the group's reference page before scripting values, and do not assume an axis exists; read it from the selected font.
- Axis values may accept Global Variables the same way other text settings do; verify per field in the builder.
- Screenshots for these controls have not been captured yet.

## Elegant Themes resources

- [Variable Fonts And New Text Styling Options For Divi 5](https://www.elegantthemes.com/blog/theme-releases/variable-fonts)
