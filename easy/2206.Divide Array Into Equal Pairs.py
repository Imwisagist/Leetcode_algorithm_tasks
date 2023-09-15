# https://leetcode.com/problems/divide-array-into-equal-pairs/

from typing import List

def divideArray(nums: List[int]) -> bool:
    seen: set = set()

    for num in nums:
        if num in seen:
            seen.discard(num)
        else:
            seen.add(num)

    return not seen


assert divideArray([3,2,3,2,2,2]) is True
assert divideArray([1,2,3,4]) is False
