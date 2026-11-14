#!/bin/bash
# Stop: don't let Claude finish with failing lint/doctests on .py files changed vs master.
input=$(cat)
# Already blocked once this turn: let the stop through rather than loop forever.
[[ $(jq -r '.stop_hook_active' <<<"$input") == true ]] && exit 0
cd "$CLAUDE_PROJECT_DIR" || exit 0
base=$(git merge-base master HEAD 2>/dev/null) || exit 0

# mcp_server is excluded: algo_server.py imports mcp, which python3.15t lacks.
mapfile -t files < <({
    git diff --name-only --diff-filter=d "$base" -- '*.py' ':!mcp_server'
    git ls-files --others --exclude-standard -- '*.py' ':!mcp_server'
} | sort -u)

out=$("$CLAUDE_PROJECT_DIR"/.claude/hooks/verify.sh "${files[@]}" 2>&1) || { echo "$out" >&2; exit 2; }
exit 0
