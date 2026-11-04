---
title: "Variable Math and Inline Content in Divi 5"
description: "Divi 5 inline variables and dynamic content chips, variable math with calc/clamp/min/max, and nested variables."
category: builder
tags: [builder, variables, dynamic-content]
related: []
divi_version: "5.18+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/17741586-variable-math-and-inline-content-in-divi-5"
---

# Variable Math and Inline Content in Divi 5

!!! abstract "Quick Reference"
    **Introduced in:** Divi 5.18 (2026-10-27).
    **What it does:** Variables and dynamic content no longer replace a whole field. They insert as *chips* at the cursor, so text and several variables can share one field.
    **Math:** Number variables can be combined with numbers (`+ - * /`) or placed inside `calc()`, `clamp()`, `min()`, `max()`.
    **Nested variables:** Number and Text variables can be built from other variables and update when those change.
    **Shortcut:** type `{{` in a supported text, URL, or number field to open the variable picker.

## Inline content

Text fields, link (URL) fields, and rich text fields (such as a Text module's Body) support inline content.

1. In the module settings, click inside the field where the variable should go.
2. Hover the field, click **Insert Dynamic Content**, and pick a variable or source. Text variables are listed under **My Global Strings**; sources such as Site Title under **Dynamic Content**.
3. The chip appears at the cursor; keep typing around it or add more chips.

Example: `Welcome to [Site Title] - [Site Tagline]`. Selecting a word first and then picking a variable replaces only the selected text. In rich text fields, formatting around chips is preserved.

### Working with chips

Click a chip for its menu: **Variable Settings** (for sources that have settings), **Detach From Variable** (replace with plain current value; not available for loop dynamic content), **Remove Variable**, or pick another variable to replace just that chip.

Also: hover to preview a value (nested variables show how they are built, e.g. `Base Spacing * 2`); drag chips to move them (ordinary text fields only, not rich text); copy, cut, and paste keep chips; undo and redo cover chip changes. A warning symbol means the variable is nested too deeply or produces too much content; simplify the variables it uses.

## Variable math

Number variables can be part of a calculation. Example: with `Base Spacing` = `20px`, typing `* 1.5` after its chip gives `30px`.

| Operator | Rule |
|---|---|
| `+` `-` | Put a space on each side, e.g. `[Base Spacing] + 10px` |
| `*` | At least one side must be a plain number with no unit |
| `/` | The divisor must have no unit |
| `( )` | Group parts; every opening bracket needs a closing one or the field shows *Parentheticals must be closed* |

To use functions, click the unit next to a number field and choose `calc`, `clamp`, `min`, or `max`, then add chips and separate arguments with commas. Example for Heading Text Size: `clamp([Minimum Size], 10vw, [Maximum Size])`. See [Advanced Units](advanced-units.md).

!!! note
    Divi does not check units inside a variable. A unit that does not suit the calculation (for example `px` on both sides of a multiplication) produces a result that does not apply.

Keep one-off adjustments in the field; if a calculation is reused, make it its own variable.

## Nested variables

In the Variable Manager, expand **Numbers** or **Text**, add or edit a variable, use **Insert Dynamic Content** to pick other variables (sources are not listed), add text or math around the chip, and click **Save Variables**.

- **Spacing scale:** `Base Spacing` = `20px`; `Large Spacing` = `[Base Spacing] * 2`; `Small Spacing` = `[Base Spacing] / 2`. Changing the base to `24px` updates both.
- **Fluid size:** `Fluid Heading` = `clamp` with `[Minimum Size], 10vw, [Maximum Size]`.
- **Reusable sentence:** `Copyright Notice` = `Copyright © [Year] [Legal Name]. All rights reserved.`

Loops are prevented: a variable cannot use itself or any variable that already uses it, and such entries are greyed out. Searching the Variable Manager also finds variables that use the searched name. Exporting a variable includes everything it depends on.

## Things to know

- Chips and calculations carry across breakpoints and hover/sticky states like any other value.
- Fields in a Loop Builder layout keep their mix of loop dynamic content, variables, and text.
- Deleting a variable that another variable uses leaves the dependent working until it is changed (see [Design Variables](design-variables.md) on archived variables).
- Existing single-variable fields keep working; you can now type around them.
