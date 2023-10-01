# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

def minBitFlips(start: int, goal: int) -> int:
    cnt = 0

    while start or goal:
        if start % 2 != goal % 2: cnt += 1
        
        start,goal = start // 2,goal // 2

    return cnt

assert minBitFlips(10,7) == 3
assert minBitFlips(3,4) == 3
