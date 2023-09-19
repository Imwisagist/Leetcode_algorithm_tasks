# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/

from typing import List

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    d = {}; d_get = d.get

    for l, r in dominoes:
        if l < r: d[l,r] = d_get((l,r),0) + 1
        else: d[r,l] = d_get((r,l),0) + 1

    return sum(count*(count-1)//2 for count in d.values())


assert numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]) == 1
assert numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]) == 3
