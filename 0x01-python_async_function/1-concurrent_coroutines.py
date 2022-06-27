#!/usr/bin/env python3
"""
Module to get a list from an asynchronous function
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Function to call wait_random n times"""
    ret_list = []
    for i in range(n):
        val = await wait_random(max_delay)
        ret_list.append(val)
        j = i
        while j != 0:
            if ret_list[j] < ret_list[j - 1]:
                temp = ret_list[j]
                ret_list[j] = ret_list[j - 1]
                ret_list[j - 1] = temp
            j -= 1
    return ret_list
