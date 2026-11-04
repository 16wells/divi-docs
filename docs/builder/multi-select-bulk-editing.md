---
title: "Multi-Select & Bulk Editing"
description: "Divi 5 Multi-Select and Bulk Editing — select multiple elements with Cmd/Ctrl+click and edit shared settings, move, copy, or delete them together."
category: builder
tags: ["builder", "bulk-editing", "multi-select", "workflow"]
related: ["visual-builder", "presets"]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/divi-multi-select-and-bulk-editing-features"
---

# Multi-Select & Bulk Editing

Select multiple elements at once and make bulk edits with ease.

!!! abstract "Quick Reference"
    **What it does:** Selects multiple elements simultaneously for batch design, content, and structural operations.
    **Where to find it:** Hold Cmd (Mac) / Ctrl (Windows) and click elements on the canvas or in Layers View.
    **Key features:**

    - Shared settings panel shows only options common to all selected element types
    - Bulk edit design, advanced, and content settings in one step
    - Copy, cut, paste, duplicate, and delete entire selections with keyboard shortcuts
    - Drag any selected element to move the entire group together

    **ET Docs:** [Multi-Select & Bulk Editing](https://www.elegantthemes.com/documentation/divi/divi-multi-select-and-bulk-editing-features){:target="_blank"}

The Divi multi-select and bulk editing feature is a powerful tool that enables you to build WordPress websites faster and more efficiently than ever before. Multiple elements can be selected at the same time allowing you to make edits to several modules, rows, or sections at once. You can drag, drop, copy, paste, delete and edit your website’s content making changes fast and easy. You no longer have to spend excessive time editing modules or sections one by one.

Divi makes editing large amounts of content a breeze with the multi-select and bulk edit feature. For instance, rebranding a website can be a tedious task if you have to edit each module individually just to change a color. For example, you can select multiple modules where background colors are used to change them at once. Another example of how multi-selecting and editing modules can save you time is when you want to add animation or scrolling effects.

<!-- ![Multi-Select & Bulk Editing overview](../assets/screenshots/builder/multi-select-bulk-editing/overview.png){ loading=lazy }
*The Multi-Select & Bulk Editing interface in Divi 5.* -->

## The Power of Divi Multi-Select and Bulk Editing Features

Multi-select lets you act on several elements simultaneously instead of repeating the same operation on each one individually. This is particularly powerful for:

- **Rebranding** -- change background colors, font styles, or spacing across multiple modules at once.
- **Animation and effects** -- add scroll effects or hover animations to a group of elements in a single step.
- **Structural reorganization** -- move an entire group of elements to a different section.
- **Bulk deletion** -- remove multiple modules, rows, or sections in one action.

## Selecting Multiple Modules

### Hold-Click Method

Hold **Cmd** (Mac) or **Ctrl** (Windows) and click each element you want to include in the selection. Selected elements display a highlight border on the canvas.

- You can select modules, rows, and sections in the same multi-selection.
- Click a selected element again (while holding Cmd/Ctrl) to deselect it.
- Click an empty area of the canvas (without holding Cmd/Ctrl) to clear the entire selection.

### Layers View Method

Open the [Layers View](layers-view.md) panel and hold **Cmd/Ctrl** while clicking layer entries. This is useful when elements overlap on the canvas and are hard to click individually.

### Select All in a Container

Right-click a row or section and choose **Select All Modules** (if available) to select every module within that container at once.

## Bulk Editing Modules

Once multiple elements are selected, open the shared settings panel to edit common properties. The settings panel displays only the settings that are shared across all selected element types.

### Supported Bulk Edit Operations

| Category | Examples |
|----------|----------|
| **Design settings** | Background color, font family, font size, text color, padding, margin, border, box shadow. |
| **Advanced settings** | Scroll effects, animation, transitions, visibility, custom CSS classes. |
| **Content settings** | Background image/gradient (when all selected elements support it). |

When you change a value in the bulk editor, it applies to every selected element simultaneously.

## Divi Multi-Select and Bulk Editing Shared Settings

The shared settings panel adapts based on what you have selected:

| Selection | Available Shared Settings |
|-----------|--------------------------|
| All same module type (e.g., all Buttons) | Full shared Content, Design, and Advanced tabs. |
| Mixed module types (e.g., Button + Text) | Only settings common to all selected types (Design and Advanced tabs mostly). |
| Mixed element levels (e.g., Module + Row) | Only universally shared settings (background, spacing, visibility). |

Settings that are not shared across the selection are hidden to prevent errors.

## Copy, Paste & Delete with Divi Multi-Select and Bulk Editing

With multiple elements selected:

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Copy** | Cmd/Ctrl + C | Copies all selected elements to the clipboard. |
| **Cut** | Cmd/Ctrl + X | Removes all selected elements and places them on the clipboard. |
| **Paste** | Cmd/Ctrl + V | Pastes previously copied elements. |
| **Delete** | Cmd/Ctrl + Backspace | Deletes all selected elements at once. |
| **Duplicate** | Cmd/Ctrl + Shift + D | Duplicates all selected elements in place. |

You can also right-click the selection and use the context menu for these operations.

## Move Elements with Multi-Select

After selecting multiple elements, drag any one of them to move the entire group. All selected elements move together, maintaining their relative order. This is useful for reorganizing page sections or moving a cluster of modules from one row to another.

## Tips and Best Practices for Divi Multi-Select and Bulk Editing

- **Select similar elements.** Bulk editing is most powerful when all selected elements share the same type (e.g., all Blurb modules in a features row). The shared settings panel shows more options.
- **Use for style consistency.** Instead of copying and pasting styles one by one, select all target elements and set the value once in the bulk editor.
- **Combine with Find & Replace.** For value-specific changes (e.g., replacing a specific color), [Find & Replace Attributes](find-replace-attributes.md) may be faster than multi-select for large pages.
- **Undo is your friend.** If a bulk edit produces unexpected results, Cmd/Ctrl + Z undoes the entire batch operation in one step.

## Additional Resources

- [Copy & Paste Attributes](copy-paste-attributes.md) -- Transfer styles between individual elements.
- [Find & Replace Attributes](find-replace-attributes.md) -- Swap specific design values across a page.
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Full shortcut reference including multi-select operations.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Feature Not Available"
    If this feature is not visible, ensure you are running the latest version of Divi 5 and that your user role has the appropriate permissions in the Role Editor.


## Related

- [Visual Builder](visual-builder.md)
- [Presets](presets.md)
