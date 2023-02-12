#!/usr/bin/env python3
""" Creating a Cache class """
import redis
from typing import List, Float, Union
from uuid import uuid4


class Cache:
    """ A Cache class """
    def __init__(self):
        """ Instantiate a Redis cache client """
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes data as an argument, generate a random key,
        set the data as the value of the key and return the key
        """
        rand_key = str(uuid4())
        self._redis.set(rand_key, data)
        return rand_key
