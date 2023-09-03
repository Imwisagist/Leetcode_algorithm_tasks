# https://leetcode.com/problems/array-partition/

from typing import List

def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


assert arrayPairSum([1,4,3,2]) == 4
assert arrayPairSum([6,2,6,5,1,2]) == 9
