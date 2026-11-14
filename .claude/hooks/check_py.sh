#!/bin/bash
# PostToolUse(Edit|Write): ruff + doctests on the edited .py file, inside algodev-mcp.
# Exit 2 sends stderr back to Claude so the failure has to be fixed.
file=$(jq -r '.tool_input.file_path // empty')
[[ "$file" == "$CLAUDE_PROJECT_DIR"/*.py ]] || exit 0
rel=${file#"$CLAUDE_PROJECT_DIR"/}
# algo_server.py imports mcp, which python3.15t in the image does not have.
[[ "$rel" == mcp_server/* ]] && exit 0

run() {
    docker run --rm --network none --user "$(id -u):$(id -g)" \
        -v "$CLAUDE_PROJECT_DIR:/repo:ro" --entrypoint "$1" algodev-mcp "${@:2}"
}

out=$(run ruff check --no-cache "$rel" 2>&1) || { echo "$out" >&2; exit 2; }
out=$(run python3.15t -m doctest "$rel" 2>&1) || { echo "$out" | tail -40 >&2; exit 2; }
exit 0
