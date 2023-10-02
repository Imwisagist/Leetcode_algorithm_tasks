# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/description/

from typing import List

def countGoodRectangles(rectangles: List[List[int]]) -> int:
    res,max_len = 0,min(rectangles[0])

    for r in rectangles:
        min_len = min(r)

        if min_len == max_len: res += 1
        elif min_len > max_len: max_len = min_len; res = 1

    return res


assert countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]) == 3
assert countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]) == 3
