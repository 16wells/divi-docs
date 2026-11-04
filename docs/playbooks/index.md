---
title: "LLM Playbooks"
description: "Divi 5 LLM playbooks — instruction guides that teach AI assistants how to build pages, manage CSS, automate the Visual Builder, and avoid common pitfalls."
category: playbooks
tags: [playbooks, llm, ai, automation, guide]
last_updated: 2026-03-12
---

# LLM Playbooks

Instruction guides that teach AI assistants how to operate Divi 5.

!!! abstract "Quick Reference"
    **What these are:** LLM-first documentation designed for AI assistants helping users build and modify Divi 5 websites.
    **How to use:** Drop playbooks into your AI assistant's context (system prompt, project knowledge, etc.) before asking Divi questions.
    **Playbooks available:** Design System Setup | Build a Page | Visual Builder Ops | CSS in Divi | Responsive Design | Layout Patterns | HTML Workarounds | REST API Content | Browser Automation | Theme Builder Ops | Divi MCP Servers | Known Limitations | Troubleshooting Tree

## What These Are

Playbooks are **LLM-first documentation**. Their primary reader is an AI assistant (Claude, ChatGPT, Copilot, etc.) that's been asked to help someone build or modify a Divi 5 website. Their secondary reader is a human trying to understand how to use AI tools with Divi effectively.

This is fundamentally different from the reference docs in the rest of this site. Reference docs answer "what does this setting do?" Playbooks answer "how do I actually accomplish this task, step by step, without hitting the landmines?"

## Why These Exist

Every Divi user who asks an AI assistant for help gets the same experience: the AI gives advice that sounds plausible but breaks in Divi's specific context. Divi 5's Visual Builder has behaviors, constraints, and quirks that no LLM has been trained on. These playbooks fix that gap.

**How to use them:** Drop one or more playbooks into your AI assistant's context (Claude Project Knowledge, ChatGPT custom instructions, system prompt, etc.) before asking Divi-related questions. The AI will follow the instructions and avoid the documented pitfalls.

## Playbook Index

### Getting Started
| Playbook | What It Teaches the LLM |
|----------|------------------------|
| [Design System Setup](design-system-setup.md) | Configure global typography, colors, and variables BEFORE building pages |
| [Build a Page](build-a-page.md) | End-to-end workflow for creating a new Divi 5 page |
| [Visual Builder Operations](visual-builder-ops.md) | How the VB works — dual-frame architecture, panels, saving behavior |

### Building & Styling
| Playbook | What It Teaches the LLM |
|----------|------------------------|
| [CSS in Divi 5](css-in-divi.md) | When to use Design tab vs Custom CSS vs Free-Form CSS vs child theme |
| [Responsive Design](responsive-design.md) | Breakpoints, device-specific overrides, mobile-first patterns |
| [Layout Patterns](layout-patterns.md) | Common section layouts with exact module/row/column configurations |
| [HTML Workarounds](html-workarounds.md) | Table-based cards, SVG icons, inline CSS patterns that survive sanitization |

### Developer Operations
| Playbook | What It Teaches the LLM |
|----------|------------------------|
| [REST API Content Management](rest-api-content.md) | Programmatic content creation — block format, encoding, boundaries |
| [Browser Automation](browser-automation.md) | Automating the Visual Builder with Playwright/Claude in Chrome |
| [Theme Builder Operations](theme-builder-ops.md) | Global headers, footers, and post templates |

### Guardrails
| Playbook | What It Teaches the LLM |
|----------|------------------------|
| [Divi MCP Servers](divi-mcp-servers.md) | Status of official and third-party MCP servers for Divi 5 |
| [Known Limitations](known-limitations.md) | Things LLMs consistently get wrong about Divi 5 |
| [Troubleshooting Decision Tree](troubleshooting-tree.md) | Systematic diagnosis for common problems |

!!! tip "Contributing Playbooks"
    If you've discovered a Divi 5 behavior that tripped up your AI assistant, write it up as a playbook. The format is different from reference docs — see the [Contributing Guide](../contributing.md) for playbook-specific guidelines.
