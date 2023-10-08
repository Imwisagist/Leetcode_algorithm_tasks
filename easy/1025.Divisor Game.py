# https://leetcode.com/problems/divisor-game/description/

def divisorGame(n: int) -> bool:
    return not n % 2


assert divisorGame(2) is True
assert divisorGame(3) is False
