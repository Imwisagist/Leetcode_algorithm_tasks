# https://leetcode.com/problems/top-k-frequent-elements/description/
import heapq
from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    items = Counter(nums)
    return heapq.nlargest(k, items, key=items.get)


assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert topKFrequent([1], 1) == [1]
