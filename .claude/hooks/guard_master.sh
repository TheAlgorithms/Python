#!/bin/bash
# PreToolUse(Bash): keep issue work on a topic branch, never on master.
cmd=$(jq -r '.tool_input.command // empty')
branch=$(git -C "$CLAUDE_PROJECT_DIR" branch --show-current)
if [[ "$branch" == master && "$cmd" =~ git[[:space:]]+(commit|push) ]]; then
    echo "On master: create a topic branch (ljg/issue-<number>) first." >&2
    exit 2
fi
exit 0
