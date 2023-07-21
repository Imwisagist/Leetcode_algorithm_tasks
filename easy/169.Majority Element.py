# https://leetcode.com/problems/majority-element/
from collections import defaultdict
from typing import List


def majorityElement(nums: List[int]) -> int:
    n, arr = len(nums) // 2, defaultdict(int)

    for num in nums:
        arr[num] += 1

    for key, value in arr.items():
        if value > n:
            return key

    return 0


assert majorityElement([3, 2, 3]) == 3
assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
assert majorityElement([2, 5, 1, 0, 15, 6, 23]) == 23
