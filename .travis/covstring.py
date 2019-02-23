"""This utility script gathers the top level packages for wich coverage should
be measured.
"""
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def gather_packages(cwd=PROJECT_ROOT):
    """Return a list of all directories in cwd containing an ``__init__.py`` file."""
    dirpaths = (path for path in os.listdir(PROJECT_ROOT) if os.path.isdir(path))
    package_names = [
        os.path.basename(path) for path in dirpaths if "__init__.py" in os.listdir(path)
    ]
    return package_names

def generate_coverage_py_string(cwd=PROJECT_ROOT):
    """Generate a string on the form ``--cov PACKAGE_1 --cov PACKAGE_2 ...`` such
    that all packages found in cwd are traced using pytest-cov.
    """
    packages = gather_packages(cwd)
    assert packages
    
    return "--cov " + " --cov ".join(packages)

def main():
    cov_string = generate_coverage_py_string()
    print(cov_string)

if __name__ == "__main__":
    main()
