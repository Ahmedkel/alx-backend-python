#!/usr/bin/env python3
"""
This module contains the function
make_multiplier(multiplier: str)
"""
from typing import Callable


def make_multiplier(multiplier: str) -> Callable[[float], float]:
    """the function returns multiplication in float"""
    def x(f: float) -> float:
        return float(f * multiplier)

    return x
