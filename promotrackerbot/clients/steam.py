import time
import requests

url_error = "Error! Malformed URL."


def extract_appid(url):
    """Extracts and return the unique appid from the Steam® Store url
    Returns
    -------
    String
        game appid in string format
        or an error message if URL has no appid in it

    Only URLs from the official Steam® Store are accepted
    """

    url = url.split("/")
    if "app" in url:
        appid_index = url.index("app") + 1
        if not url[appid_index].isnumeric():
            return url_error

    return url[appid_index]


def get_request(url):
    """Return json-formatted response of a get request.

    Returns
    -------
    json_data
        json-formatted response (dict-like)

    string
        error message if the URL is malformed
    """

    try:
        game_appid = extract_appid(url)

        if game_appid == url_error:
            return url_error

        api_url = "https://store.steampowered.com/api/appdetails?appids=" + extract_appid(url)
        response = requests.get(url=api_url)

    except requests.exceptions.SSLError as s:
        print("SSL Error:", s)

        for i in range(5, 0, -1):
            print("\rWaiting... ({})".format(i), end="")
            time.sleep(1)
        print("\rRetrying." + " " * 10)

        # recusively try again
        return get_request(url)

    if response:
        return response.json()
    else:
        # response is none usually means too many requests. Wait and try again
        print("No response, waiting 10 seconds...")
        time.sleep(10)
        print("Retrying.")

        return get_request(url)


def get_game_info(url):
    """Extracts all the useful information from the API response

    Returns
    -------
    json_data
        json-formatted response (dict-like)

    string
        error message if the URL is malformed
    """

    api_response = get_request(url)

    if api_response == url_error:
        return url_error

    game_info = {}

    for appid in api_response:
        game_data = api_response[appid]["data"]
        game_info["name"] = game_data["name"]
        game_info["original_price"] = game_data["price_overview"]["initial"]
        game_info["price"] = game_data["price_overview"]["final"]
        game_info["price_formated"] = game_data["price_overview"]["final_formatted"]
        game_info["discount"] = game_data["price_overview"]["discount_percent"]
        game_info["is_free"] = game_data["is_free"]

    return game_info


# Request error due to a bad url with no appid information
# print(get_game_info("https://store.steampowered.com/app/Battlefield_4/"))

# Well formed url with woking request
# print(get_game_info("https://store.steampowered.com/app/1238860/Battlefield_4/"))
