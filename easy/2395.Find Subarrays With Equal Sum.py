# https://leetcode.com/problems/find-subarrays-with-equal-sum/description/

from typing import List

def findSubarrays(nums: List[int]) -> bool:
    seen: set = set()

    for i in range(len(nums)-1):
        s = nums[i] + nums[i+1]

        if s in seen: return True

        seen.add(s)

    return False


assert findSubarrays([4,2,4]) is True
assert findSubarrays([1,2,3,4,5]) is False
assert findSubarrays([0,0,0]) is True
