import promotrackerbot.clients.steam as steam


def test_get_game_info_url_error():
    app_id = 323370
    url = "https://store.steampowered.com/" + str(app_id)
    result = steam.get_game_info(url)

    assert result == steam.url_error


def test_get_game_info_free():
    app_id = 323370
    url = "https://store.steampowered.com/app/" + str(app_id)
    result = steam.get_game_info(url)

    assert result == "Free"


def test_get_game_info():
    app_id = 728880
    url = "https://store.steampowered.com/app/" + str(app_id)
    result = steam.get_game_info(url)

    assert app_id in result.keys()


def test_extract_appid_fail_non_numeric():
    app_id = "abcdef"
    url = "https://store.steampowered.com/app/" + app_id
    result = steam.extract_appid(url)

    assert result == steam.url_error


def test_extract_appid_fail():
    app_id = "000000"
    url = "https://store.steampowered.com/" + app_id
    result = steam.extract_appid(url)

    assert result == steam.url_error


def test_extract_appid():
    app_id = "000000"
    url = "https://store.steampowered.com/app/" + app_id
    result = steam.extract_appid(url)

    assert result == app_id


def test_get_request():
    app_id = "323370"
    url = "https://store.steampowered.com/app/" + app_id
    result = steam.get_request(url)

    assert app_id in result.keys()
