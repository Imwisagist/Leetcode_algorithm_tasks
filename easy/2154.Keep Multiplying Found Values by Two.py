# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

from typing import List

def findFinalValue(nums: List[int], original: int) -> int:
    nums: set = set(nums)

    while original in nums: original *= 2

    return original


assert findFinalValue([5,3,6,1,12], 3) == 24
assert findFinalValue([2,7,9], 4) == 4
