# https://leetcode.com/problems/smallest-index-with-equal-value/description/

from typing import List

def smallestEqual(nums: List[int]) -> int:
    return next((i for i, n in enumerate(nums) if i % 10 == n),-1)


assert smallestEqual([0,1,2]) == 0
assert smallestEqual([4,3,2,1]) == 2
assert smallestEqual([1,2,3,4,5,6,7,8,9,0]) == -1
