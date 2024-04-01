# https://leetcode.com/problems/line-reflection/description/

from typing import List

def isReflected(points: List[List[int]]) -> bool:
    sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

    if len(sorted_points) % 2 == 1:
        return False

    