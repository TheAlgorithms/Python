# Created by sarathkaul on 12/11/19

import requests


# Slack messaging function using a webhook URL
def send_slack_message(message_body: str, slack_url: str) -> None:
    # Define headers for the HTTP POST request.
    headers = {"Content-Type": "application/json"}

    # Send the message to the Slack channel using the given webhook URL.
    response = requests.post(slack_url, json={"text": message_body}, headers=headers)

    #  Check the response status code for any errors.
    if response.status_code != 200:
        msg = (
            "Request to slack returned an error "
            f"{response.status_code}, the response is:\n{response.text}"
        )
        raise ValueError(msg)


if __name__ == "__main__":
    # Set the slack url to the one provided by Slack when you create the webhook at
    # https://my.slack.com/services/new/incoming-webhook/
    send_slack_message("<YOUR MESSAGE BODY>", "<SLACK CHANNEL URL>")
