# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
from typing import List

def maxProduct(nums: List[int]) -> int:
    nums.sort()

    return (nums[-1]-1) * (nums[-2]-1)


assert maxProduct([3,4,5,2]) == 12
assert maxProduct([1,5,4,5]) == 16
assert maxProduct([10,2,5,2]) == 36
