import json
import os
import redis


class RedisClient(object):
    def __init__(self):
        """Initialize variables."""
        self._redis_host = os.environ.get("REDIS_HOST", "localhost")
        self._redis_port = os.environ.get("REDIS_PORT", 6379)

    def connect(self):
        """Connect to the Redis instance."""
        if self.is_connected():
            print("Already connected.")
            return

        self._redis = redis.Redis(
            host=self._redis_host,
            port=self._redis_port,
            encoding="utf-8",
            decode_responses=True,
            socket_connect_timeout=1,
        )

    def close(self):
        """Disconnect of the Redis instance."""
        if not self.is_connected():
            print("Not connected.")
            return

        self._redis.close()
        del self._redis

    def set(self, key, value):
        if not self.is_connected():
            print("Not connected.")
            return

        if not isinstance(value, str):
            value = json.dumps(value)
        self._redis.set(key, value)

    def get(self, key):
        if not self.is_connected():
            print("Not connected.")
            return

        value = self._redis.get(key)

        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            pass

        return value

    def exists(self, key):
        if not self.is_connected():
            print("Not connected.")
            return

        return self._redis.exists(key)

    def delete(self, key):
        if not self.is_connected():
            print("Not connected.")
            return

        self._redis.delete(key)

    def is_connected(self):
        return hasattr(self, "_redis")
