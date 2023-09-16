# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

from typing import List

def findMaxK(nums: List[int]) -> int:
    s: set = set(nums)

    while True:
        m = max(s)
        if -m in s: return m
        s.discard(m)
        if not s: return -1


assert findMaxK([-1,2,-3,3]) == 3
assert findMaxK([-1,10,6,7,-7,1]) == 7
assert findMaxK([-10,8,6,7,-2,-3]) == -1
