# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

def balancedStringSplit(s: str) -> int:
    cnt = res = 0

    for chr in s:
        if chr == "R": cnt += 1
        else: cnt -= 1

        if cnt == 0: res += 1

    return res


assert balancedStringSplit("RLRRLLRLRL") == 4
assert balancedStringSplit("RLRRRLLRLL") == 2
assert balancedStringSplit("LLLLRRRR") == 1
