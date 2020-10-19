from unittest.mock import Mock

from promotrackerbot.clients.telegram.removeall import removeall


def test_removeall():
    # Arrange
    chat_id = 999
    response = "Your list was removed."

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_message = get_bot_answer

    # Act
    removeall(update, context)

    # Assert
    assert result["chat_id"] == chat_id
    assert result["text"] == response
