#!/usr/bin/env python3

"""2. Run time for four parallel comprehensions"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure total runtime"""
    begin = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = asyncio.get_event_loop().time()
    return end - begin
