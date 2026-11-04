---
title: "Visual Builder"
description: "Divi 5 Visual Builder — front-end drag-and-drop page editor with real-time WYSIWYG editing, responsive previews, and inline design controls."
category: builder
tags: [builder, visual-builder, editor, drag-drop, frontend]
related: [theme-builder, library, presets, global-elements]
divi_version: "5.x"
last_updated: 2026-03-12
source_url: "https://www.elegantthemes.com/documentation/divi/visual-builder/"
---

# Visual Builder

The Divi Visual Builder is the front-end, drag-and-drop page editor that lets you design pages visually in real time.

!!! abstract "Quick Reference"
    **What it does:** Front-end WYSIWYG page editor for building and styling pages with drag-and-drop controls.
    **Where to find it:** Navigate to any page → click "Enable Visual Builder" in the admin bar, or Pages → Add New → Use Divi Builder.
    **Key features:**

    - Drag-and-drop element placement with inline text editing
    - Section → Row → Column → Module content hierarchy
    - Three-tab settings panel (Content, Design, Advanced) for every element
    - Responsive editing with device preview modes
    - Undo/redo history with auto-save

    **ET Docs:** [Visual Builder](https://www.elegantthemes.com/documentation/divi/visual-builder/){:target="_blank"}

## Overview

Divi is a modern no-code visual drag-and-drop website builder for WordPress. With Divi, you can build stunning websites from the ground up without touching a single line of code. Divi harnesses the power of complex web development and lets you design custom websites using the Visual Builder so you can see the changes you are making in real time. For the official Elegant Themes documentation, see [Visual Builder](https://www.elegantthemes.com/documentation/divi/visual-builder/){:target="_blank"}.

The Visual Builder operates directly on the front end of your website. Every change you make is immediately visible, giving you a true WYSIWYG (What You See Is What You Get) editing experience. You can drag and drop elements, resize them, edit text inline, and adjust design settings through an intuitive settings panel.

The builder organizes content through a hierarchy of **sections**, **rows**, **columns**, and **modules**. Sections are the largest containers, rows sit inside sections and define column layouts, columns hold individual modules, and modules are the actual content blocks (text, images, buttons, forms, etc.).

<!-- ![Visual Builder overview](../assets/screenshots/builder/visual-builder/overview.png){ loading=lazy }
*The Divi Visual Builder interface showing a page being edited on the front end.* -->

## Loading the Visual Builder

There are two ways to access the Visual Builder:

### From an Existing Page

Navigate to any page on your website and click **Enable Visual Builder** on the WordPress top admin bar. The page will reload with the Visual Builder interface active.

### Creating a New Page

1. In your WordPress dashboard, go to **Pages > Add New**
2. Give your page a title
3. Click **Use Divi Builder**
4. The page reloads on the front end with the Visual Builder enabled

When creating a new page, you are presented with three starting options:

| Option | Description |
|--------|-------------|
| **Build From Scratch** | Loads a blank page with a single standard section. Choose this to start your page design from scratch. |
| **Choose A Premade Layout** | Opens the Divi Library where you can browse premade layout packs, your previously saved designs, and existing pages on your website. |
| **Clone An Existing Page** | Loads the design from an existing page on your website as your starting point. |

## Builder Basics

The building blocks of Divi are **sections**, **rows**, **columns**, and **modules**. These nest inside each other: sections contain rows, rows contain columns, and columns contain modules.

### Sections

Everything you build in Divi starts with a section. Sections are the largest building block, acting as horizontal stacking containers that group your content into visually distinguishable areas.

There are three types of sections:

| Section Type | Description |
|-------------|-------------|
| **Standard** | The most commonly used section. Expands to the width of the browser and contains a row set to 80% width by default. Extensive customization options are available. |
| **Fullwidth** | Gives you access to Fullwidth Modules that take advantage of the full browser width. Fullwidth modules can only be placed within Fullwidth sections. |
| **Specialty** | Allows for more advanced column structures. You can add complex column variations next to full-spanning vertical sidebars without adding unwanted breaks to the page. These layouts are not possible using standard sections. |

### Rows

Rows are nested inside sections and define the column structure for your content. Each row can contain a variety of column layouts (single column, two columns, three columns, etc.).

### Columns

Columns are nested inside rows and create the boxed structure for your content. Every row has at least one column.

### Modules

Modules are the content blocks of Divi. Contact forms, images, text blocks, sliders, blurbs, buttons, and more are all examples of modules. Modules are placed inside columns. See the [Modules documentation](../modules/index.md) for a complete list.

### Parent/Child Element Hierarchy

When adjusting settings and applying styles, the hierarchy matters. Sections contain rows, rows contain columns, and columns contain modules. These are parent and child elements. Child elements are nested inside parent elements and inherit or are affected by design styling applied to the parent element.

<!-- ![Builder hierarchy](../assets/screenshots/builder/visual-builder/hierarchy.png){ loading=lazy }
*The section > row > column > module hierarchy in the Visual Builder.* -->

## The Element Settings Window

Whenever you open an element's settings, a window pops up with all of the content, design, and advanced settings available for that element.

### Settings Window Controls

| Control | Location | Description |
|---------|----------|-------------|
| **Element Name** | Top left | Displays the name of the element you are editing (section, row, column, module, etc.). |
| **Presets Dropdown** | Below name | Load a saved preset, create a new preset, or delete a preset. See [Presets](presets.md). |
| **Expand Modal** | Top right area | Expands the settings modal to the full width of your browser. |
| **Snap/Separate Modal** | Top right area | Snaps the modal to the left sidebar (content adjusts beside it) or returns it to floating position. |
| **Three-Dot Menu** | Top right | Access additional options (see below). |
| **Search Bar** | Below controls | Type to search and quickly find specific settings. |
| **Filter Button** | Next to search | Filter to show only modified styles, responsive styles, hover state styles, or active content. |

### Three-Dot Menu Options

The three-dot menu (vertical ellipsis) provides access to advanced element operations:

| Option | Description |
|--------|-------------|
| **Save To Library** | Saves this element to your Divi Library. |
| **Save To Divi Cloud** | Saves this element to your Divi Cloud. |
| **Split Test** | Conduct a split test with this element. |
| **Disable** | Disable the element on desktop, tablet, or mobile. Green icon = visible, red icon = hidden. |
| **Lock** | Locks the element to prevent settings changes. Right-click and select "Unlock" to reverse. |
| **Copy Module** | Copies the module to your clipboard for pasting elsewhere. |
| **Copy Module Styles** | Copies only the module's styles and settings for applying to another module of the same type. |
| **Paste Styles** | Pastes previously copied styles onto this element. |
| **Reset Module Styles** | Resets the module's styles to the default, removing all customizations. |
| **Paste Module** | Pastes a previously copied module. |
| **View Modified Styles** | Displays only the settings that have been modified, useful for reviewing changes. |
| **Extend Styles** | Extend this element's styles throughout the page, section, row, or column. |
| **Apply Styles To Active Preset** | Applies the current styles to the active preset. |
| **Edit Preset Style** | Opens the current preset's settings for editing. |
| **Go To Layer** | Opens the Layers panel and navigates to this element's layer. |

!!! tip "Right-Click Access"
    You can also access these options by right-clicking on any design element. The right-click menu also includes Undo and Redo at the top of the list for quick access.

### Settings Tabs

All element settings are organized into three tabs:

| Tab | Purpose |
|-----|---------|
| **Content** | Content-specific settings that vary by element type (text content, images, links, background, etc.). |
| **Design** | Visual styling settings (fonts, colors, spacing, sizing, borders, shadows, etc.). |
| **Advanced** | Technical settings including Custom CSS, Visibility, Scroll Effects, Conditions, and more. |

### Bottom Buttons

At the bottom of the settings modal:

| Button | Color | Action |
|--------|-------|--------|
| **Exit** | Red | Closes the modal. Unsaved changes will be lost. |
| **Undo** | Purple | Undoes the previous action. |
| **Redo** | Blue | Redoes an undone action. |
| **Save** | Green | Saves the current settings. |

<!-- ![Element settings window](../assets/screenshots/builder/visual-builder/settings-window.png){ loading=lazy }
*The element settings window showing Content, Design, and Advanced tabs.* -->

## The Bottom Toolbar

The bottom toolbar provides access to the builder's main controls and features. It is divided into a left section, a middle section, and a right section.

### Left Toolbar (Builder Settings)

Click the three-dot icon on the far left to access builder interface customization:

| Setting | Description |
|---------|-------------|
| **Toolbar Icon Visibility** | Show or hide specific icons on the toolbar. |
| **History State Interval** | How often Divi auto-saves: after every action, or every 10/20/30/40 actions. |
| **Modal Default Position** | Default position when modals open: Last Used, Floating, Fullscreen, Fixed Left/Right Sidebar, or Fixed Bottom Panel. |
| **New Page Default** | How new pages load: Build from Scratch, Divi Library, Clone Page, or Give Me a Choice. |
| **Builder Animations** | Toggle the interface animations when clicking objects. |
| **Show Disabled Modules** | Display disabled modules at 50% opacity so they remain visible while editing. |
| **Closed Toggles** | Show module settings as closed or open toggles by default. |
| **Placeholder Content** | Whether new modules display placeholder content when added. |
| **Theme Builder Templates** | Enable or disable editing Theme Builder templates from the Visual Builder. |

### Left Toolbar Icons

| Icon | Function |
|------|----------|
| **Wireframe View** | Toggle the wireframe layout view of the page. |
| **Zoom In/Out** | Zoom in or out on your page design for a bird's-eye view. |
| **Desktop View** | Resize the builder to desktop dimensions. |
| **Tablet View** | Resize the builder to tablet dimensions. |
| **Mobile View** | Resize the builder to mobile phone dimensions. |
| **Hover Mode** | Element settings toolbar shows on hover. |
| **Click Mode** | Element settings toolbar shows on click. |
| **Grid Mode** | All element toolbars and containers are visible at all times. |

### Middle Toolbar

| Icon | Function |
|------|----------|
| **Plus (+) / Library** | Opens the Divi Library with tabs for Premade Layouts, Your Saved Layouts, and Clone Existing Page. |
| **Down Arrow (Save Layout)** | Save the current page layout to your Divi Library and/or Divi Cloud Library. |
| **Trash Can** | Delete the entire page design and start fresh. |
| **Toggle (+/X)** | Open or close the expanded Divi toolbar. |

### Right Toolbar

| Icon | Function |
|------|----------|
| **Gear (Page Settings)** | Opens page-specific settings (Content, Design, Advanced) that apply only to the current page. |
| **Clock (Revisions)** | View editing history including page-level and global history states (headers, footers, global modules). |
| **Import/Export** | Import or export page layouts as JSON files. |
| **Search** | Search across device views, page layout, builder settings, documentation, and elements. |
| **Layers** | View the design layer tree. Drag and drop layers to rearrange, or use layer icons to access settings, duplicate, or delete elements. |
| **Help (?)** | Opens the Divi Builder Helper with documentation, video tutorials, and keyboard shortcuts. |
| **Save** | Save the current page design. |

<!-- ![Bottom toolbar](../assets/screenshots/builder/visual-builder/toolbar.png){ loading=lazy }
*The Divi Visual Builder bottom toolbar with all control icons.* -->

## Responsive Editing

Divi is responsive by default, but it gives you complete control over every design setting on each device breakpoint. You can perfectly tailor the appearance of each element on computers, tablets, and smartphones.

To preview and edit at different breakpoints, use the device view icons in the bottom toolbar:

- **Desktop View** -- Full-width desktop display
- **Tablet View** -- Tablet-width display
- **Mobile View** -- Phone-width display

Many design settings include a responsive toggle (a small device icon) that allows you to set different values for each breakpoint. For example, you can set a heading to 48px on desktop, 36px on tablet, and 24px on mobile.

## Essential Features

### Drag and Drop

Move and resize elements by dragging them on the front end. You can also resize elements by dragging the edges to adjust height, width, padding, and margins visually.

### Copy and Paste Styles

Anything can be copied from one element and pasted onto another. You can copy individual settings, groups of settings, or an entire element's design. Design it once, then copy and paste to matching elements.

### Extend Styles

Apply a design style from one element to other elements across the page, section, row, or column. Update hundreds of elements at once by extending styles to a specified scope.

### Keyboard Shortcuts

Divi includes a full range of keyboard shortcuts for advanced users. Access the shortcuts reference by clicking the **Help (?)** icon in the toolbar and selecting the **Keyboard Shortcuts** tab.

### Multi-Select and Bulk Editing

Select multiple elements simultaneously by holding **Cmd** (Mac) or **Ctrl** (Windows) and clicking each element. Edit these elements at the same time, changing their style and content together, or move them as a group.

### Find and Replace

Make sweeping changes across your entire page instantly. Find and replace any design value (colors, fonts, etc.) across the entire page or within specific sections. This saves hours of repetitive individual element editing.

### Global Styles

Customize your website with an overarching design system by editing the default design of any element type. When you modify a module's default design, it updates across your whole website at once. See [Presets](presets.md) for more.

### Global Colors

Create a global color palette for your website. Global colors are dynamic and can be changed at any time, allowing you to transform your website's color scheme in moments.

### Advanced Code Editing

While Divi is a no-code builder, it includes a fully-featured code editor with syntax highlighting, error reporting, auto-complete, color picking, multi-line select, search, and find-and-replace. Add custom CSS to any element via the Advanced tab, or use the Code module for custom code blocks.

### Design Library

Save design elements, page layouts, headers, footers, and more to the [Divi Library](library.md) for reuse across your website. Divi also includes hundreds of premade layouts.

### Global Elements and Dynamic Content

Save builder elements (sections, rows, modules) as [global elements](global-elements.md) that sync changes across your entire website. Divi also supports dynamic content (logos, post titles, search results) so you can make changes in one place and have them reflected everywhere.

### View Modes

Switch freely between different view modes: standard front-end editing, wireframe mode for quick structural work, and different device preview modes. Zoom in and out for a bird's-eye view.

### History and Auto-Save

Every action you perform while building is saved to your editing history. You can undo, redo, and explore revisions. If your internet goes down or your computer crashes, Divi will automatically save your progress for restoration.

### Right-Click Options

Divi provides context-specific right-click menus on all elements for quick access to copy, paste, lock, disable, duplicate, and other operations.

## Saving Your Work

The Divi Builder periodically auto-saves your work, but you should always do a manual save before exiting.

To save your design:

- Click the green **Save** button at the bottom right of the screen
- Use the keyboard shortcut **Cmd + S** (Mac) or **Ctrl + S** (Windows)

Then click **Exit Visual Builder** on the top admin bar to exit the editor.

!!! warning "Save Before Exiting"
    Always save your work before exiting the Visual Builder. While Divi auto-saves periodically, a manual save ensures all your latest changes are preserved.

## Best Practices

### Switch Between Visual Builder and Wireframe Mode

Switching between the front-end visual editing and wireframe mode helps you quickly drag and drop elements while also viewing the structural layout of your design. The switch is nearly instantaneous.

### Use the Zoom Out Feature

Use the zoom icon on the toolbar to get a bird's-eye view of your entire page design. This is much faster than taking a screenshot to review your overall layout.

### Use Keyboard Shortcuts

Learning keyboard shortcuts significantly speeds up your workflow. Common shortcuts include:

| Shortcut (Mac) | Shortcut (PC) | Action |
|----------------|---------------|--------|
| Cmd + S | Ctrl + S | Save |
| Cmd + Z | Ctrl + Z | Undo |
| Cmd + Shift + Z | Ctrl + Shift + Z | Redo |
| Cmd + C | Ctrl + C | Copy |
| Cmd + V | Ctrl + V | Paste |


### Use Presets for Consistent Design

Create and apply [Presets](presets.md) to maintain consistent styling across your website without manually adjusting each element.

## Code Examples

### Adding Custom CSS to an Element

In the Advanced tab of any element's settings, you can add custom CSS:

```css
/* Custom CSS added via the Advanced tab > Custom CSS */
.my-custom-class {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease;
}

.my-custom-class:hover {
    transform: translateY(-4px);
}
```

### Using the Code Module

```html
<!-- Place inside a Divi Code module -->
<div class="custom-widget">
    <h3>Custom Content</h3>
    <p>This content is rendered via the Code module.</p>
</div>

<style>
.custom-widget {
    padding: 30px;
    background: #f7f7f7;
    border-radius: 8px;
}
</style>
```

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Visual Builder interface has been significantly updated in Divi 5 with improved performance and a modernized UI.

## Troubleshooting

!!! warning "Visual Builder Not Loading"
    If the Visual Builder fails to load or shows a blank screen, try these steps:

    1. Clear your browser cache and cookies
    2. Disable other WordPress plugins to check for conflicts
    3. Switch to a default WordPress theme temporarily to rule out theme conflicts
    4. Increase your PHP memory limit in `wp-config.php`: `define('WP_MEMORY_LIMIT', '256M');`
    5. Check the browser console for JavaScript errors

!!! warning "Changes Not Saving"
    If your changes are not saving:

    1. Check your internet connection
    2. Verify your WordPress login session has not expired
    3. Check for server-side errors in your hosting error logs
    4. Try saving with Cmd/Ctrl + S instead of the Save button

## Related

- [Theme Builder](theme-builder.md) -- Template system for headers, footers, and post templates
- [Divi Library](library.md) -- Saving and loading layouts
- [Presets](presets.md) -- Creating and managing element presets
- [Global Elements](global-elements.md) -- Reusable synced elements
- [Modules Overview](../modules/index.md) -- All available content modules
- [Playbook: Visual Builder Ops](../playbooks/visual-builder-ops.md) -- LLM playbook for automating the Visual Builder
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Complete keyboard shortcut reference
- [Layers View](layers-view.md) -- Navigate and manage page structure from the layers panel

## Visual Builder Features

The following pages document individual Visual Builder features in detail:

- [Visual Builder Interface](vb-interface.md) -- Guided tour of the workspace panels and toolbars
- [Left Sidebar](left-sidebar.md) -- Every panel in the left options sidebar
- [Keyboard Shortcuts](keyboard-shortcuts.md) -- Complete shortcut reference
- [Right-Click Menus](right-click-menus.md) -- Context menu operations
- [Wireframe View](wireframe-view.md) -- Structural editing mode
- [Responsive Options](responsive-options.md) -- Device-first responsive editing workflow
- [Add, Duplicate & Remove Elements](add-duplicate-remove.md) -- Building and managing page elements
- [Copy & Paste Attributes](copy-paste-attributes.md) -- Granular attribute transfer between elements
- [Find & Replace Attributes](find-replace-attributes.md) -- Bulk value replacement across elements
- [Element Presets](element-presets.md) -- Per-element-type design presets
