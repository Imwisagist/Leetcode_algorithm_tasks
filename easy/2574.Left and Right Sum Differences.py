# https://leetcode.com/problems/left-and-right-sum-differences/description/

from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:
    n = len(nums); left, right = [0] * n, [0] * n

    for i in range(1,n): left[i] = left[i-1] + nums[i-1]
    
    for i in range(n-2,-1,-1): right[i] = right[i+1] + nums[i+1]
    
    return [abs(l-r) for l, r in zip(left, right)]


assert leftRightDifference([10,4,8,3]) == [15,1,11,22]
assert leftRightDifference([1]) == [0]
