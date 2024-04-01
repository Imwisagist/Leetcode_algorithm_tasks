# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

from typing import List
from collections import defaultdict


def findMatrix(nums: List[int]) -> List[List[int]]:
    d, res = defaultdict(int), []

    for num in nums:
        d[num] += 1

    for _ in range(max(d.values())):
        arr = []

        for key, val in d.items():
            if val:
                arr.append(key)
                d[key] -= 1

        res.append(arr)

    return res


assert findMatrix([1, 3, 4, 1, 2, 3, 1]) == [[1, 3, 4, 2], [1, 3], [1]]
assert findMatrix([1, 2, 3, 4]) == [[1, 2, 3, 4]]
