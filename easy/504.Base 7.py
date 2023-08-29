# https://leetcode.com/problems/base-7/

def convertToBase7(num: int) -> str:
    if not num: return "0"
    
    s, f = [], False

    if num < 0:
        f = True
        num = -num
    
    while num > 0:
        s.append(str(num%7))
        num //= 7

    return ("-" if f else "") + "".join(s[::-1])


assert convertToBase7(100) == "202"
assert convertToBase7(-7) == "-10"
