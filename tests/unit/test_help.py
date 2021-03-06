from unittest.mock import Mock

from promotrackerbot.clients.telegram.help import help


def test_help():
    # Arrange
    chat_id = 999
    response = (
        "I can help you find out when a game is on sale!\n\n"
        + "You can control me by sending these commands:\n"
        + "/start - start a chat with me\n"
        + "/help - shows the list of commands\n"
        + "/add <steam game url> - add a game to your track list\n"
        + "/tracklist - shows all the games you're tracking\n"
        + "/remove - delete a specific game from tracklist\n"
        + "/removeall - delete the tracklist and all the games within it\n\n"
        + "New commands will be available soon."
    )

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_message = get_bot_answer

    # Act
    help(update, context)

    # Assert
    assert result["chat_id"] == chat_id
    assert result["text"] == response
