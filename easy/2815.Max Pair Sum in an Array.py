# https://leetcode.com/problems/max-pair-sum-in-an-array/description/

from collections import defaultdict
from typing import List

def maxSum(nums: List[int]) -> int:
##################################################
    def get_maximal_digit(n) -> int:
        max_digit = 0

        while n > 0:
            digit = n % 10
            if digit > max_digit: max_digit = digit
            n //= 10

        return max_digit
#####################################################
    max_by_digit, max_sum = defaultdict(int), -1

    for n in nums:
        max_digit = get_maximal_digit(n)

        if max_digit in max_by_digit:
            max_sum = max(max_sum, max_by_digit[max_digit] + n)

        max_by_digit[max_digit] = max(max_by_digit[max_digit], n)

    return max_sum

assert maxSum([51,71,17,24,42]) == 88
assert maxSum([1,2,3,4]) == -1
assert maxSum([84,91,18,59,27,9,81,33,17,58]) == 165
assert maxSum([8,75,28,35,21,13,21]) == 42
assert maxSum([10,68,5,62,5,100,44,36]) == 110
assert maxSum([96,79,96,87,79,98,11,78,74]) == 194
