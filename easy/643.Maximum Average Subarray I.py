# https://leetcode.com/problems/maximum-average-subarray-i/description/

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    cur = max = sum(nums[:k])

    for i in range(k, len(nums)):
        cur += nums[i] - nums[i-k]
        max = cur if cur > max else max
    
    return max / k


assert findMaxAverage([0,1,1,3,3],4) == 2.00
assert findMaxAverage([1,12,-5,-6,50,3],4) == 12.75
assert findMaxAverage([5],1) == 5.00
