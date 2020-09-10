def add(update, context):
    if len(context.args) == 0:
        empty_msg_error = "Can't add 'nothing', " + "please type /add <product url>."
        context.bot.send_message(chat_id=update.effective_chat.id, text=empty_msg_error)
    else:
        product_name = context.args[0]
        answer = f"Product {product_name} added!"

        context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
