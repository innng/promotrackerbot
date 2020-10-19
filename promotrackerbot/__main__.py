import os

from telegram.ext import CallbackQueryHandler, CommandHandler, Filters, MessageHandler, Updater

from clients.telegram.add import add
from clients.telegram.callback_query import callback_query_handler
from clients.telegram.help import help
from clients.telegram.remove import remove
from clients.telegram.removeall import removeall
from clients.telegram.start import start
from clients.telegram.tracklist import tracklist
from clients.telegram.unknown import unknown

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

if __name__ == "__main__":
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    commands = {
        "start": start,
        "help": help,
        "add": add,
        "tracklist": tracklist,
        "remove": remove,
        "removeall": removeall,
    }

    for command, callback in commands.items():
        handler = CommandHandler(command, callback)
        dispatcher.add_handler(handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    callback_query_handler = CallbackQueryHandler(callback_query_handler)
    dispatcher.add_handler(callback_query_handler)

    updater.start_polling()
