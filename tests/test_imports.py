import os
import re
import importlib
import pytest

def _split_path_rec(path):
    rest, tail = os.path.split(path)
    if rest == "":
        return [tail]
    return _split_path_rec(rest) + [tail]


def _gather_modules():
    """Gather all modules that should be imported, but exclude __init__
    modules and anything in the tests directory.
    
    Note that all top-level directories, except those listed in
    ``exclude_dirs``, will be searched. This means that, for example,
    virtual environments in the project directory will be "teste".
    """
    testdir = os.path.abspath(os.path.dirname(__file__))
    root = os.path.dirname(testdir)
    modules = []
    exclude_dirs = [os.path.abspath(p) for p in (testdir, root)]

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if os.path.abspath(d) not in exclude_dirs]
        if dirpath == root: # skip root to avoid scripts
            continue
        for filename in filenames:
            if not filename.endswith(".py") or filename.endswith("__init__.py"):
                continue
            reldirpath = os.path.relpath(dirpath, root)
            path_nodes = _split_path_rec(os.path.join(reldirpath, filename))
            module = ".".join(path_nodes)[:-3]
            modules.append(module)
    return modules


@pytest.mark.parametrize("module", _gather_modules())
@pytest.mark.timeout(2)
def test_import_module(module):
    """Test that all modules from project root can be imported"""
    mod = importlib.import_module(module)
    assert mod

if __name__ == "__main__":
    print(_gather_modules())
