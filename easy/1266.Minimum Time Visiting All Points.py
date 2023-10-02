# https://leetcode.com/problems/minimum-time-visiting-all-points/description/

from typing import List

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    prev_x,prev_y = points[0]; res = 0

    for x,y in points:
        res += max(abs(x-prev_x),abs(y-prev_y))
        prev_x,prev_y = x,y

    return res


assert minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]) == 7
assert minTimeToVisitAllPoints([[3,2],[-2,2]]) == 5
