from promotrackerbot.infra.redis import RedisClient


def removeall(update, context):
    redis = RedisClient()
    redis.connect()

    chat_id = update.effective_chat.id

    redis.set(chat_id, {})

    answer = "Your list was removed."
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

    redis.close()
