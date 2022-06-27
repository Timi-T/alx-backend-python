#!/usr/bin/env python3
"""
Basic syntac for async await functions
"""

from random import uniform


async def wait_random(max_delay = 10.0):
    """Function to wait for a random delay"""

    return uniform(0, max_delay)
