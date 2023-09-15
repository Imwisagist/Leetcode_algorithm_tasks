# https://leetcode.com/problems/count-pairs-of-similar-strings/description/

from typing import List

def similarPairs(words: List[str]) -> int:
    d: dict = {}
    d_get = d.get

    for word in words:
        word = frozenset(word)
        d[word] = d_get(word,0) + 1

    return sum(v * (v - 1) // 2 for v in d.values())


assert similarPairs(["aba","aabb","abcd","bac","aabc"]) == 2
assert similarPairs(["aabb","ab","ba"]) == 3
assert similarPairs(["nba","cba","dba"]) == 0
