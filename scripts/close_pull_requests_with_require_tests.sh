#!/bin/bash

# List all open pull requests
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Loop through each pull request
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_number=$(echo "$pr" | jq -r '.number')
  pr_title=$(echo "$pr" | jq -r '.title')
  pr_labels=$(echo "$pr" | jq -r '.labels')

  # Check if the "require_tests" label is present
  require_tests=$(echo "$pr_labels" | jq -r '.[] | select(.name == "require tests")')
  echo "Checking PR #$pr_number $pr_title ($require_tests) ($pr_labels)"

  # If there require tests, close the pull request
  if [[ -n "$require_tests" ]]; then
    echo "Closing PR #$pr_number $pr_title due to require_tests label"
    gh pr close "$pr_number" --comment "Closing require_tests PRs to prepare for Hacktoberfest"
    # sleep 2
  fi
done
