# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    allowed = set(allowed)

    return sum(1 for word in words if set(word) <= allowed)


assert countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]) == 2
assert countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]) == 7
assert countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]) == 4
