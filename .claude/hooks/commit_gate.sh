#!/bin/bash
# PreToolUse(Bash): verify staged .py files before any git commit; no bypassing.
# Runs before the command, so stage and commit in separate calls.
cmd=$(jq -r '.tool_input.command // empty')
[[ "$cmd" =~ git[[:space:]]+commit ]] || exit 0
cd "$CLAUDE_PROJECT_DIR" || exit 0

if [[ "$cmd" =~ --no-verify ]]; then
    echo "No --no-verify commits." >&2
    exit 2
fi

mapfile -t files < <(git diff --cached --name-only --diff-filter=d -- '*.py' ':!mcp_server')
out=$("$CLAUDE_PROJECT_DIR"/.claude/hooks/verify.sh "${files[@]}" 2>&1) || { echo "$out" >&2; exit 2; }
exit 0
