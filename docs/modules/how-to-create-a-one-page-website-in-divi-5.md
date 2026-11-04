---
title: "How to Create a One-Page Website in Divi 5"
description: "Step-by-step guide to building a one-page site in Divi 5 with section anchors, a custom menu, a static homepage, and optional Dot Navigation."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15069550-how-to-create-a-one-page-website-in-divi-5"
---

# How to Create a One-Page Website in Divi 5

!!! abstract "Quick Reference"
    **Goal:** One scrolling page where menu links jump to each section.
    **Core technique:** Give each Section a CSS ID, then point custom menu links at `#that-id`.
    **Extras:** Set the page as the static homepage; optionally turn on Dot Navigation in Divi Page Settings.

## Before you begin

- Divi 5 is installed and activated.
- You are logged in to WordPress as an Administrator.
- You have planned the main content areas (for example Case Studies, Services, About Us, Contact Us). Each becomes a Section with its own anchor.

!!! tip "Divi AI Agent"
    The [Divi AI Agent](https://help.elegantthemes.com/en/articles/16798164-the-divi-ai-agent-in-divi-5) in the Visual Builder sidebar can create the page, sections, and the anchor menu from a plain-language prompt, and asks for approval before anything destructive. It is part of every Divi AI subscription.

## Steps

1. **Create the page.** In WordPress go to **Pages → Add New Page** and give it a title (for example, Homepage).
2. **Open the Visual Builder.** Click **Use Divi Builder**. The Page Flow modal offers Build From Scratch, Choose a Premade Layout, or Build with AI. The anchor steps work the same with any option; a Landing Page premade layout already follows a one-page structure.
3. **Structure the content into Sections.** Create one Section per menu item (you can add more, such as a hero or footer call to action).
4. **Add a CSS ID to each Section.** For each target Section:
    1. Click the Section's gear icon.
    2. Go to **Advanced → Attributes**.
    3. Click **+ Add Attribute** and choose **ID**.
    4. Enter the value (for example `case-studies`).

    Save with the purple Save button, then exit the Visual Builder.
5. **Create the menu.** Go to **Appearance → Menus**, edit or create a menu, and expand **Custom Links**. For each Section, set the URL to `#` plus the ID (for example `#case-studies`), enter the Link Text, and click **Add to Menu**. Under **Menu Settings → Display location** tick **Primary Menu** (or your theme's main location) and click **Save Menu**.
6. **Set the homepage.** Go to **Settings → Reading**, choose **A static page** under Your homepage displays, select your page, and click **Save Changes**.
7. **Optional: turn on Dot Navigation.** Edit the page, find the **Divi Page Settings** box in the sidebar, set **Dot Navigation** to On, and click **Update**.

## CSS ID rules

- Only Sections, Rows, and Modules can have a CSS ID; attach it to the Section for a clean menu.
- Use descriptive names (`case-studies`, not `section-1`).
- Stick to one naming convention (kebab-case, camelCase, or snake_case).
- Use only lowercase letters, numbers, and hyphens; no spaces or special characters.
- Keep IDs unique on the page, short, and simple.

## Dot Navigation

Dot Navigation adds a floating vertical dot menu on the right side of the page, one dot per Section. Clicking a dot jumps to that Section. The number of dots matches the number of Sections on the page.

## Result

Visit the homepage and click each menu item; the page scrolls to the matching Section. After this you can keep refining spacing, typography, and Global Presets in the Visual Builder.

## Official documentation

[How to Create a One-Page Website in Divi 5](https://help.elegantthemes.com/en/articles/15069550-how-to-create-a-one-page-website-in-divi-5)
