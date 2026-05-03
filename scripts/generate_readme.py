#!/usr/bin/env python3
"""
Generate the catalog section of README.md from data/tools.yml.

Rewrites only the content between:
  <!-- GENERATED:CATALOG:START -->
  <!-- GENERATED:CATALOG:END -->

Everything outside those markers is left untouched.
Run from the repo root: python scripts/generate_readme.py
"""

import re
import sys
import yaml

START_MARKER = "<!-- GENERATED:CATALOG:START -->"
END_MARKER = "<!-- GENERATED:CATALOG:END -->"
LUNCH_MONEY_BASE_URL = "https://lunchmoney.app"


def should_include_in_readme(item):
    """Return True unless readme.include is explicitly False."""
    readme = item.get("readme")
    if isinstance(readme, dict):
        return readme.get("include", True)
    return True


def should_render_subsection(subsection):
    return should_include_in_readme(subsection)


def html_to_markdown(text):
    """Convert simple HTML anchor tags to Markdown links; strip remaining tags."""
    # <a href="url" ...>label</a> → [label](url)
    text = re.sub(
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>',
        r"[\2](\1)",
        text,
    )
    # Strip any remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def readme_url(url):
    """Return an absolute URL suitable for links rendered on GitHub."""
    if url.startswith("/"):
        return f"{LUNCH_MONEY_BASE_URL}{url}"
    return url


def render_tool(tool, indent=""):
    """Render a single tool entry as a Markdown list item with sub-bullets."""
    lines = []

    # Primary link — prefer github, fall back to url, fall back to plain name
    if tool.get("github"):
        primary = f"[{tool['name']}]({tool['github']})"
    elif tool.get("url"):
        primary = f"[{tool['name']}]({tool['url']})"
    else:
        primary = tool["name"]

    line = f"{indent}* {primary} - {tool['description']}"
    if tool.get("author"):
        line += f" - (by {tool['author']})"
    lines.append(line)

    # Secondary URL when tool has both a github repo and a live URL
    if tool.get("github") and tool.get("url"):
        label = tool.get("url_label", "Website")
        lines.append(f"{indent}  * [{label}]({tool['url']})")

    # Additional links
    for link in tool.get("links", []):
        lines.append(f"{indent}  * [{link['label']}]({link['url']})")

    if tool.get("spotlight"):
        lines.append(f"{indent}  * [Spotlight Blog]({readme_url(tool['spotlight'])})")

    # Discord thread
    if tool.get("discord"):
        lines.append(f"{indent}  * [Discord]({tool['discord']})")

    return "\n".join(lines)


def render_section(section):
    """Render a full section (heading + optional description + tools + subsections).

    Returns None if all tools in the section are excluded from the README.
    """
    tools = [t for t in section.get("tools", []) if should_include_in_readme(t)]

    rendered_subs = []
    for sub in section.get("subsections", []):
        if not should_render_subsection(sub):
            continue
        sub_tools = [t for t in sub.get("tools", []) if should_include_in_readme(t)]
        if sub_tools:
            rendered_subs.append((sub, sub_tools))

    if not tools and not rendered_subs:
        return None

    lines = []
    lines.append(f"## {section['title']}")
    lines.append("")

    if section.get("description"):
        lines.append(html_to_markdown(section["description"]))
        lines.append("")

    for tool in tools:
        lines.append(render_tool(tool))

    if tools:
        lines.append("")

    for sub, sub_tools in rendered_subs:
        lines.append(f"### {sub['title']}")
        lines.append("")
        if sub.get("description"):
            lines.append(html_to_markdown(sub["description"]))
            lines.append("")
        if sub.get("note"):
            lines.append(html_to_markdown(sub["note"]))
            lines.append("")
        for tool in sub_tools:
            lines.append(render_tool(tool))
        lines.append("")

    return "\n".join(lines)


def main():
    try:
        with open("data/tools.yml") as f:
            sections = yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: data/tools.yml not found. Run from the repo root.")
        sys.exit(1)

    catalog_parts = [render_section(s) for s in sections]
    catalog = "\n".join(p for p in catalog_parts if p is not None).rstrip("\n")

    try:
        with open("README.md") as f:
            content = f.read()
    except FileNotFoundError:
        print("ERROR: README.md not found. Run from the repo root.")
        sys.exit(1)

    if START_MARKER not in content or END_MARKER not in content:
        print(
            f"ERROR: README.md is missing generation markers.\n"
            f"Add '{START_MARKER}' and '{END_MARKER}' to mark the generated region."
        )
        sys.exit(1)

    new_content = re.sub(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        f"{START_MARKER}\n{catalog}\n{END_MARKER}",
        content,
        flags=re.DOTALL,
    )

    with open("README.md", "w") as f:
        f.write(new_content)

    section_count = len(sections)
    tool_count = sum(
        len(s.get("tools", [])) +
        sum(len(sub.get("tools", [])) for sub in s.get("subsections", []))
        for s in sections
    )
    print(f"Generated README.md catalog: {section_count} sections, {tool_count} tools")


if __name__ == "__main__":
    main()
