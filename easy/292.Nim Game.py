# https://leetcode.com/problems/nim-game/

def canWinNim(n: int) -> bool:
    return n % 4 != 0

assert canWinNim(4) is False
assert canWinNim(1) is True
assert canWinNim(2) is True
assert canWinNim(16) is False
