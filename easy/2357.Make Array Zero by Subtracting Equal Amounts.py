# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

from typing import List

def minimumOperations(nums: List[int]) -> int:
    return len(set(nums) - {0})


assert minimumOperations([1,5,0,3,5]) == 3
assert minimumOperations([0]) == 0
