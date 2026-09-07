---
title: "How to Display the Search Results in Alphabetical Order"
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-09-07
source_url: "https://help.elegantthemes.com/en/articles/8352749-how-to-display-the-search-results-in-alphabetical-order"
---

# How to Display the Search Results in Alphabetical Order

<!-- AUTO-CREATED: 2026-09-07 — stub from ET Help Center, needs enrichment -->

## Overview

For detailed information, see the [official Elegant Themes documentation](https://help.elegantthemes.com/en/articles/8352749-how-to-display-the-search-results-in-alphabetical-order).

<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->

## Settings & Options

### General

| Setting | Type | Description |
|---------|------|-------------|
| Child Theme for Divi |  | aChild Theme for Divi |
| WordPress Dashboard → Appearance → Theme Files Editor |  | ditor |
| functions.php |  | ions.phpfile and add this PHP snippet after the existing code:function divi_alphabetical_search_results ( $query ) {if( $query->is_search && !is_admin() ) {$query->set( 'orderby', 'title' );$query->set( 'order', 'ASC' );}}add_filter( 'pre_get_posts','divi_alphabetical_search_results' ); |
| Code Snippets |  | ctivate theCode Snippetsplugin |

## Code Examples

<!-- TODO: Add CSS/PHP code examples -->

## Common Patterns

<!-- TODO: Document 2-3 common usage patterns -->

## Troubleshooting

<!-- TODO: Document common issues and solutions -->

## AI Interaction Notes

| Task | Confidence | Notes |
|------|-----------|-------|
| Basic placement | 🔬 Needs Testing | Untested — stub page |
| Settings configuration | 🔬 Needs Testing | Untested — stub page |
| Custom styling | 🔬 Needs Testing | Untested — stub page |

## Related

<!-- TODO: Add links to related documentation pages -->
