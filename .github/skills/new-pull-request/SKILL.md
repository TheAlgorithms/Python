# Skill: New pull request for TheAlgorithms/Python

Create a new pull request using the rules already written in
[`CONTRIBUTING.md`](../../../CONTRIBUTING.md). The goal is that creating a new
pull request (human or AI) can run the same way every time, and that produces a
clear, kind, tested, type-hinted, mergeable contribution.

## How to run this skill

Make sure that the local `master` branch is synced with `upstream/master` before
creating a new pull request.

Create a new clearly named branch for the pull request. Pull request changes must
not be made or submitted on the `master` branch.

Never hand-edit or revert the `uv.lock` file. If you add a legitimate
dependency, let the `uv-lock` pre-commit hook regenerate it — do not touch it by
hand. A hand-modified `uv.lock` makes the `algorithms-keeper` bot close the pull
request as invalid, and even a repo maintainer cannot undo that.

Always check at least one Markdown checkbox in the pull request description (the "Describe your change" section), or the
`algorithms-keeper` bot will close the pull request as invalid — and it does
this *before* a human reads the PR, so a genuinely good change gets closed for a
formatting reason. This applies to **every** pull request, including CI, docs,
and tooling changes that are not algorithms: tick the boxes that genuinely apply
so the body is never submitted with all boxes empty. Any repo maintainer can
undo this if you @mention them on the closed pull request, but re-opening is
often unreliable, so it is far better to get it right the first time.

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
- [ ] For a simple class that is mostly a bundle of fields, **consider**
      `from typing import NamedTuple` or `from dataclasses import dataclass`
      instead of a hand-written `__init__`/`__repr__`/`__eq__`. These are
      underutilized tools that make simple classes shorter and clearer — use
      them where they genuinely simplify the code, not everywhere.
- [ ] Code is formatted and lint-clean (`ruff`, `pre-commit`).
- [ ] `DIRECTORY.md` and `README.md` are **not hand-edited** — the
      `algorithms-keeper` bot regenerates them automatically after merge.

### 3. Other Requirements for Submissions

- [ ] At least one **Wikipedia (or equivalent) URL** documenting the algorithm.
- [ ] Docstring explains what the function does and its parameters/returns.
- [ ] No unnecessary third-party dependencies.

## Before you click "Create pull request"

This is the final gate. Do not open the pull request until every item here is true:

- [ ] At least one Markdown checkbox in the PR description is checked. **Verify
      this by re-reading the rendered body** — if every box is still `- [ ]`, the
      `algorithms-keeper` bot will auto-close the PR before any human sees it.
      Check the boxes that genuinely apply to this change; never submit an
      all-empty checklist, even for a CI, docs, or tooling PR.
- [ ] The branch is not `master`, and `master` is synced with `upstream/master`.
- [ ] `uv.lock` was not hand-edited.
