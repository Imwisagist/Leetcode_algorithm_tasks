# https://leetcode.com/problems/plus-one/

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    last, length = -1, len(digits)

    if digits[last] == 9:
        while length != 0 and digits[last] == 9:
            digits[last] = 0
            last -= 1
            length -= 1
        if length == 0:
            digits.insert(0, 1)
        else:
            digits[last] += 1
    else:
        digits[last] += 1

    return digits


assert plusOne([9, 9, 9]) == [1, 0, 0, 0]
assert plusOne([1, 3, 9]) == [1, 4, 0]
assert plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert plusOne([9]) == [1, 0]
