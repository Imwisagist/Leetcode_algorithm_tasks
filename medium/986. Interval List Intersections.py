# https://leetcode.com/problems/interval-list-intersections/description/
from typing import List


def intervalIntersection(l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
    i, j, n1, n2, res = 0, 0, len(l1), len(l2), []

    while i < n1 and j < n2:
        start = max(l1[i][0], l2[j][0]); end = min(l1[i][1], l2[j][1])

        if start <= end: res.append([start, end])
        if l1[i][1] < l2[j][1]: i += 1
        else: j += 1

    return res


assert intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
assert intervalIntersection([[1, 3], [5, 9]], []) == []
