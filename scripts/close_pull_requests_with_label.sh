#!/bin/bash
#
# Close every open pull request that carries a given label, leaving an
# explanatory comment. This is used to clear the backlog before Hacktoberfest.
#
# Usage:
#   scripts/close_pull_requests_with_label.sh "<label>" ["<comment>"]
#
# Examples:
#   scripts/close_pull_requests_with_label.sh "require type hints"
#   DRY_RUN=1 scripts/close_pull_requests_with_label.sh "tests are failing"
#
# Environment variables:
#   DRY_RUN=1   Print the PRs that would be closed without closing them.
#   REPO        Target repository (default: TheAlgorithms/Python).
#   SLEEP       Seconds to wait between closes (default: 2) to avoid tripping
#               GitHub's secondary rate limits during bulk closes.
#
# On completion the script prints a machine-readable summary line:
#   CLOSED_COUNT=<n> CLOSED_PRS=<comma-separated PR numbers>
# so the Hacktoberfest tracker can be updated from the output.

set -euo pipefail

label="${1:-}"
if [[ -z "$label" ]]; then
  echo "error: missing label argument" >&2
  echo "usage: $0 \"<label>\" [\"<comment>\"]" >&2
  exit 2
fi

repo="${REPO:-TheAlgorithms/Python}"
sleep_seconds="${SLEEP:-2}"
comment="${2:-Closing \"${label}\" PRs to prepare for Hacktoberfest}"

# Filter by label server-side so we never miss PRs beyond an arbitrary --limit
# cap (the repo can have ~900 open PRs). --limit is set high purely as a ceiling.
prs=$(gh pr list --repo "$repo" --state open --label "$label" \
  --json number,title --limit 1000)

count=$(echo "$prs" | jq 'length')
echo "Found $count open PR(s) with label \"$label\" in $repo"

closed=()
while read -r pr; do
  [[ -z "$pr" ]] && continue
  pr_number=$(echo "$pr" | jq -r '.number')
  pr_title=$(echo "$pr" | jq -r '.title')

  if [[ "${DRY_RUN:-0}" == "1" ]]; then
    echo "[dry-run] would close PR #$pr_number: $pr_title"
    closed+=("$pr_number")
    continue
  fi

  echo "Closing PR #$pr_number: $pr_title"
  gh pr close "$pr_number" --repo "$repo" --comment "$comment"
  closed+=("$pr_number")
  sleep "$sleep_seconds"
done < <(echo "$prs" | jq -c '.[]')

# Machine-readable summary for the tracker.
IFS=,; echo "CLOSED_COUNT=${#closed[@]} CLOSED_PRS=${closed[*]:-}"
