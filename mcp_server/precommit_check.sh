#!/bin/bash
# Usage: precommit-check <repo-relative files...>
#
# Runs inside the algodev-mcp image. Runs the repo's pre-commit hooks on a scratch
# copy of /repo (which is mounted read-only), then prints whatever the fixer hooks
# would have changed. The real repository is never modified.
(( $# )) || { echo "usage: precommit-check <files...>" >&2; exit 2; }
work=$(mktemp -d) || exit 1
cp -a /repo/. "$work" || exit 1
cd "$work" || exit 1
# pre-commit detects fixer edits with `git diff`, which ignores untracked files,
# so stage the files in the scratch copy.
git add -- "$@" || exit 1
# uv-lock resolves from PyPI; skipped offline, as on pre-commit.ci.
SKIP=uv-lock pre-commit run --color never --files "$@"
status=$?
if ! git diff --quiet -- "$@"; then
    echo "---- changes the hooks would make ----"
    git --no-pager diff -- "$@"
fi
exit $status
