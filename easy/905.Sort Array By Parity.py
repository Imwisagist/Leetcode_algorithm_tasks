# https://leetcode.com/problems/sort-array-by-parity/description/

from typing import List

def sortArrayByParity(nums: List[int]) -> List[int]:
    even, odd = [], []

    for n in nums:
        if n % 2 == 0: even.append(n)
        else: odd.append(n)

    return even + odd


assert sortArrayByParity([3,1,2,4]) == [2,4,3,1]
assert sortArrayByParity([0]) == [0]
