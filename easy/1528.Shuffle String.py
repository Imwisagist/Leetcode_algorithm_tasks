# https://leetcode.com/problems/shuffle-string/description/

from typing import List

def restoreString(s: str, indices: List[int]) -> str:
    res = [None] * len(s)

    for i,c in zip(indices,s): res[i] = c

    return "".join(res)


assert restoreString("codeleet",[4,5,6,7,0,2,1,3]) == "leetcode"
assert restoreString("abc",[0,1,2]) == "abc"
