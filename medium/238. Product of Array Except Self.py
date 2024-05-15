# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    pre = post = 1
    n = len(nums)
    result = []

    for i in nums:
        result.append(pre)
        pre *= i

    for j in range(n - 1, -1, -1):
        result[j] = result[j] * post
        post *= nums[j]

    return result


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
