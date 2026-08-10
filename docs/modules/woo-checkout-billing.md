---
title: "Woo Checkout Billing"
description: "Divi 5 Woo Checkout Billing module — WooCommerce billing address form with customizable field layouts, typography, and validation styling for checkout pages."
category: modules
tags: ["modules", "woocommerce", "ecommerce", "checkout", "forms", "billing"]
related: ["woo-checkout-shipping", "woo-checkout-payment", "woo-checkout-details"]
divi_version: "5.x"
last_updated: 2026-05-06
source_url: "https://help.elegantthemes.com/en/articles/12095364"
---

<!-- AUTO-UPDATED: 2026-05-06 — verify changes -->

# Woo Checkout Billing

The Woo Checkout Billing module renders the WooCommerce billing address form on the checkout page, collecting customer name, address, phone, and email details.

!!! abstract "Quick Reference"
    **What it does:** Renders the WooCommerce billing address form (name, company, address, city, state, postcode, country, phone, email) on the checkout page.
    **When to use it:** Custom checkout page templates in the Theme Builder
    **Key settings:** Layout (Default/Fullwidth/2-Column), Field Labels, Fields styling, Form Notice styling
    **Block identifier:** `divi/woo-checkout-billing`
    **ET Docs:** [Official documentation](https://help.elegantthemes.com/en/articles/12095364)

!!! tip "When to Use This Module"
    - Building a custom WooCommerce checkout page template in the Theme Builder
    - Collecting billing address details from customers during checkout
    - Styling billing form fields and layout to match your store's design

!!! warning "When NOT to Use This Module"
    - On non-checkout pages — this module requires the WooCommerce checkout context
    - For shipping address collection — use [Woo Checkout Shipping](woo-checkout-shipping.md)
    - For general contact forms — use [Contact Form](contact-form.md)

## Overview

The Woo Checkout Billing module outputs the standard WooCommerce billing form fields that collect the customer's billing information during checkout. This includes first name, last name, company name (optional), country/region, street address, city, state/county, postcode/ZIP, phone number, and email address. The form fields are validated by WooCommerce, and any errors are displayed as form notices that you can style through the module's design options.

One of the most useful settings is the Layout option, which offers three configurations: the default WooCommerce layout that follows standard field widths, a fullwidth layout where every field spans the entire container width, and a two-column grid that arranges fields side by side. The two-column option is particularly effective for reducing the visual length of the checkout form on desktop screens, making the page feel less overwhelming to customers.

This module is designed exclusively for Theme Builder templates assigned to the WooCommerce checkout page. It works alongside the [Woo Checkout Shipping](woo-checkout-shipping.md), [Woo Checkout Payment](woo-checkout-payment.md), [Woo Checkout Details](woo-checkout-details.md), and [Woo Checkout Information](woo-checkout-information.md) modules to create a complete custom checkout experience. For the official Elegant Themes documentation, see the [Woo Checkout Billing help article](https://help.elegantthemes.com/en/articles/12095364).

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active. It will not appear in the module picker without WooCommerce.

## Use Cases

1. **Two-Column Compact Checkout** — Use the 2-column Layout option to arrange billing fields side by side, significantly reducing the vertical height of the checkout form. Pair with the shipping module in the same column for a compact, professional checkout that requires minimal scrolling.

2. **Brand-Styled Form Fields** — Apply custom border colors, border radius, background colors, and focus states to the input fields using the Fields design option. Match the field styling to your site's form design system for a cohesive experience from contact forms through checkout.

3. **Attention-Grabbing Validation** — Style the Form Notice option with a contrasting background color (such as a soft red) and custom typography so that validation errors are immediately visible to customers. Clear, well-styled error messages reduce checkout abandonment by helping users fix problems quickly.

## How to Add the Woo Checkout Billing Module

1. Ensure WooCommerce is installed and activated. Navigate to the Theme Builder and create or edit the template assigned to the WooCommerce checkout page.
2. Open the Visual Builder on your checkout page template. Click the gray **+** icon to add a new module to a row.
3. Search for "Woo Checkout Billing" in the module picker or find it in the WooCommerce category, then click to insert it. The module will display the billing form fields automatically.

## Settings & Options

The Woo Checkout Billing module settings are organized across three tabs: Content, Design, and Advanced.

### Content Tab

The Content tab controls the module's background and layout positioning. The billing form fields are generated automatically by WooCommerce based on your store's configuration.

| Setting | Type | Description |
|---------|------|-------------|
| Background | background controls | Set a background color, gradient, image, or video behind the billing form module. |
| Loop | toggle | Enable the loop builder to use this module within a loop context. |
| Order | select | Set the Flexbox order of the module within its parent row. |
| Meta — Admin Label | text | Set a custom label for the module in the Visual Builder's layer panel. |
| Meta — Disable On | device toggles | Control builder-level visibility across devices. |
| Loop- |  | Enables the loop builder. <!-- AUTO-ADDED --> |
| Order- |  | Choose the Flexbox order of the module. <!-- AUTO-ADDED --> |
| Meta |  | Choose the Woo Checkout Billing Module's Label text and force its Visibility inside the Visual Builder. <!-- AUTO-ADDED --> |

### Design Tab

The Design tab provides controls for the form layout, typography, field styling, and validation message appearance.

**Module-specific settings:**

| Setting | Type | Description |
|---------|------|-------------|
| Layout | select | Choose between Default (standard WooCommerce widths), Fullwidth (all fields span full width), or 2-Column (fields arranged in a two-column grid). |
| Title Text | text styling | Customize the font, size, weight, and color of the "Billing Details" heading. |
| Field Labels | text styling | Style the label text above each form field including font, size, weight, and color. |
| Fields | styling controls | Style the input fields including border, background color, text color, padding, border radius, and focus states. |
| Form Notice | styling controls | Style validation error messages including background color, text color, border, and padding. These notices appear when required fields are missing or invalid. |
| Default |  | Default WooCommerce field layout. <!-- AUTO-ADDED --> |
| Fullwidth |  | All fields are full-width. <!-- AUTO-ADDED --> |
| 2 Columns |  | All fields are displayed in a 2-column layout. <!-- AUTO-ADDED --> |
| Text |  | Choose the overall text styles for the Woo Checkout Billing module. <!-- AUTO-ADDED --> |
| Sizing |  | Choose the Woo Checkout Billing module's sizing. <!-- AUTO-ADDED --> |
| Spacing |  | Choose the Woo Checkout Billing module's spacing. <!-- AUTO-ADDED --> |
| Border |  | Choose the Woo Checkout Billing module's border styles. <!-- AUTO-ADDED --> |
| Box Shadow |  | Choose the Woo Checkout Billing module's Box Shadow styles. <!-- AUTO-ADDED --> |
| Filters |  | Choose the Woo Checkout Billing module's filters, including hue shifts, saturation adjustments, and blending modes. <!-- AUTO-ADDED --> |
| Transform |  | Choose the Woo Checkout Billing module's advanced design effects, including scaling, rotating, skewing, and translating. <!-- AUTO-ADDED --> |
| Animation |  | Choose the Woo Checkout Billing module's animation styles to add personality and interactivity while maintaining a polished, professional feel. <!-- AUTO-ADDED --> |

**Shared design options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Text](../options-groups/text.md) | Font, weight, alignment, color, line height, text shadow |
| [Sizing](../options-groups/sizing.md) | Width, max-width, min-height, height, alignment |
| [Spacing](../options-groups/spacing.md) | Margin and padding with responsive breakpoint controls |
| [Border](../options-groups/border.md) | Width, color, style, border radius |
| [Box Shadow](../options-groups/box-shadow.md) | Horizontal/vertical offset, blur, spread, color, position |
| [Filters](../options-groups/filters.md) | Brightness, contrast, saturation, hue rotation, blur, invert, sepia, opacity, blend mode |
| [Transform](../options-groups/transform.md) | Scale, translate, rotate, skew, transform origin |
| [Animation](../options-groups/animation.md) | Entrance animation style, direction, duration, delay, intensity |

### Advanced Tab

The Advanced tab provides low-level control over HTML attributes, custom CSS, conditional display logic, and scroll-based effects.

**Shared advanced options** — see [Options Groups](../options-groups/index.md) for detailed documentation:

| Options Group | Description |
|--------------|-------------|
| [Attributes](../options-groups/attributes.md) | CSS ID, classes, custom HTML attributes |
| [CSS](../options-groups/css.md) | Custom CSS per element target (form, fields, labels, notices) |
| HTML | Semantic HTML tag selection for the module wrapper |
| [Conditions](../options-groups/conditions.md) | Display rules (user role, page type, date, logic) |
| Interactions | Hover, click, or scroll-triggered interactions |
| [Visibility](../options-groups/visibility.md) | Device visibility toggles |
| [Transitions](../options-groups/transitions.md) | Hover transition timing |
| [Position](../options-groups/position.md) | CSS position and offsets |
| [Scroll Effects](../options-groups/scroll-effects.md) | Scroll-driven animation effects |
| Attributes |  | Assign a CSS ID, reusable CSS classes, or custom HTML attributes to the element. Use these to apply advanced styling via your child theme's stylesheet or Divi's custom CSS settings. <!-- AUTO-ADDED --> |
| CSS |  | Allows you to add custom CSS to the Woo Checkout Billing module. <!-- AUTO-ADDED --> |
| Conditions |  | Allows you to create dynamic, personalized content, ensuring the right message reaches the right audience at the right time. <!-- AUTO-ADDED --> |
| Visibility |  | Choose the Woo Checkout Billing module's visibility according to different devices. <!-- AUTO-ADDED --> |
| Transitions |  | Choose how long the Woo Checkout Billing module animation takes, adding subtle and impactful animations that enhance the user experience and make your modules stand out. <!-- AUTO-ADDED --> |
| Position |  | Choose the Woo Checkout Billing module placement and create dynamic, visually engaging designs. <!-- AUTO-ADDED --> |
| Scroll Effects |  | Control how the Woo Checkout Billing module behaves and transforms during scrolling. <!-- AUTO-ADDED --> |
| Save |  | k on theSavebutton. <!-- AUTO-ADDED --> |
| Exit |  | k on theExitbutton. <!-- AUTO-ADDED --> |

## Code Examples

### Custom CSS

```css
/* Style billing form fields with modern look */
.et_pb_wc_checkout_billing .woocommerce-billing-fields input[type="text"],
.et_pb_wc_checkout_billing .woocommerce-billing-fields input[type="email"],
.et_pb_wc_checkout_billing .woocommerce-billing-fields input[type="tel"],
.et_pb_wc_checkout_billing .woocommerce-billing-fields select {
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 15px;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

/* Focus state */
.et_pb_wc_checkout_billing .woocommerce-billing-fields input:focus,
.et_pb_wc_checkout_billing .woocommerce-billing-fields select:focus {
    border-color: #2ea3f2;
    box-shadow: 0 0 0 3px rgba(46, 163, 242, 0.15);
    outline: none;
}

/* Style field labels */
.et_pb_wc_checkout_billing .woocommerce-billing-fields label {
    font-weight: 600;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
    display: block;
}

/* Style required field asterisk */
.et_pb_wc_checkout_billing .woocommerce-billing-fields .required {
    color: #e74c3c;
}

/* Style validation errors */
.et_pb_wc_checkout_billing .woocommerce-error {
    background-color: #fdf0f0;
    border-left: 4px solid #e74c3c;
    color: #c0392b;
    padding: 12px 16px;
    border-radius: 4px;
    margin-bottom: 20px;
}

/* Two-column layout on desktop */
@media (min-width: 981px) {
    .et_pb_wc_checkout_billing .woocommerce-billing-fields__field-wrapper {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
    }
}

/* Stack to single column on mobile */
@media (max-width: 767px) {
    .et_pb_wc_checkout_billing .woocommerce-billing-fields input,
    .et_pb_wc_checkout_billing .woocommerce-billing-fields select {
        font-size: 16px; /* Prevents iOS zoom on focus */
    }
}
```

### PHP Hooks

```php
/* Filter the Woo Checkout Billing module output */
add_filter('et_module_shortcode_output', function($output, $render_slug) {
    if ('et_pb_wc_checkout_billing' !== $render_slug) {
        return $output;
    }
    return $output;
}, 10, 2);

/* Add a custom field to the billing form */
add_filter('woocommerce_billing_fields', function($fields) {
    $fields['billing_delivery_notes'] = array(
        'type'        => 'textarea',
        'label'       => 'Delivery Notes',
        'placeholder' => 'Gate code, landmark, etc.',
        'required'    => false,
        'priority'    => 120,
    );
    return $fields;
});

/* Remove the company field from billing */
add_filter('woocommerce_billing_fields', function($fields) {
    unset($fields['billing_company']);
    return $fields;
});
```

## Common Patterns

1. **Side-by-Side Billing and Shipping** — Place the Woo Checkout Billing module in a one-half column and Woo Checkout Shipping in the adjacent one-half column. Set both to the Fullwidth layout option so fields fill their columns. This creates a balanced two-panel checkout that keeps the page compact.

2. **Simplified Billing Form** — Use the `woocommerce_billing_fields` PHP filter to remove non-essential fields like Company Name and Address Line 2. Combined with the 2-column Layout option, this creates a streamlined checkout that only asks for what your business actually needs, reducing friction and increasing conversions.

3. **Progressive Checkout with Styling** — Style the billing section heading with a step number (e.g., "Step 1: Billing Details") using custom CSS on the Title Text. Apply a left border accent color to the entire module container to create a visual step indicator. Follow with similarly styled shipping and payment modules to create a clear progression through checkout.

## AI Interaction Notes

!!! warning "Create vs. Modify"
    Modifying existing module content via REST API (`wp.apiFetch` PATCH) updates
    settings attributes. **Creating new modules via REST API** produces content that
    renders on the front end but may not appear in the Visual Builder layer view.
    Use browser automation for reliable module creation.
    See [REST API Content Playbook](../playbooks/rest-api-content.md).

**Block identifier:** `divi/woo-checkout-billing` — *Needs verification on current build*

| Operation | Method | Status | Notes |
|-----------|--------|--------|-------|
| Read content | Parse `post_content` block JSON | Needs Testing | Use brace-depth parser — see [Content Encoding](../internals/content-encoding.md) |
| Modify existing | `wp.apiFetch` PATCH on post endpoint | Needs Testing | Update block attributes in `post_content` |
| Create new | Browser automation (Playwright) | Needs Testing | REST creation may break VB visibility |
| Batch modify | Sequential REST requests | Needs Testing | See [REST API Content Playbook](../playbooks/rest-api-content.md) |

## Saving Your Work

After configuring the Woo Checkout Billing module, click the green **Save** button at the bottom of the Visual Builder interface. The module can be saved as a preset for consistent styling across multiple checkout templates, or added to your Divi Library for reuse by right-clicking and selecting **Save to Library**.

## Version Notes

!!! note "Divi 5 Only"
    This page documents Divi 5 behavior exclusively. The Woo Checkout Billing module in Divi 5 supports Conditions, Interactions, Scroll Effects, and enhanced layout controls not available in Divi 4.

!!! info "WooCommerce Required"
    This module requires WooCommerce to be installed and active.

## Troubleshooting

!!! warning "Billing Fields Not Appearing"
    If the module renders but shows no form fields, verify that the template is assigned to the WooCommerce checkout page in the Theme Builder. The billing form requires the checkout page context to load. Also ensure that WooCommerce is properly configured with at least one payment method and shipping zone.

!!! warning "Validation Errors Not Styled"
    If form validation errors appear with default WooCommerce styling instead of your custom styles, check that you are using the Form Notice design option in the module settings. Custom CSS targeting `.woocommerce-error` may also be needed for full control. Validation styling only appears when a customer attempts to submit the form with missing required fields.

!!! tip "Fields Not Matching on Mobile"
    If form fields zoom in on iOS when tapped, ensure the font size is at least 16px on mobile devices. iOS Safari automatically zooms into inputs with font sizes below 16px. Set this in the responsive settings of the Fields design option or via custom CSS with a media query.

## Related

- [Woo Checkout Shipping](woo-checkout-shipping.md)
- [Woo Checkout Payment](woo-checkout-payment.md)
- [Woo Checkout Details](woo-checkout-details.md)
