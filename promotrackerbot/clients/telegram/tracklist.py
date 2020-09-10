def tracklist(update, context):
    product_list = ["Placeholder1", "Placeholder2"]
    answer = "These are the products you are tracking: " + ", ".join(product_list) + "."

    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
