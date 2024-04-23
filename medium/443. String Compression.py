# https://leetcode.com/problems/string-compression/description/
from typing import List


def compress(chars: List[str]) -> int:
    if len(chars) == 1: return 1

    cnt = 1
    idx = 0
    chars.append("*")

    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]: cnt += 1
        else:
            chars[idx] = chars[i-1]
            idx += 1

            if cnt == 1: continue

            for c in str(cnt):
                chars[idx] = c
                idx += 1

            cnt = 1

    chars.pop()

    return idx


assert compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert compress(["a"]) == 1
assert compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
