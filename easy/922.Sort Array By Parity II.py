# https://leetcode.com/problems/sort-array-by-parity-ii/description/

from typing import List

def sortArrayByParityII(nums: List[int]) -> List[int]:
    res, even = [], (n for n in nums if n % 2 == 0)
    odd = (n for n in nums if n % 2 == 1)

    for even, odd in zip(even, odd):
        res.append(even); res.append(odd)

    return res


assert sortArrayByParityII([4,2,5,7]) == [4,5,2,7]
assert sortArrayByParityII([2,3]) == [2,3]
