# Created by NiyazUrazaev on 31/05/23
import os

import requests

WEBHOOK_URL = os.getenv("YOUR_WEBHOOK_URL", "")


def send_mattermost_message(
    message: str,
    username: str,
    webhook_url: str,
) -> None:
    payload = {
        "text": message,
        "username": username
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise Exception("Failed to send a message in Mattermost")


if __name__ == "__main__":
    send_mattermost_message("<YOUR MESSAGE BODY>", "<USERNAME>", WEBHOOK_URL)
