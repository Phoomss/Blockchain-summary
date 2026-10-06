"""Compatibility entry point: build both versions from the main repository."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent.parent / 'build.py'), run_name='__main__')
