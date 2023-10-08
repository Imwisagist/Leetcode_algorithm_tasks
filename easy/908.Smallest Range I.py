# https://leetcode.com/problems/smallest-range-i/description/

from typing import List

def smallestRangeI(nums: List[int], k: int) -> int:
    diff,extension = max(nums)-min(nums),2*k
    
    if diff <= extension: return 0
    else: return diff - extension


assert smallestRangeI([1],0) == 0
assert smallestRangeI([0,10],2) == 6
assert smallestRangeI([1,3,6],3) == 0
