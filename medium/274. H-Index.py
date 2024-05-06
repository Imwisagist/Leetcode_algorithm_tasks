# https://leetcode.com/problems/h-index/description/
from typing import List


def hIndex(citations: List[int]) -> int:
    citations.sort(reverse=True); res = 0

    for i in citations:
        if res < i:
            res += 1
            continue
        else: break

    return res


assert hIndex([1, 3, 1]) == 1
assert hIndex([3, 0, 6, 1, 5]) == 3
