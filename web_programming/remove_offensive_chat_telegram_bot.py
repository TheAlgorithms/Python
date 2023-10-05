"""
A Telegram bot that can remove chat that contains offensive words provided to look after from a  Group or Channel the bot is part of.

Prerequisite:
1. This script needs two 3rd party packages:  pyTelegramBotAPI and python-dotenv

2. This script needs a BOT_TOKEN that can be generated following the simple steps provided in the official guide:
https://core.telegram.org/bots/features#creating-a-new-bot


Testing Steps:
1. Create the BOT using the above official doc
2. Add the BOT to a channel or Group
3. Install the required packages and run this Python file
4. Send any Offensive text that you have set to filter out in the group/channel and see the response


Author: Suman Mitra
https://youtube.com/@LetsCodeTogether
https://github.com/suman2023
"""
import os

import telebot
from dotenv import load_dotenv

"""
load_dotenv()

Parse a .env file and then load all the variables found as environment variables.

Add the BOT_TOKEN variable in the .env file
eg. BOT_TOKEN=<the token received from Bot Father>
"""
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Add the words to be checked for in the set.
offensive_words = {"stupid", "shit", "thug"}

"""
@bot.message_handler(func=lambda message: message != None)

Handles New incoming message of any kind - text, photo, sticker, etc.
As a parameter to the decorator function, it passes :class:`telebot.types.Message` object.
Telegram Documentation: https://core.telegram.org/bots/api#message


bot.delete_message()

Use this method to delete a message, including service messages.
- If the bot is an administrator of a group, it can delete any message there.
Returns True on success.
Telegram documentation: https://core.telegram.org/bots/api#deletemessage
"""


@bot.message_handler(func=lambda message: message != None)
def remove_offensive_chat(message):
    from_user = message.from_user
    if from_user:
        if set(message.text.lower().split()) & offensive_words:
            bot.delete_message(message.chat.id, message.message_id)


"""
bot.polling(non_stop=True)

This function creates a new Thread that calls an internal __retrieve_updates function.
This allows the bot to retrieve Updates automatically and notify listeners and message handlers accordingly.

Warning: Do not call this function more than once!

:param non_stop: Do not stop polling when an ApiException occurs.
"""
bot.polling(non_stop=True)
