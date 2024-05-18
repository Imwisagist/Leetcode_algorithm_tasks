# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter


def firstUniqChar(s: str) -> int:
    d = Counter(s)

    for i, v in enumerate(s):
        if d[v] == 1: return i
        
    return -1


assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1
