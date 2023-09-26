# https://leetcode.com/problems/shortest-distance-to-a-character/description/

from typing import List

def shortestToChar(s: str, c: str) -> List[int]:
    n, result, p = len(s), [], 0
    zero_idxs = [i for i in range(n) if s[i] == c]

    for i in range(n):
        if s[i] == c:
            result.append(0); p += 1
        elif i < zero_idxs[0]: result.append(zero_idxs[0] - i)
        elif i > zero_idxs[-1]: result.append(i - zero_idxs[-1])
        else: result.append(min(zero_idxs[p] - i, i - zero_idxs[p - 1]))

    return result


assert shortestToChar("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0]
assert shortestToChar("aaab", "b") == [3,2,1,0]
