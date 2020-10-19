from promotrackerbot.clients.telegram.unknown import unknown
from unittest.mock import Mock


def test_unknown():
    # Arrange
    chat_id = 999
    response = "Sorry, I didn't understand that command."

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_message = get_bot_answer

    # Act
    unknown(update, context)

    # Assert
    assert result["chat_id"] == chat_id
    assert result["text"] == response
