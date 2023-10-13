# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=daily-question&envId=2023-10-09

from bisect import bisect_left, bisect_right
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    left,right = bisect_left(nums,target),bisect_right(nums,target) - 1

    return [left,right] if left <= right else [-1,-1]

assert searchRange([5,7,7,8,8,10],8) == [3,4]
assert searchRange([5,7,7,8,8,10],6) == [-1,-1]
assert searchRange([],0) == [-1,-1]
