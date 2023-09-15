# https://leetcode.com/problems/points-that-intersect-with-cars/description/

from typing import List

def numberOfPoints(nums: List[List[int]]) -> int:
    s: set = set()

    for start, end in nums: s|= set(range(start,end+1))

    return len(s)


assert numberOfPoints([[3,6],[1,5],[4,7]]) == 7
assert numberOfPoints([[1,3],[5,8]]) == 7
