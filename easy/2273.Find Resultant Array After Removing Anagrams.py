# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/

from typing import List
from itertools import groupby

def removeAnagrams(words: List[str]) -> List[str]:
    return [next(g) for _, g in groupby(words, sorted)]


assert removeAnagrams(["abba","baba","bbaa","cd","cd"]) == ["abba","cd"]
assert removeAnagrams(["a","b","c","d","e"]) == ["a","b","c","d","e"]
