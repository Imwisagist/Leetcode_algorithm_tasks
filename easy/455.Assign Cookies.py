# https://leetcode.com/problems/assign-cookies/

from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    result = child_i = 0

    for cookie in s:
        if child_i >= len(g):
            break
        if cookie >= g[child_i]:
            result += 1
            child_i += 1
    
    return result


assert findContentChildren([1,2,3], [1,1]) == 1
assert findContentChildren([1,2], [1,2,3]) == 2
