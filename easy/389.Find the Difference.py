# https://leetcode.com/problems/find-the-difference/

def findTheDifference(s: str, t: str) -> str:
    if not s: return t

    d1: dict = {}

    for i in s:
        d1[i] = d1.get(i, 0) + 1

    for i in t:
        d1[i] = d1.get(i, 0) - 1

    for i in d1:
        if d1[i] != 0:
            return i


assert findTheDifference("abcd", "abcde") == "e"
assert findTheDifference("", "y") == "y"
