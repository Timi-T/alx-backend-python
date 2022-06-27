#!/usr/bin/env python3
"""
Calculate runtime of an async function
"""

import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> float:
    """Function to measure runtime of an async function"""
    my_list = []
    for i in range(n):
        start = time.time()
        await wait_n(n, max_delay)
        end = time.time()
        my_list.append((end - start) / n)
    return my_list