# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

def maxLengthBetweenEqualCharacters(s: str) -> int:
    d, result = {}, -1

    for idx, chr in enumerate(s):
        if chr in d: d[chr] = d[chr][0], idx
        else: d[chr] = idx, 0

    for idx, val in d.values():
        if val: result = max(result, val - idx - 1)

    return result


assert maxLengthBetweenEqualCharacters("aa") == 0
assert maxLengthBetweenEqualCharacters("abca") == 2
assert maxLengthBetweenEqualCharacters("cbzxy") == -1
