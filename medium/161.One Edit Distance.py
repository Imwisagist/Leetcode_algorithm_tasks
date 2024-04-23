# https://leetcode.com/problems/one-edit-distance/description/


def isOneEditDistance(s: str, t: str) -> bool:
    ns, nt = len(s), len(t)

    if ns < nt: return isOneEditDistance(t, s)

    if ns - nt > 1 or s == t: return False

    for i in range(nt):
        if s[i] != t[i]: return s[i+1:] == t[i+1:] or s[i+1:] == t[i:]

    return True


assert isOneEditDistance("abcd", "abfcd") is True
assert isOneEditDistance("ab", "acb") is True
assert isOneEditDistance("", "") is False
assert isOneEditDistance("a", "") is True
assert isOneEditDistance("", "z") is True
assert isOneEditDistance("a", "z") is True
assert isOneEditDistance("ab", "") is False
assert isOneEditDistance("", "fa") is False
assert isOneEditDistance("ab", "ab") is False
assert isOneEditDistance("ab", "ac") is True
