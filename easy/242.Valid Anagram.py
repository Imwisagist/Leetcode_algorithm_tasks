# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
    hashmap: dict = {}

    if len(s) != len(t):
        return False

    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1

    for i in t:
        hashmap[i] = hashmap.get(i, 0) - 1

    for val in hashmap.values():
        if val != 0:
            return False

    return True


assert isAnagram("anagram", "nagaram") is True
assert isAnagram("rat", "car") is False
