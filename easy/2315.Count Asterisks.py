# https://leetcode.com/problems/count-asterisks/description/

def countAsterisks(s: str) -> int:
    res,blocked = 0, False

    for chr in s:
        if chr == "|": blocked = not blocked
        elif chr == "*" and not blocked: res += 1

    return res


assert countAsterisks("l|*e*et|c**o|*de|") == 2
assert countAsterisks("iamprogrammer") == 0
assert countAsterisks("yo|uar|e**|b|e***au|tifu|l") == 5
