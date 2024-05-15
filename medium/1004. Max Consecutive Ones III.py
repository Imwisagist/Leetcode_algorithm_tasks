# https://leetcode.com/problems/max-consecutive-ones-iii/description/
from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    l_idx = r_idx = 0

    for r_idx, r_val in enumerate(nums):
        if not r_val: k -= 1

        if k < 0:
            if not nums[l_idx]: k += 1
            l_idx += 1

    return r_idx - l_idx + 1


assert longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
assert longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
