from promotrackerbot.clients.telegram.tracklist import tracklist
from unittest.mock import Mock


def test_tracklist():
    # Arrange
    tracklist_ = ["Placeholder1", "Placeholder2"]
    chat_id = 999
    response = "These are the products you are tracking: " + ', '.join(tracklist_) + "."

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_message = get_bot_answer

    # Act
    tracklist(update, context)

    # Assert
    assert result["chat_id"] == chat_id
    assert result["text"] == response
