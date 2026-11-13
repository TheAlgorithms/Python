# Fork of TheAlgorithms/Python (CS440 Lab 6)

Follow the repository's own rules: @CONTRIBUTING.md and @AGENTS.md

## Fork rules

- Pull requests target this fork (`origin`), never TheAlgorithms/Python.
  Do not comment on, claim, or open anything in the upstream repository.
- `upstream` is read-only: fetch from it to sync, never push to it.
- Agent tooling lives on `master` only. Feature branches must contain just the
  one algorithm file being changed, so the PR diff stays one file.

## Workflow

- `/contribute <issue> <file>` runs the full flow (`.claude/commands/contribute.md`).
- `contributing-reviewer` checks a branch against the rules in its own context.
- `.claude/scripts/open_fork_pr.py` checks the rules a script can enforce, then
  pushes and opens the PR against the fork. Run it with `--dry-run` first.
