from promotrackerbot.infra.redis import RedisClient

# import telegram


# def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
#     menu = [buttons[i : i + n_cols] for i in range(0, len(buttons), n_cols)]
#     if header_buttons:
#         menu.insert(0, [header_buttons])
#     if footer_buttons:
#         menu.append([footer_buttons])
#     return menu


def tracklist(update, context):

    # button_list = [
    #     telegram.InlineKeyboardButton("Yes", callback_data="dlc-yes"),
    #     telegram.InlineKeyboardButton("No", callback_data="dlc-no"),
    # ]
    # reply_markup = telegram.InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    # context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text="Would you like to track the DLCs for this game as well?",
    #     reply_markup=reply_markup,
    # )

    redis = RedisClient()
    redis.connect()

    chat_id = update.effective_chat.id
    if not redis.exists(chat_id) or redis.get(chat_id) == {}:
        answer = "No games are being tracked."
        context.bot.send_message(chat_id=chat_id, text=answer)
        return

    game_list = redis.get(str(chat_id))
    # print(game_list, flush=True)
    product_list = ""

    for appid in game_list:
        product_list += game_list[appid]["name"] + " - " + game_list[appid]["price_formated"]
        if game_list[appid]["discount"] > 0:
            product_list += " - <b>Discount: " + str(game_list[appid]["discount"]) + "% !!</b> "
        else:
            product_list += " - No discount active. "
        store_link = "https://store.steampowered.com/app/" + appid
        product_list += "<a href='" + store_link + "'> Link</a>\n"
    # print(product_list, flush=True)

    answer = "These are the products you are tracking: " + "\n\n" + product_list

    context.bot.send_message(
        chat_id=chat_id,
        text=answer,
        parse_mode="HTML",
        disable_web_page_preview=True,
    )
