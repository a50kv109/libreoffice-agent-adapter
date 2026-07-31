import subprocess
from unittest import mock
from pathlib import Path
import pytest

from adapter.libreoffice_adapter import LibreOfficeAdapter

# Helper to create a mock CompletedProcess
def mock_completed_process(stdout="", stderr="", returncode=0):
    cp = subprocess.CompletedProcess(args=[], returncode=returncode, stdout=stdout, stderr=stderr)
    return cp

@pytest.fixture(autouse=True)
def mock_subprocess_run():
    with mock.patch('subprocess.run') as m:
        m.return_value = mock_completed_process()
        yield m

def test_open_document(mock_subprocess_run):
    adapter = LibreOfficeAdapter()
    adapter.open_document(Path('file1.odt'), Path('file2.odt'))
    mock_subprocess_run.assert_called_once()
    args = mock_subprocess_run.call_args[0][0]
    assert args[0] == 'libreoffice'
    assert 'file1.odt' in args and 'file2.odt' in args

def test_create_writer(mock_subprocess_run):
    adapter = LibreOfficeAdapter()
    adapter.create_writer()
    mock_subprocess_run.assert_called_once()
    args = mock_subprocess_run.call_args[0][0]
    assert '--writer' in args

def test_create_calc(mock_subprocess_run):
    adapter = LibreOfficeAdapter()
    adapter.create_calc()
    mock_subprocess_run.assert_called_once()
    args = mock_subprocess_run.call_args[0][0]
    assert '--calc' in args

def test_export_pdf(mock_subprocess_run):
    adapter = LibreOfficeAdapter()
    adapter.export_pdf(Path('doc.odt'), outdir=Path('out'))
    mock_subprocess_run.assert_called_once()
    args = mock_subprocess_run.call_args[0][0]
    assert '--headless' in args
    assert '--convert-to' in args
    assert 'pdf' in args
    assert 'doc.odt' in args
    assert '--outdir' in args
    assert 'out' in args

def test_execute_cli(mock_subprocess_run):
    adapter = LibreOfficeAdapter()
    adapter.execute_cli('--version')
    mock_subprocess_run.assert_called_once()
    args = mock_subprocess_run.call_args[0][0]
    assert '--version' in args
