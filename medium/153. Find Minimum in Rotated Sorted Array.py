# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


def findMin(nums: List[int]) -> int:
    l, r, res = 0, len(nums), nums[0]

    while l < r:
        m = (l + r) // 2

        if nums[m] > res: l = m + 1
        else: res = nums[m]; r = m

    return res


assert findMin([3, 4, 5, 1, 2]) == 1
assert findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert findMin([11, 13, 15, 17]) == 11
