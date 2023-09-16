# https://leetcode.com/problems/count-largest-group/description/
from functools import reduce
def countLargestGroup(n: int) -> int:
    d: dict = {}
    d_get = d.get

    for number in range(1,n+1):
        sums: int = 0

        while number != 0:
            sums += number % 10
            number //= 10

        d[sums] = d_get(sums,0) + 1
    
    max_val = max(d.values())

    return sum(1 for v in d.values() if v == max_val)


assert countLargestGroup(13) == 4
assert countLargestGroup(2) == 2
