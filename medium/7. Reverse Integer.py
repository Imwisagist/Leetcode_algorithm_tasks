# https://leetcode.com/problems/reverse-integer/description/


def reverse(x: int) -> int:
    s = str(abs(x))
    s = s[::-1]

    if len(s) == 10:
        for cur, max in zip(s, "2147483648"):
            if cur < max: break
            elif cur > max: return 0

    return int(s) * -1 if x < 0 else int(s)


assert reverse(-2147483412) == -2147483412
