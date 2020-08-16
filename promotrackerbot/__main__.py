import os

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

# TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command."
    )


if __name__ == "__main__":
    print("running!")

    TELEGRAM_TOKEN = "1206877808:AAGNEexaOUna0XmbWTQ6m99m_eAnpYqerkQ"
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    caps_handler = CommandHandler("caps", caps)
    dispatcher.add_handler(caps_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
