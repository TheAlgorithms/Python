"""Run doctests for all .py files under data_structures and summarize results.

Usage: python scripts/run_doctests.py

The script will try to import each file as a package module (e.g. data_structures.x.y)
so relative imports work. If import fails, it will fall back to running doctest.testfile
on the file path.

Exits with non-zero status when any failures or uncaught exceptions occur.
"""

from __future__ import annotations

import doctest
import importlib
import importlib.util
import os
import sys
import traceback
from pathlib import Path

ROOT = (
    Path(__file__).resolve().parents[1]
)  # Python/ (project root where data_structures lives)
DATA_DIR = ROOT / "data_structures"


def main() -> int:
    sys.path.insert(0, str(ROOT))

    results = []  # tuples: (relpath, status, details)
    total_tests = 0
    total_failures = 0

    for py in sorted(DATA_DIR.rglob("*.py")):
        rel = py.relative_to(ROOT)
        module_name = ".".join(rel.with_suffix("").parts)
        # skip compiled or vendored files if any
        print(f"\n=== Running doctests for {rel} (module {module_name}) ===")
        try:
            # Try to import as module first (so package-relative imports work)
            module = importlib.import_module(module_name)
            # run doctest on module
            res = doctest.testmod(module, verbose=False)
            failures, tests = res
            total_tests += tests
            total_failures += failures
            status = "ok" if failures == 0 else "fail"
            details = f"imported module; tests={tests}, failures={failures}"
            print(details)
            if failures:
                # rerun verbosely to show failing examples
                print("--- Verbose output for failures ---")
                doctest.testmod(module, verbose=True)
            results.append((str(rel), status, details))
        except Exception as e:
            # Import failed; try doctest.testfile on the path
            print(f"Import failed: {e.__class__.__name__}: {e}")
            traceback.print_exc()
            try:
                failures, tests = doctest.testfile(str(py), module_relative=False)
                total_tests += tests
                total_failures += failures
                status = "ok" if failures == 0 else "fail"
                details = f"testfile fallback; tests={tests}, failures={failures}"
                print(details)
                if failures:
                    print("--- Verbose output for failures ---")
                    doctest.testfile(str(py), module_relative=False, verbose=True)
                results.append((str(rel), status, details))
            except Exception as ex2:
                print(f"Fallback testfile raised {ex2.__class__.__name__}: {ex2}")
                traceback.print_exc()
                results.append(
                    (str(rel), "error", f"import error: {e}; fallback error: {ex2}")
                )

    # Summary
    print("\n=== Summary ===")
    print(f"Files checked: {len(results)}")
    print(f"Total doctest examples run: {total_tests}")
    print(f"Total failures: {total_failures}")
    print("")
    for f, status, details in results:
        if status != "ok":
            print(f"{f}: {status} - {details}")

    if total_failures > 0:
        print("\nSome doctests failed.")
        return 1

    # If any file had 'error' status, exit non-zero
    if any(r[1] == "error" for r in results):
        print("\nSome files raised errors while running doctests.")
        return 2

    print("\nAll doctests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
