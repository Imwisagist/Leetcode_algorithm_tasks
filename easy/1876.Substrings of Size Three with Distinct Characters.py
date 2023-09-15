# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

def countGoodSubstrings(s: str) -> int:
    return sum(1 for i in range(len(s)-2) if len(set(s[i:i+3])) == 3)


assert countGoodSubstrings("xyzzaz") == 1
assert countGoodSubstrings("aababcabc") == 4
