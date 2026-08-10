---
title: "Login"
description: "Divi 5 Login module — front-end WordPress authentication form with custom redirect, field styling, and conditional display options."
category: modules
tags: ["modules", "forms", "interactive", "authentication", "user-access", "membership"]
related: ["contact-form", "email-optin"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/10315833-the-login-form-module-in-divi-5"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Login

The Login module displays a WordPress login form that allows registered users to sign in directly from any page.

!!! abstract "Quick Reference"
    **What it does:** Renders a styled WordPress login form with username, password fields, and custom redirect.
    **When to use it:** Membership site login pages, client portals, gated content areas
    **Key settings:** Title, Body text, Redirect URL, Fields styling, Display Conditions
    **Block identifier:** `divi/login`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/10315833-the-login-form-module-in-divi-5)

!!! tip "When to Use This Module"
    - Providing front-end login access for membership or client portal sites
    - Creating gated content pages that show the login form to logged-out users
    - Building branded login pages that match your site design

!!! warning "When NOT to Use This Module"
    - For collecting visitor information or inquiries → use [Contact Form](contact-form.md)
    - For email newsletter signups → use [Email Optin](email-optin.md)
    - For user registration (this module handles login only) → use a registration plugin

## Overview

The Login module provides a fully styled WordPress authentication form that you can place anywhere in your Divi 5 layout. It renders username and password fields along with a submit button, giving registered users a convenient way to log in without navigating to the default WordPress login page. This is especially valuable for membership sites, client portals, gated content areas, and any site where front-end authentication improves the user experience.

In Divi 5, the Login module includes a title and description area above the form fields, letting you provide context or instructions for visitors. You can customize the redirect URL so that users land on a specific page after a successful login, rather than defaulting to the WordPress dashboard. The module also displays a link to the password recovery page, helping users who have forgotten their credentials.

The Design tab gives you comprehensive control over the visual presentation of every element within the module — from the input field styling and button appearance to the title and body text typography. Combined with the Advanced tab's conditional display options, you can show the login form only to logged-out users and display different content to those already authenticated. This makes the Login module a practical building block for any site that requires user registration.

For additional reference, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/10315833-the-login-form-module-in-divi-5).

[View A Live Demo Of This Module](https://www.16wells.dev/module-demos/login/)

![Login module](../assets/screenshots/modules/login/element.png){ loading=lazy }
*The Login module as it appears on the live demo.*

## Use Cases

1. **Membership Site Login** — Place the Login module on a dedicated sign-in page or in a sidebar to give members quick access to protected content, downloads, courses, or community forums without redirecting to the WordPress admin login screen.

2. **Client Portal Access** — Add the Login module to a client-facing page where customers can authenticate to view invoices, project updates, support tickets, or other private resources. Set the redirect URL to point directly to the portal dashboard after login.

3. **Gated Content Landing Page** — Combine the Login module with Divi 5 display conditions to show the form only to logged-out visitors. Once authenticated, the user sees the protected content in place of the login form, creating a seamless access experience.

## How to Add the Login Module

1. **Open the Visual Builder** — Navigate to the page where you want the login form and activate the Divi 5 Visual Builder. Click the plus icon within the section and row where the form should appear.

2. **Select the Login Module** — Search for "Login" in the module picker or browse the module list. Click to insert it into your chosen column.

3. **Configure the Settings** — Add a title and description in the Content tab to provide context for visitors. Set the redirect URL if you want users to land on a specific page after logging in. Then style the form fields, button, and text using the Design tab.

## Settings & Options

### Content Tab

The Content tab controls the text displayed above the form, the post-login redirect behavior, and general module configuration.

| Setting | Type | Description |
|---------|------|-------------|
| Text | group | Contains the title and body text fields displayed above the login form. The title serves as a heading and the body text provides instructions or context for the visitor. |
| Redirect | group | Set a custom URL where users are redirected after a successful login. If left empty, WordPress uses its default redirect behavior, which typically sends users to the admin dashboard. |
| Link | group | Configure a link URL applied to the module wrapper, along with link target (same window or new tab) settings. |
| Background | group | Apply a background color, gradient, or image to the module container. This fills the area behind the form fields and text content. |
| Loop | toggle | When used inside a dynamic layout such as a Theme Builder template, this setting controls whether the module repeats for each item in a post loop. |
| Order | select | Determines the display order of the module relative to sibling modules within the same container. |
| Meta | group | Contains the admin label field for assigning a custom name to this module instance in the Visual Builder layers panel. |
| Elements |  | Allows you to add nested modules, such as theLink moduleand more. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides styling controls for the form fields, button, typography, and overall module appearance.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Fields | group | Style the username and password input fields. Control the field background color, text color, placeholder color, focus border color, and field border radius. These settings determine how the form inputs look in their default, focused, and filled states. |
| Layout - |  | Choose the Layout Style. It allows you to change how the child modules are being displayed.BlockFlex(default)Grid <!-- AUTO-ADDED --> |
| Block |  |  <!-- AUTO-ADDED --> |
| Flex |  | (default) <!-- AUTO-ADDED --> |
| Grid |  |  <!-- AUTO-ADDED --> |
| Text |  | Choose the overall Login module's text styles for this module. <!-- AUTO-ADDED --> |
| Title Text |  | Choose the Login module's title styles. <!-- AUTO-ADDED --> |
| Body Text |  | Choose the module's body text styles. <!-- AUTO-ADDED --> |
| Button |  | Choose the Login module's button styles. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Login module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Login module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Login module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Login module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Login module's filters, such as hue shifts, saturation changes, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Login module's advanced design effects, such as scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Login module's animation styles. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Text color, alignment, text shadow |
| [Title Text](../options-groups/title-text.md) | Font, size, color, letter spacing, line height, text shadow for the module title |
| [Body Text](../options-groups/body-text.md) | Font, size, color, line height for the description text |
| [Button](../options-groups/button.md) | Text color, background, border, border radius, font, icon, hover states |
| [Sizing](../options-groups/sizing.md) | Width, max-width, height, min-height |
| [Spacing](../options-groups/spacing.md) | Margin and padding per side, responsive breakpoints |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Color, offsets, blur radius, spread |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue, blur, invert, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level HTML, CSS, and behavior controls.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (form wrapper, input fields, button, title, body text) |
| HTML | Custom HTML attributes for module wrapper (data attributes, ARIA labels) |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS- |  | Allows you to add custom CSS code to fine-tune your Login module, enabling advanced styling that perfectly aligns with your vision. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Login module's visibility based on different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Login module animation takes, adding subtle, impactful animations that enhance user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose precise control of the Login module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Login module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS — Styled Login Form

```css
/* Clean, card-style login form */
.et_pb_login {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    padding: 40px;
    max-width: 480px;
    margin: 0 auto;
}

.et_pb_login input[type="text"],
.et_pb_login input[type="password"] {
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 16px;
    transition: border-color 0.2s ease;
}

.et_pb_login input:focus {
    border-color: #2ea3f2;
    outline: none;
}
```

### Custom CSS — Full-Width Button

```css
/* Make the login button span the full form width */
.et_pb_login .et_pb_button {
    width: 100%;
    text-align: center;
    padding: 14px 24px;
    border-radius: 6px;
    font-weight: 600;
}
```

### Custom CSS — Responsive Layout

```css
/* Stack login form nicely on mobile */
@media (max-width: 767px) {
    .et_pb_login {
        padding: 24px 16px;
    }

    .et_pb_login h2 {
        font-size: 22px;
    }

    .et_pb_login input[type="text"],
    .et_pb_login input[type="password"] {
        font-size: 16px; /* Prevents iOS zoom on focus */
    }
}
```

### PHP — Customize Login Redirect

```php
/* Redirect users to a custom page after logging in via the Divi Login module */
add_filter('login_redirect', function($redirect_to, $requested_redirect_to, $user) {
    if (!is_wp_error($user) && isset($user->roles)) {
        if (in_array('subscriber', $user->roles)) {
            return home_url('/members/dashboard/');
        }
    }
    return $redirect_to;
}, 10, 3);
```

### PHP — Filter Login Module Output

```php
/* Add a custom message above the login form */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_login' !== $render_slug) {
        return $output;
    }

    $notice = '<div class="login-notice">Members: Log in to access exclusive content.</div>';
    return $notice . $output;
}, 10, 2);
```

## Common Patterns

### 1. Centered Login Card

Place the Login module in a single-column row with a maximum width of 480px and center alignment. Apply a white background, border radius, and box shadow to create a floating card effect. Add a title like "Member Login" and a short description. This pattern is ideal for dedicated login pages.

### 2. Sidebar Login Widget

Add the Login module to a narrow sidebar column (one-quarter or one-third width) alongside your main page content. Use compact spacing and a smaller title font size so the form fits neatly within the sidebar without dominating the layout. Set a display condition to hide the module for logged-in users.

### 3. Conditional Login and Welcome

Use two modules in the same row: a Login module with a display condition set to "User is not logged in" and a Text module with a welcome message conditioned to "User is logged in." This creates a seamless experience where visitors see the login form and authenticated users see personalized content in its place.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    title, body text, and settings attributes. **Creating new modules via REST API**
    produces content that renders on the front end but may not appear in the Visual
    Builder layer view. Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/login` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Observed | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Observed | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Observed | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

**Key content attributes** — *JSON paths need verification*:

| Attribute | JSON Path | Notes |
|-----------|-----------|-------|
| Title | `attrs.title` | Form heading text |
| Body | `attrs.content` | Description text above the form |
| Redirect URL | `attrs.current_page_redirect` | Post-login redirect destination |

!!! tip "Module Selection Guidance"
    For user login forms use Login; for email signups use Email Optin; for general forms use Contact Form.

## Saving Your Work

After configuring the Login module, click the green checkmark button at the bottom of the settings panel to apply your changes. Save the page using the save button in the Visual Builder toolbar or press Ctrl+S (Cmd+S on Mac). Test the login form on the front end by logging out and attempting to sign in with valid credentials.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively.

## Troubleshooting

!!! warning "Login Form Not Submitting"
    If clicking the login button does not authenticate the user or the page simply reloads:

    - Check that the username and password are correct by testing them on the standard WordPress login page at `/wp-login.php`.
    - Verify that no security plugin is blocking the login request or requiring additional fields like a CAPTCHA.
    - Inspect the browser console for JavaScript errors that may be preventing the form submission.
    - If using a custom redirect URL, confirm the URL is valid and accessible.

!!! warning "Login Form Visible to Logged-In Users"
    If authenticated users can still see the login form:

    - Add a display condition in the Advanced tab to show the module only when the user is not logged in.
    - Check that browser caching or a page cache plugin is not serving a stale version of the page. Full-page caching can interfere with conditional display logic since it serves the same HTML to all visitors.

!!! warning "Styling Not Applying to Form Fields"
    If your custom CSS or Design tab changes do not affect the input fields or button:

    - Use more specific CSS selectors to override default styles — for example, `.et_pb_login input[type="text"]` instead of just `input`.
    - Check for conflicting styles from your WordPress theme or other plugins using the browser inspector.
    - Ensure custom CSS is placed in the correct element target within the Advanced tab CSS fields.

## Related

- [Contact Form](contact-form.md) — Collect visitor inquiries with a customizable form
- [Email Optin](email-optin.md) — Capture email subscribers with an integrated signup form
- [Form field design](../options-groups/fields.md) — Input / Checkbox / Radio groups and presets
- [Conditions Options](../options-groups/conditions.md) — Show the login form only to logged-out users
- [Theme Builder](../builder/theme-builder.md) — Place the login module in header or footer templates
