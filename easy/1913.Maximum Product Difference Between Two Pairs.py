# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

from typing import List

def maxProductDifference(nums: List[int]) -> int:
    nums.sort()

    return nums[-1] * nums[-2] - nums[0] * nums[1]


assert maxProductDifference([5,6,2,7,4]) == 34
assert maxProductDifference([4,2,5,9,7,4,8]) == 64
