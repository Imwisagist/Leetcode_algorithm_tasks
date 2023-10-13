# https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=daily-question&envId=2023-10-11

from bisect import bisect_right,bisect_left
from typing import List

def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
    start,end = [],[]

    for s,e in flowers: start.append(s); end.append(e)

    start.sort(); end.sort()

    return [bisect_right(start,p) - bisect_left(end,p) for p in people]


assert fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]],[2,3,7,11]) == [1,2,2,2]
assert fullBloomFlowers([[1,10],[3,3]],[3,3,2]) == [2,2,1]
