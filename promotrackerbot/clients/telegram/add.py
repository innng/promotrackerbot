from promotrackerbot.clients.steam import get_game_info
from promotrackerbot.infra.redis import RedisClient


def add(update, context):
    """Add a game in the user tracklist"""
    if len(context.args) == 0:
        empty_msg_error = "Can't add 'nothing', please type /add <product url>."
        context.bot.send_message(chat_id=update.effective_chat.id, text=empty_msg_error)
    else:

        game_url = context.args[0]

        game_info = get_game_info(game_url)
        appid = list(game_info.keys())[0]

        if game_info == "Free":
            answer = "This game is already free!"
            context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
            return

        chat_id = update.effective_chat.id

        redis = RedisClient()
        redis.connect()

        if redis.exists(chat_id):
            user_id = redis.get(chat_id)
            game_info.update(user_id)

        redis.set(chat_id, game_info)
        variavel = redis.get(str(chat_id))

        answer = f"Product {variavel[str(appid)]['name']} added!"
        if variavel[str(appid)]["discount"] > 0:
            answer += "\nThis game has already a discount!"

        redis.close()

        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=variavel[str(appid)]["image"],
            caption=answer,
        )
