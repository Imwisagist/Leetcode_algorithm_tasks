# https://leetcode.com/problems/check-distances-between-same-letters/description/

from typing import List

def checkDistances(s: str, distance: List[int]) -> bool:
    d: dict = {}
    d_get = d.get

    for i, v in enumerate(s): d[v] = d_get(v,[]) + [i]

    for char, (from_, to_) in d.items():
        if (to_ - from_ - 1) != distance[ord(char)-97]:
            return False

    return True
    

assert checkDistances("abaccb",[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) is True
assert checkDistances("aa",[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) is False
assert checkDistances("zz", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]) is False