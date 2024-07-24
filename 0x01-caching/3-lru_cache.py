#!/usr/bin/env pyhton3


"""
implements FIFO caching
"""
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    implemnts FIFO caching
    """
    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.order = deque()

    def __getitem__(self, key):
        """overides __getitem__ to hanle print operations"""
        return self.get(key)

    def put(self, key, item):
        """adds dictionary item to LRU chache"""
        if key and item:
            if key in self.order:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru = self.order.pop()
                del self.cache_data[lru]
                print(f"DISCARD: {lru}")
            self.cache_data.update({key: item})
            self.order.appendleft(key)

    def get(self, key):
        """gets dictionary item"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache_data[key]
        return None
