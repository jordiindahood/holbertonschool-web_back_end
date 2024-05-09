#!/usr/bin/env python3
"""
script 4
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the tasks
    """
    my_list = []
    for i in range(n):
        my_list.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(my_list)]
