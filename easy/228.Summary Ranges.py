# https://leetcode.com/problems/summary-ranges/

from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    ranges: list = []

    for i in nums:
        if ranges and ranges[-1][1] == i-1:
            ranges[-1][1] = i
        else:
            ranges.append([i, i])

    return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]


assert summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
assert summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
