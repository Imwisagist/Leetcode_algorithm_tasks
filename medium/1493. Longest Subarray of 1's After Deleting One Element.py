# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


def longestSubarray(nums: List[int]) -> int:
    prev = cur = res = 0

    for i in nums:
        if i:
            cur += 1
        else:
            res = max(prev + cur, res)
            prev = cur
            cur = 0

    return cur - 1 if cur == len(nums) else max(res, prev + cur)


assert longestSubarray([1, 1, 0, 1]) == 3
assert longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
assert longestSubarray([1, 1, 1]) == 2
