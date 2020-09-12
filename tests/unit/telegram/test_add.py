from promotrackerbot.clients.telegram.add import add
from unittest.mock import Mock


def test_add_success():
    # Arrange
    url = "https://store.steampowered.com/app/782330/DOOM_Eternal/"
    chat_id = 999
    response = "Product " + url + " added!"

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()
    context.args = [url]

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_message = get_bot_answer

    # Act
    add(update, context)

    # Assert
    assert result["chat_id"] == chat_id
    assert result["text"] == response


def test_add_fail():
    # Arrange
    chat_id = 999
    response = "Can't add 'nothing', please type /add <product url>."

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()
    context.args = []

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_message = get_bot_answer

    # Act
    add(update, context)

    # Assert
    assert result["chat_id"] == chat_id
    assert result["text"] == response
