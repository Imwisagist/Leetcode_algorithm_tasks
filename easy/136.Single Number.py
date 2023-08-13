# https://leetcode.com/problems/single-number/

from functools import reduce
from typing import List

def singleNumber(nums: List[int]) -> int:

    return reduce(lambda total, el: total ^ el, nums)


assert singleNumber([2,2,1]) == 1
assert singleNumber([4,1,2,1,2]) == 4
assert singleNumber([1]) == 1
