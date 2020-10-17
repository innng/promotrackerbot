from promotrackerbot.infra.redis import RedisClient


def tracklist(update, context):

    redis = RedisClient()
    redis.connect()

    chat_id = update.effective_chat.id
    if not redis.exists(str(chat_id)):
        answer = "No games are being tracked."
        context.bot.send_message(chat_id=chat_id, text=answer)

    game_list = redis.get(str(chat_id))
    # print(game_list, flush=True)
    product_list = ""

    for appid in game_list:
        product_list += game_list[appid]["name"] + " - " + game_list[appid]["price_formated"]
        if game_list[appid]["discount"] > 0:
            product_list += " - <b>Discount: " + str(game_list[appid]["discount"]) + "% !!</b> "
        else:
            product_list += " - No discount active."
        store_link = "https://store.steampowered.com/app/" + appid
        product_list += "<a href='" + store_link + "'> Link</a>\n"

    answer = "These are the products you are tracking: " + "\n\n" + product_list

    context.bot.send_message(
        chat_id=chat_id,
        text=answer,
        parse_mode="HTML",
        disable_web_page_preview=True,
    )
