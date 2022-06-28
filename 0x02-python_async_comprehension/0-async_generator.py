#!/usr/bin/env python3
"""
Async generator
"""

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Function to generate random numbers asyncronously"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(uniform(0, 10))
