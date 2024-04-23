# https://leetcode.com/problems/max-consecutive-ones-ii/description/

from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    ans = curr = 0
    prev = -1

    for x in nums:
        if x: curr += 1
        else: prev, curr = curr, 0
        ans = max(ans, prev + 1 + curr)

    return ans


assert findMaxConsecutiveOnes([1, 0, 1, 1, 0]) == 4
assert findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 4
