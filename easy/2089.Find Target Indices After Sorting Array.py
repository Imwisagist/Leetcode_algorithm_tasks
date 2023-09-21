# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

from typing import List

def targetIndices(nums: List[int], target: int) -> List[int]:
    nums.sort(); length = len(nums) - 1; l, r = 0, length

    while l <= r:
        m = (l + r) // 2

        if nums[m] >= target: r = m - 1
        else: l = m + 1

    left_idx = l; l, r = 0, length

    while l <= r:
        m = (l + r + 1) // 2

        if nums[m] <= target: l = m + 1
        else: r = m - 1

    return [x for x in range(left_idx, l)]


assert targetIndices([1,2,5,2,3],2) == [1,2]
assert targetIndices([1,2,5,2,3],3) == [3]
assert targetIndices([1,2,5,2,3],5) == [4]