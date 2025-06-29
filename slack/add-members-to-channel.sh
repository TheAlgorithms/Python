#!/bin/bash

# Assign arguments to variables
SLACK_TOKEN=$1
CHANNEL_ID=$2
clientId=$3
clientSecret=$4
run_id=$5
MEMBER_EMAILS_JSON=$6

# Get the Port access token
PORT_TOKEN_RESPONSE=$(curl -s -X 'POST' \
  'https://api.getport.io/v1/auth/access_token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "{
        \"clientId\": \"$clientId\",
        \"clientSecret\": \"$clientSecret\"
      }"
    )

echo $PORT_TOKEN_RESPONSE
PORT_ACCESS_TOKEN=$(echo $PORT_TOKEN_RESPONSE | jq -r '.accessToken')

# Ensure the access token was obtained successfully
if [ -z "$PORT_ACCESS_TOKEN" ] || [ "$PORT_ACCESS_TOKEN" == "null" ]; then
  error_message="Failed to obtain Port access token ❌"
  echo $error_message
  report_error "$error_message"
  exit 1
fi

# Function to report error
report_error() {
  local message=$1
  echo $message
  echo "ADD_MEMBER_TO_CHANNEL_ERROR=$message" >> $GITHUB_ENV
  curl -s -X POST "https://api.getport.io/v1/actions/runs/$run_id/logs" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $PORT_ACCESS_TOKEN" \
    -d "{\"message\": \"$message\"}"
}

user_ids=""

# Convert MEMBER_EMAILS_JSON to an array
readarray -t MEMBER_EMAILS < <(echo $MEMBER_EMAILS_JSON | jq -r 'fromjson | .[]')

for email in "${MEMBER_EMAILS[@]}"; do
  user_response=$(curl -s -X GET "https://slack.com/api/users.lookupByEmail?email=$email" \
    -H "Authorization: Bearer $SLACK_TOKEN")

  if [[ "$(echo $user_response | jq -r '.ok')" == "true" ]]; then
    user_id=$(echo $user_response | jq -r '.user.id')
    user_ids+="${user_id},"
  else
    error_message="Failed to retrieve user id for $email: $(echo $user_response | jq -r '.error' | tr '_' ' ') ⚠️"
    report_error "$error_message"
  fi
done

user_ids=${user_ids%,}

if [[ -n "$user_ids" ]]; then
  invite_response=$(curl -s -X POST "https://slack.com/api/conversations.invite" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $SLACK_TOKEN" \
    --data "{\"channel\":\"$CHANNEL_ID\",\"users\":\"$user_ids\"}")

  if [[ "$(echo $invite_response | jq -r '.ok')" == "false" ]]; then
    error_message="Failed to invite users to channel: $(echo $invite_response | jq -r '.error' | tr '_' ' ') ⚠️"
    report_error "$error_message"
  fi
else
  report_error "No user IDs found to invite."
fi
