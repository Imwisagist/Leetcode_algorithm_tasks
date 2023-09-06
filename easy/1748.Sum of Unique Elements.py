# https://leetcode.com/problems/sum-of-unique-elements/

from typing import List

def sumOfUnique(nums: List[int]) -> int:
    return sum(i for i in nums if nums.count(i) == 1)


assert sumOfUnique([1,2,3,2]) == 4
assert sumOfUnique([1,1,1,1,1]) == 0
assert sumOfUnique([1,2,3,4,5]) == 15
