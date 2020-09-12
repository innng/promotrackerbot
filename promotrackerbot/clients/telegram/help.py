def help(update, context):
    cmd_list = (
        "I can help you find out when a game is on sale!\n\n"
        + "You can control me by sending these commands:\n"
        + "/start - start a chat with me\n"
        + "/help - show a list of commands\n\n"
        + "New commands will be available soon."
    )

    context.bot.send_message(chat_id=update.effective_chat.id, text=cmd_list)
