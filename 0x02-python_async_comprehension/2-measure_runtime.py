#!/usr/bin/env python3
"""
Measure runtime of an asyncronous function
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run an asyncronous function 4 times and measure runtime"""

    task1 = asyncio.gather(*[async_comprehension()])
    task2 = asyncio.gather(*[async_comprehension()])
    task3 = asyncio.gather(*[async_comprehension()])
    task4 = asyncio.gather(*[async_comprehension()])

    tasks = asyncio.gather(task1, task2, task3, task4)
    start = time.time()
    await tasks
    end = time.time()
    return end - start
