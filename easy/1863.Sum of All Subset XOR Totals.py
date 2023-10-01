# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

from typing import List
from functools import reduce

def subsetXORSum(nums: List[int]) -> int:
    return reduce(lambda x,y: x|y,nums) << len(nums)-1


assert subsetXORSum([1,3]) == 6
assert subsetXORSum([5,1,6]) == 28
assert subsetXORSum([3,4,5,6,7,8]) == 480
