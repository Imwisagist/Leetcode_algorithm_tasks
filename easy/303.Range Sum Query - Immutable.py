# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        arr, sums = [], 0

        for i in nums:
            sums += i
            arr.append(sums)

        self.arr = arr

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right] - self.arr[left - 1] if left else self.arr[right]
    

arr = NumArray([-2, 0, 3, -5, 2, -1])

assert arr.sumRange(0, 2) == 1
assert arr.sumRange(2, 5) == -1
assert arr.sumRange(0, 5) == -3