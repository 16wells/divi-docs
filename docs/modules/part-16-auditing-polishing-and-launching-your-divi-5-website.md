---
title: "Part 16: Auditing, Polishing, and Launching Your Divi 5 Website"
description: "Divi 5 Mastery Course part 16: a pre-launch audit, performance, accessibility and SEO checklist, device testing, and go-live steps."
category: modules
tags: [modules]
related: []
divi_version: "5.x"
last_updated: 2026-11-04
source_url: "https://help.elegantthemes.com/en/articles/15704558-part-16-auditing-polishing-and-launching-your-divi-5-website"
---

# Part 16: Auditing, Polishing, and Launching Your Divi 5 Website

!!! abstract "Quick Reference"
    **What it is:** The final part of the Elegant Themes Divi 5 Mastery Course, a checklist for taking a finished Divi 5 build live.
    **Phases:** Audit, performance, accessibility and SEO, final refinements, device testing, pre-launch prep, go live.
    **Divi settings touched:** **Divi > Theme Options > General > Performance**, Semantic Elements, Style Inspector, Layers panel, Page Manager, Responsive Editor.
    **Most-missed step:** Unchecking **Discourage search engines from indexing this site** under **Settings > Reading**.

## Get in the right mindset

After weeks of building, small inconsistencies and broken links are easy to miss. Experience the site as a first-time visitor:

1. Take a break so you return with fresh eyes.
2. Open the site in an Incognito (Chrome) or Private (Safari) window.
3. Stay logged out of WordPress while testing the front end.
4. Browse on a physical phone or tablet, not just the builder preview.

Ask whether navigation is clear, content flows well, calls to action are easy to find, and whether you would trust the site. Work through it with your power-user tools: the Layers panel, Command Center, Page Manager, Style Inspector, Design Variables, and presets. Fix problems at the variable or preset level when you can.

!!! tip
    The tutorial notes that the Divi AI Agent (part of every Divi AI subscription, opened from the Visual Builder sidebar) can do much of this sweep in one pass: proofreading, finding missing alt text, flagging skipped heading levels, checking color consistency, and reviewing phone-width layouts. It asks for approval before destructive changes.

## Visual and functional audit

**Consistency on every major page** (homepage, inner pages, Blog, archive templates, single post template, search results, 404):

| Area | What to check |
|---|---|
| Typography | Heading sizes, weights, line heights, and spacing match the design system |
| Colors | Colors come from Design Variables so a palette change updates everywhere |
| Buttons | Correct Option Group and Element Presets; text size, padding, hover states, radius, spacing |
| Spacing | Gaps between sections and modules feel balanced on desktop, tablet, and phone |

**Header and footer**

- Sticky header behaves as intended on every page and breakpoint.
- Custom navigation does not overlap content, wrap awkwardly, or hide links on small screens.
- Footer spacing, column stacking, social icons, copyright text, and link alignment are correct everywhere.

**Interactive elements**

- Open and close off-canvas menus, pop-ups, notices, and slide-ins.
- Test hover states and that interactions fire at the right moment.
- Scroll through Loop Builder layouts and check images, titles, terms, excerpts, metadata, links, and pagination.
- Click every link and submit every form (contact, opt-in, navigation, social, dynamic Read More).

**Content accuracy**

- Proofread spelling, grammar, punctuation, and formatting.
- Hunt for placeholder text, repeated phrases, wrong dates, outdated offers, and unfinished captions.
- Replace placeholder images and check internal and external links.
- Make sure contact details, hours, address, email, phone, and social links match everywhere. If they are stored as Text or Link Variables, update them there.

**Mobile and tablet**

- Test across active breakpoints with the Customizable Responsive Breakpoints and the Responsive Editor.
- Watch for overlap, hidden content that should show, tiny text, awkward column stacking, and cramped buttons.
- Fix globally at the variable or preset level; use module-level edits only for one-off issues.

**Layers panel and Style Inspector:** use Layers to scan complex structure quickly, and the Style Inspector to review styles, content, variables, and presets across pages without opening every module.

## Optimize performance

1. Go to **Divi > Theme Options > General > Performance**.
2. Review **Dynamic Module Framework**, **Dynamic Icons**, and **Critical CSS**. Critical CSS prioritizes above-the-fold CSS and defers the rest; set **Critical Threshold Height** to suit your layout, with Medium a reasonable start.
3. Consider **Defer jQuery and jQuery Migrate** and **Defer Gutenberg Block CSS**. After enabling any deferral, test forms, menus, sliders, pop-ups, and third-party integrations, then save.

**Images**

- Resize close to the largest displayed size (a hero that never exceeds 1920px should not be uploaded at 4000px).
- Compress and export with a tool such as Photoshop, Affinity Photo, Squoosh, or TinyPNG.
- Use WebP for large photographs.
- Use Divi 5's Aspect Ratio and Image Framing settings to keep proportions consistent, especially in Loop Builder templates and grids.

Recheck image-heavy pages afterwards for sharpness and layout shifts.

## Accessibility and SEO

Run the site through WAVE, axe DevTools, or Lighthouse and look for weak color contrast, missing alt text, keyboard navigation problems, unlabeled form fields, and interactive elements without accessible names.

**Semantic Elements:** assign HTML tags by purpose, such as **nav** for primary navigation, **Section** for thematic groups, **Article** for standalone post or card content, and **Aside** for secondary content. Keep heading structure clean: one **H1** per page, **H2** for major sections, **H3** for supporting ones.

**SEO basics**

- Write unique meta titles and descriptions for key pages, using an SEO plugin (Yoast SEO, Rank Math, All in One SEO) or Divi's built-in SEO settings.
- Make sure the XML sitemap is on. In Yoast SEO, check **Yoast SEO > Settings > Site Features > XML sitemaps**; its index is commonly at `/sitemap_index.xml`.
- Check `robots.txt` is not blocking important pages or the sitemap.

## Final refinements

- Make only necessary adjustments, and fix global inconsistencies at the variable or preset level.
- Add subtle polish (small scroll animations, tasteful hovers) without overdoing it.
- Reread copy for consistent tone, terminology, button labels, and calls to action.
- Use the Page Manager to move between pages without leaving the builder; Speculative Prerendering can make that navigation feel faster.

## Test across devices and browsers

- Test real phones, tablets, laptops, and desktops, in Chrome, Safari, Firefox, and Edge.
- Tools such as BrowserStack, Sizzy, or ResponsivelyApp preview many sizes at once.
- Pay attention to scroll behavior, touch interactions, type size, sticky elements, forms, and off-canvas UI.
- Ask a few friends or colleagues to click around; they often spot issues you no longer see.

## Pre-launch preparations

- Use strong passwords and confirm SSL, so the site loads over HTTPS.
- Take a full backup. If you built on staging, migrate carefully and confirm links, media paths, forms, and Theme Builder assignments still work.
- Set up contact forms, analytics, email marketing, CRM connections, and other third-party services.
- Add needed 301 redirects, review DNS, and confirm the domain configuration.

## Go live

1. **Make the site public.** Under **Settings > Reading**, make sure **Discourage search engines from indexing this site** is unchecked.
2. **Publish all content and templates.** Confirm pages, posts, and Theme Builder templates (header, footer, single post, archives, search results, 404) are published and assigned.
3. **Flush permalinks.** Go to **Settings > Permalinks** and click **Save Changes**.
4. **Clear all caches:** Divi static CSS, optimization plugin, server, CDN, and browser.
5. **Test once more** on the live site in a private window while logged out: navigation, forms, responsive layouts, pop-ups, dynamic content, search, and any checkout or booking flow.
6. **Submit the sitemap** in the Google Search Console Sitemaps report.
7. **Announce the launch** via social, email, and relevant communities.
8. **Monitor** analytics, form submissions, server logs, uptime, and Search Console for the first 24 to 48 hours.

## Official documentation

[Part 16: Auditing, Polishing, and Launching Your Divi 5 Website](https://help.elegantthemes.com/en/articles/15704558-part-16-auditing-polishing-and-launching-your-divi-5-website)
