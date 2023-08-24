# https://leetcode.com/problems/perfect-number/

def checkPerfectNumber(num: int) -> bool:
    count: int = 1

    if num == 1: return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count += i + num // i

    return num == count


assert checkPerfectNumber(28) is True
assert checkPerfectNumber(7) is False
