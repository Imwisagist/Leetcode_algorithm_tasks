# https://leetcode.com/problems/search-insert-position/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)

    while low < high:
        mid: int = (low + high) // 2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid

    return low


assert searchInsert([1, 3, 5, 6], 5) == 2
assert searchInsert([1, 3, 5, 6], 2) == 1
assert searchInsert([1, 3, 5, 6], 7) == 4
