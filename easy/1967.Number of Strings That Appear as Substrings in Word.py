# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/

from typing import List

def numOfStrings(patterns: List[str], word: str) -> int:
    return sum(p in word for p in patterns)


assert numOfStrings(["a","abc","bc","d"],"abc") == 3
assert numOfStrings(["a","b","c"],"aaaaabbbbb") == 2
assert numOfStrings(["a","a","a"],"ab") == 3
