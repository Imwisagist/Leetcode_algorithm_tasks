# https://leetcode.com/problems/check-if-array-is-good/description/

from typing import List

def isGood(nums: List[int]) -> bool:
    n, sm, mx = len(set(nums)), sum(nums), max(nums)
    
    return sm == (n+3)*n//2 and n == mx


assert isGood([2, 1, 3]) is False
assert isGood([1, 3, 3, 2]) is True
assert isGood([1, 1]) is True
assert isGood([3, 4, 4, 1, 2, 1]) is False
