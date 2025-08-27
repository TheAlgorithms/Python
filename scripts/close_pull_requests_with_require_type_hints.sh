#!/bin/bash

# List all open pull requests
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Loop through each pull request
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_number=$(echo "$pr" | jq -r '.number')
  pr_title=$(echo "$pr" | jq -r '.title')
  pr_labels=$(echo "$pr" | jq -r '.labels')

  # Check if the "require type hints" label is present
  require_type_hints=$(echo "$pr_labels" | jq -r '.[] | select(.name == "require type hints")')
  echo "Checking PR #$pr_number $pr_title ($require_type_hints) ($pr_labels)"

  # If require_type_hints, close the pull request
  if [[ -n "$require_type_hints" ]]; then
    echo "Closing PR #$pr_number $pr_title due to require_type_hints label"
    gh pr close "$pr_number" --comment "Closing require_type_hints PRs to prepare for Hacktoberfest"
  fi
done
