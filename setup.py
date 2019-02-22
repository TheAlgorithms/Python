"""This is a setup module for installing this project. To install the project,
set the current working directory to the project root, and run:

``pip install .``

Depending on your environment, you may need some modifiers. To install for the
current user only, run:

``pip install . --user``

``pip`` is sometimes aliased to the Python 3 version of pip, and sometimes to
the Python 2 version. If you want to be sure to use the one for Python 3, run:

``python3 -m pip install . --user``

If you also want to be able to develop and run the test suite, you need to install
with test dependencies (preferably in a virtual environment):

``pip install --editable .[TEST]``
"""
from setuptools import setup, find_packages

with open("README.md", mode="r") as file:
    README = file.read()

TEST_REQUIREMENTS = ["pytest>=4.0.0", "pytest-cov", "pytest-timeout"]
REQUIRED = ["numpy", "matplotlib", "sympy", "scikit-learn", "tensorflow"]

setup(
    name="TheAlgorithms",
    description="All algorithms implemented in Python (for education)",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=("tests", "docs")),
    tests_require=TEST_REQUIREMENTS,
    install_requires=REQUIRED,
    extras_require=dict(TEST=TEST_REQUIREMENTS),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
)
