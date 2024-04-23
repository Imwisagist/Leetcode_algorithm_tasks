# https://leetcode.com/problems/find-k-closest-elements/description/
from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    lo, hi = 0, len(arr) - k

    while lo < hi:
        mid = (lo + hi) // 2

        if x - arr[mid] > arr[mid + k] - x: lo = mid + 1
        else: hi = mid

    return arr[lo:lo + k]


assert findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
assert findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
assert findClosestElements([1, 1, 1, 10, 10, 10], 1, 9) == [10]
