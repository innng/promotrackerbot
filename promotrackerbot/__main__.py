import os

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from clients.telegram.start import start
from clients.telegram.help import help
from clients.telegram.add import add
from clients.telegram.tracklist import tracklist
from clients.telegram.unknown import unknown

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

if __name__ == "__main__":
    print("running!")

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    commands = {"start": start, "help": help, "add": add, "tracklist": tracklist}

    for command, callback in commands.items():
        handler = CommandHandler(command, callback)
        dispatcher.add_handler(handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
