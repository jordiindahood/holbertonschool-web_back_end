#!/usr/bin/env python3
"""
script 3
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an integer max_delay
    and returns a asyncio.Task
    """
    return asyncio.Task(wait_random(max_delay))
