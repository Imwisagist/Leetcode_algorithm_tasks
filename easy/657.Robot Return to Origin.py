# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


assert judgeCircle("UD") is True
assert judgeCircle("LL") is False
