# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

def minTimeToType(word: str) -> int:
    prev,res = "a",len(word)

    for chr in word:
        diff = abs(ord(chr)-ord(prev)); prev = chr
        res += diff if diff < 26 - diff else 26 - diff

    return res


assert minTimeToType("abc") == 5
assert minTimeToType("bza") == 7
assert minTimeToType("zjpc") == 34
