#!/usr/bin/env python3

"""1. Async Comprehensions"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine collect 10 random numbers"""
    random_number = [i async for i in async_generator()]
    return random_number
