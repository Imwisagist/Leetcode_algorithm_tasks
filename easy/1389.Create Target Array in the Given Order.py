# https://leetcode.com/problems/create-target-array-in-the-given-order/description/

from typing import List

def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    res = []

    for i in range(len(index)): res.insert(index[i],nums[i])

    return res


assert createTargetArray([0,1,2,3,4],[0,1,2,2,1]) == [0,4,1,3,2]
assert createTargetArray([1,2,3,4,0],[0,1,2,3,0]) == [0,1,2,3,4]
assert createTargetArray([1],[0]) == [1]
