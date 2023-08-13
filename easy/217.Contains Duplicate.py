# https://leetcode.com/problems/contains-duplicate/

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    seen: set = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


assert containsDuplicate([1, 2, 3, 1]) is True
assert containsDuplicate([1, 2, 3, 4]) is False
assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
