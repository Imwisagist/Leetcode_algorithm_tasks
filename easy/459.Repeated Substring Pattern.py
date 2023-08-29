# https://leetcode.com/problems/repeated-substring-pattern/

def repeatedSubstringPattern(s: str) -> bool:
    return s in (s + s)[1:-1]


assert repeatedSubstringPattern("abab") is True
assert repeatedSubstringPattern("aba") is False
assert repeatedSubstringPattern("abcabcabcabc") is True
