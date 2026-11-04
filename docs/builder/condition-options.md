---
title: "Condition Options"
description: "Divi 5 Condition Options — show or hide elements based on user role, device, browser, date/time, post type, and other conditional display rules."
category: builder
tags: ["builder", "conditions", "display-logic", "dynamic"]
related: ["visual-builder", "theme-builder"]
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://www.elegantthemes.com/documentation/divi/divi-condition-options"
---

# Condition Options

Divi Condition Options allow you to apply advanced logic to any section, row, or module to hide or display elements based on a set of conditions.

!!! abstract "Quick Reference"
    **What it does:** Controls element visibility based on rules like user role, device type, date range, browser, and post type.
    **Where to find it:** Any element's settings → Advanced Tab → Conditions → +Add Condition.
    **Key features:**

    - User conditions: logged-in status, user role
    - Device and browser conditions: device type, browser, operating system
    - Date/time conditions: date range, time of day, day of week
    - Post conditions: post type, category, tag
    - Multiple conditions combined with AND logic

    **ET Docs:** [Condition Options](https://www.elegantthemes.com/documentation/divi/divi-condition-options){:target="_blank"}

The Divi Condition Options allow you to apply advanced logic to any section, row, or module to hide or display elements based on a set of conditions. You can define a set of conditions such as user role, date and time, browser, device, post information, website location, and more.

For example, you can choose to display specific content based on date and time. Or you can choose to display unique content to users when they log in and show unique elements to specific users based on their user role.

<!-- ![Condition Options overview](../assets/screenshots/builder/condition-options/overview.png){ loading=lazy }
*The Condition Options interface in Divi 5.* -->

## How To Access Condition Options

To add conditions to any element:

1. Click the element (section, row, or module) to open its settings.
2. Navigate to the **Advanced** tab.
3. Locate the **Conditions** option group.
4. Click **+ Add Condition** to add your first condition rule.
5. Select a condition type from the dropdown and configure its parameters.
6. Add additional conditions as needed -- multiple conditions can be combined to create complex visibility logic.

For more detail, see the [Elegant Themes Condition Options reference](https://help.elegantthemes.com/en/articles/10102758){:target="_blank"}.

## Condition Types Reference

Divi 5 provides the following condition categories and types:

### User Conditions

| Condition | Description |
|-----------|-------------|
| **Logged-In Status** | Show or hide the element based on whether the visitor is logged in or logged out. |
| **User Role** | Target specific WordPress user roles (Administrator, Editor, Author, Subscriber, etc.). |

### Browsing History Conditions

| Condition | Description |
|-----------|-------------|
| **Visited Page** | Display the element only if the visitor has previously viewed a specific page on your site. |
| **Purchase History** | Show content to customers who have made prior purchases (requires WooCommerce). |

### Device & Browser Conditions

| Condition | Description |
|-----------|-------------|
| **Device Type** | Target mobile, tablet, or desktop users based on their device. |
| **Browser** | Personalize content based on the visitor's browser (Chrome, Safari, Firefox, Edge, etc.). |
| **Operating System** | Customize visibility by operating system (iOS, Android, Windows, macOS, Linux). |

### Date & Time Conditions

| Condition | Description |
|-----------|-------------|
| **Date Range** | Show the element only during a specified date range (useful for promotions, seasonal content). |
| **Time of Day** | Display content during specific hours of the day. |
| **Day of Week** | Target specific days of the week. |

### Post & Page Conditions

| Condition | Description |
|-----------|-------------|
| **Post Type** | Show the element only on specific post types (posts, pages, products, custom post types). |
| **Category / Tag** | Display based on the current post's category or tag assignments. |

## Combining Conditions (AND / OR Logic)

When you add multiple conditions to an element, they are combined using **AND logic** by default -- all conditions must be true for the element to display. For example, setting both "Logged-In Status = Logged In" and "Device Type = Mobile" means the element only appears for logged-in visitors on mobile devices.

## Use Case Examples of Condition Options

### Personalized Greeting for Members

Show a welcome-back message only to logged-in users while displaying a sign-up CTA to logged-out visitors. Create two modules at the same position: one with the condition "Logged-In Status = Logged In" and the other with "Logged-In Status = Logged Out."

### Holiday Promotion Banner

Display a promotional banner only during a specific date range. Add a "Date Range" condition with the start and end dates of your sale.

### Mobile-Only CTA

Show a click-to-call button only on mobile devices by adding a "Device Type = Mobile" condition.

### Browser-Specific Notices

Display a "For the best experience, use Chrome" notice to visitors using Internet Explorer or older browsers by targeting them with a Browser condition.

## Tips & Best Practices For Using the Divi Conditions Options

- **Keep conditions simple.** Start with one or two conditions per element. Complex condition stacks are harder to debug when an element is not appearing as expected.
- **Test across scenarios.** After setting conditions, test them by logging in/out, switching devices, and verifying date-based rules manually.
- **Avoid conflicting rules.** If two elements at the same position have overlapping conditions, both may display simultaneously. Use mutually exclusive conditions (e.g., logged-in vs. logged-out) to prevent this.
- **Document your conditions.** For complex pages, add a note in the element's label or the Advanced tab's CSS ID field so other editors understand why an element is conditionally displayed.
- **Use conditions sparingly for SEO content.** Content hidden by conditions is typically not rendered server-side, so search engines may not index it.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Related

- [Visual Builder](visual-builder.md)
- [Theme Builder](theme-builder.md)
- [Conditions Options](../options-groups/conditions.md) — Per-element conditional display rules in the options panel
- [Visibility Options](../options-groups/visibility.md) — Device-level visibility toggles
- [Interactions](interactions.md) — Trigger visual changes based on user actions
- [Dynamic Content](dynamic-content.md) — Pull dynamic values for use in condition logic
