# https://leetcode.com/problems/third-maximum-number/

from typing import List

def thirdMax(nums: List[int]) -> int:
    a = b = c = -float("inf")

    for n in nums:
        if n in (a, b, c): continue
        if n > a: n, a = a, n
        if n > b: n, b = b, n
        if n > c: n, c = c, n

    return a if c == -float("inf") else c


assert thirdMax([3, 2, 1]) == 1
assert thirdMax([1, 2]) == 2
assert thirdMax([2, 2, 3, 1]) == 1
