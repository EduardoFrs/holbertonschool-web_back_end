"""Redis"""
import redis
from typing import Callable, Optional, Union
import uuid
import functools


def count_calls(method: Callable) -> Callable:
    """Count how many times a method has been called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """Cache"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """Get value"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Convert str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Convert int"""
        return self.get(key, int)