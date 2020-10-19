from promotrackerbot.infra.redis import RedisClient
from promotrackerbot.clients.steam import extract_appid
from promotrackerbot.clients.telegram.tracklist import tracklist


def remove(update, context):
    redis = RedisClient()
    redis.connect()

    chat_id = update.effective_chat.id
    game_url = context.args[0]

    appid = extract_appid(game_url)

    user_tracklist = redis.get(chat_id)
    game_name = user_tracklist[str(appid)]["name"]

    # print(user_tracklist, flush=True)
    del user_tracklist[str(appid)]
    # print(user_tracklist, flush=True)

    redis.set(chat_id, user_tracklist)

    answer = "The game " + game_name + " was removed from your tracklist."
    context.bot.send_message(chat_id=chat_id, text=answer)

    redis.close()
    tracklist(update, context)
