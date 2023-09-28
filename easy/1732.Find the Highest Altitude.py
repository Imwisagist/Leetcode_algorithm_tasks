# https://leetcode.com/problems/find-the-highest-altitude/description/

from typing import List

def largestAltitude(gain: List[int]) -> int:
    highest = sum = 0

    for i in gain:
        sum += i; highest = max(sum, highest)

    return highest


assert largestAltitude([-5,1,5,0,-7]) == 1
assert largestAltitude([-4,-3,-2,-1,4,3,2]) == 0
