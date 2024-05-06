# https://leetcode.com/problems/insert-delete-getrandom-o1/
from random import choice


class RandomizedSet:

    def __init__(self):
        self.hashmap, self.values = {}, []

    def insert(self, val: int) -> bool:
        if val in self.hashmap: return False

        self.hashmap[val] = len(self.values); self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap: return False

        index, last = self.hashmap[val], self.values[-1]
        self.values[index], self.hashmap[last] = last, index
        self.values.pop()

        del self.hashmap[val]

        return True

    def getRandom(self) -> int:
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
