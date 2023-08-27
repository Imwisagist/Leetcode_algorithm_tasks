# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s: str, t: str) -> bool:
    t = iter(t)
    
    return all(c in t for c in s)


assert isSubsequence("abc", "ahbgdc") is True
assert isSubsequence("axc", "ahbgdc") is False
