# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")

# arr = [0]*18
#
# for c in moves: arr[ord(c)-68] += 1
#
# return arr[0] == arr[17] and arr[8] == arr[14]


assert judgeCircle("UD") is True
assert judgeCircle("LL") is False
