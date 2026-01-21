import os
import sys

# Ensure project root (the parent of `machine_learning`) is on sys.path so
# tests can import `machine_learning` when pytest runs tests from inside
# subdirectories.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
