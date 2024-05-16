# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        m = (l + r) // 2
        left, mid, right = nums[l], nums[m], nums[r]

        if mid == target: return m
        elif mid >= left:
            if mid > target >= left: r = m - 1
            else: l = m + 1
        elif right >= target > mid: l = m + 1
        else: r = m - 1

    return -1


assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search([1], 0) == -1
