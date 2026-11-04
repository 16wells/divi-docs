---
title: "Editing and Customizing Theme Builder Templates in Divi 5"
description: "Step-by-step guide to Theme Builder template quick actions and building global headers and footers, blog post, archive, 404, and search results templates in Divi 5."
category: builder
tags: [builder, theme-builder, templates]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/10587485-editing-and-customizing-theme-builder-templates-in-divi-5"
---

# Editing and Customizing Theme Builder Templates in Divi 5

!!! abstract "Quick Reference"
    **What it is:** The Theme Builder workflow for managing templates and building headers, footers, and body layouts for posts, archives, 404 pages, and search results.
    **Where to find it:** **Divi → Theme Builder**.
    **Key behavior:** Body layouts for posts need the Post Content module; archive and search templates use the Blog module with **Posts For Current Page** enabled.

Templates in the Theme Builder use the Visual Builder as their layout editor and can include dynamic content.

## Quick actions

Hover over a template card to see its quick actions:

| Action | What it does |
|---|---|
| Drag handle | Reorder the template |
| Settings | Open the template settings |
| Duplicate | Copy the template |
| Save | Store it in the Divi Library or Divi Cloud |
| Export | Export the template |
| Contextual menu | Manage assignments, duplicate, disable, delete, and more; also opens with a right-click on the card |

The **Eye** icon switches the template's Header, Custom Body, or Footer section off.

!!! tip "Divi AI Agent"
    The source notes that the Divi AI Agent (part of a Divi AI subscription) can create a Theme Builder template, set its display conditions from chat, and build the header, body, or footer layout, pausing for approval before destructive changes.

## Create a global header

A global header appears site-wide.

1. Go to **Divi → Theme Builder**.
2. In the **Default Website Template**, click **Add Global Header**.
3. Choose **Build a Global Header**.
4. Build the layout.
5. Click **Save**, then **Exit** to return to the Theme Builder.

Best practices: include a logo, primary navigation (the Menu module), contact details, and a call-to-action; keep navigation clear; test responsiveness across devices; use design variables for consistency; save the layout to the Divi Library for reuse.

## Create a global footer

The steps are the same as for the header, using **Add Global Footer** in the Default Website Template. (The source text says to choose "Build a Global Header" at step 3 of the footer procedure, which looks like a copy error; pick the build option for the footer.)

Best practices: organize sections by priority (legal notices, support links, calls to action), keep text high-contrast and legible, add a call to action such as a newsletter signup, include secondary links to privacy, terms, and FAQs, and keep the copyright year current.

!!! note
    A global body is usually unnecessary. If you add one, include the Post Content module in its layout so each page or post's content still appears on the front end.

## Create a blog post template

The post template is assigned to All Posts.

1. Go to **Divi → Theme Builder** and click **Add New Template**.
2. Choose **Build New Template**.
3. Assign it to **All Posts** and click **Create Template**.
4. Click **Add Custom Body**, then **Build Custom Body**.
5. Insert the **Post Title** module.
6. Insert the **Post Content** module and any other static modules your design needs.
7. **Save**, then **Exit**.

An All Posts template should always contain both the Post Title and Post Content modules.

## Create an All Archive template

An archive page lists posts grouped by taxonomy, date, author, or post type.

1. Go to **Divi → Theme Builder** and click **Add New Template**, then **Build New Template**.
2. In the Template Settings modal, scroll to **Archive Pages**, choose **All Archive Pages**, and click **Create Template**.
3. Click **Add Custom Body**, then **Build Custom Body**.
4. Add the **Blog** module and enable **Posts For Current Page**.
5. Add any other modules your design needs.
6. **Save**, then **Exit**.

## Create a custom 404 template

This template replaces the default WordPress not-found page, so you can guide visitors to useful pages.

1. Go to **Divi → Theme Builder**, click **Add New Template**, then **Build New Template**.
2. In Template Settings, scroll to **Other**, choose **404 Page**, and click **Create Template**.
3. Click **Add Custom Body**, then **Build Custom Body**.
4. Add the modules you need.
5. **Save**, then **Exit**.

## Create a custom search results template

This template controls the page shown after a visitor uses the built-in WordPress search.

1. Go to **Divi → Theme Builder**, click **Add New Template**, then **Build New Template**.
2. In Template Settings, scroll to **Other**, choose **Search Results**, and click **Create Template**.
3. Click **Add Custom Body**, then **Build Custom Body**.
4. Add the **Blog** module and enable **Posts For Current Page**.
5. **Save**, then **Exit**.

## Official documentation

[Editing and Customizing Theme Builder Templates in Divi 5](https://help.elegantthemes.com/en/articles/10587485-editing-and-customizing-theme-builder-templates-in-divi-5){:target="_blank"}
