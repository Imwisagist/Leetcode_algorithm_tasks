# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

from typing import List

def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    ranges.sort()

    for l, r in ranges:
        if l <= left <= r:
            if l <= right <= r: return True
            else: left = r + 1

    return False


assert isCovered([[1,2],[3,4],[5,6]],2,5) is True
assert isCovered([[1,10],[10,20]],21,21) is False
