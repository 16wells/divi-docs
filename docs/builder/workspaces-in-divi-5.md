---
title: "Workspaces in Divi 5"
description: "How Divi 5 workspaces save and switch Visual Builder preferences and layout, including the Website, Your, and Premade workspace groups."
category: builder
tags: [builder, workspaces, visual-builder, preferences]
related: []
divi_version: "5.7+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15459160-workspaces-in-divi-5"
---

# Workspaces in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A saved configuration of the Visual Builder itself: your builder preferences plus its layout (window arrangement, sidebar, open panels, current view, breakpoint).
    **Where to find it:** The **Workspaces** icon on the Visual Builder's left sidebar, which opens the **Workspace Settings** modal.
    **Key behavior:** Workspaces never change page content, only how the builder looks and behaves.

## Workspace Settings

At the top of the modal, the **Active Workspace** selector lists every workspace available to you and marks the active one with a checkmark. The preferences a workspace stores include:

| Setting | Description |
|---|---|
| Builder Default View Mode | View the builder opens in. Default is Desktop. |
| History State Interval | How often an action is recorded in the History panel. Default is After Every Action. |
| Page Creation Flow | What the builder does on an empty page: Give me a Choice (a modal offering the options), Build From Scratch, Load Premade Layout, or Build with AI. |
| Page Bar Icon | Which icons always show in the top bar. |
| Show Disabled Module at 50% Opacity | Whether modules disabled via Advanced → Visibility appear at 50% opacity or are hidden. |
| Group Settings Into Closed Toggle | Whether option groups start collapsed or all open. |
| Add Placeholder Content to New Module | Whether new modules get placeholder text. |
| Speed Up The Builder With Prerendering | Turns Speculative Prerendering on or off. |
| Interface Mode | Light or Dark. |
| Color Scheme | The interface color scheme. |
| Show Theme Builder Layouts | Lets you edit the Theme Builder template while editing a page. |
| Enable Admin Bar | Whether the WordPress admin bar stays visible in the Visual Builder. |

## The three workspace groups

- **Website Workspaces:** contains **Global**, a site-wide workspace shared rather than tied to a user account. Global is the default out of the box.
- **Your Workspaces:** your own custom workspaces, listed alphabetically. The group appears once you save one. They are stored per WordPress user, so each editor keeps their own set.
- **Premade Workspaces:** Divi's built-in **Builder** and **Minimal** starting points. They are read-only; the only available action is **Set as Default Workspace**.

## Save a new workspace

1. Arrange the builder how you like: panels such as Layers View, Variable Manager, and Style Inspector, plus Interface Mode and Page Bar Icons.
2. Open **Workspace Settings** from the Workspaces icon.
3. Click **Save as New Workspace**.
4. Enter a name in the **Workspace Name** field.
5. Optionally turn on **Set As Default** so the builder loads this workspace automatically.
6. Click **Save**.

Tip: keep one workspace for building (wireframe view, all page bar icons on) and another for client presentations (minimal toolbar, light mode).

## Switch and manage workspaces

Open the **Active Workspace** selector and click a workspace to switch. When the active workspace is not a premade one, these quick actions appear above the list:

- **Edit Workspace:** rename the selected workspace.
- **Duplicate Workspace:** copy it.
- **Update Active Workspace:** save the current builder state into it.
- **Reset Active Workspace:** return it to its initial state.
- **Delete Workspace:** remove it.
- **Set as Default Workspace:** make it your default.

## Command Center

Press **Cmd/Ctrl + K** to open the Command Center. It offers **Update Active Workspace** and **Reset Active Workspace**, and you can switch workspaces by typing a name.

## FAQ

**Do workspaces change my page content?** No. Only builder preferences and layout are stored.

**Who sees the Global workspace?** Everyone editing the site, since it is stored site-wide. Workspaces under Your Workspaces belong to your WordPress user only.

**Which workspace is the default?** Global, until you use Set as Default Workspace on another.

**Can I edit the premade Builder or Minimal workspaces?** No. Activate one, adjust the builder, and click Save as New Workspace to make your own copy.

## Official documentation

[Workspaces in Divi 5](https://help.elegantthemes.com/en/articles/15459160-workspaces-in-divi-5){:target="_blank"}
