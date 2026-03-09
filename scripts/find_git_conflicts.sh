#!/bin/bash

# Replace with your repository (format: owner/repo)
REPO="TheAlgorithms/Python"

# Fetch open pull requests with conflicts into a variable
echo "Checking for pull requests with conflicts in $REPO..."

prs=$(gh pr list --repo "$REPO" --state open --json number,title,mergeable --jq '.[] | select(.mergeable == "CONFLICTING") | {number, title}' --limit 500)

# Process each conflicting PR
echo "$prs" | jq -c '.[]' | while read -r pr; do
    PR_NUMBER=$(echo "$pr" | jq -r '.number')
    PR_TITLE=$(echo "$pr" | jq -r '.title')
    echo "PR #$PR_NUMBER - $PR_TITLE has conflicts."
done
