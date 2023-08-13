# https://leetcode.com/problems/max-consecutive-ones/

from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    best, current = 0, 0

    for i in nums:
        if i == 1:
            current += 1
            if best < current:
                best = current
        else: 
            current = 0

    return best


assert findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
assert findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
