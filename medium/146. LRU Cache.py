# https://leetcode.com/problems/lru-cache/description/
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity; self.linkedList = OrderedDict()

    def put(self, key, value):
        if key in self.linkedList: self.linkedList.move_to_end(key)
        else:
            if len(self.linkedList) == self.capacity: self.linkedList.popitem(last=False)

        self.linkedList[key] = value

    def get(self, key):
        if key not in self.linkedList: return -1

        self.linkedList.move_to_end(key)

        return self.linkedList[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
