---
title: "Part 2: Exploring Every Aspect of the Divi 5 Interface"
description: "A tour of the Divi 5 Visual Builder: Page Bar, Builder Bar, Canvas, and Sidebar, with the tools and settings each one holds."
category: modules
tags: [modules, visual-builder, interface, course]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15501608-part-2-exploring-every-aspect-of-the-divi-5-interface"
---

# Part 2: Exploring Every Aspect of the Divi 5 Interface

!!! abstract "Quick Reference"
    **Course position:** Part 2 of the 16-part Divi 5 Mastery Course. Previous: [Part 1](part-1-what-to-prepare-before-building-your-divi-5-website.md). Next: [Part 3](part-3-creating-a-divi-5-global-design-system-with-design-variables.md).
    **Four areas:** Page Bar (top), Builder Bar (left), Canvas (center), Sidebar (right).
    **Customizable:** Panels can be docked left or right, grouped into tabs, or floated. Workspaces store per-user layouts.

## The Page Bar (top)

The fixed top toolbar for page-level actions.

- **Gear menu:** page settings, save to library, import/export, clear layout, edit history, and recently edited pages.
- **Canvas navigation:** every page has a Main Canvas, and you can add detached canvases. Use them as staging areas or as the basis for off-canvas elements such as popups, slide-ins, and mega menus. The **Canvas Select** dropdown jumps between them; **Grid View** shows all at once.
- **Responsive tools:** Desktop, Tablet, and Phone are on by default. The ellipsis menu reveals the other breakpoints (seven in total). Drag the Canvas edge to resize, or type an exact width such as 360px in **Responsive Select**.
- **Actions and publishing** (some must be enabled in the current Workspace):
    - Undo/Redo and the History panel.
    - Export a layout as JSON (including global canvases), import one, **Clear Layout**, or **Add To Library** (including to Divi Cloud).
    - Preview Mode, the Exit menu, and Save (publish, or set to draft, pending, or private).

## The Builder Bar (left)

| Tool | What it does |
|---|---|
| Add Layout / Divi Library | Insert premade layouts, saved library items, or a Divi AI layout. |
| Layers View | Searchable tree of every element; expand, collapse, rename, jump. |
| Inspector | Overview of an element's colors and fonts for bulk editing across many elements. |
| Variable Manager | Hub for Design Variables (colors, fonts, numbers, text, images, links), including relative colors in HSL and values like `clamp()` in number variables. |
| Preset Manager | Central home for Element Presets (whole module) and Option Group Presets (one settings group, such as Box Shadow or Typography). |
| Page Manager | Search all pages, posts, and projects and open any in the Builder; speculative prerendering preloads likely next pages. |
| Command Center | Type to act. Enter a module name and press Enter to add it; chain commands such as `row > column > blurb > button` with Cmd + Return between steps. |
| Wireframe View | Hides styling to focus on hierarchy. |
| Action Icons On Hover / Parent Action Icons On Hover | Reduce visual noise by showing edit buttons only on mouseover. |
| X-Ray Mode | Keeps content visible but outlines every element, useful for spacing conflicts. |
| Workspaces | Personalize the interface: default view mode, history interval, settings modal position, page creation flow, page bar icons, disabled-module opacity, closed toggles, placeholder content, prerendering, interface mode, color scheme, Theme Builder layouts, and admin bar. |
| Help | Video tutorials and keyboard shortcuts. |
| Light/Dark Mode | Changes the interface theme only, not your site. |

## The Canvas (center)

The Canvas is a detached workspace showing what visitors will see.

- **Right-click menus:** on any section, row, column, or module: duplicate, move, delete, copy, paste, inspect, add above/inside/below, reset, save to library.
- **Extend Attributes:** push styles, content, and presets across the layout. Choose a whole option group or only **Modified Fields**, and scope from one module group to the whole page, even across module types (for example, a Contact Form's button styling onto standalone Buttons).
- **Copy and Paste Attributes:** copy parts of an element and paste all attributes, only styles, only content, or an applied preset.
- **Style Inspector:** lists every color, font, spacing value, content item, and preset in the selected area. Change a color once and all uses update.
- **Multi-select:** Shift-click several modules and drag them as a group.
- **One-click editing:** clicking a module opens its settings in the Sidebar immediately.

## The Sidebar (right)

Shows controls for the current selection, or **Page Settings** when nothing is selected.

- **Breadcrumbs** jump from a module to its Column, Row, or Section.
- **Element Presets** sit beside the module name: apply, or create from current styles.
- **Responsive State Picker** chooses breakpoint, hover state, or sticky state. Each panel has a search bar and filters for modified fields and variables in use.

### Content tab

- **Elements:** nested modules, such as a Button inside a Blurb.
- **Loop:** turns an element (Column, Row, Group, Link module, and others) into a repeating loop of dynamic content.
- **Apply Structure Template** (Row): redefine columns per breakpoint.
- **Order** (Column): change display order on smaller screens.
- Responsive Editor, Dynamic Content, and Divi AI icons appear over applicable fields.

### Design tab

- **Composable settings:** add Background, Sizing, Spacing, Border, and more to sub-elements that lacked them, via the composable settings icon beside a group like Title Text.
- **Advanced units:** spacing, sizing, and typography fields accept `clamp()`, `calc()`, `min()`, `max()`, or a Design Variable.
- **Flexbox** (Layout menu): Layout Direction, Wrap, Justify Content, Align Items, Gap.
- **CSS Grid:** two-dimensional layouts that can be redefined per breakpoint.

### Advanced tab

- **Custom Attributes:** HTML attributes such as data attributes or aria-labels.
- **Semantic Elements and Custom HTML Wrappers:** swap div wrappers for tags like article, aside, or nav, and inject HTML before and after an element. Related CSS goes in the page-level Custom CSS field.
- **Interactions:** translate, scale, rotate, or tilt animations triggered by mouse movement; combined with Canvases they can open popups, slide-ins, and mega menus.

## Official documentation

[Part 2: Exploring Every Aspect of the Divi 5 Interface](https://help.elegantthemes.com/en/articles/15501608-part-2-exploring-every-aspect-of-the-divi-5-interface)
