# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/

from typing import List

def countWords(words1: List[str], words2: List[str]) -> int:
    d1, d2 = {}, {}
    d_get1, d_get2 = d1.get, d2.get

    for i in words1: d1[i] = d_get1(i,0) + 1

    for i in words2: d2[i] = d_get2(i,0) + 1

    return sum(1 for i, v in d1.items() if (v == 1) and (d2.get(i,0) == 1))


assert countWords(["leetcode","is","amazing","as","is"],["amazing","leetcode","is"]) == 2
assert countWords(["b","bb","bbb"],["a","aa","aaa"]) == 0
assert countWords(["a","ab"],["a","a","a","ab"]) == 1
