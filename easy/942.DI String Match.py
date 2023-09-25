# https://leetcode.com/problems/di-string-match/description/

from typing import List


def diStringMatch(s: str) -> List[int]:
    l, r, res = 0, len(s), []

    for chr in s:
        if chr == "I": res.append(l); l += 1
        else: res.append(r); r -= 1

    res.append(l if s[-1] == "I" else r)

    return res


assert diStringMatch("IDID") == [0,4,1,3,2]
assert diStringMatch("III") == [0,1,2,3]
assert diStringMatch("DDI") == [3,2,0,1]
