# https://leetcode.com/problems/count-prefixes-of-a-given-string/description/

from typing import List

def countPrefixes(words: List[str], s: str) -> int:
    return sum(1 for w in words if s[:len(w)] == w)


assert countPrefixes(["a","b","c","ab","bc","abc"],"abc") == 3
assert countPrefixes(["a","a"],"aa") == 2
