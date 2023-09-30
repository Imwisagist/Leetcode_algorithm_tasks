# https://leetcode.com/problems/monotonic-array/description/?envType=daily-question&envId=2023-09-29

from typing import List

def isMonotonic(nums: List[int]) -> bool:
    prev,middle,next = nums[0],nums[len(nums)//2],nums[-1]

    if prev <= middle <= next:
        for n in nums:
            if prev > n: return False

            prev = n

    elif prev >= middle >= next:
        for n in nums:
            if prev < n: return False

            prev = n

    else: return False

    return True


assert isMonotonic([1,2,2,3]) is True
assert isMonotonic([6,5,4,4]) is True
assert isMonotonic([1,3,2]) is False
