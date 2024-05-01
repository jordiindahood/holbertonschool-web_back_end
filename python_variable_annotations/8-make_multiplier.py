#!/usr/bin/env python3
"""
    script 3
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that returns a tuple that has a string
    and a number(float or integer) given as parameters
    """

    def mul(number: float) -> float:
        """
        a function that return a float of
        """
        return number * multiplier

    return mul
