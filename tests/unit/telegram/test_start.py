from promotrackerbot.clients.telegram.start import start
from unittest.mock import Mock

import datetime

now = datetime.datetime.now()

today = now.day
hour = now.hour

text_instruction = (
    "How it works:\n\n"
    + "You search for your favorite game in the Steam "
    + "game database with the /add command.\n\n"
    + "Set the amount you want to pay for the game and "
    + "the bot will send a message when the game reaches "
    + "the selected or lower price.\n\n"
    + "You can track how many games do you want.\n\n"
    + "To view and manage all the games on your wish list, "
    + "enter the command /tracklist.\n\n"
    + "To see all the commands in detail, type the command /help")

if today == now.day and 5 <= hour < 12:
    def test_start_morning():
        # Arrange
        chat_id = 999
        response = (
            "Good morning! Welcome to promobot, the easy solution to track steam game "
            + "prices\n\n" + text_instruction)

        update = Mock()
        update.effective_chat.id = chat_id

        context = Mock()

        result = {}

        def get_bot_answer(**kwargs):
            result.update(kwargs)

        context.bot.send_message = get_bot_answer

        # Act
        start(update, context)

        # Assert
        assert result["chat_id"] == chat_id
        assert result["text"] == response


elif today == now.day and 12 <= hour < 17:
    def test_start_afternoon():
        # Arrange
        chat_id = 999
        response = (
            "Good afternoon! Welcome to promobot, the easy solution to track steam game "
            + "prices\n\n" + text_instruction)

        update = Mock()
        update.effective_chat.id = chat_id

        context = Mock()

        result = {}

        def get_bot_answer(**kwargs):
            result.update(kwargs)

        context.bot.send_message = get_bot_answer

        # Act
        start(update, context)

        # Assert
        assert result["chat_id"] == chat_id
        assert result["text"] == response

elif today == now.day and 17 <= hour < 24:
    def test_start_night():
        # Arrange
        chat_id = 999
        response = (
            "Good night! Welcome to promobot, the easy solution to track steam game "
            + "prices\n\n" + text_instruction)

        update = Mock()
        update.effective_chat.id = chat_id

        context = Mock()

        result = {}

        def get_bot_answer(**kwargs):
            result.update(kwargs)

        context.bot.send_message = get_bot_answer

        # Act
        start(update, context)

        # Assert
        assert result["chat_id"] == chat_id
        assert result["text"] == response

elif today == now.day and 0 <= hour < 5:
    def test_start_dawn():
        # Arrange
        chat_id = 999
        response = (
            "Good night! Welcome to promobot, the easy solution to track steam game "
            + "prices\n\n" + text_instruction)

        update = Mock()
        update.effective_chat.id = chat_id

        context = Mock()

        result = {}

        def get_bot_answer(**kwargs):
            result.update(kwargs)

        context.bot.send_message = get_bot_answer

        # Act
        start(update, context)

        # Assert
        assert result["chat_id"] == chat_id
        assert result["text"] == response
