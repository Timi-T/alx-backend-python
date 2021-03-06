#!/usr/bin/env python3
"""
Async comprehension
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Take in 10 random numbers from a generator and return the numbers"""
    return [random_no async for random_no in async_generator()]
