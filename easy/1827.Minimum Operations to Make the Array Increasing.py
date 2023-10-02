# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/

from typing import List

def minOperations(nums: List[int]) -> int:
    res,prev = 0,nums[0]

    for i in range(1,len(nums)):
        num = nums[i]

        if num <= prev:
            res += prev - num + 1; prev += 1
        else: prev = num

    return res


assert minOperations([1,1,1]) == 3
assert minOperations([1,5,2,4,1]) == 14
assert minOperations([8]) == 0
