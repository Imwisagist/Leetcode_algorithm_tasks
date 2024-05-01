# https://leetcode.com/problems/continuous-subarray-sum/description/
from typing import List


def checkSubarraySum(nums: List[int], k: int) -> bool:
    d, sum_ = {0: -1}, 0

    for i, n in enumerate(nums):
        sum_ += n; diff = sum_ % k

        if diff not in d: d[diff] = i
        elif i - d[diff] > 1: return True

    return False


assert checkSubarraySum([23, 2, 4, 6, 7], 6) is True
assert checkSubarraySum([23, 2, 6, 4, 7], 6) is True
assert checkSubarraySum([23, 2, 6, 4, 7], 13) is True
