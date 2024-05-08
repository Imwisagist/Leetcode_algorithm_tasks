# https://leetcode.com/problems/majority-element/
from typing import List


def majorityElement(nums: List[int]) -> int:
    count, candidate = 0, 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


assert majorityElement([3, 2, 3]) == 3
assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
