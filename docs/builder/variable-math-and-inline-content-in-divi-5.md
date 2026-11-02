---
title: "Variable Math and Inline Content in Divi 5"
category: builder
tags: [builder]
related: []
divi_version: "5.x"
last_updated: 2026-11-02
source_url: "https://help.elegantthemes.com/en/articles/17741586-variable-math-and-inline-content-in-divi-5"
---

# Variable Math and Inline Content in Divi 5

<!-- AUTO-CREATED: 2026-11-02 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/17741586-variable-math-and-inline-content-in-divi-5).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Text and variables in one field |  | Type static text before, between, and after variables and dynamic content in the same field. |
| Several variables per field |  | Add as many text variables and dynamic content sources to one field as you need. |
| Editable chips |  | Each variable or source is its own chip that you can replace, move, copy, or delete without touching the rest of the field. |
| Variable math |  | Combine number variables with plain numbers using addition, subtraction, multiplication, and division, or place them insidecalc(),clamp(),min(), andmax(). |
| Nested variables |  | Build a Number or Text variable out of other variables, so it updates whenever the variables it uses change. |
| A keyboard shortcut |  | Type{{in a supported field to open the variable picker without leaving the keyboard. |
| Gear Icon |  | module's settings by clicking theGear Iconor the module itself. |
| Content |  | ontenttab, click inside a text field, such as theHeadingfield in theTextgroup of a Heading module, and place your cursor where the variable should go. |
| Insert Dynamic Content |  | nd click theInsert Dynamic Contenticon. |
| My Global Strings |  | or a dynamic content source from the list. Text variables are listed underMy Global Strings, and sources such asSite Titleare listed underDynamic Content. |
| Variable Settings |  | Opens the chip's own settings, such as text to show before or after it. This only appears for sources that have settings. |
| Detach From Variable |  | Replaces the chip with its current value as plain text, so it no longer updates. Loop dynamic content can't be detached. |
| Remove Variable |  | Deletes the chip and leaves the rest of the field as it is. |
| Any other variable or source in the list |  | Replaces only this chip with the one you pick. |
| Preview a value |  | Hover over a chip to see what it holds. A dynamic content chip shows its value on the current page, and a variable chip shows the variable's value. If the variable is built from other variables, you see how it's built instead, such asBase Spacing * 2. |
| Move a chip |  | Drag a chip to a new spot in the field. Dragging works in ordinary text fields, not in rich text editors. |
| Copy, cut, and paste |  | Select chips along with any text and use the usual keyboard shortcuts. Pasted chips stay chips. |
| Undo and redo |  | CMD + Zon a Mac orCTRL + Zon a PC undoes chip changes along with your typing. |
| Enter |  | Enteror click a result to replace the two brackets you typed with the variable. |
| Base Spacing |  | e inside it a margin of[Base Spacing] * -1, so it reaches past the section's edge by exactly the padding. ChangeBase Spacing, and the negative margin automatically gets recalculated based on the new Base Spacing value. |
| Design |  | he module's settings and go to a number field in theDesigntab, such asPaddingin theSpacingoption group. |
| Insert Dynamic Content |  | click theInsert Dynamic Contenticon, and choose a number variable. |
| + |  | (add) and-(subtract) - Put a space on each side, such as[Base Spacing] + 10px. |
| * |  | (multiply) - At least one side must be a plain number with no unit, such as[Base Spacing] * 2. |
| / |  | (divide) - The number you divide by must have no unit, such as[Base Spacing] / 2. |
| ( ) |  | (parentheses) - Group parts of a calculation. Every opening bracket needs a closing one, or the field showsParentheticals must be closed. |
| Insert Dynamic Content |  | and add variables with theInsert Dynamic Contenticon or by typing{{. |
| Variable Manager |  | Managerby clicking its icon in the left toolbar. |
| Numbers |  | theNumbersorTextdrawer and add a new variable, or click the value of an existing one. |
| Insert Dynamic Content |  | nd click theInsert Dynamic Contenticon. |
| Save Variables |  | ables. |
| A spacing scale |  | Create a Number variable namedBase Spacingwith the value20px. Then createLarge Spacingwith the value[Base Spacing] * 2andSmall Spacingwith[Base Spacing] / 2. ChangeBase Spacingto24px, and update the other two to48pxand12pxeverywhere they're used. |
| A fluid size |  | Create Number variables namedMinimum SizeandMaximum Size. Then createFluid Heading, click the unit next to its value, chooseclamp, and enter[Minimum Size], 10vw, [Maximum Size]. The middle value controls how the size scales with the screen, and your two variables set its limits. UseFluid Headingfor your heading sizes, and when you need a larger maximum, changeMaximum Sizeonce. |
| A reusable sentence |  | Create Text variables namedLegal NameandYear. Then createCopyright Noticewith the valueCopyright © [Year] [Legal Name]. All rights reserved.Use it in your footer and anywhere else you need it. When you updateLegal NameorYear, every copyright notice on the site updates automatically. |
| Base Spacing |  | e Variable Manager, or the variable list in a field, also finds variables that use the name you search for. Searching forBase SpacingshowsLarge SpacingandSmall Spacingtoo. |
| Responsive and hover settings |  | Chips and calculations carry over from desktop to tablet and phone, and to the hover and sticky states, the same way any other value does. |
| Loop Builder |  | Fields inside aLoop Builderlayout keep their mix of loop dynamic content, variables, and text. |
| Deleted variables |  | If you delete a variable that another variable still uses, the dependent variable keeps working until you change it. SeeWorking with Archived VariablesinDesign Variables in Divi 5. |
| Existing designs |  | Fields that already use a single variable or dynamic content source keep working as they did. You can now type around those chips too. |

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
