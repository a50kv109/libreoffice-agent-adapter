# KNOWN_LIMITATIONS.md

## Known Limitations of the Current LibreOffice Adapter

- **Limited language bindings**: Only a thin Python wrapper is provided. Full UNO API coverage is not implemented.
- **No cross‑platform testing**: The adapter has been tested on Linux only; Windows/macOS behaviour may differ (especially regarding headless mode).
- **Partial capability coverage**: Only a subset of capabilities listed in `capabilities.yaml` are implemented (`open_document`, `create_writer`, `create_calc`, `export_pdf`, `execute_cli`). All others are marked as *planned*.
- **No error‑handler abstractions**: Errors from the LibreOffice CLI are raised as generic `RuntimeError` without custom exception hierarchy.
- **No unit tests**: The repository currently lacks automated tests for the adapter methods.
- **CLI help files are static**: `docs/cli_help.txt` is a placeholder and does not reflect the actual help output of the installed LibreOffice version.

These limitations are intentional for the first public experimental release. Future releases will address them incrementally.
