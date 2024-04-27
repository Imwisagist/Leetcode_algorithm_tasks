# https://leetcode.com/problems/merge-intervals/
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    left, right = intervals[0]; res = []

    for start, end in intervals[1:]:
        if right >= start: right = max(right, end)
        else: res.append([left, right]); left, right = start, end

    res.append([left, right])

    return res


assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
