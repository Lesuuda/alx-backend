#!/usr/bin/env pyhton3


"""
implements FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    implemnts FIFO caching
    """
    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """updates the dictionary"""
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data.update({key: item})
            self.order.append(key)

    def get(self, key):
        """gets the key value of a dictionary"""
        return self.cache_data.get(key, None)
