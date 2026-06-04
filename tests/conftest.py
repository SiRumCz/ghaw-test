"""Shared pytest configuration for the calculator test suite.

Adds the ``src`` directory to ``sys.path`` so each per-function test module
can simply ``from calculator import <function>``.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
