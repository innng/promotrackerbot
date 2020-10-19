import json

import pytest
import redis

from promotrackerbot.infra.redis import RedisClient


@pytest.fixture
def redis_client():
    """Set up method to instantiate the redis."""
    redis_client = RedisClient()
    redis_client._redis = redis.Redis("localhost", 6379)
    return redis_client


def test_connect():
    """Check if the client corretly connects to an redis instance."""
    redis_client = RedisClient()

    redis_client.connect()

    assert isinstance(redis_client._redis, redis.Redis)


def test_close_correctly(redisdb, redis_client):
    """Check if the client closes the redis connection and clean its internal instance."""
    redis_client.close()

    assert not hasattr(redis_client, "_redis")


def test_set(redisdb, redis_client):
    """Check if the client can insert a new pair key-value on redis successfully."""
    redis_client.set("test", "result")
    result = redisdb.get("test").decode("utf-8")

    assert isinstance(result, str)


@pytest.mark.parametrize("value, expected", [("test", str), (["test"], list), ({"test": 1}, dict)])
def test_get(redisdb, redis_client, value, expected):
    """Check if the client can to retrive data from redis and transform it from string if needed."""
    redisdb.set("test", json.dumps(value))
    result = redis_client.get("test")

    assert isinstance(result, expected)


def test_redis_connected(capsys, redis_client):
    response = "Already connected.\n"
    redis_client.connect()
    captured = capsys.readouterr()

    assert captured.out == response


@pytest.mark.parametrize(
    "method_name, args",
    [("close", []), ("set", [None, None]), ("get", [None]), ("exists", [None]), ("delete", [None])],
)
def test_redis_not_connected(capsys, method_name, args):
    response = "Not connected.\n"

    redis_client = RedisClient()

    method = getattr(redis_client, method_name)
    method(*args)
    captured = capsys.readouterr()

    assert captured.out == response
