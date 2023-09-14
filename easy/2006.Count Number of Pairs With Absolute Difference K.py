# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

from collections import defaultdict
from typing import List

def countKDifference(nums: List[int], k: int) -> int:
    seen, counter = defaultdict(int), 0

    for num in nums:
        counter += seen[num-k] + seen[num+k]
        seen[num] += 1

    return counter


assert countKDifference([1,2,2,1], 1) == 4
assert countKDifference([1,3], 3) == 0
assert countKDifference([3,2,1,5,4], 2) == 3
