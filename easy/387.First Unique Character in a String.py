# https://leetcode.com/problems/first-unique-character-in-a-string/

def firstUniqChar(s: str) -> int:
    d: dict = {}

    for i in s:
        d[i] = d.get(i, 0) + 1

    for i, j in d.items():
        if j == 1:
            return s.index(i)
        
    return -1


assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1
