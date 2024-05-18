# https://leetcode.com/problems/valid-anagram/
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


assert isAnagram("anagram", "nagaram") is True
assert isAnagram("rat", "car") is False
