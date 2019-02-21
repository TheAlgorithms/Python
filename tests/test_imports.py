import os
import re
import importlib
import pytest

import thealgorithms


def _split_path_rec(path):
    rest, tail = os.path.split(path)
    if rest == "":
        return [tail]
    return _split_path_rec(rest) + [tail]


def _gather_modules():
    """Gather all modules that should be imported, but exclude __init__
    modules.
    """
    testdir = os.path.dirname(__file__)
    root = os.path.dirname(testdir)
    algos_root = os.path.dirname(thealgorithms.__file__)
    modules = []

    for dirpath, dirnames, filenames in os.walk(algos_root):
        for filename in filenames:
            if not filename.endswith(".py") or filename.endswith("__init__.py"):
                continue
            reldirpath = os.path.relpath(dirpath, root)
            path_nodes = _split_path_rec(os.path.join(reldirpath, filename))
            module = ".".join(path_nodes)[:-3]
            modules.append(module)
    return modules


@pytest.mark.parametrize("module", _gather_modules())
@pytest.mark.timeout(1)
def test_import_module(module):
    """Test that all modules from project root can be imported"""
    mod = importlib.import_module(module)
    assert mod
