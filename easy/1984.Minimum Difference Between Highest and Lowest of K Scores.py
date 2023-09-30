# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

from typing import List

def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort(); lowest = float("inf")

    if len(nums) == 1: return 0

    for i in range(len(nums)+1-k):
        num = nums[i+k-1] - nums[i]
        
        if num < lowest: lowest = num

    return lowest


assert minimumDifference([90],1) == 0
assert minimumDifference([9,4,1,7],2) == 2
