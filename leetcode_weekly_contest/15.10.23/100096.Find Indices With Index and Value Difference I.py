from typing import List


def findIndices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    for i,n in enumerate(nums):
        for j in range(i,len(nums)):
            if abs(i-j) >= indexDifference and abs(nums[j]-n) >= valueDifference:
                return [i,j]

    return [-1,-1]
