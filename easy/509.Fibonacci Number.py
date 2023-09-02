# https://leetcode.com/problems/fibonacci-number/

def fib(n: int) -> int:
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    return a


assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
