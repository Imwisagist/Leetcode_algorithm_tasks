# https://leetcode.com/problems/integer-break/description/?envType=daily-question&envId=2023-10-06

def integerBreak(n: int) -> int:
    return (
            (n-1) if n <= 3 else 
            (3 ** (n//3)) if n % 3 == 0 else
            (3 ** (n//3 - 1) * 4) if n % 3 == 1 else
            (3 ** (n//3) * 2)
        )


assert integerBreak(2) == 1
assert integerBreak(10) == 36
