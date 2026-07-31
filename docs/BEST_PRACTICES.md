# BEST_PRACTICES.md

## Best Practices for Using LibreOffice Adapter

- Use the headless mode (`--headless`) for batch conversions to avoid GUI overhead.
- When working with UNO, ensure the acceptor is started on a free port and closed after use.
- Prefer explicit output directories via `--outdir` to keep results organized.
- Handle errors by catching `RuntimeError` from the adapter and logging the `stderr`.
- For large document sets, process them in chunks to avoid memory pressure.
