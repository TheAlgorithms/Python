#!/bin/bash
#
# Fork TheAlgorithms/Python (if needed), push the current work to a branch on
# the fork, and open a pull request against the FORK's default branch.
#
# The pull request never targets the upstream repository: `gh pr create`
# defaults to the parent repo for forks, so --repo is always set to the fork.
#
# Usage:
#   scripts/fork_pr.sh <branch> "<pr title>" [<fork issue number>]
#
# Examples:
#   scripts/fork_pr.sh devcontainer-ci "Add devcontainer CI workflow" 1
#   DRY_RUN=1 scripts/fork_pr.sh my-branch "My change"
#
# Environment variables:
#   UPSTREAM   Repository to fork (default: TheAlgorithms/Python).
#   DRY_RUN=1  Print the commands instead of running them.

set -euo pipefail

if [[ $# -lt 2 ]]; then
  sed -n '2,18p' "$0"
  exit 1
fi

branch="$1"
title="$2"
issue="${3:-}"
upstream="${UPSTREAM:-TheAlgorithms/Python}"

run() {
  if [[ -n "${DRY_RUN:-}" ]]; then
    echo "+ $*"
  else
    "$@"
  fi
}

user="$(gh api user --jq .login)"
fork="${user}/${upstream#*/}"

# 1. Fork once; `gh repo fork` is a no-op if the fork already exists.
if ! gh repo view "$fork" >/dev/null 2>&1; then
  run gh repo fork "$upstream" --clone=false
fi

# 2. Make sure an `origin`-independent remote points at the fork.
if ! git remote get-url fork >/dev/null 2>&1; then
  run git remote add fork "https://github.com/${fork}.git"
fi

# 3. Push the branch to the fork.
if ! git rev-parse --verify --quiet "$branch" >/dev/null; then
  run git checkout -b "$branch"
fi
run git push -u fork "$branch"

# 4. Open the PR against the fork's default branch, never upstream.
base="$(gh repo view "$fork" --json defaultBranchRef --jq .defaultBranchRef.name)"
body="$(cat .github/pull_request_template.md)"
if [[ -n "$issue" ]]; then
  body="Fixes #${issue}"$'\n\n'"${body}"
fi
run gh pr create --repo "$fork" --base "$base" --head "$branch" \
  --title "$title" --body "$body"
