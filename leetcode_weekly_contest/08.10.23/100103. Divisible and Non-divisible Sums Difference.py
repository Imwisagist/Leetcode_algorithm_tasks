
def differenceOfSums(n: int, m: int) -> int:
    n1 = n2 = 0

    for i in range(1,n+1):
        if i % m: n1 += i
        else: n2 += i

    return n1 - n2


assert differenceOfSums(10,3) == 19
assert differenceOfSums(5,6) == 15
assert differenceOfSums(5,1) == -15