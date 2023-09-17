# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    d: dict = {chr:idx for idx,chr in enumerate(order)}; prev = []

    for word in words:
        cur = [d[chr] for chr in word]

        if cur < prev: return False

        prev = cur

    return True

        


assert isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz") is True
assert isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz") is False
assert isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz") is False
