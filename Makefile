PYTHON ?= python3

.PHONY: validate generate

validate:
	$(PYTHON) scripts/validate_tools.py

generate: validate
	$(PYTHON) scripts/export_marketing_yaml.py
	$(PYTHON) scripts/generate_readme.py
