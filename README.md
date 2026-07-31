# LibreOffice Agent Adapter

## What is this?
A standalone **LibreOffice Agent Adapter** that enables AI agents to interact with LibreOffice applications. It was originally developed and refined during **Field Trial 001** using the ST Builder framework.

## Who is it for?
- Developers building AI‑driven automation for LibreOffice.
- Researchers needing a programmable interface to LibreOffice documents.
- Anyone interested in extending the capabilities of AI agents with office suite automation.

## Features
- Provides a rich set of capabilities described in `capabilities.yaml`.
- Includes ready‑to‑use CLI help and a man‑page excerpt.
- Comes with example tasks, test results, and documentation.
- Fully documented with agent description, field notes, best practices and known limitations.

## Installation
```bash
pip install -r requirements.txt
```

## Package installation
```bash
pip install .
```

## Usage
```bash
cat docs/cli_help.txt
python examples/example_tasks.py
```

## Project Structure
```
/libreoffice-agent-adapter
├── README.md               # (this file)
├── LICENSE                 # License file (MIT placeholder)
├── CHANGELOG.md            # Change history
├── CONTRIBUTING.md         # Contribution guidelines
├── .gitignore              # Ignored files
├── PROJECT_HISTORY.md      # Origin and provenance
├── ARCHITECTURE.md         # (optional) Architecture overview
├── ROADMAP.md              # (optional) Future plans
├── adapter/                # Adapter definition files
│   ├── adapter.yaml
│   ├── capabilities.yaml
│   └── metadata.json
├── docs/                   # Documentation
│   ├── AGENT.md
│   ├── FIELD_NOTES.md
│   ├── EXPERIENCE.md
│   ├── BEST_PRACTICES.md
│   ├── KNOWN_LIMITATIONS.md
│   ├── implementation_plan.md
│   ├── cli_help.txt
│   └── man_page_excerpt.txt
├── examples/               # Example scripts and usage
│   └── example_tasks.py
├── tests/                  # Test artifacts
│   └── test_results.json
├── scripts/                # Helper scripts (currently empty)
└── assets/                 # Sample files (sample.*)
```

## Example
```python
from examples.example_tasks import run_example
run_example()
```

## Status
- **Initial release** – ready for local development and testing.
- No remote repository configured yet; this is a local setup.

---
*For more details, see the documentation in the `docs/` folder.*
