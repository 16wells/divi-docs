---
title: "Multi-Select and Bulk Editing in Divi 5"
description: "Divi 5.16 multi-select on the canvas and Layers panel, bulk editing in the settings panel, mixed values, presets, shortcuts, and AI Agent scoping."
category: builder
tags: [builder, multi-select, bulk-editing]
related: [multi-select-bulk-editing.md, presets.md, style-inspector.md]
divi_version: "5.16+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/17633664-multi-select-and-bulk-editing-in-divi-5"
---

# Multi-Select and Bulk Editing in Divi 5

!!! abstract "Quick Reference"
    **Introduced in:** Divi 5.16 (2026-10-16). An earlier overview exists at [Multi-Select & Bulk Editing](multi-select-bulk-editing.md); this page follows the current Help Center article.
    **Select:** Cmd/Ctrl + click adds or removes one element; Shift + click selects a range inside the same parent; Cmd/Ctrl + A selects all in the hovered container.
    **Edit:** with two or more elements selected, the settings panel becomes **Elements** and every change applies to all of them.
    **Clear:** Cmd/Ctrl + D, or a plain click on any element.

## Selecting

- Works on the canvas and in the **Layers** panel; both share one selection. Drag several selected layers to move them together.
- Mix element types freely (modules and a row, for example).
- Range selection (Shift + click) only works between elements in the same parent; clicking one in another container adds just that element.
- In the Theme Builder a selection cannot span more than one template area.

## Acting on a selection

- **Drag and drop** moves the whole selection (not possible if a locked element is included).
- **Right-click menu** acts on all: Duplicate, Delete, Move (up, down, top, bottom, parent), Copy/Cut/Paste (only when all are the same type), Lock/Unlock, Paste Attributes, Reset Attributes, Add Element above/inside/below/around (Around only when all share a parent), Detach Component.
- **Shortcuts:** Cmd/Ctrl + C/X/V, Shift + D (duplicate), Backspace (delete), Shift + K (lock), Shift + U (unlock), Up/Down Arrow (move), Shift + V (paste all attributes), Shift + 0 (reset all attributes), D (deselect), G (group). The Cmd/Ctrl modifier applies to all of these. Press Shift + ? for the searchable shortcut list.
- **Group:** Cmd/Ctrl + G wraps selected *modules* in a new Group module at the first module's position. Sections, rows, columns, Groups, and child items cannot be grouped.

## Bulk editing

- Content, Design, and Advanced tabs, search, and responsive/state controls all work; edits apply at the breakpoint or state you pick.
- **Different types:** option groups from all types appear; shared groups (Spacing, Border) appear once and update everything; type-specific settings only change elements of that type.
- **Elements option group:** with several containers selected, it lists all children, and **Add Element** adds one to every container.

### Mixed values

When selected elements disagree, the field shows **Mixed**: empty text/number fields with a placeholder, dropdowns with no option highlighted, gray color swatches, a "Mixed" label for previews, toggles neither on nor off, and button/checkbox options showing all used values in gray. Entering a value applies it to every element.

### Inherited vs. set values

For checkbox and button option fields, **blue** means set directly on the element at the current breakpoint and state; **gray** means inherited (from a preset, default, larger breakpoint, or normal state when editing hover).

### Presets

In the panel header: preset chips show every preset in use (remove one to strip it from all); picking a preset adds it to every element lacking it (or removes it from all if all have it); **Default Preset** clears presets; **New Preset From Current Styles** creates and assigns a preset. With mixed element types, presets are grouped by type and new presets cannot be created from the menu. Option Group Presets work across types, so one border preset can go on a Text and an Image module together.

### Field and group right-click

Reset, Paste attributes, **Convert to Variable** (one Design Variable per distinct value, each element linked to its match), Find & Replace; Copy and Extend only when all elements share a type.

## Inspector and AI Agent

- The [Style Inspector](style-inspector.md) supports selections via the toolbar icon (the right-click *Inspect* appears only for a single element). Changes there affect only the selected elements.
- With several elements selected, the [Divi AI Agent](../modules/the-divi-ai-agent-in-divi-5.md) shows each as a chip and applies your request to all. Removing a chip changes the Agent's scope, not your selection.

## Limitations

- Locked elements are skipped by bulk edits, resets, moves, and pastes.
- Copy Attributes, Extend Attributes, Inspect, and Save To Library are hidden for multi-selections; Save as Component is unavailable in the panel header.
- Editing a preset or component drops to single-element editing and returns afterward; the selection is kept.
- **Attributes, Interactions, and Conditions** do not show mixed values yet; edit them one element at a time to avoid overwriting.

## Official documentation

- [Multi-Select and Bulk Editing in Divi 5](https://help.elegantthemes.com/en/articles/17633664-multi-select-and-bulk-editing-in-divi-5)
