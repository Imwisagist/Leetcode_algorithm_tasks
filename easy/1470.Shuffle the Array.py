# https://leetcode.com/problems/shuffle-the-array/description/

from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    res = []

    for i,j in zip(nums[:n],nums[n:]): res += [i,j]

    return res


assert shuffle([2,5,1,3,4,7],3) == [2,3,5,4,1,7]
assert shuffle([1,2,3,4,4,3,2,1],4) == [1,4,2,3,3,2,4,1]
assert shuffle([1,1,2,2],2) == [1,2,1,2]
