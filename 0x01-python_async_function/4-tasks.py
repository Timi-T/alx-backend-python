#!/usr/bin/env python3
"""
Calculate runtime of an async function
"""

import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> float:
    """Function to measure runtime of an async function"""
    task = asyncio.create_task(wait_n(n, max_delay))
    return await task
