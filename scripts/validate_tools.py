#!/usr/bin/env python3
"""
Validate data/tools.yml against the required schema.

Exits with code 0 on success, 1 if any validation errors are found.
Run from the repo root: python scripts/validate_tools.py
"""

import sys
import yaml

REQUIRED_TOOL_FIELDS = ["name", "description"]


def validate_tool(tool, location):
    errors = []
    for field in REQUIRED_TOOL_FIELDS:
        if not tool.get(field):
            errors.append(f"{location}: missing required field '{field}'")
    return errors


def validate_subsection(sub, location):
    errors = []
    if not sub.get("title"):
        errors.append(f"{location}: missing required field 'title'")
    if not sub.get("tools"):
        errors.append(f"{location}: 'tools' list is empty or missing")
    for i, tool in enumerate(sub.get("tools", [])):
        tool_loc = f"{location} > tool[{i}] ({tool.get('name', '?')})"
        errors.extend(validate_tool(tool, tool_loc))
    return errors


def validate_section(section, index):
    errors = []
    loc = f"section[{index}] (id={section.get('id', '?')})"

    for field in ["id", "title"]:
        if not section.get(field):
            errors.append(f"{loc}: missing required field '{field}'")

    has_tools = bool(section.get("tools"))
    has_subsections = bool(section.get("subsections"))
    if not has_tools and not has_subsections:
        errors.append(f"{loc}: must have at least one of 'tools' or 'subsections'")

    for i, tool in enumerate(section.get("tools", [])):
        tool_loc = f"{loc} > tool[{i}] ({tool.get('name', '?')})"
        errors.extend(validate_tool(tool, tool_loc))

    for i, sub in enumerate(section.get("subsections", [])):
        sub_loc = f"{loc} > subsection[{i}] ({sub.get('title', '?')})"
        errors.extend(validate_subsection(sub, sub_loc))

    return errors


def main():
    try:
        with open("data/tools.yml") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: data/tools.yml not found. Run from the repo root.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"ERROR: data/tools.yml is not valid YAML:\n{e}")
        sys.exit(1)

    if not isinstance(data, list):
        print("ERROR: data/tools.yml must be a list of sections at the top level")
        sys.exit(1)

    errors = []
    for i, section in enumerate(data):
        errors.extend(validate_section(section, i))

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print(f"\n{len(errors)} error(s) found in data/tools.yml")
        sys.exit(1)

    tool_count = sum(
        len(s.get("tools", [])) +
        sum(len(sub.get("tools", [])) for sub in s.get("subsections", []))
        for s in data
    )
    print(f"OK: {len(data)} sections, {tool_count} tools validated successfully")


if __name__ == "__main__":
    main()
