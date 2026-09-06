# Skill: New pull request for TheAlgorithms/Python

Create a new pull request using the rules already written in
[`CONTRIBUTING.md`](../../../CONTRIBUTING.md). The goal is that creating a new
pull request (human or AI) can run the same way every time, and that produces a
clear, kind, tested, type-hinted, mergeable contribution.

## How to run this skill

Make sure that the local `master` branch is synced with `upstream/master` before
creating a new pull request.

Create a new clearly named branch for the pull request.  Pull request changes must
not be made or submitted on the `master` branch.

Never modify the `uv.lock` file because the `algorithms-keeper` bot will close
the pull request as invalid.  Even a repo maintainer cannot undo this.

Always have one checked Markdown checkbox in the pull request commit body, or the
`algorithms-keeper` bot will close the pull request as invalid.  Any repo
maintainer can undo this if you @mention them on the closed pull request.

### 1. Before contributing / Is this an algorithm?

- [ ] The change adds, fixes, or documents **one algorithm** — not multiple, and
      not both code and doctest changes in the same PR.
- [ ] It is a genuine algorithm or data structure (see the *What is an Algorithm?*
      section), not a script, snippet, how-to-use for an existing API, or exercise
      dump.
- [ ] It is **not already in the repository** (search the existing directories).
- [ ] **No earlier open PR** already does the same thing — link it if one exists.
- [ ] Properly attributed — no plagiarism; prior sources credited.

### 2. Coding Style

- [ ] `from __future__ import annotations` is not needed because this repo only uses
      the latest version of CPython.
- [ ] File and directory names are lowercase, use underscores, and land inside an
      existing directory.
- [ ] Public functions/classes have **type hints**.
- [ ] Public functions have **doctests that actually pass**.
- [ ] Descriptive variable and function names (no single letters where a word helps).
- [ ] Code is formatted and lint-clean (`ruff`, `pre-commit`).

### 3. Other Requirements for Submissions

- [ ] At least one **Wikipedia (or equivalent) URL** documenting the algorithm.
- [ ] Docstring explains what the function does and its parameters/returns.
- [ ] No unnecessary third-party dependencies.
