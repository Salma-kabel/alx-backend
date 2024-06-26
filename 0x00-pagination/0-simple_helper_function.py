#!/usr/bin/env python3
"""Simple helper function """


def index_range(page, page_size):
    """ return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list"""
    end = page * page_size
    start = end - page_size
    return (start, end)
