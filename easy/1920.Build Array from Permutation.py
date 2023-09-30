# https://leetcode.com/problems/build-array-from-permutation/description/

from typing import List

def buildArray(nums: List[int]) -> List[int]:
    return [nums[nums[i]] for i in range(len(nums))]


assert buildArray([0,2,1,5,3,4]) == [0,1,2,4,5,3]
assert buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]
