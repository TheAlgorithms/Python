#!/bin/bash
# Shared checker used by the Stop and commit gates.
# Usage: verify.sh <repo-relative .py files...>   exit 0 = all checks pass
#
# Runs inside the algodev-mcp image (no network, repo mounted read-only), with the
# same flags as .mcp.json. Build the image with mcp_server/check_server.sh.
cd "$CLAUDE_PROJECT_DIR" || exit 1
(( $# )) || exit 0

run() {
    docker run --rm --network none --user "$(id -u):$(id -g)" \
        -v "$CLAUDE_PROJECT_DIR:/repo:ro" --entrypoint "$1" algodev-mcp "${@:2}"
}

fail=0
# CONTRIBUTING.md line 119: ruff check must pass. Line 112: ruff format encouraged.
run ruff check --no-cache "$@" || fail=1
run ruff format --check --no-cache "$@" || fail=1
# Lines 151, 167-171: doctests must be found and pass, on free-threaded 3.15t (line 103).
for f in "$@"; do
    run python3.15t -m doctest "$f" 2>&1 | tail -30
    (( PIPESTATUS[0] == 0 )) || fail=1
done
# Line 211: snake_case filenames (same script as the validate-filenames pre-commit hook).
python3 scripts/validate_filenames.py || fail=1
# Full pre-commit suite from .pre-commit-config.yaml, on a scratch copy inside the
# container (uv-lock skipped: it needs the network).
run precommit-check "$@" || fail=1
exit $fail
