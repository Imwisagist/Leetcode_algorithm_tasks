# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

from typing import List

def differenceOfSum(nums: List[int]) -> int:
    ds = 0

    for n in nums:
        while n: ds += n % 10; n //= 10

    return abs(sum(nums)-ds)


assert differenceOfSum([1,15,6,3]) == 9
assert differenceOfSum([1,2,3,4]) == 0
