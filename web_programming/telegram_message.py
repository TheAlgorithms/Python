# Created by NiyazUrazaev on 03/05/23

import requests


def send_message_to_telegram(token: str, chat_id: str, message_text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url, data=data)
    if not response.ok:
        print("Failed to send a message in Telegram:", response.text)


if __name__ == "__main__":
    token = "<YOUR BOT TOKEN>"
    chat_id = "<YOUR CHANNEL ID>"
    message_text = "<YOUR MESSAGE BODY>"
    send_message_to_telegram(token, chat_id, message_text)
