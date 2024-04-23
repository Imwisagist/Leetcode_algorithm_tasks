# https://leetcode.com/problems/line-reflection/

from typing import List


def isReflected(points: List[List[int]]) -> bool:
    s = set()
    max_x, min_x = -float('inf'), float('inf')

    for i, j in points:
        max_x = max(max_x, i)
        min_x = min(min_x, i)
        s.add((i, j))

    sum_x = max_x + min_x

    return all(
        (sum_x - x, y) in s for x, y in points
    )


assert isReflected([[1, 1], [0, 0], [-1, 1]])
assert isReflected([[-16, 1], [16, 1], [16, 1]])
assert isReflected([[0, 0], [1, 0]]) is True
assert isReflected([[1, 1], [-1, 1]]) is True
assert isReflected([[1, 1], [-1, -1]]) is False
assert isReflected([[-10, 5], [10, 5], [-8, 4], [6, 4]]) is False
assert isReflected([[0, 0]]) is True
assert isReflected([[2, 4], [4, 4], [0, 1], [6, 1], [2, 5], [12, 5]]) is False
assert isReflected([[-10, 4], [-6, 4], [-12, 1], [-4, 1]]) is True
