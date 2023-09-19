# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

def areAlmostEqual(s1: str, s2: str) -> bool:
    diff = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
            if diff > 2: return False

    for i in set(s1):
        if s1.count(i) != s2.count(i): return False
    
    return diff == 0 or diff == 2


assert areAlmostEqual("bank","kanb") is True
assert areAlmostEqual("attack","defend") is False
assert areAlmostEqual("kelb","kelb") is True
