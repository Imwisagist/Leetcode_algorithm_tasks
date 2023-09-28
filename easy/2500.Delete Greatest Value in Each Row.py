# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

from typing import List
from heapq import heapify, heappop

def deleteGreatestValue(grid: List[List[int]]) -> int:
    return sum(max(c) for c in zip(*[sorted(r) for r in grid]))

assert deleteGreatestValue([[1,2,4],[3,3,1]]) == 8
assert deleteGreatestValue([[10]]) == 10
