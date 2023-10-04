# https://leetcode.com/problems/count-operations-to-obtain-zero/

def countOperations(n1: int, n2: int) -> int:
    res = 0

    while n1 and n2:
        res += n1 // n2; n1,n2 = n2,n1 % n2

    return res


assert countOperations(79,68) == 14
assert countOperations(2,3) == 3
assert countOperations(10,10) == 1
