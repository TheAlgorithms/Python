#! /bin/bash
#
# Script for running the test suite with branch coverage.

# Coverage.py caches interfere with subsequent runs for some reason
rm -f .coverage*

python -m pytest tests/ $(python .travis/covstring.py) --cov-branch
