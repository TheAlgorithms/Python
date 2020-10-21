__author__ = "@ansanbinoy"

from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

from emoji import emojize

import json, os, sys

os.system("clear")

# Class for echo bot.

class EchoBot:

	def __init__(self, tocken):		self.tocken = tocken

		self.smile = emojize(':smiling_face_with_smiling_eyes:')

	def start(self, update, context): # Start command handling.

		uid = update.message.chat_id

		name = update.message.chat.first_name

		context.bot.send_message(chat_id = uid,

			text = f"Hey {name},\nThis is just a echo bot.{self.smile}")

	def message(self, update, context): # For handle all messages.

		uid = update.message.chat_id

		msg = update.message.text

		context.bot.send_message(uid,msg)

	def run(self):

		updater = Updater(self.tocken,use_context=True)

		dp = updater.dispatcher

		dp.add_handler(CommandHandler("start", self.start))

		dp.add_handler(MessageHandler(Filters.text, self.message))

		updater.start_polling()

		updater.idle()

def main():

"""

	jsf = open("credential.json")

	crd = json.load(jsf)

	tocken = crd["tocken"]

"""

	tocken = ""

	bot = EchoBot(tocken)

	bot.run()

if __name__ == '__main__':

	main()
