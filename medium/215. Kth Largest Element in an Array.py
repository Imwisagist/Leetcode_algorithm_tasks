# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
from heapq import heapify, heappushpop


def findKthLargest(nums: List[int], k: int) -> int:
    heapify(heap := nums[:k])

    [heappushpop(heap, num) for num in nums[k:] if num > heap[0]]

    return heap[0]


assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
