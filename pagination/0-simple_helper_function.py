#!/usr/bin/env python3

"""0. Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """return tuple witj start and end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
