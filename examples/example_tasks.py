# example_tasks.py
"""Simple demonstration of the LibreOfficeAdapter.
Runs a few basic operations:
1. Opens a sample document (if provided).
2. Creates an empty Writer document.
3. Converts the Writer document to PDF.
"""

import sys
from pathlib import Path
from adapter.libreoffice_adapter import LibreOfficeAdapter


def run_example(sample_path: str = None):
    adapter = LibreOfficeAdapter()
    # 1. Open a sample document if given
    if sample_path:
        print(f"Opening sample document: {sample_path}")
        adapter.open_document(Path(sample_path))
    # 2. Create a new Writer document (headless creates a blank file)
    print("Creating a new Writer document...")
    result = adapter.create_writer()
    # LibreOffice creates a temporary .odt in the current directory; we locate it.
    # For demonstration, we just list files after creation.
    print("Current directory contents after creating Writer:")
    for p in Path('.').glob('*.odt'):
        print(p)
        writer_file = p
        break
    else:
        print("No .odt file created; skipping PDF export.")
        return
    # 3. Export to PDF
    pdf_dir = Path('output')
    pdf_dir.mkdir(exist_ok=True)
    print(f"Exporting {writer_file} to PDF in {pdf_dir}...")
    adapter.export_pdf(writer_file, outdir=pdf_dir)
    print("Done. Check the output directory for the PDF file.")


if __name__ == "__main__":
    sample = sys.argv[1] if len(sys.argv) > 1 else None
    run_example(sample)
