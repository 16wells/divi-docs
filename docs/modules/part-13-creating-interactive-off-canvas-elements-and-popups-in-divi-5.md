---
title: "Part 13: Creating Interactive Off-Canvas Elements and Popups in Divi 5"
description: "Part 13 of the Divi 5 Mastery Course: build a local-canvas event notice and a global-canvas email pop-up using visibility, interactions, and cookie display conditions."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15704140-part-13-creating-interactive-off-canvas-elements-and-popups-in-divi-5"
---

# Part 13: Creating Interactive Off-Canvas Elements and Popups in Divi 5

!!! abstract "Quick Reference"
    **What it is:** Part 13 of the Divi 5 Mastery Course. It builds two off-canvas elements: an Event Reminder notice (local Canvas) and an email opt-in pop-up (Global Canvas).
    **Core pattern:** Hide the element by default (Visibility) → reveal it with an Interaction → optionally block it from returning with a cookie Display Condition.
    **Where to start:** The Off Canvas dropdown in the Visual Builder → Add Canvas.

## What a Canvas is

A Canvas is a detached workspace in Divi 5. The main Canvas holds your visible page; additional Canvases hold alternate layouts, hidden UI, off-canvas elements, pop-ups, menus, and experiments. You build in them with the usual Sections, Rows, Columns, Groups, Modules, Presets, and Design Variables. Canvas content can be appended to the front-end page or injected with a [Canvas Portal](https://help.elegantthemes.com/en/articles/14718409-the-canvas-portal-module-in-divi-5) module.

| Type | Scope | Good for |
|---|---|---|
| Global Canvas | Available across the site | Reusable UI such as pop-ups, menus, notification bars |
| Local Canvas | Tied to one page or template | One-off UI for a specific context |

In this tutorial the Event Notice is a local Canvas for the homepage, and the opt-in pop-up is a Global Canvas triggered from the homepage. To show the pop-up elsewhere, add similar trigger interactions on other pages or templates.

## How visibility works

Three features combine to make a Canvas behave like a pop-up, notice, or slide-in:

- **[Visibility settings](https://help.elegantthemes.com/en/articles/10102735-understanding-the-visibility-option-group-in-divi-5):** hide an element by default.
- **[Interactions](https://help.elegantthemes.com/en/articles/11666517-interactions-in-divi-5):** a trigger (Click, Load, Viewport Enter) runs an effect (Show Element, Hide Element, Toggle Visibility, Add Cookie, Remove Cookie) on a target element.
- **Display Conditions:** decide whether an element renders based on user role, device, date, or cookie values.

## Build 1: Event Reminder notice (local Canvas)

A small card pinned bottom-left with a light background, dark border, heading, short description, and close icon. It shows on page load and can be dismissed for the current view; with no cookie set, it can return on a later load.

### Create the Canvas

1. Open the **Off Canvas** dropdown and click **Add Canvas**.
2. Name it (for example Event Notice).
3. Set **Append to Main Canvas** to **Append Below**.
4. Set **Z-index** to `999`.
5. Click **Add Canvas**. The builder switches to editing the new Canvas.

### Section

1. Close the Insert Row modal. In the Section's **Content → Meta → Element Label**, name it Event Notice so it is easy to target.
2. **Content → Background → Color:** the White variable with opacity 0.
3. **Design → Sizing → Max Width:** `min(250px, 40%)`.
4. **Design → Spacing:** Margin bottom, left, and right of `1rem`; Padding top and bottom of `0px`.
5. **Advanced → Position:** Fixed, with Offset Origin bottom left.

### Row and Column

1. Insert a 1 Column Row and apply the **Contained - Dark** element preset.
2. Row background color: the **Background - Light Gray** variable.
3. Row **Design → Sizing:** Width 100%, Max Width none.
4. Row **Design → Border:** the **Outline - Dark** option group preset.
5. Via **Content → Elements**, edit the Column and set **Design → Layout → Vertical Gap** to `1rem`.

### Content

Add an Icon module, a Heading module, and a Text module in the Column.

| Module | Settings |
|---|---|
| Icon | A close icon such as an X; Icon Size 26px; Margin -0.5rem on all sides; Position Absolute with Offset Origin Top Right. |
| Heading | **Subheading** element preset; text "Reminder!". |
| Text | **Small Text** element preset; body text announcing the networking event (Wednesday, August 16th, 4 pm to 6 pm). |

### Close interaction

1. Open the Icon module → **Advanced → Interactions → + Add Interaction**.
2. Set Trigger **Click**, Effect **Hide Element**, Target the Event Notice Section.
3. Save and reload the front end. The notice appears bottom left and disappears on close.

## Build 2: Email opt-in pop-up (Global Canvas)

A centered modal with a headline, reassurance text, a close icon, and an Email Optin form. It is hidden by default, shown when a visitor reaches a chosen homepage section, and blocked from returning once closed.

### Create the Canvas

1. From the Off Canvas dropdown click **Add New Canvas** and name it Sign Up Pop-up Form.
2. Turn on **Make Global**.
3. Set **Append to Main Canvas** to **Append Below** and **Z-index** to `1000`.
4. Click **Add Canvas**.

### Section

1. Close the Insert Row modal.
2. **Background:** the Background - Light Gray variable.
3. **Content → Meta → Element Label:** Subscribe.
4. **Design → Sizing:** Width `980px`, Max Width `80%`.
5. **Design → Border:** the Outlined - Dark option group preset.
6. **Advanced → Position:** Fixed, Offset Origin Center.

### Row and Columns

1. Add a 1 Column Row and duplicate the Column so there are three.
2. Row **Design → Layout:** Horizontal Gap and Vertical Gap both the Spacing - Medium variable; Layout Wrapping **Wrap**.
3. Row **Design → Sizing → Max Width:** the Max Width - 900 variable.
4. Set each Column's **Design → Sizing → Column Class**:

| Column | Desktop | Tablet and smaller |
|---|---|---|
| 1 | 3/5 | Fullwidth |
| 2 | 2/5 | Fullwidth |
| 3 | Fullwidth | Fullwidth |

### Modules

- **Column 1:** a Heading with the **Heading 4** preset, text "Discounts, Giveaways, & Other News".
- **Column 2:** a close Icon (size 26px, margin 1rem on all sides, Position Fixed, Offset Origin Top Right) and a Text module with the **Small Text** preset reading "Max one email per month". Optionally right-align it on desktop and left-align on tablet and smaller.
- **Column 3:** an Email Optin module with the **Dark** element preset; clear the placeholder Title and Body; choose your Email Provider under **Content → Email Account**; turn off Show First Name and Show Last Name under **Content → Fields**.

### Cookie display condition

1. Open the Section → **Advanced → Conditions → + Add Condition**.
2. Choose **Cookie** (near the bottom of the list).
3. Set Display Rule **Cookie Value Does Not Equal**, Cookie Name `hide-popup`, Cookie Value `true`. Click **Apply**.

The pop-up renders only while `hide-popup` does not equal `true`, so once the cookie is written it stays hidden until the cookie expires or is cleared.

### Close and cookie interactions

On the Icon in Column 2 (**Advanced → Interactions**), add two interactions:

1. Trigger **Click**, Effect **Hide Element**, Target the Subscribe Section in the Sign Up Pop-up Form Canvas.
2. Trigger **Click**, Effect **Add Cookie**, Cookie Name `hide-popup`.

The first closes the pop-up immediately; the second records the cookie the condition checks on later loads.

Then open the Section's **Advanced → Visibility** and enable all breakpoints so it is hidden by default.

### Homepage trigger

1. Save the Canvas and return to the main homepage Canvas.
2. In Layers View, select the Features section containing the "Thrive in a better work environment" heading.
3. **Advanced → Interactions → + Add Interaction:** Trigger **Viewport Enter**, Effect **Show Element**, Target the Subscribe Section under the Sign Up Pop-up Form Canvas.

The pop-up appears when that section scrolls into view rather than immediately on load.

## Notes

- The small notice can appear on load because it is out of the way; the pop-up takes over the screen center, so it waits for a scroll trigger.
- Both close through Icon interactions; the pop-up also uses a cookie condition to prevent repeat views.
- The same Canvas, Interactions, and Display Conditions pattern can power cookie banners, slide-ins, announcement bars, confirmation prompts, onboarding panels, and off-canvas menus.

## Resources

- [Download the homepage layout with the Notice and pop-up off-canvases](https://www.dropbox.com/scl/fi/nxzroc1n2awb5z1g18vg1/Coworking-Homepage-with-Off-Canvases.json?rlkey=sdo3pasdigoxogdf0ve719y86&st=1rjlr83z&dl=1)

## Official documentation

[Part 13: Creating Interactive Off-Canvas Elements and Popups in Divi 5](https://help.elegantthemes.com/en/articles/15704140-part-13-creating-interactive-off-canvas-elements-and-popups-in-divi-5)
