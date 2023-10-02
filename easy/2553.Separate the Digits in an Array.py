# https://leetcode.com/problems/separate-the-digits-in-an-array/description/

from typing import List

def separateDigits(nums: List[int]) -> List[int]:
    return [int(d) for n in nums for d in str(n)]


assert separateDigits([13,25,83,77]) == [1,3,2,5,8,3,7,7]
assert separateDigits([7,1,3,9]) == [7,1,3,9]
