#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Divi 5 Docs - Content Monitor (v2)

Scans the Elegant Themes Help Center for new and changed articles,
compares against local documentation, detects content gaps, checks
for new Divi releases, and optionally auto-updates settings tables
or creates stub pages.

Usage:
    python3 scripts/monitor_updates.py --all                    # Report only
    python3 scripts/monitor_updates.py --all --dry-run          # Show what would change
    python3 scripts/monitor_updates.py --all --auto-update      # Auto-update changed pages
    python3 scripts/monitor_updates.py --all --auto-update --auto-create  # Also create stubs
    python3 scripts/monitor_updates.py --sources                # Only check source changes
    python3 scripts/monitor_updates.py --gaps                   # Only check content gaps
    python3 scripts/monitor_updates.py --scan                   # Only scan ET for new articles
    python3 scripts/monitor_updates.py --releases               # Only check Divi releases

Output:
    Writes a report to reports/update-report-YYYY-MM-DD.md
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Install dependencies: pip install requests beautifulsoup4")
    sys.exit(1)

try:
    import yaml
except ImportError:
    yaml = None

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPORT_DIR = "reports"
DOCS_DIR = "docs"
HASH_FILE = "scripts/et_content_hashes.json"
REQUEST_DELAY = 1  # seconds between ET fetches

ET_HELP_CENTER_COLLECTIONS = {
    "modules": "https://help.elegantthemes.com/en/collections/10650978-divi-5-modules",
    "woo-modules": "https://help.elegantthemes.com/en/collections/14719628-divi-5-woocommerce-modules",
    "options-groups": "https://help.elegantthemes.com/en/collections/10777927-divi-5-options-groups",
    "features": "https://help.elegantthemes.com/en/collections/11349519-divi-5-features",
    "flexbox": "https://help.elegantthemes.com/en/collections/13895918-flexbox-layout-system",
    "css-grid": "https://help.elegantthemes.com/en/collections/15495410-css-grid-layout-system",
    "vb-basics": "https://help.elegantthemes.com/en/collections/16928157-divi-5-visual-builder-basics",
    "vb-core": "https://help.elegantthemes.com/en/collections/16928174-divi-5-visual-builder-core-concepts",
    "vb-advanced": "https://help.elegantthemes.com/en/collections/17812093-divi-5-visual-builder-advanced-concepts",
    "getting-started": "https://help.elegantthemes.com/en/collections/16928111-getting-started",
    "faq": "https://help.elegantthemes.com/en/collections/14577685-divi-5-faq-and-troubleshooting",
}

# Map ET collection keys to local doc directories / categories
COLLECTION_CATEGORY_MAP = {
    "modules": "modules",
    "woo-modules": "modules",
    "options-groups": "builder",
    "features": "builder",
    "flexbox": "builder",
    "css-grid": "builder",
    "vb-basics": "builder",
    "vb-core": "builder",
    "vb-advanced": "builder",
    "getting-started": "builder",
    "faq": "troubleshooting",
}

HEADERS = {"User-Agent": "Divi5Docs Monitor/2.0"}

# Protected sections — auto_update_page will NEVER touch these
PROTECTED_SECTIONS = {
    "overview", "use cases", "code examples", "common patterns",
    "ai interaction notes", "troubleshooting", "related", "version notes",
    "how to add",
}

# ---------------------------------------------------------------------------
# Content hashing helpers
# ---------------------------------------------------------------------------


def load_hashes() -> dict:
    """Load the stored content hashes from disk."""
    path = Path(HASH_FILE)
    if path.exists():
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_hashes(hashes: dict) -> None:
    """Write content hashes to disk."""
    Path(HASH_FILE).write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n")


def fetch_page(url: str) -> str | None:
    """Fetch a URL and return the response text, or None on failure."""
    try:
        resp = requests.get(url, timeout=20, headers=HEADERS)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  [WARN] Failed to fetch {url}: {e}")
        return None


def extract_article_content(html: str) -> str:
    """Extract the main article body from an ET Help Center page.

    Strips navigation, footer, sidebars, and other boilerplate so that only
    the article content is hashed.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove script, style, nav, footer, header elements
    for tag in soup.find_all(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()

    # Try common Intercom Help Center article selectors
    article = (
        soup.find("article")
        or soup.find("div", class_="article__body")
        or soup.find("div", class_="intercom-interblocks-html-block")
        or soup.find("main")
    )

    if article:
        return article.get_text(separator="\n", strip=True)

    # Fallback: entire body text
    body = soup.find("body")
    return body.get_text(separator="\n", strip=True) if body else ""


def hash_content(text: str) -> str:
    """SHA-256 hex digest of the given text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Extract settings from ET articles
# ---------------------------------------------------------------------------


def extract_settings_from_html(html: str) -> dict:
    """Parse an ET article and return settings grouped by tab.

    Returns dict like:
        {"Content Tab": [{"setting": "...", "type": "...", "description": "..."}, ...], ...}
    """
    soup = BeautifulSoup(html, "html.parser")
    settings_by_tab: dict[str, list[dict]] = {}
    current_tab = "General"

    # Look for headings that indicate tabs
    for heading in soup.find_all(["h2", "h3", "h4", "strong", "b"]):
        text = heading.get_text(strip=True).lower()
        if "content tab" in text or "content settings" in text:
            current_tab = "Content Tab"
        elif "design tab" in text or "design settings" in text:
            current_tab = "Design Tab"
        elif "advanced tab" in text or "advanced settings" in text:
            current_tab = "Advanced Tab"

    # Look for tables in the article
    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if not rows:
            continue

        # Determine which tab this table belongs to by looking at preceding headings
        tab_name = "General"
        prev = table.find_previous(["h2", "h3", "h4"])
        if prev:
            prev_text = prev.get_text(strip=True).lower()
            if "content" in prev_text:
                tab_name = "Content Tab"
            elif "design" in prev_text:
                tab_name = "Design Tab"
            elif "advanced" in prev_text:
                tab_name = "Advanced Tab"

        if tab_name not in settings_by_tab:
            settings_by_tab[tab_name] = []

        for row in rows[1:]:  # skip header row
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                setting_name = cells[0].get_text(strip=True)
                description = cells[-1].get_text(strip=True)
                setting_type = cells[1].get_text(strip=True) if len(cells) >= 3 else ""
                if setting_name and setting_name.lower() != "setting":
                    settings_by_tab[tab_name].append({
                        "setting": setting_name,
                        "type": setting_type,
                        "description": description,
                    })

    # Also look for bold/strong items in lists as settings
    if not settings_by_tab:
        current_tab = "General"
        for element in soup.find_all(["h2", "h3", "h4", "li"]):
            if element.name in ("h2", "h3", "h4"):
                text = element.get_text(strip=True).lower()
                if "content" in text:
                    current_tab = "Content Tab"
                elif "design" in text:
                    current_tab = "Design Tab"
                elif "advanced" in text:
                    current_tab = "Advanced Tab"
            elif element.name == "li":
                bold = element.find(["strong", "b"])
                if bold:
                    setting_name = bold.get_text(strip=True).rstrip(":")
                    desc_text = element.get_text(strip=True)
                    # Remove the setting name from the description
                    description = desc_text[len(bold.get_text(strip=True)):].strip().lstrip(":-–— ")
                    if current_tab not in settings_by_tab:
                        settings_by_tab[current_tab] = []
                    settings_by_tab[current_tab].append({
                        "setting": setting_name,
                        "type": "",
                        "description": description,
                    })

    return settings_by_tab


# ---------------------------------------------------------------------------
# Parse local doc settings tables
# ---------------------------------------------------------------------------


def parse_local_settings(content: str) -> dict:
    """Parse settings tables from a local Markdown doc.

    Returns dict like:
        {"Content Tab": [{"setting": "...", "type": "...", "description": "..."}, ...], ...}
    """
    settings_by_tab: dict[str, list[dict]] = {}
    current_tab = None

    lines = content.split("\n")
    in_table = False
    header_seen = False

    for line in lines:
        stripped = line.strip()

        # Detect tab headings
        if re.match(r"^###\s+Content\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Content Tab"
            in_table = False
            header_seen = False
        elif re.match(r"^###\s+Design\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Design Tab"
            in_table = False
            header_seen = False
        elif re.match(r"^###\s+Advanced\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Advanced Tab"
            in_table = False
            header_seen = False
        elif stripped.startswith("### "):
            # A different subsection — stop collecting
            in_table = False
            header_seen = False

        # Detect table rows
        if current_tab and stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if not header_seen:
                # This is the header row
                header_seen = True
                continue
            if all(set(c) <= {"-", " ", ":"} for c in cells):
                # Separator row
                continue
            if len(cells) >= 3:
                setting_name = cells[0]
                setting_type = cells[1]
                description = cells[2] if len(cells) == 3 else cells[-1]
                description = re.sub(r"\s*<!--.*?-->\s*$", "", description).strip()
                if current_tab not in settings_by_tab:
                    settings_by_tab[current_tab] = []
                settings_by_tab[current_tab].append({
                    "setting": setting_name,
                    "type": setting_type,
                    "description": description,
                })
            elif len(cells) == 2:
                # Some tables use Setting | Description
                if current_tab not in settings_by_tab:
                    settings_by_tab[current_tab] = []
                settings_by_tab[current_tab].append({
                    "setting": cells[0],
                    "type": "",
                    "description": cells[1],
                })

    return settings_by_tab


# ---------------------------------------------------------------------------
# Diff settings
# ---------------------------------------------------------------------------


def diff_settings(local: dict, remote: dict) -> dict:
    """Compare local and remote settings, returning structured diff.

    Returns:
        {
            "added": {"Tab Name": [{"setting": ..., "type": ..., "description": ...}]},
            "changed": {"Tab Name": [{"setting": ..., "old_desc": ..., "new_desc": ...}]},
            "removed": {"Tab Name": ["setting_name", ...]},
        }
    """
    result = {"added": {}, "changed": {}, "removed": {}}

    all_tabs = set(list(local.keys()) + list(remote.keys()))
    for tab in all_tabs:
        local_settings = {s["setting"].lower(): s for s in local.get(tab, [])}
        remote_settings = {s["setting"].lower(): s for s in remote.get(tab, [])}

        # New settings (in remote but not local)
        for key, setting in remote_settings.items():
            if key not in local_settings:
                result["added"].setdefault(tab, []).append(setting)

        # Changed descriptions
        for key, local_s in local_settings.items():
            if key in remote_settings:
                remote_s = remote_settings[key]
                # Only flag if descriptions differ meaningfully
                if (remote_s["description"].lower().strip() != local_s["description"].lower().strip()
                        and len(remote_s["description"]) > 5):
                    result["changed"].setdefault(tab, []).append({
                        "setting": local_s["setting"],
                        "old_desc": local_s["description"],
                        "new_desc": remote_s["description"],
                    })

        # Removed settings (in local but not remote)
        for key in local_settings:
            if key not in remote_settings:
                result["removed"].setdefault(tab, []).append(local_settings[key]["setting"])

    return result


# ---------------------------------------------------------------------------
# Collect known source URLs from local docs
# ---------------------------------------------------------------------------


def get_known_source_urls(docs_dir: str) -> dict:
    """Return mapping of source_url -> local file path for all docs with source_url."""
    known = {}
    for md_file in Path(docs_dir).rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="replace")
        fm_match = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
        if not fm_match:
            continue
        source_match = re.search(r'source_url:\s*["\'](.+?)["\']', fm_match.group(1))
        if source_match:
            url = source_match.group(1).rstrip("/")
            known[url] = str(md_file)
    return known


# ---------------------------------------------------------------------------
# Core check functions
# ---------------------------------------------------------------------------


def check_content_gaps(docs_dir: str) -> list:
    """Identify pages that are placeholders or have TODO markers."""
    gaps = []

    for md_file in Path(docs_dir).rglob("*.md"):
        if md_file.name == "index.md":
            continue

        content = md_file.read_text(encoding="utf-8", errors="replace")

        todo_count = content.count("<!-- TODO")
        is_placeholder = "Placeholder" in content and "needs community contributions" in content
        has_no_settings = "## Settings & Options" not in content and "modules/" in str(md_file)
        word_count = len(content.split())

        if is_placeholder:
            gaps.append({
                "file": str(md_file),
                "issue": "PLACEHOLDER",
                "detail": "Page is a stub placeholder with no real content",
                "word_count": word_count,
            })
        elif todo_count > 3:
            gaps.append({
                "file": str(md_file),
                "issue": "MANY_TODOS",
                "detail": f"{todo_count} TODO markers — needs enrichment",
                "word_count": word_count,
            })
        elif has_no_settings:
            gaps.append({
                "file": str(md_file),
                "issue": "MISSING_SETTINGS",
                "detail": "Module page has no Settings section",
                "word_count": word_count,
            })

    return gaps


def check_divi_releases() -> list:
    """Check for new Divi releases and changelog entries."""
    findings = []
    urls_to_check = [
        "https://www.elegantthemes.com/blog/theme-releases/divi-release-notes",
        "https://www.elegantthemes.com/api/changelog/divi",
    ]

    for url in urls_to_check:
        try:
            resp = requests.get(url, timeout=15, headers=HEADERS)
            if resp.status_code == 200:
                findings.append({
                    "url": url,
                    "status": "ACCESSIBLE",
                    "detail": f"Check for new release notes. Response size: {len(resp.text)} bytes",
                })
        except Exception as e:
            findings.append({
                "url": url,
                "status": "ERROR",
                "detail": str(e),
            })

    return findings


def scan_et_help_center(docs_dir: str) -> list:
    """Scan ET Help Center collections for articles not in our repo.

    Returns list of dicts with keys: title, url, collection, suggested_file, category.
    """
    known_urls = get_known_source_urls(docs_dir)
    # Extract article IDs for fuzzy matching — handles both
    # "articles/10063343" and "articles/10063343-the-accordion-module" formats
    known_ids = set()
    known_set = set()
    for u in known_urls:
        u_clean = u.rstrip("/")
        known_set.add(u_clean)
        m = re.search(r"/articles/(\d+)", u_clean)
        if m:
            known_ids.add(m.group(1))

    new_articles = []
    total_collections = len(ET_HELP_CENTER_COLLECTIONS)

    for idx, (collection_key, collection_url) in enumerate(ET_HELP_CENTER_COLLECTIONS.items(), 1):
        print(f"  Scanning collection {idx}/{total_collections}: {collection_key}")

        html = fetch_page(collection_url)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")

        # Find article links — Intercom uses /en/articles/ pattern
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if "/en/articles/" not in href:
                continue

            # Normalize URL
            if href.startswith("/"):
                full_url = "https://help.elegantthemes.com" + href
            elif not href.startswith("http"):
                continue
            else:
                full_url = href

            full_url = full_url.rstrip("/")

            # Skip if we already have this (match by article ID, not full URL)
            if full_url in known_set:
                continue
            article_id_match = re.search(r"/articles/(\d+)", full_url)
            if article_id_match and article_id_match.group(1) in known_ids:
                continue

            title = a_tag.get_text(strip=True)
            if not title or len(title) < 3:
                continue

            # Generate suggested file path
            category = COLLECTION_CATEGORY_MAP.get(collection_key, "builder")
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            suggested_file = f"docs/{category}/{slug}.md"

            new_articles.append({
                "title": title,
                "url": full_url,
                "collection": collection_key,
                "suggested_file": suggested_file,
                "category": category,
            })

        time.sleep(REQUEST_DELAY)

    # Deduplicate by article ID
    seen_ids = set()
    unique = []
    for article in new_articles:
        aid = re.search(r"/articles/(\d+)", article["url"])
        key = aid.group(1) if aid else article["url"]
        if key not in seen_ids:
            seen_ids.add(key)
            unique.append(article)

    return unique


def check_source_changes(docs_dir: str) -> list:
    """Check docs with ET source_url for content changes using hashing.

    Returns list of dicts with keys: file, source_url, diff, new_hash.
    """
    hashes = load_hashes()
    known_urls = get_known_source_urls(docs_dir)
    changes = []
    updated_hashes = dict(hashes)  # copy to update

    # Filter to only help.elegantthemes.com URLs
    et_docs = {
        url: path for url, path in known_urls.items()
        if "help.elegantthemes.com" in url
    }

    total = len(et_docs)
    print(f"  Checking {total} articles with ET source URLs...")

    for idx, (source_url, local_path) in enumerate(et_docs.items(), 1):
        if idx % 10 == 0 or idx == 1:
            print(f"  Checking {idx}/{total} articles...")

        html = fetch_page(source_url)
        if not html:
            continue

        article_text = extract_article_content(html)
        new_hash = hash_content(article_text)
        old_hash = hashes.get(source_url)

        # Always store the hash
        updated_hashes[source_url] = new_hash

        if old_hash is None:
            # First time seeing this URL — store hash, no diff
            continue

        if new_hash == old_hash:
            # No change
            continue

        # Content changed — compute diff
        local_content = Path(local_path).read_text(encoding="utf-8", errors="replace")
        local_settings = parse_local_settings(local_content)
        remote_settings = extract_settings_from_html(html)
        settings_diff = diff_settings(local_settings, remote_settings)

        has_meaningful_diff = (
            any(settings_diff["added"].values())
            or any(settings_diff["changed"].values())
            or any(settings_diff["removed"].values())
        )

        changes.append({
            "file": local_path,
            "source_url": source_url,
            "diff": settings_diff if has_meaningful_diff else None,
            "new_hash": new_hash,
            "content_changed": True,
            "settings_changed": has_meaningful_diff,
        })

        time.sleep(REQUEST_DELAY)

    # Save updated hashes
    save_hashes(updated_hashes)
    return changes


# ---------------------------------------------------------------------------
# Auto-update and stub creation
# ---------------------------------------------------------------------------


def auto_update_page(source_url: str, local_path: str, dry_run: bool = False) -> dict:
    """Auto-update settings tables in a local doc from its ET source article.

    Only appends new settings rows. Never deletes. Never modifies protected sections.

    Returns dict summarizing what was changed.
    """
    result = {"file": local_path, "settings_added": 0, "tabs_updated": [], "skipped": []}

    html = fetch_page(source_url)
    if not html:
        result["error"] = "Failed to fetch source article"
        return result

    remote_settings = extract_settings_from_html(html)
    local_content = Path(local_path).read_text(encoding="utf-8", errors="replace")
    local_settings = parse_local_settings(local_content)
    settings_diff = diff_settings(local_settings, remote_settings)

    if not any(settings_diff["added"].values()):
        result["skipped"].append("No new settings to add")
        return result

    if dry_run:
        for tab, new_settings in settings_diff["added"].items():
            result["settings_added"] += len(new_settings)
            result["tabs_updated"].append(tab)
        return result

    # Apply additions
    lines = local_content.split("\n")
    new_lines = []
    current_tab = None
    last_table_row_idx = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        if re.match(r"^###\s+Content\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Content Tab"
            last_table_row_idx = None
        elif re.match(r"^###\s+Design\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Design Tab"
            last_table_row_idx = None
        elif re.match(r"^###\s+Advanced\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Advanced Tab"
            last_table_row_idx = None
        elif stripped.startswith("### ") or stripped.startswith("## "):
            # Flush any pending additions for previous tab
            if current_tab and current_tab in settings_diff["added"] and last_table_row_idx is not None:
                # We already passed the table — insert will happen below
                pass
            if stripped.startswith("## "):
                current_tab = None
            last_table_row_idx = None

        # Track last table row in current tab
        if current_tab and stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if not all(set(c) <= {"-", " ", ":"} for c in cells):
                last_table_row_idx = len(new_lines)

        new_lines.append(line)

    # Now we need a second pass to actually insert rows
    # Strategy: find the last table row for each tab and insert after it
    output_lines = []
    current_tab = None
    in_table = False
    table_ended = False
    pending_additions = {}

    for tab, new_settings in settings_diff["added"].items():
        pending_additions[tab] = new_settings

    for line in new_lines:
        stripped = line.strip()

        if re.match(r"^###\s+Content\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Content Tab"
            in_table = False
            table_ended = False
        elif re.match(r"^###\s+Design\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Design Tab"
            in_table = False
            table_ended = False
        elif re.match(r"^###\s+Advanced\s+Tab", stripped, re.IGNORECASE):
            current_tab = "Advanced Tab"
            in_table = False
            table_ended = False
        elif stripped.startswith("### ") or stripped.startswith("## "):
            # If we were in a tab and the table ended but we haven't flushed, flush now
            if current_tab and current_tab in pending_additions and in_table:
                for s in pending_additions[current_tab]:
                    row = f"| {s['setting']} | {s['type']} | {s['description']} <!-- AUTO-ADDED --> |"
                    output_lines.append(row)
                    result["settings_added"] += 1
                if current_tab not in result["tabs_updated"]:
                    result["tabs_updated"].append(current_tab)
                del pending_additions[current_tab]
                in_table = False

            if stripped.startswith("## "):
                current_tab = None
            in_table = False
            table_ended = False

        # Detect table rows
        if current_tab and stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            table_ended = False
        elif in_table and not stripped.startswith("|"):
            # Table just ended — flush additions
            if current_tab and current_tab in pending_additions:
                for s in pending_additions[current_tab]:
                    row = f"| {s['setting']} | {s['type']} | {s['description']} <!-- AUTO-ADDED --> |"
                    output_lines.append(row)
                    result["settings_added"] += 1
                if current_tab not in result["tabs_updated"]:
                    result["tabs_updated"].append(current_tab)
                del pending_additions[current_tab]
            in_table = False
            table_ended = True

        output_lines.append(line)

    # Flush any remaining pending additions (if table was at end of file)
    if current_tab and current_tab in pending_additions and in_table:
        for s in pending_additions[current_tab]:
            row = f"| {s['setting']} | {s['type']} | {s['description']} <!-- AUTO-ADDED --> |"
            output_lines.append(row)
            result["settings_added"] += 1
        if current_tab not in result["tabs_updated"]:
            result["tabs_updated"].append(current_tab)

    if result["settings_added"] > 0:
        updated_content = "\n".join(output_lines)

        # Update last_updated in frontmatter
        today = date.today().isoformat()
        updated_content = re.sub(
            r"(last_updated:\s*)\S+",
            f"\\g<1>{today}",
            updated_content,
            count=1,
        )

        # Add auto-update marker after frontmatter
        if f"<!-- AUTO-UPDATED:" not in updated_content:
            updated_content = updated_content.replace(
                "---\n\n",
                f"---\n\n<!-- AUTO-UPDATED: {today} — verify changes -->\n\n",
                1,
            )

        Path(local_path).write_text(updated_content, encoding="utf-8")

    return result


def create_stub_page(
    et_url: str, target_dir: str, slug: str, title: str = "",
    category: str = "modules", dry_run: bool = False,
) -> dict:
    """Create a minimal stub page from an ET article.

    Returns dict with keys: file, title, settings_count.
    """
    result = {"file": "", "title": "", "settings_count": 0}

    html = fetch_page(et_url)
    if not html:
        result["error"] = "Failed to fetch ET article"
        return result

    # Extract title from page if not provided
    if not title:
        soup = BeautifulSoup(html, "html.parser")
        h1 = soup.find("h1")
        title = h1.get_text(strip=True) if h1 else slug.replace("-", " ").title()

    result["title"] = title
    target_path = os.path.join(target_dir, f"{slug}.md")
    result["file"] = target_path

    # Extract settings
    settings_by_tab = extract_settings_from_html(html)
    total_settings = sum(len(v) for v in settings_by_tab.values())
    result["settings_count"] = total_settings

    if dry_run:
        return result

    # Build the stub page
    today = date.today().isoformat()
    lines = [
        "---",
        f'title: "{title}"',
        f"category: {category}",
        f"tags: [{category}]",
        f"related: []",
        f'divi_version: "5.x"',
        f"last_updated: {today}",
        f'source_url: "{et_url}"',
        "---",
        "",
        f"# {title}",
        "",
        f"<!-- AUTO-CREATED: {today} — stub from ET Help Center, needs enrichment -->",
        "",
        "## Overview",
        "",
        f"For detailed information, see the [official Elegant Themes documentation]({et_url}).",
        "",
        "<!-- TODO: Write a 2-3 paragraph overview of this feature/module -->",
        "",
    ]

    # Settings section
    if settings_by_tab:
        lines.append("## Settings & Options")
        lines.append("")

        for tab_name, settings in settings_by_tab.items():
            lines.append(f"### {tab_name}")
            lines.append("")
            lines.append("| Setting | Type | Description |")
            lines.append("|---------|------|-------------|")
            for s in settings:
                lines.append(f"| {s['setting']} | {s['type']} | {s['description']} |")
            lines.append("")
    else:
        lines.append("## Settings & Options")
        lines.append("")
        lines.append("<!-- TODO: Document all settings from the three tabs (Content, Design, Advanced) -->")
        lines.append("")

    # Remaining standard sections
    lines.extend([
        "## Code Examples",
        "",
        "<!-- TODO: Add CSS/PHP code examples -->",
        "",
        "## Common Patterns",
        "",
        "<!-- TODO: Document 2-3 common usage patterns -->",
        "",
        "## Troubleshooting",
        "",
        "<!-- TODO: Document common issues and solutions -->",
        "",
        "## AI Interaction Notes",
        "",
        "| Task | Confidence | Notes |",
        "|------|-----------|-------|",
        "| Basic placement | \U0001f52c Needs Testing | Untested — stub page |",
        "| Settings configuration | \U0001f52c Needs Testing | Untested — stub page |",
        "| Custom styling | \U0001f52c Needs Testing | Untested — stub page |",
        "",
        "## Related",
        "",
        "<!-- TODO: Add links to related documentation pages -->",
        "",
    ])

    os.makedirs(target_dir, exist_ok=True)
    Path(target_path).write_text("\n".join(lines), encoding="utf-8")

    return result


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def generate_report(
    source_changes: list,
    content_gaps: list,
    release_checks: list,
    new_articles: list,
    actions_taken: list,
    needs_review: list,
) -> str:
    """Generate a Markdown report."""
    today = date.today().isoformat()
    lines = [
        f"# Divi 5 Docs — Update Report ({today})",
        "",
        "Auto-generated by `scripts/monitor_updates.py`. Review and act on findings below.",
        "",
    ]

    # Actions Taken
    lines.append("## Actions Taken")
    lines.append("")
    if actions_taken:
        for action in actions_taken:
            lines.append(f"- {action}")
    else:
        lines.append("- No automated actions taken (report-only mode)")
    lines.append("")

    # Source Changes Detected
    if source_changes:
        changed = [c for c in source_changes if c.get("settings_changed")]
        content_only = [c for c in source_changes if c.get("content_changed") and not c.get("settings_changed")]

        if changed:
            lines.append("## Source Changes Detected (Settings)")
            lines.append("")
            lines.append("| File | Settings Added | Settings Changed | Detail |")
            lines.append("|------|---------------|-----------------|--------|")
            for c in changed:
                diff = c.get("diff", {})
                added_count = sum(len(v) for v in diff.get("added", {}).values()) if diff else 0
                changed_count = sum(len(v) for v in diff.get("changed", {}).values()) if diff else 0
                detail = []
                if added_count:
                    detail.append(f"{added_count} new")
                if changed_count:
                    detail.append(f"{changed_count} modified")
                lines.append(
                    f"| `{c['file']}` | {added_count} | {changed_count} | {', '.join(detail)} |"
                )
            lines.append("")

        if content_only:
            lines.append("## Source Changes Detected (Content Only)")
            lines.append("")
            lines.append("These articles changed but no settings table differences were found:")
            lines.append("")
            for c in content_only:
                lines.append(f"- `{c['file']}` — [{c['source_url']}]({c['source_url']})")
            lines.append("")

    # New ET Articles
    if new_articles:
        lines.append("## New ET Articles")
        lines.append("")
        lines.append("| Title | ET URL | Suggested File | Category |")
        lines.append("|-------|--------|---------------|----------|")
        for a in new_articles:
            lines.append(
                f"| {a['title']} | [{a['url']}]({a['url']}) | `{a['suggested_file']}` | {a['category']} |"
            )
        lines.append("")

    # Content Gaps
    if content_gaps:
        lines.append("## Content Gaps")
        lines.append("")
        lines.append("| File | Issue | Words | Detail |")
        lines.append("|------|-------|-------|--------|")
        for g in sorted(content_gaps, key=lambda x: x.get("word_count", 0)):
            lines.append(
                f"| `{g['file']}` | {g['issue']} | {g.get('word_count', '?')} | {g['detail']} |"
            )
        lines.append("")

    # Divi Release Notes
    if release_checks:
        lines.append("## Divi Release Notes")
        lines.append("")
        for r in release_checks:
            lines.append(f"- **{r.get('url', 'Unknown')}**: {r['detail']}")
        lines.append("")

    # Needs Human Review
    if needs_review:
        lines.append("## Needs Human Review")
        lines.append("")
        for item in needs_review:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Divi 5 Docs Content Monitor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/monitor_updates.py --all                    Report only (default)
  python3 scripts/monitor_updates.py --all --dry-run          Show what would change
  python3 scripts/monitor_updates.py --all --auto-update      Auto-update changed pages
  python3 scripts/monitor_updates.py --all --auto-update --auto-create  Also create stubs
  python3 scripts/monitor_updates.py --sources                Only check source changes
  python3 scripts/monitor_updates.py --gaps                   Only check content gaps
  python3 scripts/monitor_updates.py --scan                   Only scan ET for new articles
  python3 scripts/monitor_updates.py --releases               Only check Divi releases
""",
    )
    parser.add_argument("--all", action="store_true", help="Run all checks")
    parser.add_argument("--sources", action="store_true", help="Check source content changes (hashing)")
    parser.add_argument("--gaps", action="store_true", help="Check content gaps")
    parser.add_argument("--scan", action="store_true", help="Scan ET Help Center for new articles")
    parser.add_argument("--releases", action="store_true", help="Check Divi releases")
    parser.add_argument("--auto-update", action="store_true", help="Auto-update settings tables for changed pages")
    parser.add_argument("--auto-create", action="store_true", help="Create stub pages for new ET articles")
    parser.add_argument("--dry-run", action="store_true", help="Log changes without writing files")

    args = parser.parse_args()

    if not any([args.all, args.sources, args.gaps, args.scan, args.releases]):
        args.all = True

    actions_taken = []
    needs_review = []

    # --- Source changes ---
    source_changes = []
    if args.all or args.sources:
        print("Checking source content changes...")
        source_changes = check_source_changes(DOCS_DIR)
        print(f"  Found {len(source_changes)} changed articles")

        hashes_updated = len(source_changes)  # approximate
        if hashes_updated:
            actions_taken.append(f"Updated content hashes for checked articles")

        if args.auto_update:
            update_count = 0
            for change in source_changes:
                if change.get("settings_changed") and change.get("diff"):
                    diff = change["diff"]
                    if any(diff["added"].values()):
                        print(f"  Auto-updating: {change['file']}")
                        result = auto_update_page(
                            change["source_url"], change["file"], dry_run=args.dry_run
                        )
                        if result.get("settings_added", 0) > 0:
                            update_count += 1
                            if args.dry_run:
                                actions_taken.append(
                                    f"[DRY RUN] Would update {change['file']}: "
                                    f"+{result['settings_added']} settings"
                                )
                            else:
                                actions_taken.append(
                                    f"Updated settings tables in {change['file']}: "
                                    f"+{result['settings_added']} settings"
                                )
                    # Flag changed descriptions for human review
                    if any(diff["changed"].values()):
                        for tab, changed_list in diff["changed"].items():
                            for cs in changed_list:
                                needs_review.append(
                                    f"`{change['file']}` — {tab} — "
                                    f"**{cs['setting']}** description changed"
                                )
            if update_count:
                actions_taken.append(f"Updated settings tables in {update_count} pages")

    # --- Scan ET Help Center ---
    new_articles = []
    if args.all or args.scan:
        print("Scanning ET Help Center collections...")
        new_articles = scan_et_help_center(DOCS_DIR)
        print(f"  Found {len(new_articles)} new articles not in our repo")

        if args.auto_create and new_articles:
            create_count = 0
            for article in new_articles:
                target_dir = os.path.join(DOCS_DIR, article["category"])
                slug = re.sub(r"[^a-z0-9]+", "-", article["title"].lower()).strip("-")
                print(f"  Creating stub: {article['category']}/{slug}.md")
                result = create_stub_page(
                    et_url=article["url"],
                    target_dir=target_dir,
                    slug=slug,
                    title=article["title"],
                    category=article["category"],
                    dry_run=args.dry_run,
                )
                if result.get("file"):
                    create_count += 1
                    if args.dry_run:
                        actions_taken.append(
                            f"[DRY RUN] Would create {result['file']} "
                            f"({result['settings_count']} settings)"
                        )
                    else:
                        actions_taken.append(f"Created stub page: {result['file']}")
                time.sleep(REQUEST_DELAY)
            if create_count:
                actions_taken.append(f"Created {create_count} new stub pages")

    # --- Content gaps ---
    content_gaps = []
    if args.all or args.gaps:
        print("Checking content gaps...")
        content_gaps = check_content_gaps(DOCS_DIR)
        print(f"  Found {len(content_gaps)} content gaps")

    # --- Divi releases ---
    release_checks = []
    if args.all or args.releases:
        print("Checking Divi releases...")
        release_checks = check_divi_releases()

    # --- Generate report ---
    report = generate_report(
        source_changes=source_changes,
        content_gaps=content_gaps,
        release_checks=release_checks,
        new_articles=new_articles,
        actions_taken=actions_taken,
        needs_review=needs_review,
    )

    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(REPORT_DIR, f"update-report-{date.today().isoformat()}.md")
    with open(report_path, "w") as f:
        f.write(report)

    print(f"\nReport written to {report_path}")
    print(f"  Source changes: {len(source_changes)}")
    print(f"  New ET articles: {len(new_articles)}")
    print(f"  Content gaps: {len(content_gaps)}")
    print(f"  Release checks: {len(release_checks)}")
    print(f"  Actions taken: {len(actions_taken)}")
    print(f"  Needs review: {len(needs_review)}")


if __name__ == "__main__":
    main()
