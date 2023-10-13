# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/?envType=daily-question&envId=2023-10-10

from typing import List

def minOperations(nums: List[int]) -> int:
    n,j,nums = len(nums),0,sorted(set(nums))

    for i in nums: j += i - nums[j] > n-1

    return j + n - len(nums)


assert minOperations([4,2,5,3]) == 0
assert minOperations([1,2,3,5,6]) == 1
assert minOperations([1,10,100,1000]) == 3
