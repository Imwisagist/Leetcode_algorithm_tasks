# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

from typing import List

def prefixCount(words: List[str], pref: str) -> int:
    return sum(1 for w in words if w.startswith(pref))


assert prefixCount(["pay","attention","practice","attend"],"at") == 2
assert prefixCount(["leetcode","win","loops","success"],"code") == 0
