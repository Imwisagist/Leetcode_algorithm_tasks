# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

from typing import List

def sumZero(n: int) -> List[int]:
    res = [0] if n % 2 else []

    for i in range(1,n//2+1): res += [i,-i]

    return res


assert sumZero(5) == [0,1,-1,2,-2]
assert sumZero(3) == [0,1,-1]
assert sumZero(1) == [0]
