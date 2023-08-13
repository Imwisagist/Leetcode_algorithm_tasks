# https://leetcode.com/problems/missing-number/

from functools import reduce
from typing import List

def missingNumber(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y[0] ^ y[1], enumerate(nums), len(nums))


assert missingNumber([3, 0, 1]) == 2
assert missingNumber([0, 1]) == 2
assert missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
