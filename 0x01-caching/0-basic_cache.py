#!/usr/bin/env python3
"""class BasicCache that inherits from
BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching system doesn’t have limit"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
         return self.cache_data.get(key, None)
