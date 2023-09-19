# https://leetcode.com/problems/second-largest-digit-in-a-string/description/

def secondHighest(s: str) -> int:
    first_found = False

    for num in "9876543210":
        if s.find(num) + 1:
            if first_found: return int(num)
            first_found = True

    return -1


assert secondHighest("dfa12321afd") == 2
assert secondHighest("abc1111") == -1
