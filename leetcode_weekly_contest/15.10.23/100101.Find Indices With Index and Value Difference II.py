from typing import List


def findIndices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    n = len(nums)
    
    for i in range(n):
        for j in range(i+indexDifference,n):
            if abs(nums[j]-nums[i]) >= valueDifference: return [i, j]

    return [-1, -1]


assert findIndices([5,1,4,1],2,4) == [0,3]

# TL