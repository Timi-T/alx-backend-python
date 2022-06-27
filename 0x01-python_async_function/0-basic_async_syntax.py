#!/usr/bin/env python3
"""
Basic syntac for async await functions
"""

import asyncio
from random import uniform


async def wait_random(max_delay: float = 10) -> float:
    """Function to wait for a random delay"""

    delay_time = uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
