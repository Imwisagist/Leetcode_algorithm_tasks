# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return "".join(word1) == "".join(word2)


assert arrayStringsAreEqual(["ab", "c"],["a", "bc"]) is True
assert arrayStringsAreEqual(["a", "cb"],["ab", "c"]) is False
assert arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"]) is True
