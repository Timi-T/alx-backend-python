#!/usr/bin/env python3
"""
Basic syntac for async await functions
"""

from random import uniform


async def wait_random(max_delay: float = 10.0) -> float:
    """Function to wait for a random delay"""

    return uniform(0, max_delay)
