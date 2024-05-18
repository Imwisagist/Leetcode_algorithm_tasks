# https://leetcode.com/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d: dict = {}

    for i, v in enumerate(nums):
        if target - v in d: return [d[target - v], i]

        d[v] = i


assert twoSum([2, 5, 5, 11], 10) == [1, 2]
assert twoSum([2, 5, 5, 11], 12) is None
assert twoSum([3], 6) is None
