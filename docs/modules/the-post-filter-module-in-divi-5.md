---
title: "The Post Filter Module in Divi 5"
description: "The Divi 5 module that builds a front-end filter form to refine a Loop on the page, with search, taxonomy, price, and sorting controls."
category: modules
tags: [modules]
related: []
divi_version: "5.10+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/16186978-the-post-filter-module-in-divi-5"
---

# The Post Filter Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A filter form that narrows the results of a [Loop](https://help.elegantthemes.com/en/articles/11863867-loop-builder-in-divi-5) already on the page. Visitors can search, tick categories, set a price range, or change the sort order.
    **Structure:** Each control is its own **Post Filter Item** child module; add, remove, and reorder them freely.
    **Key rule:** The module creates no content. You must build a looped element first, then point **Target Loop** at it.

New modules start with a Search field, a Category checkbox list, a Reset button, and an Apply button so the form is visible immediately. For the details of each item type, see [The Post Filter Items in Divi 5](the-post-filter-items-in-divi-5.md).

## Add the module

1. In the Visual Builder, click the green plus icon to insert a Row into the Section.
2. Click the gray plus icon inside the Row to open the module list.
3. Find **Post Filter** (or search for it) and click it.
4. Connect it to a Loop (see below).

## Use cases

- **Filterable blog archives:** narrow a post loop by category, tag, or author, plus keyword search.
- **Product catalogs:** on a WooCommerce product loop, offer a price range slider, stock status filter, and review rating filter.
- **Team and staff directories:** filter a user loop by name or username and sort by display name.
- **Custom post type listings:** filter properties, events, or recipes by custom fields such as price, date, or capacity.
- **Sortable listings:** an **Order By** dropdown lets visitors re-sort a loop without reloading the whole page.

## Connect the module to a loop

1. Build the content to filter and turn on the **Loop** option group on that Section, Row, Column, or module.
2. Give the looped element a clear label in its **Meta** group; loops are listed in the dropdown by their module label.
3. Add the Post Filter module above, beside, or below the loop.
4. In the Post Filter's **Content** tab, open the **Target** group and pick the loop from **Target Loop**.
5. Choose an **Apply Mode**:
    - **Submit** waits for a button click and reloads the page with the filters in the URL.
    - **Auto** updates the loop as the visitor types or ticks a box, with no page reload.
6. Choose a **Relation**: **And** narrows results with every filter, **Or** widens them.

Filtered results are stored in the page URL, so a filtered view can be bookmarked and shared. A Pagination module targeting the same loop stays in sync with the active filters and returns to page one whenever they change.

!!! note
    More than one Post Filter module can point at the same loop and they stay in sync. Filters on one loop never affect another loop on the same page.

## Content tab

| Setting | Description |
|---|---|
| Target Loop | The loop this form controls. Lists every loop on the current page by label; there is no default. Unlike the Pagination module, it cannot target the main query. Until you pick one, the module shows "Select a Loop" and does nothing |
| Apply Mode | **Submit** (default) applies filters when the visitor clicks the submit button; **Auto** updates as soon as a control changes |
| Relation | **And** (default) requires every filter to match; **Or** requires at least one |
| Elements | Add, edit, duplicate, reorder, and delete the Post Filter Items that make up the form |
| Background | Background styles |
| Loop | Enables the Loop Builder on the Post Filter module itself. This repeats the filter form; it does not choose what the form filters |
| Order | Position in a Flexbox or Grid layout |
| Meta | Label text and forced visibility inside the Visual Builder |

### Add, edit, and delete items

1. Click the module (or its gear icon) to open its settings.
2. **Edit:** click the pencil icon next to an item.
3. **Add:** in the **Content** tab, click **Add New Post Filter Item**.
4. **Duplicate:** click the duplicate icon (copies settings and styling).
5. **Delete:** click the trash icon.

Drag the handle at the left edge of an item to reorder the controls.

!!! note
    Every form needs a **Submit** item unless Apply Mode is **Auto**. A **Reset** item is optional but recommended; it clears the filters for this loop only and leaves the rest of the page's query untouched.

## Design tab

Styling set here applies to every Post Filter Item, and each item can override it.

| Setting | Description |
|---|---|
| Layout | Layout Style: Block, Flex (default), or Grid |
| Field | Styling for text inputs, number inputs, and dropdowns, plus **Label Text** typography |
| Option | Styling for checkbox and radio option rows: Background, Border, Box Shadow, Sizing, Spacing |
| Checkbox | Checkbox field types and their labels |
| Radio Options | Radio button field types and their labels |
| Multiple Order Button | The small add and remove buttons inside a Multiple Order control |
| Button | The submit and reset buttons |
| Sizing, Spacing, Border, Box Shadow | Standard option groups |
| Filters | Hue shifts, saturation changes, blend modes |
| Transform | Scale, rotate, skew, translate |
| Animation | Animation styles |

## Advanced tab

| Setting | Description |
|---|---|
| Attributes | CSS ID, reusable CSS classes, or custom HTML attributes |
| CSS | Custom CSS for the module |
| HTML | Semantic HTML tag |
| Conditions | Show content based on conditions |
| Interactions | Custom interactions such as showing or hiding the module |
| Visibility | Visibility per device |
| Transitions | Duration of animations |
| Position | Precise placement |
| Scroll Effects | Behavior during scrolling |

## Post Filter Item settings

Each item has its own Content, Design, and Advanced tabs. The Content tab holds a single **Field** group whose contents depend on the field type and the parent's loop type.

### Field Type

| Type | Behavior |
|---|---|
| Text | A single input. **Field Value Type** switches it between keyword search, number input, or a date, date-time, or time picker |
| Select, Radio | A dropdown or radio list; the visitor picks one value |
| Checkbox | A checkbox list; the visitor can pick several values |
| WooCommerce: Price Range, Stock Status, Review Rating | Only available when the target loop is a WooCommerce product loop |
| Sort options: Order By, Order, Multiple Order | Let visitors change how the loop is sorted; Multiple Order allows up to five stacked sort rules |
| Button: Submit, Reset | The form's action buttons |

A post type loop offers all types. A taxonomy, user, or menu loop offers only Text, Order By, Order, Submit, and Reset. WooCommerce types appear only on a product loop with WooCommerce active. If you change the parent's Target Loop to one that does not support an item's field type, Divi resets that item to Text.

### The rest of the Field group

These settings appear only when they apply to the chosen field type.

| Setting | Description |
|---|---|
| Field Label | Label above the control. On Submit and Reset items it is named **Button Text** and becomes the button label. Divi fills it in automatically; you can overwrite it |
| Field Value Type | How input is collected and compared: Text, Number, Date, Date Time, or Time (Text, Select, Radio, Checkbox types) |
| Field Option | The data source being filtered, such as a taxonomy, the post author, or a custom field (Select, Radio, Checkbox) |
| Field Value | The same setting as Field Option under another name, for the Text type: what the keyword, number, or date is matched against |
| Meta Key | The custom field meta key, used when Field Option or Field Value is set to a manual custom field |
| Field Placeholder | Hint text for Text items using the Text or Number value type. Falls back to the Field Label, then to "Search". Hidden for date and time pickers |
| Field Comparison | How the input is compared to the stored value (equals, not equals, greater than, contains, and so on). Matches the Compare options in the Loop builder's Meta Query. Shown for number, date, date-time, and time values, and for custom field Select and Radio items |
| Label Date Format | A PHP date format string (for example `M j, Y`) that makes date option labels readable. Changes only labels, not submitted values |
| Options Method | How a custom-field list is populated. **Automatic** discovers distinct database values at render time and caches them for a day; **Manual** lets you define the list |
| Clear Cached Options | Empties the cache so the next page load rediscovers values (Automatic only) |
| Generate Options | Fetches distinct values from the database into the Options list (Manual only) |
| Options | Sortable list of choices for a manual Select, Radio, or Checkbox; each row has a **Value** (submitted) and a **Label** (shown to visitors) |
| Order By Options | Which sort choices visitors can pick, for Order By and Multiple Order items. Switching to those types ticks the core post options automatically and leaves custom field groups unticked |

!!! tip
    Automatic option discovery warns you when a custom field has many unique values or records behind it. When you see that warning, switch Options Method to Manual, click Generate Options, and trim the list to the values that matter.

### Style an individual item

Each item has its own Design tab with Layout, Field, Option, Checkbox, Radio Options, Multiple Order Button, Button, Sizing, Spacing, Border, Box Shadow, Filters, Transform, and Animation groups, plus the full Advanced tab. Anything set on the item beats the same setting on the parent. To return to the parent's settings, click the arrow icon at the top left of the modal. Use an item's **Sizing** group to control its width; that is how the starter form places Reset and Apply side by side.

Save the page with `CMD + S` (Mac) or `CTRL + S` (PC), or use the **Save** and **Exit** buttons.

## Official documentation

- [The Post Filter Module in Divi 5](https://help.elegantthemes.com/en/articles/16186978-the-post-filter-module-in-divi-5)
