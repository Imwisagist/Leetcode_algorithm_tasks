# https://leetcode.com/problems/teemo-attacking/

from typing import List

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    result: int = duration

    for i in range(len(timeSeries)-1):
        result += min(duration, timeSeries[i + 1] - timeSeries[i])

    return result


assert findPoisonedDuration([1, 4, 10], 5) == 13
assert findPoisonedDuration([1, 4], 2) == 4
assert findPoisonedDuration([1, 2], 2) == 3
