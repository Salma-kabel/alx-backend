#!/usr/bin/env python3
"""class BasicCache that inherits from
BaseCaching and is a caching system"""


class BasicCache(BaseCaching):
    """caching system doesn’t have limit"""
    """Add an item in the cache"""
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    """return the value in self.cache_data linked to key"""
    def get(self, key):
         return self.cache_data.get(key, None)
