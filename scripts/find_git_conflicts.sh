#!/bin/bash
#
# Find every open pull request that has git merge conflicts with the base
# branch and label it "git merge conflict".
#
# Why this is not a one-liner: GitHub computes PR mergeability *asynchronously*,
# so `gh pr list --json mergeable` frequently reports UNKNOWN for PRs it has not
# recomputed yet. Viewing a PR individually nudges GitHub to compute the value,
# so we re-query only the UNKNOWN PRs a few times before giving up. We also
# avoid `--limit 500`, which silently skips any PR past the 500th (this repo has
# well over 500 open PRs).
#
# Usage:
#   scripts/find_git_conflicts.sh            # label conflicting PRs
#   DRY_RUN=1 scripts/find_git_conflicts.sh  # list only, add no labels
#
# Environment overrides: REPO, LABEL, SLEEP (seconds between UNKNOWN retries).

set -euo pipefail

REPO="${REPO:-TheAlgorithms/Python}"
LABEL="${LABEL:-git merge conflict}"
DRY_RUN="${DRY_RUN:-0}"
SLEEP="${SLEEP:-2}"

echo "Checking for pull requests with conflicts in $REPO..."

# Make sure the label exists (idempotent; ignore "already exists").
if [[ "$DRY_RUN" != "1" ]]; then
    gh label create "$LABEL" --repo "$REPO" \
        --color "d93f0b" \
        --description "This pull request has git merge conflicts with the base branch" \
        2>/dev/null || true
fi

# First pass: one bulk call. Fast, but mergeable is often UNKNOWN.
mapfile -t rows < <(
    gh pr list --repo "$REPO" --state open --limit 5000 \
        --json number,mergeable --jq '.[] | "\(.number)\t\(.mergeable)"'
)
echo "Found ${#rows[@]} open pull requests to inspect."

conflicting=()
unknown=()
for row in "${rows[@]}"; do
    number="${row%%$'\t'*}"
    mergeable="${row##*$'\t'}"
    case "$mergeable" in
        CONFLICTING) conflicting+=("$number") ;;
        UNKNOWN) unknown+=("$number") ;;
    esac
done

# Second pass: re-query only the UNKNOWN PRs until GitHub finishes computing.
for pr in "${unknown[@]}"; do
    mergeable="UNKNOWN"
    for _ in 1 2 3; do
        mergeable=$(gh pr view "$pr" --repo "$REPO" --json mergeable --jq '.mergeable')
        [[ "$mergeable" != "UNKNOWN" ]] && break
        sleep "$SLEEP"
    done
    [[ "$mergeable" == "CONFLICTING" ]] && conflicting+=("$pr")
done

# Label the conflicting PRs.
for pr in "${conflicting[@]}"; do
    echo "PR #$pr has conflicts."
    if [[ "$DRY_RUN" != "1" ]]; then
        gh pr edit "$pr" --repo "$REPO" --add-label "$LABEL"
    fi
done

# Machine-readable summary (mirrors the close_pull_requests_with_*.sh scripts).
printf 'CONFLICTING_COUNT=%d CONFLICTING_PRS=%s\n' \
    "${#conflicting[@]}" "$(IFS=,; echo "${conflicting[*]}")"
