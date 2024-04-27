# https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(s: str, t: str) -> bool:
    chars: dict = {}
    
    for i in range(len(s)):
        left, right = s[i], t[i]

        if left not in chars:
            if right in chars.values(): return False
            chars[left] = right
        else:
            if chars[left] != right: return False
            
    return True


assert isIsomorphic("egg", "add") is True
assert isIsomorphic("foo", "bar") is False
assert isIsomorphic("paper", "title") is True
assert isIsomorphic("badc", "baba") is False

