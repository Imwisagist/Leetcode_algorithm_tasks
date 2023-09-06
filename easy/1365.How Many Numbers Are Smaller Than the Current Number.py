# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    numbers: dict = {}

    for i in nums:
        numbers[i] = numbers.get(i, 0) + 1

    return [sum(numbers[j] for j in numbers if j < i) for i in nums]


assert smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]
assert smallerNumbersThanCurrent([6,5,4,8]) == [2,1,0,3]
assert smallerNumbersThanCurrent([7,7,7,7]) == [0,0,0,0]
