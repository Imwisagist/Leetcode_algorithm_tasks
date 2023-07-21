# https://leetcode.com/problems/remove-element/
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    idx: int = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[idx] = nums[i]
            idx += 1

    return idx


assert removeElement([3, 2, 2, 3], 3) == 2
assert removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
