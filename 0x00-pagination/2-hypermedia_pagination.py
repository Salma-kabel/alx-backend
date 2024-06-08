#!/usr/bin/env python3
"""Hypermedia pagination """


import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page, page_size):
    """ return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list"""
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default value 1
        and page_size with default value 10"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if (start >= len(data) or end >= len(data)):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """takes the same arguments (and defaults) as get_page"""
        dic = {}
        dic["page_size"] = page_size
        dic["page"] = page
        data = self.get_page(page, page_size)
        dic["data"] = data
        start, end = index_range(page, page_size)
        total = end // page_size
        if total == page:
            dic["next_page"] = None
            print("t",total, "p",page)
        else:
            print("p",page, "t", total)
            dic["next_page"] = page + 1
        if page == 1:
            dic["prev_page"] = None
        else:
            dic["prev_page"] = page - 1
        dic["total_pages"] = total
        return dic
