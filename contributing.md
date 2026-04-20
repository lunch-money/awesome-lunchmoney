We appreciate and recognize all the members of the Lunch Money community that have contributed projects.

If you've built something you'd like to share with the community, please feel free to add it following these guidelines.


# Contribution Guidelines

**To add, remove, or change an entry:** submit a pull request that edits [`data/tools.yml`](./data/tools.yml).

- Follow the [Pull Request template](./PR_TEMPLATE.md)
- Add the reason why the resource is worth including
- Do **not** edit the README catalog directly — it is generated from `data/tools.yml`

## Adding a tool

Open `data/tools.yml` and add a new entry under the appropriate section's `tools` list. The full set of available fields is documented at the top of that file. Required fields are `name` and `description`.

**Minimal entry:**
```yaml
- name: my-tool
  description: A short, clear description of what the tool does.
  author: Your Name
  github: https://github.com/you/my-tool
```

**All fields:**
```yaml
- name: my-tool
  description: A short, clear description of what the tool does.
  author: Your Name
  lang: python          # js, python, go, ruby, dart, kotlin, rust, ios, android, chrome, web, cli, pwa
  lang_label: Python    # optional override for the displayed tag label
  github: https://github.com/you/my-tool
  url: https://my-tool.example.com
  url_label: "Try it"   # defaults to "Website"
  discord: https://discord.com/channels/...
  links:
    - url: https://pypi.org/project/my-tool
      label: "PyPI"
```

## What gets generated automatically

When your PR merges to `main`, GitHub Actions runs two scripts:

- `scripts/generate_readme.py` — rewrites the catalog section of `README.md`
- `scripts/export_marketing_yaml.py` — writes `generated/developer_tools.yml` for the marketing site

You do not need to run these locally. The generated files are committed automatically.

## Optional: local validation

If you have Python 3 installed, you can validate your changes before committing:

```bash
python3 scripts/validate_tools.py
```

To get automatic validation on every commit, install the included git hook once:

```bash
git config core.hooksPath .githooks
```

If you don't have Python, the hook is skipped and GitHub Actions will validate your changes when you open a PR.

**To install dependencies for local script use:**
```bash
pip install -r requirements.txt
# or, with uv (no prior Python install required):
uv run --with pyyaml python3 scripts/validate_tools.py
```

## Quality standards

To be on the list, projects should:

- Function as documented
- Be generally useful to the wider Lunch Money community
- Be actively maintained (regular commits, or issues/PRs are responded to for finished projects)
- Be stable or progressing toward stable
- Be thoroughly documented (README, comments, samples)
- Include tests where practical

## Reporting issues

Please open an issue if you'd like to discuss anything that could be improved or have suggestions for making the list more valuable.

We realize sometimes projects fall into abandonment or have breaking builds for extended periods of time. If you see that, feel free to submit a PR or open an issue.

Removal changes not suggested by the project's author will not be applied until they have been pending for a minimum of 1 week (7 days).

Thanks everyone!
