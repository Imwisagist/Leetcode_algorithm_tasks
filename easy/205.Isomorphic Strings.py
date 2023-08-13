# https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(s: str, t: str) -> bool:
    chars: dict = {}
    
    for i in range(len(s)):
        if s[i] not in chars:
            if t[i] in chars.values(): return False
            chars[s[i]] = t[i]
        else:
            if chars[s[i]]!=t[i]: return False
            
    return True


assert isIsomorphic("egg", "add") is True
assert isIsomorphic("foo", "bar") is False
assert isIsomorphic("paper", "title") is True
assert isIsomorphic("badc", "baba") is False

