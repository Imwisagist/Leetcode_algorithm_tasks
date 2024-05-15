# https://leetcode.com/problems/max-consecutive-ones/
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    best, cur = 0, 0

    for i in nums:
        if i: cur += 1
        else:
            if best < cur: best = cur
            cur = 0

    return max(best, cur)


assert findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
assert findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
