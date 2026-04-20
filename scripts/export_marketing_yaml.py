#!/usr/bin/env python3
"""
Export data/tools.yml to generated/developer_tools.yml for the marketing site.

Filters out any tool or section with marketing_site.include: false and strips
internal control fields before writing. The output is a drop-in replacement for
marketing-site/_data/developer_tools.yml.

Run from the repo root: python scripts/export_marketing_yaml.py
"""

import copy
import os
import sys
import yaml

OUTPUT_PATH = "generated/developer_tools.yml"

HEADER = """\
#
# GENERATED FILE — do not edit manually.
# Source: awesome-lunchmoney/data/tools.yml
#
# To update entries: edit data/tools.yml in the awesome-lunchmoney repository.
# Changes are applied automatically when that repo merges to main.
#

"""

# Fields that are internal to tools.yml and should not appear in the export.
INTERNAL_FIELDS = {"marketing_site", "readme"}


def should_include_in_marketing(item):
    """Return True unless marketing_site.include is explicitly False."""
    ms = item.get("marketing_site")
    if isinstance(ms, dict):
        return ms.get("include", True)
    return True


def should_include_in_readme(item):
    """Return True unless readme.include is explicitly False."""
    readme = item.get("readme")
    if isinstance(readme, dict):
        return readme.get("include", True)
    return True


def should_include(item):
    """Return True only if the item is included in both outputs (i.e. not archived)."""
    return should_include_in_marketing(item) and should_include_in_readme(item)


def clean_tool(tool):
    return {k: v for k, v in tool.items() if k not in INTERNAL_FIELDS}


def export():
    try:
        with open("data/tools.yml") as f:
            sections = yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: data/tools.yml not found. Run from the repo root.")
        sys.exit(1)

    output = []

    for section in sections:
        if not should_include(section):
            continue

        out_section = {k: v for k, v in section.items() if k not in INTERNAL_FIELDS}

        # Filter direct tools
        if "tools" in section:
            filtered = [clean_tool(t) for t in section["tools"] if should_include(t)]
            out_section["tools"] = filtered

        # Filter subsection tools
        if "subsections" in section:
            out_subs = []
            for sub in section["subsections"]:
                filtered = [clean_tool(t) for t in sub.get("tools", []) if should_include(t)]
                if filtered:
                    out_sub = dict(sub)
                    out_sub["tools"] = filtered
                    out_subs.append(out_sub)
            out_section["subsections"] = out_subs

        # Skip section if it ended up with no tools after filtering
        has_tools = bool(out_section.get("tools")) or bool(out_section.get("subsections"))
        if not has_tools:
            continue

        output.append(out_section)

    os.makedirs("generated", exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        f.write(HEADER)
        yaml.dump(
            output,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        )

    tool_count = sum(
        len(s.get("tools", [])) +
        sum(len(sub.get("tools", [])) for sub in s.get("subsections", []))
        for s in output
    )
    print(f"Exported {OUTPUT_PATH}: {len(output)} sections, {tool_count} tools")


if __name__ == "__main__":
    export()
