#!/bin/bash

# List all open pull requests
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Loop through each pull request
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_number=$(echo "$pr" | jq -r '.number')
  pr_title=$(echo "$pr" | jq -r '.title')
  pr_labels=$(echo "$pr" | jq -r '.labels')

  # Check if the "require descriptive names" label is present
  require_descriptive_names=$(echo "$pr_labels" | jq -r '.[] | select(.name == "require descriptive names")')
  echo "Checking PR #$pr_number $pr_title ($require_descriptive_names) ($pr_labels)"

  # If there are require_descriptive_names, close the pull request
  if [[ -n "$require_descriptive_names" ]]; then
    echo "Closing PR #$pr_number $pr_title due to require_descriptive_names label"
    gh pr close "$pr_number" --comment "Closing require_descriptive_names PRs to prepare for Hacktoberfest"
  fi
done
