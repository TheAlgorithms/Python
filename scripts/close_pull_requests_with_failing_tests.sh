#!/bin/bash

# List all open pull requests
prs=$(gh pr list --state open --json number,title,labels --limit 500)

# Loop through each pull request
echo "$prs" | jq -c '.[]' | while read -r pr; do
  pr_number=$(echo "$pr" | jq -r '.number')
  pr_title=$(echo "$pr" | jq -r '.title')
  pr_labels=$(echo "$pr" | jq -r '.labels')

  # Check if the "tests are failing" label is present
  tests_are_failing=$(echo "$pr_labels" | jq -r '.[] | select(.name == "tests are failing")')
  echo "Checking PR #$pr_number $pr_title ($tests_are_failing) ($pr_labels)"

  # If there are failing tests, close the pull request
  if [[ -n "$tests_are_failing" ]]; then
    echo "Closing PR #$pr_number $pr_title due to tests_are_failing label"
    gh pr close "$pr_number" --comment "Closing tests_are_failing PRs to prepare for Hacktoberfest"
    sleep 2
  fi
done
