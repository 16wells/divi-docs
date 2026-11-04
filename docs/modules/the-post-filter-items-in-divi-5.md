---
title: "The Post Filter Items in Divi 5"
description: "The filter controls available inside the Post Filter module, how they depend on the target loop type, and how to add taxonomy, ACF, and ordering filters."
category: modules
tags: [modules]
related: []
divi_version: "5.10+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/16187393-the-post-filter-items-in-divi-5"
---

# The Post Filter Items in Divi 5

!!! abstract "Quick Reference"
    **What it is:** The individual controls (search box, category filter, reset button, and so on) that live inside a Post Filter module.
    **Key rule:** The type of loop chosen as the module's **Target Loop** decides which filter items are available.
    **Where to add them:** Post Filter settings > **Content** > **Elements** > **+ Add Post Filter Item**.

## Post Loop

When the Target Loop is a Post Loop, the Post Filter module starts with these items already added:

| Item | Description |
|---|---|
| Search | Search box; shows only posts whose title or content contains the term |
| Category Filter | Lists the post categories that have at least one published post |
| Reset button | Clears any filters previously applied |
| Apply button | Starts the filtering when the module's **Apply Mode** is set to **Submit** |

### Add a taxonomy or author filter

1. Open the Post Filter module's settings.
2. In **Content** > **Elements**, click **+ Add Post Filter Item**.
3. Choose the **Post Filter Item** option.
4. Click the pencil icon to edit the new item.
5. In the item's **Content** tab, set **Field Type** to **Radio** or **Checkbox**.
6. In the **Field Options** dropdown, choose **Tags** (or **Categories**).

Selecting a taxonomy value shows only posts assigned to it. An **Authors** filter is built the same way; just choose **Authors** in the Field Options dropdown.

### Add an ACF filter

1. Follow steps 1 to 4 above.
2. In the item's **Content** tab, set **Field Type** to match how you want the ACF field's values shown:
    - **Text:** has a Field Type Value of **Text**, **Number**, **Date**, **Date Time**, or **Time**, matching the ACF field type (Text, Number, Date Picker, Date Time Picker, Time Picker).
    - **Select** or **Radio:** the visitor picks a single value.
    - **Checkbox:** the visitor can pick several values.
3. In the **Field Option** dropdown, choose the ACF field.
4. Set **Field Comparison**, the comparison used between the filter's value and the ACF field's value.
5. Set **Option Method**, which controls how the ACF values are produced:
    - **Automatic:** shows every value of the ACF field. If values are missing or new ones do not appear, click **Clear Cached Options**.
    - **Manual:** lets you show only some values. Click **Generate Options** to create the correct ACF values, then drag to reorder them or delete the ones you do not want.

## WooCommerce Product Loop

When the Target Loop is a WooCommerce Product Loop, the module starts with the same four items (Search, Category Filter, Reset, Apply). The Category Filter needs one extra step: open the item's settings, go to **Content** > **Field** > **Field Options**, and choose **Product Categories**.

You can add other product-related filters, built exactly as in the Post section above:

- Authors
- Product attributes (such as color or size)
- Product Tags
- Product Brands
- Product Shipping Classes
- ACF or Custom Fields
- Price Range
- Stock status

## Ordering filters

### Order By field type

Adds a control that lets visitors choose how results are ordered.

1. Open the Post Filter settings.
2. In **Content** > **Elements**, click **+ Add Post Filter Item**.
3. Set **Field Type** to **Order by**.
4. Select which options should be available:

| Option | Orders by |
|---|---|
| Default | WordPress's default order |
| Publish Date | Publish date of the post, page, product, or custom post type |
| None | No ordering |
| ID | Item ID |
| Title | Title text |
| Post Name | Slug text |
| Last Modified Date | Last modified date |
| Random | Random order |
| Comment Count | Number of comments |
| Price | Product price (WooCommerce Product Loop only) |
| Popularity | Number of sales (WooCommerce Product Loop only) |
| Rating | Product rating (WooCommerce Product Loop only) |

### Order

Offers the direction of the sort:

- **Default:** WordPress's default order.
- **Ascending** or **Descending:** sorts results by the value of the Order By filter.

### Multiple Order

Lets visitors combine several order and order-by choices on the front end. Results must satisfy all the combinations the visitor sets up.

## Official documentation

- [The Post Filter Items in Divi 5](https://help.elegantthemes.com/en/articles/16187393-the-post-filter-items-in-divi-5)
