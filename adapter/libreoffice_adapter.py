# adapter/libreoffice_adapter.py
"""Minimal LibreOffice Adapter implementation.
Provides a thin wrapper around the LibreOffice CLI (`libreoffice` command).
The class offers a subset of capabilities listed in `capabilities.yaml`.
Unimplemented capabilities are marked as planned in the YAML file.
"""

import subprocess
import shlex
from pathlib import Path
from typing import List, Optional

class LibreOfficeAdapter:
    """A simple adapter to interact with LibreOffice via command‑line.

    It assumes the `libreoffice` binary is available in PATH.
    Methods raise `RuntimeError` if the subprocess exits with a non‑zero status.
    """

    def __init__(self, executable: str = "libreoffice"):
        self.executable = executable

    def _run(self, args: List[str]) -> subprocess.CompletedProcess:
        """Execute the LibreOffice command with given arguments.
        Returns the CompletedProcess instance. Raises RuntimeError on failure.
        """
        cmd = [self.executable] + args
        # Use subprocess.run for simplicity; capture stdout/stderr for debugging.
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(
                f"LibreOffice command failed: {' '.join(shlex.quote(a) for a in cmd)}\n"
                f"Return code: {result.returncode}\n"
                f"Stdout: {result.stdout}\n"
                f"Stderr: {result.stderr}"
            )
        return result

    # ---------- Implemented capabilities ----------
    def open_document(self, *files: Path) -> subprocess.CompletedProcess:
        """Open one or more documents for editing (default GUI mode)."""
        args = [str(f) for f in files]
        return self._run(args)

    def create_writer(self) -> subprocess.CompletedProcess:
        """Create a new empty Writer document."""
        return self._run(["--writer"])

    def create_calc(self) -> subprocess.CompletedProcess:
        """Create a new empty Calc spreadsheet."""
        return self._run(["--calc"])

    def export_pdf(self, *files: Path, outdir: Optional[Path] = None) -> subprocess.CompletedProcess:
        """Convert given document(s) to PDF using headless mode.
        If `outdir` is provided, the `--outdir` flag is added.
        """
        args = ["--headless", "--convert-to", "pdf"] + [str(f) for f in files]
        if outdir:
            args.extend(["--outdir", str(outdir)])
        return self._run(args)

    def execute_cli(self, cli: str) -> subprocess.CompletedProcess:
        """Execute an arbitrary LibreOffice CLI command.
        `cli` should be a string of arguments, e.g. "--version".
        """
        args = shlex.split(cli)
        return self._run(args)

    # ---------- Placeholder for future capabilities ----------
    # The remaining capabilities listed in capabilities.yaml are not yet implemented.
    # They will be added in future releases and are currently marked as `planned`.

    # Example placeholder method signature:
    # def create_draw(self):
    #     raise NotImplementedError("Planned capability: create_draw")

    # def accept_uno(self, connect_string: str):
    #     raise NotImplementedError("Planned capability: accept_uno")

    # Add further methods as needed.
