---
title: "Components in Divi 5"
description: "Divi 5 Components: reusable modules, rows, and sections that stay in sync site-wide, with selective sync, slots, the Components Manager, and import/export."
category: builder
tags: [builder, components, slots, global-elements, library]
related: [../modules/the-slot-module-in-divi-5.md, presets.md, multi-select-bulk-editing.md]
divi_version: "5.15+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/17438180-components-in-divi-5"
---

# Components in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A component is a module, row, or section you save once and reuse across the site. Every copy (an *instance*) stays linked to the original.
    **Introduced in:** Divi 5.15. Components replace the global modules (global elements) of earlier Divi versions; existing global modules became components automatically.
    **Key idea:** Settings are *synced* by default. You choose which settings each instance may override (*selective sync*), and a **Slot** module lets each instance hold its own content.
    **Where to manage them:** the **Components Manager** in the Visual Builder left sidebar, next to the Preset Manager.

## What changed from global modules

| Global modules (older) | Components (Divi 5.15+) |
|---|---|
| Unsyncing a setting left it empty on the copy | An editable setting starts with the component's value; a copy differs only where you change it |
| Whole module only | Selective sync works on every element inside a section or row component |
| No partial detach | Detach one module inside a component, then re-attach it later |
| Edit the global in place | Separate **component editing mode** (like editing a preset) |
| No bulk management | Components Manager: search, filter, duplicate, reorder, delete, import, export |
| Single content per module | **Slots** let each instance hold unique content |
| Could not nest | Components can be nested inside other components |

## Creating a component

Anything except the Post Content module can become a component: any module, a row, or a section. Columns cannot be saved alone; save the row that contains them.

1. Right-click the element (or use its three-dots menu) and choose **Save To Library**.
2. Name it clearly. This name is how you find it later. Optionally add categories or tags.
3. Turn on **Save as Component** and click **Save To Library**.

Alternatives:

- **From the settings panel:** click the element's name at the top (tooltip *Manage Component*) and choose **Save as Component**.
- **From the Divi Library:** *WordPress Dashboard → Divi → Divi Library → Add New*, choose Module, Row, or Section, tick **Save as Component**, then **Edit With The Divi Builder**. The Library list has a **Component** column and a **Scope** filter (All Scopes, Component, Not Component).

Components are stored in the Divi Library.

### Convert an existing element

Open the element's settings, click its name to open **Manage Component**, and pick a component under **Convert to Component**.

- Only components of the same type are listed (Button → Button component, row → row component, section → section component).
- The element takes the component's design and content. Settings the component marks as editable keep the values the element already had.
- An existing instance can be swapped for a different component of the same type the same way.
- The conversion is recorded in History as *Converted to Component*, so Cmd/Ctrl + Z restores the original.

## Recognizing components

Components show a purple hover outline and toolbar, appear purple in Wireframe view and the Layers panel, and show the component's name (with a link icon) in the settings header instead of the module name.

## Instance mode vs. component editing mode

Opening a component's settings always starts in **instance mode**.

| | Instance mode | Component editing mode |
|---|---|---|
| Affects | This copy only | Every copy on the site |
| Visible settings | Only settings the component lets copies change | Everything, including presets |
| Look | Purple link icon in the header | Purple color scheme; **Component Settings** group with a **Component Title** field |
| Buttons | none | **Save** and **Cancel** at the bottom |

If the component allows no overrides, instance mode shows: *This component doesn't have any unsynced settings.* Use **Edit Component** to switch modes.

### Edit a component from the page

1. Open a copy's settings, click the component name (*Manage Component*), and choose **Edit Component** (or select the component and click the **Edit Component** button).
2. Change any setting, or add, move, or remove elements inside it.
3. Click **Save**, then **Confirm** on *This will update all instances across your entire site.*

**Cancel** undoes everything since you entered editing mode. Clicking away, closing the panel, or opening another panel with unsaved changes triggers the same confirmation.

While editing, Divi keeps a separate undo history (first step *Loaded Component*). Cmd/Ctrl + Z steps through component changes only, and the history clears on save or cancel.

!!! warning "Structure changes edit the component"
    Adding, moving, duplicating, or deleting elements *inside* a component instance on a page changes the component itself, and therefore every copy on the site.

## Selective sync

By default every setting is synced, so all copies look identical. To let copies differ:

1. Enter component editing mode.
2. Hover a setting's label and click the small **link icon** next to it. The setting is now *editable on instances*. Click again to share it (tooltip *Use Component Value*).
3. Click **Save**, then **Confirm**.

Rules:

- Sync is chosen **per setting**. There is no switch for a whole option group; a group shows on copies as soon as one of its settings is editable.
- On a copy, editable settings start with the component's value. If you later change that value in the component, every copy that hasn't overridden it updates too.
- Reset an override with the setting's reset icon or the right-click menu.
- On a copy, right-click actions (Reset, Paste, Extend Attributes) affect that copy only, never the component.
- **List modules (Accordion, Tabs, etc.):** in component editing mode the item list has its own link icon (*Make Editable on Instances*). Turn it on and each copy can add, remove, and reorder items separately while the design stays shared.
- **Sections and rows:** every module, row, and column inside the component can have its own editable settings. Open that inner module's settings, choose **Edit Component** from its name menu, and set the link icons.

### Detach part of a component

You can detach one module inside a component so it is fully editable on that page, and attach it again later. See the official guide linked below for the exact controls.

## Slots

The [Slot module](../modules/the-slot-module-in-divi-5.md) is placed inside a component to mark an area where each instance supplies its own content. This is also how components are nested inside other components.

## The Components Manager

Open it from the left sidebar icon right after the Preset Manager icon. The window can be dragged, resized, expanded, or docked like other Visual Builder panels.

- **Visibility:** the icon appears only for roles allowed to use and edit Divi Library items (check *Role Editor* permissions). Users can hide it via *Workspace Settings → Sidebar Icons → Components Manager*.
- **Organization:** grouped by element type (one group per module, plus Rows and Sections), sorted alphabetically; one group open at a time.
- **Find:** the **Search components...** box matches name or module type; the dropdown filters to one element type.
- **Per component:**
    - **Edit Component** opens a separate *Component Preview* (desktop width) with settings already in component editing mode. Rename via **Component Title**, **Save**, **Confirm**, then **Back To Components Manager**. The page you came from is not changed by the preview.
    - **Duplicate Component** creates "Name Copy" as a starting point for a variation.
    - **Delete Component** removes it site-wide. Existing instances may no longer render and this cannot be undone.
- **Reorder:** drag components within a group; order is saved site-wide.
- **Read-only components** show *This Component is read-only.* and cannot be edited or deleted.
- **Import / export:** the Manager can import or export your whole component library; components also travel with exported layouts.

## Divi AI Agent

The [Divi AI Agent](../modules/the-divi-ai-agent-in-divi-5.md) can create components, save existing elements as components, convert matching elements, duplicate them, and update their settings from a plain-language prompt. It stops for approval before destructive changes. It requires a Divi AI subscription.

## Gotchas for implementers and AI assistants

- Changing structure inside an instance changes the component (see warning above); use selective sync or Slots for per-page variation instead.
- Deleting a component can leave instances that no longer render.
- Convert to Component only lists same-type components; if the list is missing, none exist yet.
- Component UI depends on Divi Library permissions; a missing Components Manager icon is usually a role issue.

## Elegant Themes tutorials

- [Introducing Components and Slots for Divi 5](https://www.elegantthemes.com/blog/theme-releases/components-slots)

## Official documentation

- [Components in Divi 5](https://help.elegantthemes.com/en/articles/17438180-components-in-divi-5)
- [How to Create a Component in Divi 5](https://help.elegantthemes.com/en/articles/17438185-how-to-create-a-component-in-divi-5)
- [How to Edit a Component in Divi 5](https://help.elegantthemes.com/en/articles/17438188-how-to-edit-a-component-in-divi-5)
- [How to Use Selective Sync With Components in Divi 5](https://help.elegantthemes.com/en/articles/17438191-how-to-use-selective-sync-with-components-in-divi-5)
- [The Components Manager in Divi 5](https://help.elegantthemes.com/en/articles/17438193-the-components-manager-in-divi-5)
- [The Slot Module in Divi 5](https://help.elegantthemes.com/en/articles/17438196-the-slot-module-in-divi-5)
