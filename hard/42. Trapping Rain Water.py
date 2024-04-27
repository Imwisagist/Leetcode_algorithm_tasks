# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List


def trap(height: List[int]) -> int:
    max_height = max(height); cur_height = cnt = 0
    peak = height.index(max_height)

    for i in height[:peak]:
        if i >= cur_height: cur_height = i
        else: cnt += cur_height - i

    cur_height = 0

    for i in height[-1:peak:-1]:
        if i >= cur_height: cur_height = i
        else: cnt += cur_height - i

    return cnt


assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
