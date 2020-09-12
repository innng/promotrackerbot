def add(update, context):
    if len(context.args) == 0:
        empty_msg_error = "Can't add 'nothing', please type /add <product url>."
        context.bot.send_message(chat_id=update.effective_chat.id, text=empty_msg_error)
    else:
        size_name = len(context.args)
        product_name = context.args[0]
        for position in range(1, size_name):
            if position != size_name:
                product_name = product_name + " "
            product_name = product_name + context.args[position]
        answer = f"Product {product_name} added!"

        context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
