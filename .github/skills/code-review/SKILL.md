# Skill: Code review for TheAlgorithms/Python

Review a pull request against the rules already written in
[`CONTRIBUTING.md`](../../../CONTRIBUTING.md). The goal is a review that any
reviewer (human or AI) can run the same way every time, and that produces a clear,
kind, actionable verdict.

## How to run this skill

Read the PR diff, then work through the four `CONTRIBUTING.md` sections in order
and emit the fixed output shape below. Cite the exact rule you are applying and
suggest the fix — never just "rejected".

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

### 4. Verdict — fixed output shape

Emit exactly these headings so reviews are comparable and easy to automate:

```
### Is this an algorithm? — <yes/no + one-line why>
### Duplicate / prior-art check — <#NNNN | none found>
### Coding style — <pass | issues: …>
### Other requirements (doctests, type hints, descriptive names, Wikipedia URL) — <pass | issues: …>
### Verdict — <approve | request changes | close> + one-line reason
```

## Tone

Be specific and kind. Point at the exact `CONTRIBUTING.md` rule and offer the fix
rather than a bare rejection — first-time and Hacktoberfest contributors are more
likely to come back and improve the PR when the path forward is clear.

## Map findings to labels

Where a finding matches an existing label, name it so the review lines up with the
maintenance/cleanup tooling:

- missing/failing doctests → `require tests`
- missing type hints → `require type hints`
- non-descriptive names → `require descriptive names`
- CI red → `tests are failing`
- otherwise ready for a maintainer → `awaiting reviews`
