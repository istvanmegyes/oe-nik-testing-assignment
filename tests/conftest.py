# tests/conftest.py
import os
import sys

# Add project root (one level up from tests/) to PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
