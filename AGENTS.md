# AGENTS.md

Guidance for AI coding agents (and their humans) contributing to
**TheAlgorithms/Python**. This complements — and never overrides —
[`CONTRIBUTING.md`](CONTRIBUTING.md). Read that first.

This repository is educational: implementations should be clear and correct
rather than maximally optimized. Every change goes through CI and the
`algorithms-keeper` bot, both of which reject non-conforming PRs automatically.

## Before opening a pull request

- **Check at least one box in the PR description.** The `algorithms-keeper`
  bot **closes any PR whose "Describe your change" section has no checked
  box** (`* [x]`). Fill in the template that ships in
  `.github/pull_request_template.md` and tick every item that applies before
  you submit — this is the single most common reason automated PRs get closed.
- **One algorithm file per PR.** Split unrelated changes into separate PRs to
  keep review focused.
- **Don't change code and its doctests in the same PR.** If you're only
  updating tests, say so and touch nothing else.

## Code conventions (enforced by CI)

- **Formatting & linting:** `ruff` (`uvx ruff check .` and `uvx ruff format .`).
  Run `uvx pre-commit run --all-files` locally to catch everything CI will.
- **Type hints:** annotate every function parameter and return value with
  [type hints](https://docs.python.org/3/library/typing.html).
- **Doctests:** every function needs at least one
  [doctest](https://docs.python.org/3/library/doctest.html) that passes under
  `python -m doctest -v your_file.py` (and `pytest`).
- **Naming:** filenames are all-lowercase with underscores (no spaces or
  dashes); functions and variables follow standard Python naming.
- **Placement:** new files go inside an existing directory.
- **References:** new algorithms include a URL to Wikipedia or a comparable
  explanation.

## Running the suite locally

This project is managed with [`uv`](https://docs.astral.sh/uv/) — there is no
`requirements.txt`. Dependencies live in `pyproject.toml`/`uv.lock`, and `uvx`
runs a tool in a throwaway environment without polluting yours:

```bash
uvx pre-commit run --all-files                       # ruff, formatting, hooks
uvx pytest your_module/your_file.py --doctest-modules
```

(`uv run pytest ...` works too if you'd rather use the project's locked
environment.)

Some directories are intentionally skipped in CI (`--ignore` entries in
`.github/workflows/build.yml`), usually because a heavy dependency lacks a
wheel for the CPython version the repo currently targets. Check that list
before assuming a file is untested.

## Good agent behavior

- Keep diffs minimal and scoped to the stated change.
- Preserve existing style and structure; prefer clarity over cleverness.
- Never fabricate doctest output — run it and paste the real result.
- If CI is red, read the log and fix the cause rather than re-running blindly.
