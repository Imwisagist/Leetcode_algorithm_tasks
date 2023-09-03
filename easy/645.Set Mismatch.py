# https://leetcode.com/problems/set-mismatch/

from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
    arr_len, arr_sum, set_sum = len(nums), sum(nums), sum(set(nums))
    arith_progres = arr_len * (arr_len + 1) // 2

    return [arr_sum - set_sum, arith_progres - set_sum]


assert findErrorNums([1,2,2,4]) == [2,3]
assert findErrorNums([1,1]) == [1,2]
assert findErrorNums([3,2,2]) == [2,1]
assert findErrorNums([3,2,3,4,6,5]) == [3,1]
