# https://leetcode.com/problems/construct-the-rectangle/
from typing import List


def constructRectangle(area: int) -> List[int]:
    return next([area // w, w] for w in range(int(area ** 0.5), 0, -1) if area % w == 0)


assert constructRectangle(4) == [2,2]
assert constructRectangle(37) == [37,1]
assert constructRectangle(122122) == [427,286]
