# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

def countBalls(lowLimit: int, highLimit: int) -> int:
    d: dict = {}

    for i in range(lowLimit, highLimit + 1):
        if i > 9:
            sum_digit: int = 0

            while i > 9:
                sum_digit += i % 10
                i //= 10
            i += sum_digit

        d[i] = d.get(i,0) + 1
    
    return max(d.values())


assert countBalls(1,10) == 2
assert countBalls(5,15) == 2
assert countBalls(19,28) == 2