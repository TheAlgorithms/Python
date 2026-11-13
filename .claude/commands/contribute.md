---
description: Contribute a fix for a TheAlgorithms/Python issue to this fork, from sync to pull request
argument-hint: <issue-number> <file-path>
---

Contribute to issue #$1 by changing `$2`. Follow `CONTRIBUTING.md` and
`AGENTS.md` throughout. The pull request goes to this fork only.

1. **Guard the target.** Run `git remote get-url origin`. Stop if it points at
   TheAlgorithms. Make sure an `upstream` remote exists
   (`git remote add upstream https://github.com/TheAlgorithms/Python.git`).
2. **Sync the fork.** `git fetch upstream`, then fast-forward `master` to
   `upstream/master`.
3. **Check it is still needed.** Read issue #$1 and the current `$2` on
   master. If master already fixes it, stop and report that instead of
   duplicating work (CONTRIBUTING.md forbids identical implementations).
4. **Branch.** `git switch -c <short-descriptive-name>` from `master`.
5. **Change one file.** Edit `$2` only (plus `tests/` if the issue asks for
   tests). Keep the diff minimal and behaviour unchanged unless the issue is a
   bug fix. Never edit doctest output to make it pass.
6. **Verify.** Run `uvx ruff check`, `uvx ruff format --check`,
   `uv run --with pytest pytest -q --doctest-modules $2`, and `uvx ty check $2`.
   Fix the root cause of any failure.
7. **Commit.** Message: `<area>: <what changed>`, body explains why and ends
   with `Part of #$1` (tracking issue) or `Fixes #$1` (fully resolved).
8. **Review in isolation.** Ask the `contributing-reviewer` sub-agent to review
   the branch for issue #$1. If it says NOT READY, fix and repeat from step 6.
9. **Open the PR.** Save the reviewer's filled template to `.git/PR_BODY.md`
   (inside `.git`, so it is never committed), then run
   `python .claude/scripts/open_fork_pr.py --title "<commit subject>" --body-file .git/PR_BODY.md --dry-run`.
   Show the user the dry run, and run it again without `--dry-run` only after
   they approve.
