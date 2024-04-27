# https://leetcode.com/problems/squares-of-a-sorted-array/description/
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums);  p = r = n - 1; l, res = 0, [0]*n

    while l <= r:
        left, right = nums[l], nums[r]

        if abs(right) > abs(left): res[p] = right ** 2; r -= 1
        else: res[p] = left ** 2; l += 1

        p -= 1

    return res


assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
