"""This is a subpackage because the directory is on sys.path for _in_process.py

The subpackage should stay as empty as possible to avoid shadowing modules that
the backend might import.
"""
from os.path import dirname, abspath, join as pjoin
from contextlib import contextmanager

try:
    import importlib.resources as resources

    def _in_proc_script_path():
        return resources.path(__package__, '_in_process.py')
except ImportError:
    @contextmanager
    def _in_proc_script_path():
        yield pjoin(dirname(abspath(__file__)), '_in_process.py')
