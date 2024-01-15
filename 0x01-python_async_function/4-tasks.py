#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
from random import uniform
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random
    n times with the specified max_delay.

    Parameters:
    - n (int): Number of tasks to spawn.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - List[float]: List of delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
