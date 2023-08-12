# https://leetcode.com/problems/binary-search/

from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        middle: int = (left + right) // 2
        current_value: int = nums[middle]
        if target == current_value:
            return middle
        elif target > current_value:
            left = middle + 1
        else:
            right = middle

    return -1


assert search([-1, 0, 3, 5, 9, 12], 9) == 4
assert search([-1, 0, 3, 5, 9, 12], 2) == -1
