# https://leetcode.com/problems/split-with-minimum-sum/description/

def splitNum(num: int) -> int:
    l = []; n1 = n2 = 0

    while num: l.append(num%10); num //= 10

    l.sort(); f = True

    for i in l:
        if f: n1 = n1*10 + i; f = False
        else: n2 = n2*10 + i; f = True

    return n1 + n2


assert splitNum(11) == 2
assert splitNum(4325) == 59
assert splitNum(687) == 75
