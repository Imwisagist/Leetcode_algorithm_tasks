# https://leetcode.com/problems/move-zeroes/

from typing import List

def moveZeroes(nums: List[int]) -> List[int]:
    start_idx: int = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[start_idx], nums[j] = nums[j], nums[start_idx]
            start_idx += 1

    return nums


assert moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert moveZeroes([0]) == [0]
