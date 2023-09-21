# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

from typing import List

def maximumCount(nums: List[int]) -> int:
    if nums[0] > 0 or nums[-1] < 0: return len(nums)

    length = len(nums) - 1; l, r = 0, length

    while l <= r:
        m = (l + r) // 2

        if nums[m] >= 0: r = m - 1
        else: l = m + 1

    left_zero_idx = l; l, r = 0, length

    while l <= r:
        m = (l + r + 1) // 2

        if nums[m] <= 0: l = m + 1
        else: r = m - 1

    return max(left_zero_idx, length - l + 1)


assert maximumCount([-925,-170,-5,728,795,810,821,919,1776,1861]) == 7
assert maximumCount([-2,-1,-1,1,2,3]) == 3
assert maximumCount([-3,-2,-1,0,0,1,2]) == 3
assert maximumCount([5,20,66,1314]) == 4
