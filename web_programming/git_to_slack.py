"""
# Git Push to Slack Notifier

This Python script allows you to send a message to a Slack channel when a Git push event occurs in your repository. You can use this script to receive notifications about code changes directly in your Slack workspace.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your system.
- The `requests` library installed. You can install it using `pip`:

   ```bash
   pip install requests

"""

import requests
import json

# Your Slack webhook URL
slack_webhook_url = "YOUR_SLACK_WEBHOOK_URL"

# Define the message to send to Slack
push_message = {
    "text": "A Git push event has occurred!",
    "attachments": [
        {
            "color": "#36a64f",  # Slack attachment color
            "title": "Git Push Event",
            "fields": [
                {"title": "Repository", "value": "Your Repository Name", "short": True},
                {"title": "Branch", "value": "Branch Name", "short": True},
                {"title": "Committer", "value": "Committer Name", "short": True},
            ],
        }
    ],
}

# Send the message to Slack
response = requests.post(
    slack_webhook_url,
    data=json.dumps(push_message),
    headers={"Content-Type": "application/json"},
)

# Check the response and print the result
if response.status_code == 200:
    print("Message sent to Slack successfully.")
else:
    print(
        f"Failed to send message to Slack. Status code: {response.status_code}, Response: {response.text}"
    )
