---
title: "Divi MCP Servers"
description: "Status of MCP (Model Context Protocol) servers for Divi 5: the built-in Divi AI Agent, the not-yet-released official MCP, and third-party options."
category: playbooks
tags: [playbook, mcp, ai, automation]
divi_version: "5.x"
last_updated: 2026-11-04
content_type: playbook
audience: llm
---

# Divi MCP Servers

!!! abstract "Quick Reference"
    **Official Divi MCP server:** announced by Elegant Themes on 2026-11-04 as "coming soon" (preview video, no release date). Not yet available. The shipped product is the **Divi AI Agent** inside the Visual Builder.
    **Third-party MCP servers exist** (DiviOps, Wiplink, Respira, D5MCP). They are independent projects, not endorsed by Elegant Themes. Verify version support and maintenance before relying on one.
    **Rule for assistants:** never describe a third-party MCP as official, and never invent tool names. Read the project's own tool list.

## What MCP gives you

The Model Context Protocol lets an AI client (Claude Desktop, Claude Code, Cursor, etc.) call typed tools against a site, instead of driving the Visual Builder through screenshots. For Divi 5 that means reading and writing page content as Divi 5 block markup through WordPress, with the server handling authentication and validation. See [Block Format](../internals/block-format.md) and [REST API Content](rest-api-content.md) for the format underneath.

## Official status

| Item | Status (2026-11-04) |
|---|---|
| Divi AI Agent (in the Visual Builder, Divi AI subscribers) | Introduced in Divi 5.12 (2026-09-03). See [The Divi AI Agent in Divi 5](../modules/the-divi-ai-agent-in-divi-5.md) |
| Divi AI Agent tools | Elegant Themes describes ~200 agentic tools that let an AI model work in the builder like a human |
| Official Divi MCP server | **Coming soon** (Elegant Themes email, 2026-11-04). Exposes those tools over MCP so you can connect Divi sites to an AI agent of choice (ChatGPT, Codex, Claude Code, Cursor named). No release date, install steps, or help-center article yet |

Source: Elegant Themes email "First Look at the Divi MCP!" with a [preview video](https://www.youtube.com/watch?v=9_BHJGkt_qw). Until it ships, do not document connection steps, tool names, or authentication for it. When it is published, add the help-center article here and to the monitor's tracked list.

## Third-party servers (independent, unaffiliated)

Details are from each project's own listing as of the date above; re-check before use.

| Project | Notes |
|---|---|
| [DiviOps](https://www.npmjs.com/package/@diviops/mcp-server) (`@diviops/mcp-server` plus the DiviOps Agent WordPress plugin) | Typed tools over Divi 5 and WordPress state via the REST API. Listing states Divi 5.1+ and WordPress 6.5+; its plugin page states it is not affiliated with Elegant Themes |
| [Wiplink](https://wordpress.org/plugins/wiplink-mcp-for-divi-5/) | WordPress plugin for Divi 5 that connects Claude clients without a separate local install |
| [Respira](https://www.respira.press/divi-mcp) | Independent server for reading and editing Divi 4 and Divi 5 pages; advertises undo |
| [D5MCP](https://github.com/moeadas/D5MCP) | GitHub prototype that renders page-plan JSON into Divi 5 serialized blocks; not a supported product |

## Guidance for assistants using any Divi MCP

1. Work on a staging copy first; MCP tools write to the live database.
2. Prefer the server's own validation and undo features over raw block edits.
3. Confirm the Divi version (these docs track 5.15+ features such as [Components](../builder/components.md)); a server built against an older Divi 5 may not know newer modules or settings.
4. If a tool fails, fall back to [REST API Content](rest-api-content.md) or the [Visual Builder Ops](visual-builder-ops.md) playbook rather than guessing parameters.
