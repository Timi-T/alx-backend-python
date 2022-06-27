#!/usr/bin/env python3
"""
Module to get a list from an asynchronous function
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """Function to call wait_random n times"""
    ret_list = [await wait_random(max_delay) for i in range(n)]
    return ret_list.sort()