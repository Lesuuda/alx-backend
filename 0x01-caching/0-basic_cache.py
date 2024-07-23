#!/usr/bin/env python3
""" Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and is a chaching system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
