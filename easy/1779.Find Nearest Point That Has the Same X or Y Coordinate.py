# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/

from typing import List

def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    res = (float("inf"),-1)

    for i,(j,k) in enumerate(points):
        if j == x or k == y:
            dist = abs(j-x)+abs(k-y)

            if dist < res[0]: res = (dist,i)

    return res[1]


assert nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]) == 2
assert nearestValidPoint(3,4,[[3,4]]) == 0
assert nearestValidPoint(3,4,[[2,3]]) == -1
