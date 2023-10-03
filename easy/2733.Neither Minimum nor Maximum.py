# https://leetcode.com/problems/neither-minimum-nor-maximum/description/


from typing import List

def findNonMinOrMax(nums: List[int]) -> int:
    if len(nums) < 3: return -1
    
    max = min = nums[0]

    for n in nums:
        if n > max: max = n

        elif n < min: min = n

    for n in nums:
        if n != min and n != max: return n


assert findNonMinOrMax([3,2,1,4]) == 3
assert findNonMinOrMax([1,2]) == -1
assert findNonMinOrMax([2,1,3]) == 2
