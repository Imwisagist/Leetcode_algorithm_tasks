# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/

from collections import defaultdict
from itertools import combinations
from typing import List


def countPairs(nums: List[int], k: int) -> int:
    d = defaultdict(list)

    for i,n in enumerate(nums): d[n].append(i)

    return sum(
        1
        for l in d.values()
        for c in combinations(l,2)
        if c[0] * c[1] % k == 0
    )


assert countPairs([3,1,2,2,2,1,3],2) == 4
assert countPairs([1,2,3,4],1) == 0
