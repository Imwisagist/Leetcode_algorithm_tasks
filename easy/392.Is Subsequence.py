# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s: str, t: str) -> bool:
    return all(c in iter(t) for c in s)


assert isSubsequence("abc", "ahbgdc") is True
assert isSubsequence("axc", "ahbgdc") is False
