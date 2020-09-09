import datetime
now = datetime.datetime.now()

today = now.day
hour = now.hour

def start(update, context):
    if today == now.day and 5 <= hour < 12:
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Good morning! Welcome to promobot, the easy solution to track steam games prices")
    elif today == now.day and 12 <= hour < 17:
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Good afternoon! Welcome to promobot, the easy solution to track steam games prices")
    elif today == now.day and 17 <= hour < 24:
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Good night! Welcome to promobot, the easy solution to track steam games prices")
    elif today == now.day and 0 <= hour < 5:
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Good night! Welcome to promobot, the easy solution to track steam games prices")
    context.bot.send_message(chat_id=update.effective_chat.id, text=
        "Please enter the desired option:\n" +
        "/help to see all the options\n" +
        "/add to add a new product\n" +
        "/tracklist to see all the registered products\n")