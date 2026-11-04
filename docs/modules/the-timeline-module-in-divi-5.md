---
title: "The Timeline Module in Divi 5"
description: "The Divi 5 Timeline module: dated events as Timeline Item child modules along a track, with Even options for alternating-side layouts."
category: modules
tags: ["modules", "timeline", "animation", "loop"]
related: ["post-content", "blog"]
divi_version: "5.5+"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15162149-the-timeline-module-in-divi-5"
---

# The Timeline Module in Divi 5

!!! abstract "Quick Reference"
    **What it is:** A module that lays out dated events along a connecting track. Each event is a Timeline Item child module.
    **Where it lives:** Gray Plus icon inside a Row, then search for "Timeline". It is inserted with starter items.
    **Key feature:** "Even" sub-options let you style every second item differently, so alternating left/right timelines need no custom CSS.

## Use cases

- Company or brand history, one event per year.
- Product roadmaps with past releases and upcoming milestones.
- Resume or CV pages (education, jobs, certifications).
- Case studies split into discovery, design, build, and launch.
- Process pages, onboarding flows, and how-it-works sections.

## Adding the module

1. Click the **Green Plus** icon to insert a Row.
2. Click the **Gray Plus** icon inside the Row.
3. Choose **Timeline** (or search for it). Divi adds it with a starter set of Timeline Items.

## Managing items

Manage items from the Content tab of the parent Timeline module.

1. Edit: click the pencil icon next to an item to change its date, title, body, or design settings.
2. Add: click **Add New Timeline Item**, then fill in date, title, and body.
3. Duplicate: click the duplicate icon; content and per-item styling are copied.
4. Delete: click the trash icon.
5. Reorder: drag the handle on the left edge of an item.

## Settings

### Content tab

| Setting | Description |
|---|---|
| Timeline items | Add, edit, duplicate, delete, and reorder events. |
| Link | Makes the whole module clickable. |
| Background | Module background styles. |
| Loop | Enables the Loop Builder so events can come from a dynamic data source. |
| Order | Position within a Flexbox or Grid layout. |
| Meta | Label text and forced Visual Builder visibility. |

### Design tab

| Group | Controls |
|---|---|
| Timeline | Overall layout, including the alternating-sides toggle that drives the Even styling. |
| Track | The connecting line: color, weight, spacing. |
| Item | The item wrapper (has Even options). |
| Spacer | Gap between items along the track (has Even options). |
| Connector | The short line joining each marker to its card. |
| Marker | The dot, icon, or shape on the track at each event. |
| Card | The block holding each event's date, title, and body (has Even options). |
| Date Text | Date label typography (has Even options). |
| Title Text | Title typography (has Even options). |
| Body Text | Body typography (has Even options). |
| Sizing, Spacing, Border, Box Shadow, Filters, Transform, Animation | Standard groups. |

### Advanced tab

Attributes, CSS, HTML (semantic tag), Conditions, Interactions, Visibility, Transitions, Position, and Scroll Effects.

## Styling every second item with Even options

The Even sub-options live inside the Item, Spacer, Card, Date Text, Title Text, and Body Text groups. A typical alternating-side timeline:

1. In the Design tab, open the **Card** group and set the card to sit on the left of the track.
2. In the same group, use the Even sub-options to put every second card on the right.
3. Repeat the odd/even pairing in **Item** and **Spacer** to tune offset and gap on each side.

Even options also work for subtler effects such as alternating card backgrounds, title colors, or spacing. Connector and Marker have no Even options, which keeps the spine of the timeline consistent.

## Styling an individual item

Settings on the parent module apply to all items. To override one item, click the gear icon next to it. Its own Content and Design tabs offer:

- **Item Content:** the date, title, and body for that event.
- **Spacer, Connector, Marker, Card:** per-item structural overrides.
- **Date Text, Title Text, Body Text:** per-item typography overrides.

Changes there affect only that item. Use the arrow icon at the top left of the modal to return to the parent module's settings.

## Official documentation

[The Timeline Module in Divi 5](https://help.elegantthemes.com/en/articles/15162149-the-timeline-module-in-divi-5)
