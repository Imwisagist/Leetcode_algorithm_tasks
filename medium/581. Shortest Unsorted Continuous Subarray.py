# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
from typing import List


def findUnsortedSubarray(nums: List[int]) -> int:
    min_int, max_int = float("inf"), -float("inf"); left = right = 0; n = len(nums)

    for i, v in enumerate(nums):
        if v >= max_int: max_int = max(v, max_int)
        else: right = i

    for i, v in enumerate(nums[::-1]):
        if v <= min_int: min_int = min(v, min_int)
        else: left = n - i - 1

    return abs(right - left + 1) if left != right else 0


assert findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
assert findUnsortedSubarray([1, 2, 3, 4]) == 0
assert findUnsortedSubarray([1]) == 0
