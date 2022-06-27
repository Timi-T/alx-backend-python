#!/usr/bin/env python3
"""
Module to get a list from an asynchronous function
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def sort_list(my_list: list) -> list:
    """Function to asyncronously sort a list"""
    my_list.sort()


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Function to call wait_random n times"""
    ret_list = []
    for i in range(n):
        val = await wait_random(max_delay)
        print("appending")
        ret_list.append(val)
        await sort_list(ret_list)
    return ret_list
