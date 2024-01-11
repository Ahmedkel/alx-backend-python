#!/usr/bin/env python3
"""This module contains the function"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """the function returns multiplication in float"""
    return [(i, len(i)) for i in lst]
