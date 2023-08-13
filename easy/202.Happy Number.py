# https://leetcode.com/problems/happy-number/

def isHappy(n: int) -> bool:
    map: set = set()

    while n != 1:
        if n in map: return False
        map.add(n)
        n: int = sum([int(i) ** 2 for i in str(n)])

    return True 


assert isHappy(19) is True
assert isHappy(2) is False
