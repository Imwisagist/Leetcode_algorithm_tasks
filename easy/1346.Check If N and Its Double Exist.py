# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

from typing import List

def checkIfExist(arr: List[int]) -> bool:
    seen = set()

    for n in arr:
        if (n * 2 in seen or
            n % 2 == 0 and n // 2 in seen):
            return True
        
        seen.add(n)

    return False


assert checkIfExist([10,2,5,3]) is True
assert checkIfExist([3,1,7,11]) is False
assert checkIfExist([-2,0,10,-19,4,6,-8]) is False
