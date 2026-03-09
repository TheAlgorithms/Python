#!/bin/bash

# List all open pull requests
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Loop through each pull request
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_number=$(echo "$pr" | jq -r '.number')
  pr_title=$(echo "$pr" | jq -r '.title')
  pr_labels=$(echo "$pr" | jq -r '.labels')

  # Check if the "awaiting changes" label is present
  awaiting_changes=$(echo "$pr_labels" | jq -r '.[] | select(.name == "awaiting changes")')
  echo "Checking PR #$pr_number $pr_title ($awaiting_changes) ($pr_labels)"

  # If awaiting_changes, close the pull request
  if [[ -n "$awaiting_changes" ]]; then
    echo "Closing PR #$pr_number $pr_title due to awaiting_changes label"
    gh pr close "$pr_number" --comment "Closing awaiting_changes PRs to prepare for Hacktoberfest"
    sleep 2
  fi
done
