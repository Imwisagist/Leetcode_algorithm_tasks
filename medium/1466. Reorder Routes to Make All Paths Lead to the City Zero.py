# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
from collections import defaultdict
from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
    res, d, visited = 0, defaultdict(list), set()

    for from_, to_ in connections:
        d[from_].append(to_)
        d[to_].append(-from_)

    def dfs(node):
        nonlocal res
        visited.add(node)

        for i in d[node]:
            abs_val = abs(i)

            if abs_val in visited: continue

            res += i > 0
            dfs(abs_val)

    dfs(0)

    return res


assert minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
assert minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
assert minReorder(3, [[1, 0], [2, 0]]) == 0
