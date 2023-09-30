# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

from heapq import heapify, heappush, heappushpop, heapreplace
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k, = nums[:k], k; heapify(self.nums)

        for i in range(k,len(nums)):
            if nums[i] > self.nums[0]: heappushpop(self.nums,nums[i])

    def add(self,val: int) -> int:
        if len(self.nums) < self.k: heappush(self.nums,val)
        elif val > self.nums[0]: heapreplace(self.nums,val)

        return self.nums[0]
