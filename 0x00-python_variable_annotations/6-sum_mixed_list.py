#!/usr/bin/env python3
"""This module contains the function sum_mixed_list(mxd_lst)"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """the function returns sum of list"""
    return sum(mxd_lst)
