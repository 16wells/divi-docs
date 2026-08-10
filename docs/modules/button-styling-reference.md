---
title: "Button Module — Styling Reference"
category: modules
tags: [button, hover, presets, css-classes, styling, design-system, custom-css]
related: [button, design-system-setup, global-elements]
divi_version: "5.x"
last_updated: 2026-08-10
source_url: "https://help.elegantthemes.com/en/articles/10259665-the-button-module-divi-5"
---

<!-- AUTO-UPDATED: 2026-08-10 — verify changes -->

# Button Module — Styling Reference

Comprehensive guide to styling buttons in Divi 5 using hover states, custom CSS, presets, and the visual design system.

## Overview

Divi 5 fundamentally changed button styling from Divi 4. Hover state controls moved into the Responsive Editor, CSS classes now live in the Attributes panel, and the visual preset system replaces most custom CSS use cases.

This page covers four approaches to button styling:

1. **Visual Design Tab** — built-in style properties with instant preview
2. **Hover States** — responsive editor workflow for interactive effects
3. **Button Presets** — reusable, stackable style sets for design systems
4. **Custom CSS** — for specialized effects not covered by the Design tab

<!-- TODO: Screenshot showing a styled button with active hover state in Visual Builder -->

## Settings & Options

### Design Tab — Button

The **Design → Button** panel contains all visual styling controls for the button element.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Use Custom Styles for Button | Toggle | OFF | Enable to unlock design properties. When OFF, the button uses default theme styles. When ON, all properties below become editable. |
| Button Background Color | Color | Theme default | Primary background color of the button. Supports solid colors and gradients. |
| Button Background Color (Hover) | Color (Responsive) | Inherited | Background color when cursor hovers over button. Set via Responsive Editor. Common use: darken or lighten on interaction. |
| Button Text Color | Color | Theme default | Text/label color on the button. |
| Button Text Color (Hover) | Color (Responsive) | Inherited | Text color on hover. Often changes for contrast when background darkens. |
| Button Border Style | Select | Solid | Visual style of the border: Solid, Dashed, Dotted, Double, Groove, Ridge, Inset, Outset. |
| Button Border Color | Color | Theme default | Color of the border outline. |
| Button Border Color (Hover) | Color (Responsive) | Inherited | Border color on hover. Useful for emphasis effects. |
| Button Border Width | Range (px) | 0px | Thickness of the border. 0 = no visible border. |
| Button Border Radius | Range (px) | Theme default | Corner rounding on the button. 0 = sharp corners, higher values = rounder. |
| Button Border Radius (Hover) | Range (Responsive) | Inherited | Border radius on hover. Allows subtle shape changes. |
| Button Box Shadow | Text/Select | None | Drop shadow effect. Supports custom shadow values (e.g., `0 4px 8px rgba(0,0,0,0.2)`). |
| Button Box Shadow (Hover) | Text/Select (Responsive) | None | Shadow on hover. Common use: add depth or glow on interaction. |
| Button Letter Spacing | Range (px) | 0px | Space between letters in button text. Useful for emphasis or visual weight. |
| Button Icon | Icon picker | None | Icon displayed inside button (before or after text). |
| Button Icon Color | Color | Inherit text color | Color of the icon element. |
| Button Icon Color (Hover) | Color (Responsive) | Inherit | Icon color on hover. Usually matches text color change. |
| Button Text Transform | Select | None | Letter case transformation: Uppercase, Lowercase, Capitalize, None. |
| Button Font Size | Range (px) | Theme default | Size of button text. |
| Button Font Weight | Select | Theme default | Text weight: 300, 400, 500, 600, 700, 800, 900. |
| Alignment |  | Choose the Button module's alignment on the page. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall Button module's text styles for this module. <!-- AUTO-ADDED --> |
| Button |  | Choose the Button module's design styles. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Button module's spacing. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Button module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Button module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Button module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Button module's animation styles, adding personality and interactivity while keeping a polished, professional feel. <!-- AUTO-ADDED --> |

### Responsive Editor — Hover States

The **Responsive Editor** (accessed by clicking the icon next to any style property) manages device breakpoints AND hover states in a single panel.

| Breakpoint | Icon | Purpose |
|-----------|------|---------|
| Desktop | Monitor | Styles for screens >992px wide. Default baseline. |
| Tablet | Tablet | Styles for screens 768px–992px wide. Inherits from Desktop if not set. |
| Mobile | Phone | Styles for screens <768px wide. Inherits from Tablet if not set. |
| Hover | Pointer/Cursor | Interactive states for all devices. Applied when cursor enters the button. Always the bottom row. |

**Key behavior:** If you set a property on Desktop but leave Tablet blank, the Tablet view uses the Desktop value. Hover states work on all devices when CSS hover is available (desktop/tablet); mobile uses touch states.

### Advanced Tab — Attributes

Custom HTML attributes (including CSS classes) are added here, not via a dedicated CSS panel.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Add Attribute | Button | — | Click to add a new key-value pair. Each attribute is a separate row. |
| Attribute Name | Text | — | The attribute name (e.g., `class`, `data-tracking`, `aria-label`). |
| Attribute Value | Text | — | The attribute value (e.g., `light-cta`, `button-click`, `Shop now`). |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Button module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| HTML |  | Choose the semantic HTML tag for the Button module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Interactions |  | Create custom interactions, such as showing or hiding the Button, and many more. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Button's module visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long Button's module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Button's module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Button module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

### Advanced Tab — Custom CSS

The **CSS → Free-Form CSS** area allows module-specific CSS rules.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Free-Form CSS | Text area | (empty) | Raw CSS rules applied only to this button. Use the `selector` keyword to target the button without knowing its generated class. Example: `selector { color: red; }` |

## How to Set Hover States

Hover states are not on a separate tab — they live in the **Responsive Editor**, accessed from any style property you want to change on hover.

### Step-by-Step: Add a Hover Effect

1. Open the **Button module settings**.
2. Go to **Design → Button** and toggle **"Use Custom Styles for Button"** to **ON**.
3. Choose a property to change on hover (e.g., **Button Background Color**).
4. Click the **Responsive Editor icon** (next to the color picker).
5. The editor opens with **four rows:**
   - Desktop (monitor icon)
   - Tablet (tablet icon)
   - Mobile (phone icon)
   - **Hover** (pointer icon — bottom row)
6. Set your hover value in the **bottom "Hover" row**.
7. Click **OK** to close the Responsive Editor.

**Example hover effects:**

| Property | Desktop Value | Hover Value | Effect |
|----------|---------------|------------|--------|
| Button Background Color | `#0066CC` (blue) | `#004499` (darker blue) | Darkens on hover |
| Button Text Color | `#FFFFFF` (white) | `#FFDD00` (yellow) | Text lightens on hover |
| Button Box Shadow | `none` | `0 4px 12px rgba(0,0,0,0.3)` | Adds shadow on hover (depth) |
| Button Border Width | `0px` | `2px` | Reveals border on hover |

<!-- TODO: Screenshot of Responsive Editor showing desktop, tablet, mobile, and hover rows -->

!!! tip "Hover Is Always the Bottom Row"
    Scroll down in the Responsive Editor if you don't see the Hover row — it's always present for properties that support it.

## Creating and Using Button Presets

Presets are named, reusable style sets. Once created, apply them to any button, and update all instances instantly by editing the preset.

### Step-by-Step: Create a "Light Button" Preset

1. Add a **Button module** to your page.
2. Go to **Design → Button** and toggle **"Use Custom Styles for Button"** to **ON**.
3. Set **default state styles:**
   - Button Background Color → `#FFFFFF` (white)
   - Button Text Color → `#000000` (black)
   - Button Border Color → `#CCCCCC` (light gray)
4. Set **hover state styles** (via Responsive Editor):
   - Button Background Color (hover) → `#F5F5F5` (off-white)
   - Button Text Color (hover) → `#000000` (stays black)
   - Button Border Color (hover) → `#999999` (darker gray)
5. At the **top of the settings panel**, click the **Preset dropdown** (icon next to "Button Module").
6. Select **"Create New Preset From Current Styles"**.
7. Name it (e.g., `Light Button`, `Button - Light on Dark`, `CTA Primary`).
8. Click **Save Preset**.

The preset is now saved and available to apply to any button on the site.

<!-- TODO: Screenshot of Preset dropdown showing "Create New Preset From Current Styles" option -->

### Applying a Preset to Other Buttons

1. Add or open a **Button module**.
2. Click the **Preset dropdown** at the top of settings.
3. Select your **"Light Button"** preset.
4. All default and hover styles apply instantly.

### Editing a Preset Globally

1. Open any button that uses your preset.
2. In the **Preset dropdown**, hover over the preset name and click the **gear icon**.
3. The settings panel enters **Global Preset editing mode** (gray/distinctive header).
4. Change any properties.
5. Click **"Save Preset"** — **all instances using this preset update site-wide**.

!!! warning "Preset Editing Mode"
    When you're editing a preset globally, the changes apply to EVERY button using that preset. Be intentional and save only when ready. To avoid global changes, edit a single button by choosing **"Use Custom Styles for Button"** without selecting the preset.

### Set a Default Preset

If one button style is used most often:

1. Open the **Preset dropdown**.
2. Hover over the preset name.
3. Click the **star icon** to mark it as default.

From then on, every new Button module uses that preset automatically.

## Stacked Presets — Combining Multiple Style Sets

Divi 5 allows applying **multiple presets** to the same button. Later presets override earlier ones for the same property.

### Example: Base + Color Variant

| Preset Name | Controls |
|-------------|----------|
| **"Button Base"** (Preset 1) | Font size: 16px, Padding: 12px 24px, Border radius: 4px, Icon |
| **"Light Variant"** (Preset 2) | Background: white, Text color: dark gray |

**Workflow:**
1. Create "Button Base" with sizing and shape properties.
2. Create "Light Variant" with only color properties.
3. Apply both presets to the same button.
4. The button gets base sizing + light colors.
5. Later, edit "Button Base" padding — all buttons (light, dark, accent variants) update together.

### When to Use Stacked Presets

- You have **multiple color treatments** (light, dark, accent, secondary) but want consistent sizing across all of them.
- You want to **separate structural styles** (padding, radius, font size) from **color styles** (background, text color, border).
- You're building a **design system** with base + modifier patterns.

For a comprehensive design system guide with nested presets and Option Group Presets, see the [Design System Setup Playbook](../playbooks/design-system-setup.md).

## Adding Custom CSS Classes

CSS classes for buttons are added via the **Attributes** panel, not a dedicated CSS Classes toggle (that was Divi 4 workflow).

### Step-by-Step: Add a Custom Class

1. Open the **Button module settings**.
2. Go to **Advanced → Attributes**.
3. Click **"Add Attribute"**.
4. Set **Attribute Name** to `class`.
5. Set **Attribute Value** to your class name (e.g., `light-cta`, `shop-button`, `call-to-action-primary`).
6. Click **Save** or **OK**.

### Targeting Custom Classes with CSS

Once you add a class via Attributes, target it in your **page custom CSS** or **theme custom CSS**:

```css
.light-cta {
  background-color: #ffffff !important;
  color: #000000 !important;
  border-color: #ffffff !important;
}

.light-cta:hover {
  background-color: #f0f0f0 !important;
}
```

!!! note "Presets vs. Custom CSS Classes"
    In most cases, a **Button Preset** is better than custom CSS classes because:
    - Presets are managed visually in the editor — no CSS knowledge needed.
    - Changes propagate instantly to all instances.
    - No `!important` overrides required.
    - Easier for teams to collaborate and maintain.
    
    Use custom CSS classes for edge cases (special interactions, third-party integrations, accessibility customizations) not available via the Design tab.

### Migrating Divi 4 CSS Classes to Divi 5

If you're upgrading from Divi 4, any CSS ID or class values carry over automatically. They appear in the **Attributes** list when you open the element in Divi 5. No manual migration required.

## Custom CSS in the Module

The **Advanced → CSS → Free-Form CSS** area adds styles scoped to just this button.

### Using the `selector` Keyword

Instead of knowing the button's generated class name, use the `selector` keyword to target the button:

```css
selector {
  background-color: #ffffff;
  color: #000000;
}

selector:hover {
  background-color: #f0f0f0;
}
```

### Common Custom CSS Patterns

**Add a smooth color transition:**

```css
selector {
  transition: background-color 0.3s ease, color 0.3s ease;
}
```

**Create a glowing effect on hover:**

```css
selector:hover {
  box-shadow: 0 0 12px rgba(0, 102, 204, 0.5);
}
```

**Uppercase text with letter spacing:**

```css
selector {
  text-transform: uppercase;
  letter-spacing: 1px;
}
```

## Troubleshooting

### "Identifier is expected" Error in Custom CSS

This error appears in the **Free-Form CSS** area when CSS syntax is invalid. Most common cause is a **trailing comma** after a selector:

```css
/* ❌ WRONG — trailing comma expects another selector */
selector,
{
  background-color: #ffffff;
}
```

**Fix:** Remove the trailing comma or separate into distinct rule blocks:

```css
/* ✅ CORRECT */
selector {
  background-color: #ffffff;
}

selector:hover {
  background-color: #f0f0f0;
}
```

### Hover States Not Working on Mobile

Hover states rely on CSS `:hover` pseudo-class, which doesn't exist on touch devices. On mobile:

- Hover styles are ignored.
- Use `:active` (while tapping) or JavaScript for mobile interactivity.
- Desktop/tablet users see full hover effects.

If you need button feedback on mobile, use a separate mobile preset or consider a Focus Ring for keyboard users.

### Custom Class Not Being Applied

If a custom class (set via Attributes) isn't working:

1. **Verify the class name** — check for typos in Attributes.
2. **Check CSS specificity** — your custom CSS may need `!important` if theme styles are stronger.
3. **Use the Browser Inspector** — right-click the button, select "Inspect," and confirm the class is in the HTML.

Example with higher specificity:

```css
.light-cta.light-cta {  /* Double selector increases specificity */
  background-color: #ffffff;
}
```

### Button Preset Changes Aren't Updating

If you edited a preset globally but some buttons aren't updating:

- **Confirm edit mode:** when editing a preset, the settings panel header should show "Global Preset editing mode" or similar.
- **Save after changes:** click **"Save Preset"** button (not "Save Button" or other save).
- **Hard refresh:** reload the page in the browser to clear cached styles.

## Common Patterns

### Pattern: Ghost Button (Outline Only)

| Property | Value |
|----------|-------|
| Use Custom Styles | ON |
| Button Background Color | Transparent |
| Button Text Color | `#0066CC` (blue) |
| Button Border Style | Solid |
| Button Border Width | 2px |
| Button Border Color | `#0066CC` (blue) |
| Button Background Color (Hover) | `#E6F0FF` (light blue) |

Result: Bordered button with transparent fill, fills lightly on hover.

### Pattern: Icon + Text Button

| Property | Value |
|----------|-------|
| Button Icon | (choose an icon) |
| Button Text | "Shop Now" |
| Button Icon Color | Inherit text color |
| Button Font Size | 16px |
| Button Padding | 12px 24px |

Result: Icon appears next to text with aligned styling.

### Pattern: Gradient Button

| Property | Value |
|----------|-------|
| Use Custom Styles | ON |
| Button Background Color | Gradient (blue → purple) |
| Button Text Color | `#FFFFFF` (white) |
| Button Background Color (Hover) | Gradient (purple → dark purple) |

Result: Smooth color transition on hover with gradient depth.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. Divi 4 used a different approach to button styling (CSS Classes toggle, legacy preset system). For Divi 4, refer to the official Elegant Themes documentation.

## Related

- [Button Module](../modules/button.md) — full button module reference
- [Design System Setup Playbook](../playbooks/design-system-setup.md) — advanced preset strategies and global styling
- [Global Elements](../builder/global-elements.md) — saving buttons as reusable global modules
- [CSS Reference](../css-reference/index.md) — custom CSS selectors and override techniques
