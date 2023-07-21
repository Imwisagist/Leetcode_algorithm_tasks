# https://leetcode.com/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap: dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i


assert twoSum(nums=[2, 5, 5, 11], target=10) == [1, 2]
assert twoSum(nums=[2, 5, 5, 11], target=12) is None
