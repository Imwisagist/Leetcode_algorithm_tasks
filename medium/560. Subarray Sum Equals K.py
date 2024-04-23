# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List
from collections import defaultdict


def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum, d = 0, defaultdict(int); d[0] = 1; res = 0

    for num in nums:
        prefix_sum += num; missing_part = prefix_sum - k

        if missing_part in d: res += d[missing_part]

        d[prefix_sum] += 1

    return res


assert subarraySum([1, 1, 1], 2) == 2
assert subarraySum([1, 2, 3], 3) == 2
