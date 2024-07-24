#!/usr/bin/env python3
"""
uses LIFO to implement chaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Class to implment caching"""

    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """"adds item to a cache"""
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                newest_entry = self.order.pop(len(self.order) - 1)
                del self.cache_data[newest_entry]
                print(f"DISCARD: {newest_entry}")
            self.cache_data.update({key: item})
            self.order.append(key)

    def get(self, key):
        """gets corresponding key data"""
        return self.cache_data.get(key, None)
