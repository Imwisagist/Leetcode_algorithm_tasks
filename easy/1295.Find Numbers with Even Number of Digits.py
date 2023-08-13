# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List

def findNumbers(nums: List[int]) -> int:
    length, count = 0, 0

    for num in nums:
        while num > 0:
            num = num // 10
            length += 1
        if length % 2 == 0:
            count += 1
        length = 0

    return count


assert findNumbers([12,345,2,6,7896]) == 2
assert findNumbers([555,901,482,1771]) == 1
