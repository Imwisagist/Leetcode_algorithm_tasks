# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/

from typing import List

def repeatedNTimes(nums: List[int]) -> int:
    seen: set = set()

    for i in nums:
        if i in seen: return i
        seen.add(i)


assert repeatedNTimes([1,2,3,3]) == 3
assert repeatedNTimes([2,1,2,5,3,2]) == 2
assert repeatedNTimes([5,1,5,2,5,3,5,4]) == 5
