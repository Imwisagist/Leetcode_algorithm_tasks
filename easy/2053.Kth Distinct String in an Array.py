# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

from typing import List

def kthDistinct(arr: List[str], k: int) -> str:
    d: dict = {}
    d_get = d.get

    for i in arr: d[i] = d_get(i,0) + 1

    for i, v in d.items():
        if v == 1:
            k -= 1
            if not k: return i
    
    return ""


assert kthDistinct(["d","b","c","b","c","a"], 2) == "a"
assert kthDistinct(["aaa","aa","a"], 1) == "aaa"
assert kthDistinct(["a","b","a"], 3) == ""
