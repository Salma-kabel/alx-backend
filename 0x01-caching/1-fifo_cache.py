#!/usr/bin/env python3
"""class FIFOCache that inherits from
BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class that is a caching system"""
    def __init__(self):
        """initiate method"""
        super().__init__()

    def put(self, key, item):
        """assign to dictionary self.cache_data the item value for the key"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[0]
            del self.cache_data[discarded_key]

            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
