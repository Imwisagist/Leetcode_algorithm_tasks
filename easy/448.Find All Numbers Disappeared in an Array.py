# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1
    
    res: list = []
    for i,n in enumerate(nums):
        if n > 0:
            res.append(i+1)
    
    return res


assert findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
assert findDisappearedNumbers([1,1]) == [2]
