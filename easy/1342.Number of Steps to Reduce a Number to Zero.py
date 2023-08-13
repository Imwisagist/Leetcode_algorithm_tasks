# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numberOfSteps(num: int) -> int:
    if num == 0: return 0

    return num.bit_length() - 1 + num.bit_count()


assert numberOfSteps(14) == 6
assert numberOfSteps(8) == 4
assert numberOfSteps(123) == 12
