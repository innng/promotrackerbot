from promotrackerbot.clients.telegram.add import add
from unittest.mock import Mock, patch


@patch("promotrackerbot.clients.telegram.add.RedisClient")
@patch("promotrackerbot.clients.telegram.add.get_game_info")
def test_add_free_game(mock_steam, mock_redis):
    # Arrange
    url = "test"
    chat_id = 999
    game = "test"
    response = "Product " + game + " added!"

    game_info = "Free"
    response = "This game is already free!"

    mock_steam.return_value = game_info

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


@patch("promotrackerbot.clients.telegram.add.RedisClient")
@patch("promotrackerbot.clients.telegram.add.get_game_info")
def test_add_url_error(mock_steam, mock_redis):
    # Arrange
    url = "test"
    chat_id = 999
    game = "test"
    response = "Product " + game + " added!"

    url_error = "Error! Malformed URL."
    response = "The url you tried to add is invalid. Try again."

    mock_steam.return_value = url_error

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


@patch("promotrackerbot.clients.telegram.add.RedisClient")
@patch("promotrackerbot.clients.telegram.add.get_game_info")
def test_add_success_discount(mock_steam, mock_redis):
    # Arrange
    url = "test"
    chat_id = 999
    game = "test"
    appid = "1234"
    image = "image"
    response = "Product " + game + " added!" + "\nThis game has already a discount!"

    mock_steam.return_value = {appid: {}}
    redis = mock_redis.return_value
    redis.get.return_value = {appid: {"discount": 50, "name": game, "image": image}}

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()
    context.args = [url]

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_photo = get_bot_answer

    # Act
    add(update, context)
    # print(result)
    # Assert
    assert result["chat_id"] == chat_id
    assert result["photo"] == image
    assert result["caption"] == response


@patch("promotrackerbot.clients.telegram.add.RedisClient")
@patch("promotrackerbot.clients.telegram.add.get_game_info")
def test_add_success(mock_steam, mock_redis):
    # Arrange
    url = "test"
    chat_id = 999
    game = "test"
    appid = "1234"
    image = "image"
    response = "Product " + game + " added!"

    mock_steam.return_value = {appid: {}}
    redis = mock_redis.return_value
    redis.get.return_value = {appid: {"discount": 0, "name": game, "image": image}}

    update = Mock()
    update.effective_chat.id = chat_id

    context = Mock()
    context.args = [url]

    result = {}

    def get_bot_answer(**kwargs):
        result.update(kwargs)

    context.bot.send_photo = get_bot_answer

    # Act
    add(update, context)
    # print(result)
    # Assert
    assert result["chat_id"] == chat_id
    assert result["photo"] == image
    assert result["caption"] == response


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
