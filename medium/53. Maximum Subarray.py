# https://leetcode.com/problems/maximum-subarray/description/
from typing import List


def maxSubArray(nums: List[int]) -> int:
    cur_sum, res = 0, nums[0]

    for num in nums:
        if cur_sum < 1: cur_sum = num
        else: cur_sum += num

        res = max(cur_sum, res)

    return res


assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert maxSubArray([1]) == 1
assert maxSubArray([5, 4, -1, 7, 8]) == 23
