# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    idxs: dict = {}

    for i in range(len(nums)):
        if nums[i] in idxs and abs(idxs[nums[i]] - i) <= k:
            return True
        idxs[nums[i]] = i

    return False


assert containsNearbyDuplicate([1,2,3,1], 3) is True
assert containsNearbyDuplicate([1,0,1,1], 1) is True
assert containsNearbyDuplicate([1,2,3,1,2,3], 2) is False
