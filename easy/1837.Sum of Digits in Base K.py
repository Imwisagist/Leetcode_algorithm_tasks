# https://leetcode.com/problems/sum-of-digits-in-base-k/description/

def sumBase(n: int, k: int) -> int:
    res = 0

    while n: n,r = divmod(n,k); res += r

    return res


assert sumBase(34,6) == 9
assert sumBase(10,10) == 1
