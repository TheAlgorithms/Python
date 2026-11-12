# Agent Instructions for TheAlgorithms/Python

## Objective

Fix the bug in `other/password.py` (Issue #15633).

## Rules (Based on CONTRIBUTING.md and AGENTS.md)

1. **Code Style:** Use Python 3.15+, descriptive variable names, and type hints.
2. **Doctests:** Every modified function must have doctests.
3. **Exceptions:** Raise `ValueError` for invalid inputs.
4. **PR Requirements:** You must check at least one box in the PR template.
5. **Scope:** Only change one algorithm file. Do not update README.md or DIRECTORY.md.

## Task Instructions

1. Fork the repository and create a new branch.
2. Edit `other/password.py` to add a `ValueError` guard in `alternative_password_generator`.
3. Run `python -m doctest -v other/password.py` to ensure tests pass.
4. Submit a PR with the description "Fixes #15633".
