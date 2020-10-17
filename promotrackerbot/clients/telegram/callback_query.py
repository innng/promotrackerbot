def dont_track_dlcs(update, context):
    print("botao funcionou", flush=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Ok, tracking only the main game.",
    )


def callback_query_handler(update, context):
    query = update.callback_query
    cqd = query.data
    # message_id = update.callback_query.message.message_id
    # update_id = update.update_id
    if cqd == "dlc-yes":
        context.bot.answer_callback_query(query.id)
        # Função pra rastrear as DLCs
    elif cqd == "dlc-no":
        context.bot.answer_callback_query(query.id)
        dont_track_dlcs(update, context)
