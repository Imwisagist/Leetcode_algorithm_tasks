# https://contest.yandex.ru/contest/51022/enter/

from math import comb
from typing import Iterable

class Node:
    def __init__(self) -> None:
        self.value = 0; self.kids = {}


class Tree:
    def __init__(self) -> None:
        self.root = Node(); self.count = 0

    def insert(self, nums: Iterable) -> None:
        node = self.root

        for n in nums:
            if n not in node.kids: node.kids[n] = Node()

            node = node.kids[n]; node.value += 1

    def traversal(self) -> int:
        stack = [c for c in self.root.kids.values() if c.value > 1]

        while stack:
            node = stack.pop(); self.count += comb(node.value, 2)
            stack.extend(c for c in node.kids.values() if c.value > 1)

        return self.count


tree = Tree()

for _ in range(int(input())): _ = input(); tree.insert(map(int, input().split()))

print(tree.traversal())
