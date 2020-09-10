import datetime

now = datetime.datetime.now()

today = now.day
hour = now.hour


def start(update, context):
    if today == now.day and 5 <= hour < 12:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Good morning! Welcome to promobot, the easy solution to track steam game prices",
        )
    elif today == now.day and 12 <= hour < 17:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Good afternoon! Welcome to promobot, the easy solution to track steam game "
            + "prices",
        )
    elif today == now.day and 17 <= hour < 24:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Good night! Welcome to promobot, the easy solution to track steam game prices",
        )
    elif today == now.day and 0 <= hour < 5:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Good night! Welcome to promobot, the easy solution to track steam game prices",
        )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="How it works:\n"
        + "You search for your favorite game in the Steam "
        + "game database with the /add command.\n"
        + "Set the amount you want to pay for the game and "
        + "the bot will send a message when the game reaches "
        + "the selected or lower price.\n"
        + "You can track how many games do you want.\n"
        + "To view and manage all the games on your wish list, "
        + "enter the command /tracklist.\n"
        + "To see all the commands in detail, type the command /help",
    )
