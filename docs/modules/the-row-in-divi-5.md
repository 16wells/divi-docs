---
title: "The Row in Divi 5"
category: modules
tags: ["modules", "row", "layout", "columns", "grid", "responsive"]
related: ["the-section-in-divi-5", "advanced-styling-using-option-group-presets-in-divi-5", "element-presets"]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10316106-the-row-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# The Row in Divi 5

The Row is the horizontal container that sits inside a Section and holds columns or modules. Rows control column structure, alignment, spacing, and enable complex multi-column layouts on your pages.

!!! abstract "Quick Reference"
    **What it does:** Organizes content into columns with customizable layouts, spacing, backgrounds, and responsive behavior; sits directly inside a section.
    
    **Block identifier:** `divi/row`
    
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10316106-the-row-in-divi-5)

## Overview

The Row is the intermediate layout container between Sections (which span full-width) and Columns (which hold individual modules). Every visible content area on your page lives inside a row. Rows define how many columns exist, their widths, alignment, spacing, and visual styling.

Think of rows as horizontal "layers" inside your sections. Each row can have a different column structure, background color, spacing, or animation. Rows are where you decide whether content should be displayed in two equal columns, three unequal columns, a sidebar layout, or a full-width single column.

Rows are essential for:
- Creating multi-column layouts (2-col, 3-col, sidebar, etc.)
- Aligning content side-by-side (text + image, feature + icon, etc.)
- Organizing page structure into distinct horizontal bands
- Building responsive designs that reflow on smaller screens

![Row with multiple columns](../assets/screenshots/modules/the-row/overview.png){ loading=lazy }
*A row with three equal columns containing feature cards.*

## Column Structures

Rows support multiple built-in column configurations:

| Structure | Description |
|-----------|-------------|
| **1 Column** | Full-width single column. |
| **2 Equal Columns** | Two columns of equal width. |
| **2 Unequal (2/1)** | Two columns: 2/3 and 1/3 width. |
| **2 Unequal (1/2)** | Two columns: 1/3 and 2/3 width. |
| **3 Columns** | Three columns of equal width. |
| **3 Unequal** | Three columns with custom width ratios (e.g., 1/2, 1/4, 1/4). |
| **4 Columns** | Four columns of equal width. |
| **Specialty Row** | Allows multiple column widths in a single row for advanced layouts. |

You can change the column structure at any time in the Row settings under **Content > Change Column Structure**. Divi will preserve existing column content when changing structures.

## Anatomy

Every row consists of:

| Component | Description |
|-----------|-------------|
| **Container** | The outer wrapper controlling the row's background, spacing, borders, and layout rules |
| **Columns** | Child containers, each holding modules or other content; number and width determined by the row's structure |
| **Modules** | Individual content blocks (Text, Image, Button, etc.) placed inside columns |

## Settings & Options

### Content Tab

| Setting | Description |
|---------|-------------|
| **Change Column Structure** | Switch the row's column layout. Choose from preset structures (1, 2, 3, 4 columns) or specialty rows. |
| **Link** | Make the entire row clickable, directing users to another page or external URL. |
| **Background** | Set the row's background: solid color, image, video, or gradient. |
| **Loop** | Enable the loop builder to repeat the row's content for dynamic data sources (e.g., repeating product cards). |
| **Order** | Control the row's order when the parent section uses Flexbox or Grid layout (useful for responsive reordering). |
| **Meta** | Assign a custom label to the row for easier identification in the builder; force its visibility in the visual editor. |
| Change Column Structure |  | Choose the Row's column structure. <!-- AUTO-ADDED --> |
| Link |  | Make the entire Row clickable, creating a seamless way to direct users to another page, Row, or external site. <!-- AUTO-ADDED --> |
| Background |  | Choose the Row's background styles. <!-- AUTO-ADDED --> |
| Loop |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order |  | Choose the order in which the Row module appears inside a Flexbox and Grid layout. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Row's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

| Setting | Description |
|---------|-------------|
| **Sizing** | Set the row's width (full-width, constrained, custom), height (auto, fixed, min-height), and padding. |
| **Spacing** | Control top, bottom, left, and right padding (internal) and margin (external). |
| **Border** | Define border width, color, style (solid, dashed, etc.), and radius. |
| **Box Shadow** | Add shadow effects (blur, spread, offset, color). |
| **Filters** | Apply CSS filters: hue rotation, saturation, brightness, contrast, blur, opacity, blend modes. |
| **Transform** | Apply 2D/3D transforms: scale, rotate, skew, translate. |
| **Animation** | Choose entrance, loop, or exit animations with customizable timing. |
| Layout |  | Choose how the Row arranges its columns and modules - as a standard block, aFlexbox layout, or aCSS Grid layout. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Row's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Row's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Row's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Row's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Row's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Row's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Row's animation styles. <!-- AUTO-ADDED --> |

### Advanced Tab

| Setting | Description |
|---------|-------------|
| **Attributes** | Add custom CSS ID, classes, or HTML attributes for targeted styling or JavaScript. |
| **CSS** | Write custom CSS code to fine-tune the row's styling. |
| **HTML Tag** | Change the semantic HTML tag (default `div`, can use `section`, `article`, etc.). |
| **Conditions** | Show/hide the row based on user roles, devices, custom fields, or other conditions. |
| **Interactions** | Define custom interactive behaviors: show/hide on scroll, hover, click; parallax effects. |
| **Visibility** | Control visibility per device (hide on mobile, tablet, or desktop). |
| **Transitions** | Set animation duration, delay, and easing. |
| **Position** | Use CSS position properties and offset values (top, left, z-index) for precise placement. |
| **Scroll Effects** | Define scroll-triggered effects: parallax, fade, scale, or custom animations. |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Row, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| HTML |  | Choose the semantic HTML tag for the Row. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Interactions |  | Create custom interactions, such as showing or hiding the Row, and many more. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Row's visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Row's animation takes, adding subtle, impactful animations that enhance user experience and make your Row stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Row's placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Row behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Open the Row setting |  | Click on the Row on your page or click the Gear icon to open its settings. <!-- AUTO-ADDED --> |
| Edit a Column |  | Click thePencil icon(1)next to the Column item you want to update. Modify the title, body content, or design settings as needed. <!-- AUTO-ADDED --> |
| Add a New Item |  | In theContenttab, clickAdd New Column (2). Click the arrow icon at the top left to return to the main Row settings. <!-- AUTO-ADDED --> |
| Duplicate |  | Click on theDuplicateiconto duplicate the selected Column item. <!-- AUTO-ADDED --> |
| Delete Item |  | Click theTrash icon (3)next to the Column item to delete it. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Common Patterns

### Two-Column Content + Image
A popular layout pairing text on the left with an image on the right.

```
Row (2 Equal Columns)
  ├─ Column 1
  │   ├─ Heading
  │   ├─ Text
  │   └─ Button
  └─ Column 2
      └─ Image
```

### Three-Column Feature Cards
Display three feature cards side-by-side, each with an icon, heading, and text.

```
Row (3 Columns)
  ├─ Column 1 (card with icon + title + description)
  ├─ Column 2 (card with icon + title + description)
  └─ Column 3 (card with icon + title + description)
```

### Sidebar Layout
A main content area with a narrower sidebar for widgets or secondary content.

```
Row (2 Unequal: 2/1)
  ├─ Column 1 (wider, main content)
  └─ Column 2 (narrower, sidebar)
```

### Alternating Layouts (Responsive)
Use multiple rows with reversed column orders to create alternating text-image patterns.

```
Row 1 (2 Equal)
  ├─ Column 1 (text)
  └─ Column 2 (image)

Row 2 (2 Equal, reversed via CSS or drag-drop)
  ├─ Column 1 (image)
  └─ Column 2 (text)
```

## Responsive Behavior

Rows adapt to screen size via:

- **Device-specific column structures:** Collapse to fewer columns or single-column on mobile.
- **Padding/margin adjustments:** Reduce spacing on smaller screens for better fit.
- **Column reordering:** Use the `order` property or visual drag-drop to rearrange columns on different devices.
- **Visibility toggles:** Hide/show rows entirely on specific devices.

Configure responsive behavior in the Design tab using device toggles (desktop, tablet, mobile icons).

## Troubleshooting

**Columns are not equal width:**
- Verify the row's column structure is set correctly (e.g., "2 Equal Columns" vs. "2 Unequal").
- Check if custom CSS is overriding column widths.
- Ensure no column has a fixed width that conflicts with the structure.

**Row height is too tall or too short:**
- Check padding/margin settings—these add to the row's height.
- Verify the Height setting in Sizing (auto vs. fixed).
- Inspect child columns for excessive padding.

**Background image not showing:**
- Ensure the image URL is correct and publicly accessible.
- Check background size (cover, contain, custom).
- Verify opacity or overlay is not hiding the image.

**Responsive layout breaking on mobile:**
- Check the device-specific Spacing settings (may have different padding on mobile).
- Verify column visibility toggles are not hiding crucial columns.
- Test in actual mobile browser (not just desktop mobile preview).

**Row not spanning full width:**
- Check the parent section's layout style and max-width settings.
- Verify the row's width setting is set to "Full Width."
- Inspect CSS for conflicting width rules.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 used a different row structure and settings layout.

## Related

- [The Section in Divi 5](../modules/the-section-in-divi-5.md) — Container that holds rows; full-page layout control
- [Advanced Styling Using Option Group Presets in Divi 5](../builder/advanced-styling-using-option-group-presets-in-divi-5.md) — Save and reuse row design patterns
- [Element Presets](../builder/element-presets.md) — Create preset configurations for rows
