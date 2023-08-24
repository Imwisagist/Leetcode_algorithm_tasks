# https://leetcode.com/problems/word-pattern/

def wordPattern(pattern: str, s: str) -> bool:
    d1, l1 = {}, s.split()

    if len(pattern) != len(l1): return False

    for i, v in enumerate(pattern):
        if v not in d1:
            if l1[i] in d1.values(): return False
            d1[v] = l1[i]
        else:
            if d1[v] != l1[i]: return False
    
    return True


assert wordPattern("abba", "dog cat cat dog") is True
assert wordPattern("abba", "dog cat cat fish") is False
assert wordPattern("aaaa", "dog cat cat dog") is False
assert wordPattern("abba", "dog dog dog dog") is False
