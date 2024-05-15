# https://leetcode.com/problems/max-consecutive-ones-ii/description/

from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    ans = cur = 0
    prev = -1

    for x in nums:
        if x: cur += 1
        else: prev, cur = cur, 0
        ans = max(ans, prev + 1 + cur)

    return ans


assert findMaxConsecutiveOnes([1, 0, 1, 1, 0]) == 4
assert findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 4
