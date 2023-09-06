# https://leetcode.com/problems/number-of-good-pairs/

from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    return sum(1 for i, num in enumerate(nums) for j in nums[i+1:] if num == j)

assert numIdenticalPairs([1,2,3,1,1,3]) == 4
assert numIdenticalPairs([1,1,1,1]) == 6
assert numIdenticalPairs([1,2,3]) == 0
