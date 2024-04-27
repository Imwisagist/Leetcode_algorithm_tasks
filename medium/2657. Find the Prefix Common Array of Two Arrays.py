# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
from typing import List


def findThePrefixCommonArray(arr1: List[int], arr2: List[int]) -> List[int]:
    cnt, res, s = 0, [], set()

    for i in range(len(arr1)):
        left, right = arr1[i], arr2[i]

        if left in s: cnt += 1
        else: s.add(left)

        if right in s: cnt += 1
        else: s.add(right)

        res.append(cnt)

    return res


assert findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]) == [0, 2, 3, 4]
assert findThePrefixCommonArray([2, 3, 1], [3, 1, 2]) == [0, 1, 3]
