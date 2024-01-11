#!/usr/bin/env python3
"""This module contains the function to_kv(k, v)"""
from typing import Tuple, Union


def to_kv (k: str, v: Union[int, float]) -> Tuple[str, float]:
    """the function returns a tuple."""
    return k, v**2
