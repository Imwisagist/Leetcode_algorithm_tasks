# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


assert removeDuplicates([1, 1, 2]) == 2
assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
