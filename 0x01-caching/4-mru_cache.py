#!/usr/bin/env pyhton3


"""
implements FIFMRUO caching
"""
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
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
                mru = self.order.popleft()
                del self.cache_data[mru]
                print(f"DISCARD: {mru}")
            self.cache_data.update({key: item})
            self.order.appendleft(key)

    def get(self, key):
        """gets dictionary item"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache_data[key]
        return None
