#!/usr/bin/env python3
"""
    script 9
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    a function that returns a list of tuple
    Return: list[tuple[sequence]]
    """

    return [(i, len(i)) for i in lst]
