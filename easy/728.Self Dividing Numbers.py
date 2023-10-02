# https://leetcode.com/problems/self-dividing-numbers/description/

from typing import List

def selfDividingNumbers(left: int, right: int) -> List[int]:
    res = []

    for i in range(left,right+1):
        num = i

        while num:
            digit = num % 10

            if i % digit if digit else 1: break
            
            num //= 10 
        else: res.append(i)

    return res
    

assert selfDividingNumbers(1,22) == [1,2,3,4,5,6,7,8,9,11,12,15,22]
assert selfDividingNumbers(47,85) == [48,55,66,77]
