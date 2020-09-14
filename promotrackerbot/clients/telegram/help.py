def help(update, context):
    cmd_list = (
        "I can help you find out when a game is on sale!\n\n"
        + "You can control me by sending these commands:\n"
        + "/start - start a chat with me\n"
        + "/help - shows the list of commands\n\n"
        + "/add <steam game url> - add a game to your track list"
        + "/tracklist - shows all the games you're tracking"
        + "New commands will be available soon."
    )

    context.bot.send_message(chat_id=update.effective_chat.id, text=cmd_list)
