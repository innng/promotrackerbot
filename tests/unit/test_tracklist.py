from promotrackerbot.clients.telegram.tracklist import tracklist
from unittest.mock import Mock, patch


@patch("promotrackerbot.clients.telegram.tracklist.RedisClient")
def test_tracklist(mock_redis):
    # Arrange
    chat_id = "999"
    url = "https://store.steampowered.com/app/"
    appid_1 = "1234"
    game_1 = "test1"
    appid_2 = "5678"
    game_2 = "test2"
    response_basic = "These are the products you are tracking"

    redis = mock_redis.return_value
    redis.get.return_value = {
        appid_1: {"name": game_1, "price_formated": "0", "discount": 0},
        appid_2: {"name": game_2, "price_formated": "0", "discount": 0},
    }

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
    assert response_basic in result["text"]
    assert game_1 in result["text"]
    assert url + appid_1 in result["text"]
    assert game_2 in result["text"]
    assert url + appid_2 in result["text"]


@patch("promotrackerbot.clients.telegram.tracklist.RedisClient")
def test_empty_tracklist(mock_redis):
    # Arrange
    chat_id = "999"
    response = "No games are being tracked."

    redis = mock_redis.return_value
    redis.exists.return_value = False

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
    # print(response, end="\n\n\n\n")
    # print(result["text"])
    assert result["chat_id"] == chat_id
    assert result["text"] == response
