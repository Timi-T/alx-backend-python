#!/usr/bin/env python3
"""
Module to get a list from an asynchronous function
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function to call wait_random n times"""
    ret_list = []
    for i in range(n):
        task = task_wait_random(max_delay)
        ret_list.append(await task)
        j = i
        while j != 0:
            if ret_list[j] < ret_list[j - 1]:
                temp = ret_list[j]
                ret_list[j] = ret_list[j - 1]
                ret_list[j - 1] = temp
            j -= 1
    return ret_list
