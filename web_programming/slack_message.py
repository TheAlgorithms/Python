# Created by sarathkaul on 12/11/19

import json
import requests


def send_slack_message(message_body, slack_url):
    slack_data = {"text": message_body}
    headers = {"Content-Type": "application/json"}
    response = requests.post(slack_url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise ValueError(
            "Request to slack returned an error %s, the response is:\n%s"
            % (response.status_code, response.text)
        )


if __name__ == "main":
    # Set the slack url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
    send_slack_message("<YOUR MESSAGE BODY>", "<SLACK CHANNEL URL>")
