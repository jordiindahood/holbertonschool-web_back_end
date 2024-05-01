#!/usr/bin/env python3
"""
    script 3
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a function that returns a tuple that has a string
    and a number(float or integer) given as parameters
    """
    return (k, v**2)
