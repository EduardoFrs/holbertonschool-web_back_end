#!/usr/bin/env python3

"""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function for multiply float by multiplier"""
    def multiply(n: float) -> float:
        """return product of n and multiplier"""
        return n * multiplier
    return multiply
