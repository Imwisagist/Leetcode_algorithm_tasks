# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


def longestSubarray(nums: List[int]) -> int:
    # pref, post = [], []
    # cnt = result = 0
    #
    # for i in nums:
    #     if i: cnt += 1
    #     else: cnt = 0
    #
    #     pref.append(cnt)
    #
    # cnt = 0
    #
    # for i in range(len(nums), 0, -1):
    #     if i: cnt += 1
    #     else: cnt = 0
    #
    #     post.append(cnt)
    #
    # for i in range(len(nums)):
    #     if i == 0:
    #         size = post[i+1]
    #     elif i == len(nums) - 1:
    #         size = pref[i-1]
    #     else:
    #         size = pref[i-1] + post[i+1]
    #
    #     result = max(result, size)
    #
    # return result

    n = len(nums)

    left = 0
    zeros = 0
    ans = 0

    for right in range(n):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        ans = max(ans, right - left + 1 - zeros)

    return ans - 1 if ans == n else ans


assert longestSubarray([1, 1, 0, 1]) == 3
assert longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
assert longestSubarray([1, 1, 1]) == 2
