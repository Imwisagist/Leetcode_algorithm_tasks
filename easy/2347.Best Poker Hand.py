# https://leetcode.com/problems/best-poker-hand/description/

from typing import List
from collections import Counter

def bestHand(ranks: List[int], suits: List[str]) -> str:
    if len(set(suits)) == 1: return "Flush"

    d: dict = {}; d_get = d.get

    for i in ranks: d[i] = d_get(i,0) + 1

    m = max(d.values())

    if m > 2: return "Three of a Kind"

    if m == 2: return "Pair"

    return "High Card"


assert bestHand([13,2,3,1,9],["a","a","a","a","a"]) == "Flush"
assert bestHand([4,4,2,4,4],["d","a","a","b","c"]) == "Three of a Kind"
assert bestHand([10,10,2,12,9],["a","b","c","a","d"]) == "Pair"
